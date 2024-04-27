
import subprocess
from tools import *


commande = "frama-c -wp "
answer_path = "./examples/answer.c"
answer_h_path =  "./examples/answer.h"

def checking_the_invariant(path, invariant):
    copier_fichier(answer_path, path)
    true_invariant = extraire_invariant(invariant)
    remplacer_invariant(answer_path, true_invariant)
    subprocess.run(commande + answer_path , shell=True)