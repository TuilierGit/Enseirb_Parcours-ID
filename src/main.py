from file import *
from model import model, get_invariant_sentence_from_response, get_invariant_from_invariant_sentence
from print import *
from framaC import checking_the_invariant
import openai
import os
from dotenv import load_dotenv
import argparse



load_dotenv()

list_of_model = ["Llama 3 Instruct", "Nous Hermes 2 Mistral DPO", "Mistral Instruct", "Mistral OpenOrca", "GPT4All Falcon", "Orca 2 (Medium)"]
openai.api_base = "http://localhost:4891/v1"
openai.api_key = os.getenv("OPENAI_API_KEY")


def run(path,myModel,no_color):
    
    exemple = read_file(path)
    print_file(path, exemple,no_color)

    invariant_sentence = get_invariant_sentence_from_response(myModel.response_with_long_prompt(exemple))
    print_invariant(invariant_sentence,no_color)
    invariant = get_invariant_from_invariant_sentence(invariant_sentence)

    #validation = checking_the_invariant( path,invariant)
    #print_validation(validation,no_color)

def main(no_color):

    for my_LLM_model in list_of_model:
        myModel = model(my_LLM_model)
        print(f"model: {my_LLM_model}")

        
        run("./examples/naive/sv-benchmarks/loop-acceleration/array_1-1.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-acceleration/array3.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-acceleration/diamond_2-2.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-acceleration/underapprox_1-1.c",myModel,no_color)

        run("./examples/naive/sv-benchmarks/loop-invariants/even.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-invariants/linear-inequality-inv-a.c",myModel,no_color)

        run("./examples/naive/sv-benchmarks/loop-simple/deep-nested.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-simple/nested_1.c",myModel,no_color)

        run("./examples/naive/sv-benchmarks/loop-zilu/benchmark01_conjunctive.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-zilu/benchmark12_linear.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loop-zilu/benchmark31_disjunctive.c",myModel,no_color)

        run("./examples/naive/sv-benchmarks/loops/array-1.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loops/matrix-1.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loops/terminator_01.c",myModel,no_color)

        run("./examples/naive/sv-benchmarks/loops-crafted-1/in-de20.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loops-crafted-1/mono-crafted_1.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loops-crafted-1/sumt9.c",myModel,no_color)
        run("./examples/naive/sv-benchmarks/loops-crafted-1/vnew1.c",myModel,no_color)

        print("\n=========================================\n")

        # run("./examples/naive/examples-article/loops-count_up_down-1.c",myModel,no_color)
        # run("./examples/naive/examples-article/underapprox_1-2.c",myModel,no_color)
        # run("./examples/naive/examples-article/benchmark04_conjunctive.c",myModel,no_color)

        # chemin_dossier =  "./examples/naive/sv-benchmarks/loop-zilu/"
        # for nom_fichier in os.listdir(chemin_dossier):
        #     chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
        #     if os.path.isfile(chemin_fichier):
        #         run(chemin_fichier,myModel,no_color)
        #         print("\n=========================================\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Description de votre programme.')
    parser.add_argument('--no-color', action='store_true', help='Désactiver les couleurs dans la sortie.')
    args = parser.parse_args()
    main(args.no_color)
    


