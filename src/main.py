from file import *
from model import model, get_invariant_sentence_from_response, get_invariant_from_invariant_sentence
from print import *
from framaC import checking_the_invariant
import openai
import os
from dotenv import load_dotenv


load_dotenv()

LLM_model = "Mistral OpenOrca"
openai.api_base = "http://localhost:4891/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")


def run(path):
    
    exemple = read_file(path)
    print_file(path, exemple)

    invariant_sentence = get_invariant_sentence_from_response(myModel.response_with_long_prompt(exemple))
    print_invariant(invariant_sentence)
    invariant = get_invariant_from_invariant_sentence(invariant_sentence)

    validation = checking_the_invariant( path,invariant)
    #print_validation(validation)



if __name__ == "__main__":

    myModel = model(LLM_model)

    run("./examples/naive/loops-count_up_down-1.c")
    run("./examples/naive/underapprox_1-2.c")
    run("./examples/naive/benchmark04_conjunctive.c")

