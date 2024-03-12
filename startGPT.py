import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Mise en place de nos variables globales
GPT_version = "gpt-3.5-turbo"
GPT_temperature = 0.2
GPT_max_tokens = 15

###########################
##    Fonctions utiles   ##
###########################


def askGPT(myPrompt, temperature=GPT_temperature, maxTokens=GPT_max_tokens, gptVersion = GPT_version):
  response = openai.completions.create(
    model=gptVersion,
    prompt=myPrompt,
    temperature=GPT_temperature
    # , max_tokens=GPT_max_tokens
  )
  return response


def readProgram(programPath):
  with open(programPath, 'r') as file:
    contenu = file.read()
  return contenu



def getInvariant(program):
  GPT_Prompt = "Compute a loop invariant for the following program!\n" + program,
  return askGPT(GPT_Prompt)


#######################
##    Partie Main    ##
#######################


if __name__ == "__main__":
  example1 = readProgram("./examples/loops-count_up_down-1.c")
  ex1_Invariant = getInvariant(example1)
  print(ex1_Invariant)
