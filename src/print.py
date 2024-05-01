from file import * 

line = "========================================="

def print_file(path, file,no_color):

    if no_color :
        print(f"{get_filename_from_path(path)}")
    else :
        print(f"\n\t\033[1m{get_filename_from_path(path)}\033[0m") # title
        print(f"\n{line}")
        print(f"\n\033[94m{file}\033[0m") # file
        print(f"\n{line}")

def print_invariant(invariant,no_color):
    if no_color :
        print(f"{invariant}")
    else :
        print(f"\n\033[92m{invariant}\033[0m")
        print(f"\n{line}")

def print_validation(validation,no_color):
    if no_color :
        print(f"{validation}")  
    else :
        print(f"\n\033[93m{validation}\033[0m")  
        print(f"\n{line}")