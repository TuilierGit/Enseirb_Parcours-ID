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



def ask_my_model( prompt,model = LLM_model, mt = _max_tokens,temp = _temperature, number_of_answers=1):
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



def getInvariant(program):
  GPT_Prompt = "Compute a loop invariant for the following program!\n" + program,
  return ask_my_model(GPT_Prompt)


#######################
##    Partie Main    ##
#######################


if __name__ == "__main__":
  example1 = readProgram("./examples/naive/loops-count_up_down-1.c")
  example2 = readProgram("./examples/naive/underapprox_1-2.c")
  example3 = readProgram("./examples/naive/benchmark04_conjunctive.c")

  ex1_Invariant = getInvariant(example1).to_dict()
  ex2_Invariant = getInvariant(example2).to_dict()
  ex3_Invariant = getInvariant(example3).to_dict()
  
  print(f"\n\tExemple 1:\n==============================\n\n\033[94m{example1}\033[0m\n\n==============================")
  print(f"\n\033[92m{ex1_Invariant['choices'][0]['text']}\033[0m")
  print("\n==============================")

  print(f"\n\tExemple 2:\n==============================\n\n\033[94m{example2}\033[0m\n\n==============================")
  print(f"\n\033[92m{ex2_Invariant['choices'][0]['text']}\033[0m")
  print("\n==============================")

  print(f"\n\tExemple 3:\n==============================\n\n\033[94m{example2}\033[0m\n\n==============================")
  print(f"\n\033[92m{ex3_Invariant['choices'][0]['text']}\033[0m")
  print("\n==============================")