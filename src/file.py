import os

def get_filename_from_path(file_path):
    filename = os.path.basename(file_path)
    return filename

def read_file(programPath):
  with open(programPath, 'r') as file:
    contenu = file.read()
  return contenu