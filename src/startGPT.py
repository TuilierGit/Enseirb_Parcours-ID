import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()

openai.api_base = "http://localhost:4891/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")


# Mise en place de nos variables globales
LLM_model = "Mistral OpenOrca"
#GPT_version = "gpt-3.5-turbo"
_temperature = 0.2
_max_tokens = 500

###########################
##    Fonctions utiles   ##
###########################



def ask_my_model( prompt,model = LLM_model,number_of_answers=1, mt = _max_tokens,temp = _temperature):
  response = openai.Completion.create(
    model=model,
    prompt=prompt,
    max_tokens=mt,
    temperature=temp,
    #top_p=0.95, # limite la somme cumulative des probabilités des tokens 
    n=number_of_answers, # nombre de réponse
    echo=False, # est ce qu'on ecrit la question dans la réponse
    stream=False #  détermine si les résultats doivent être retournés en entier ou s'ils doivent être diffusés en continu.
  )
  return response


def readProgram(programPath):
  with open(programPath, 'r') as file:
    contenu = file.read()
  return contenu



def getInvariant(program,number_of_answers=1 ):
  GPT_Prompt = "Compute a loop invariant for the following program!\n" + program,
  return ask_my_model(GPT_Prompt,number_of_answers)

def get_filename_from_path(file_path):
    filename = os.path.basename(file_path)
    return filename

def run(path, n = 1):
  line = "========================================="
  exemple = readProgram(path)
  invariant = getInvariant(exemple).to_dict()
  print(f"\n\t\033[1m{get_filename_from_path(path)}\033[0m\n{line}\n\n\033[94m{exemple}\033[0m\n\n{line}")
  print(f"\n\033[92m{invariant['choices'][0]['text']}\033[0m")
  print(f"\n{line}")


#######################
##    Partie Main    ##
#######################

if __name__ == "__main__":

  run("./examples/naive/loops-count_up_down-1.c")
  run("./examples/naive/underapprox_1-2.c")
  run("./examples/naive/benchmark04_conjunctive.c")
