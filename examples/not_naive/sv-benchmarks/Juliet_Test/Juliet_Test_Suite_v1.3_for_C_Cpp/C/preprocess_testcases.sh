#!/usr/bin/env bash

# This file is part of the SV-Benchmarks collection of verification tasks:
# https://github.com/sosy-lab/sv-benchmarks
# SPDX-FileCopyrightText: 2020 The SV-Benchmarks Community
# SPDX-License-Identifier: Apache-2.0

# Running this script the .c files in each CWE directory are preprocessed
# and a _bad.i , _good.i and .yml file are created for each .c file.
# The preprocessed/yml files are saved in the preprocessed folder
# in each CWE directory in testcases.
# Files with a windows.h header can only be preprocessed on a windows system.

set -euo pipefail

# change into the directory of this script
cd "$( dirname "${BASH_SOURCE[0]}")"

# use environment variable CC if available or fallback to plain gcc
CC="${CC:-gcc}"

# options for preprocessing
OPTIONS="-E -P -D INCLUDEMAIN=1 -m64 -I testcasesupport"

# property_file
property_dir="../../../properties/"
property_dir_relative_to_output_folder="../../../"${property_dir}
property_file=""
digit_re='^[0-9]$'
export CC OPTIONS property_dir property_dir_relative_to_output_folder property_file folder digit_re

process_file () {
    output_folder=$1
    f=$2

    echo -ne "." # one dot per file to see progress

    # get the plain file name
    file="$(basename $f)"

    # Juliet benchmarks are sometimes defined over multiple
    # files. This will be the second case in the conditional
    
    # if file is ...[0-9][0-9][a-e].c, this means we need to make only on yml file with the different input files given to it
    # we only do this processing for the a file in that case
    file_noext=${file%.c}
    # note that some implementations are not processed this way, you may want to temporarily include "io.c" in c/Juliet_Test/Juliet_Test_Suite_v1.3_for_C_Cpp/C/testcasesupport/std_testcase_io.h
    if [[ "${file_noext: -1}" =~ $digit_re ]]; then
        # usual case
	badfile="${file%.c}_bad"
	goodfile="${file%.c}_good"

	cp "${f}" "${output_folder}/${file}"
	# get the preprocessed file with OMITGOOD=1/OMITBAD=1
	$CC -D OMITGOOD=1 $OPTIONS "${output_folder}/${file}" -o "${output_folder}/${badfile}.i"
	$CC -D OMITBAD=1 $OPTIONS "${output_folder}/${file}" -o "${output_folder}/${goodfile}.i"
	
	reuse addheader --template header.jinja2 --year "2022" --copyright "NIST" --copyright "The SV-Benchmarks Community" --license CC0-1.0 --style c "${output_folder}/${f}" >/dev/null

    elif [ ${file_noext: -1} = "a" ]; then
        # multiple files, first case
        #write the .yml files
	file_group="${file_noext::-1}"
        badfile="${file_group}_bad"
        goodfile="${file_group}_good"

	find "${folder}" -iname "${file_group}*.c" -exec cat {} \; > "${output_folder}/_${file_group}.c"
	mv "${output_folder}/_${file_group}.c" "${output_folder}/${file_group}.c"
	
	# get the preprocessed file with OMITGOOD=1/OMITBAD=1
	$CC -D OMITGOOD=1 $OPTIONS "${output_folder}/${file_group}.c" -o "${output_folder}/${badfile}.i"
	$CC -D OMITBAD=1 $OPTIONS "${output_folder}/${file_group}.c" -o "${output_folder}/${goodfile}.i"

    elif [ ${file_noext: -1} = "b" ] || [ ${file_noext: -1} = "c" ] || [ ${file_noext: -1} = "d" ] || [ ${file_noext: -1} = "e" ]; then
        return 0
    else
        echo "weird case $f"
    fi

    # add license
    reuse addheader --template header.jinja2 --year "2022" --copyright "NIST" --copyright "The SV-Benchmarks Community" --license CC0-1.0 --style c "${output_folder}/${badfile}.i" >/dev/null
    reuse addheader --template header.jinja2 --year "2022" --copyright "NIST" --copyright "The SV-Benchmarks Community" --license CC0-1.0 --style c "${output_folder}/${goodfile}.i" >/dev/null

    #write the .yml files
    echo "format_version: '2.0'
input_files: '${badfile}.i'
properties:
  - property_file: '${property_dir_relative_to_output_folder}${property_file}'
    expected_verdict: false
options:
  language: C
  data_model: LP64
" > "${output_folder}/${badfile}.yml"

    echo "format_version: '2.0'
input_files: '${goodfile}.i'
properties:
  - property_file: '${property_dir_relative_to_output_folder}${property_file}'
    expected_verdict: true
options:
  language: C
  data_model: LP64
" > "${output_folder}/${goodfile}.yml"
    
}
export -f process_file

#for loop runs over all folders in testcases
for folder in testcases/*/
do
    # get the matching property_file for the CWE-Id
    cwe_folder="$(basename $folder)" # get the plain directory name
    cwe="${cwe_folder%${cwe_folder#??????}}" # extract the first 6 chars from the string

    case "$cwe" in

        "CWE190" | "CWE191")
	    property_file="no-overflow.prp"
            ;;

        # "CWE119" | "CWE121" | "CWE122" | "CWE124" | "CWE125" | "CWE126" | "CWE127" | "CWE401" | "CWE415" | "CWE416" | "CWE476" | "CWE590" | "CWE761"| "CWE787" | "CWE789"| "CWE843" )
        #     property_file="valid-memsafety.prp"
        #     ;;

        # "CWE835")
        #     property_file="termination.prp"
        #     ;;

        *)
            property_file=""
            ;;
    esac

    # if propertyfile is empty then skip the directory otherwise analyse/preprocess the directory
    if [ -z "$property_file" ]
    then
        echo "SKIPPING directory '${folder}' because of missing propertyfile"
        continue
    elif [ ! -f "${property_dir}${property_file}" ]; then
        echo "WARNING directory '${property_dir}${property_file}' is referenced, but does not exist"
    fi

    echo "PROCESSING directory '${folder}' with property file '${property_file}'"

    output_folder="${folder}preprocessed"
    mkdir -p "${output_folder}"

    #while loop through all c files in the current folder
    #     | while read f
    # do$
    find "${folder}" -iname "*__int*.c" | sort > jobs # for juliet overflows
    parallel -j+0 -k --lb -N1 "process_file $output_folder" < jobs
    # done
    echo "" # newline after the dots above

    # write out a set file for further processing with BenchExec
    set_folder="set-files"
    mkdir -p ${set_folder}
    echo "../${output_folder}/*.yml" > ${set_folder}/${cwe_folder}.set
done
