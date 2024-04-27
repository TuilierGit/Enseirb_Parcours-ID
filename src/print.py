from file import * 

line = "========================================="

def print_file(path, file):
    print(f"\n\t\033[1m{get_filename_from_path(path)}\033[0m") # title
    print(f"\n{line}")
    print(f"\n\033[94m{file}\033[0m") # file
    print(f"\n{line}")

def print_invariant(invariant):
    print(f"\n\033[92m{invariant}\033[0m")
    print(f"\n{line}")

def print_validation(validation):
    print(f"\n\033[93m{validation}\033[0m")  
    print(f"\n{line}")