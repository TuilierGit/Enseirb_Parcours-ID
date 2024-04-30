
import os

def transformer_assert(ligne):
    if "__VERIFIER_assert" in ligne:
        # Récupérer la condition de l'assert
        condition = ligne.split("__VERIFIER_assert(")[1].split(");")[0]
        # Construire la nouvelle ligne avec le format spécifié
        nouvelle_ligne = "//@ assert {};".format(condition.strip())
        return nouvelle_ligne
    else:
        return ligne

def transformer_contenu_fichier(contenu):
    lignes = contenu.split('\n')
    nouveau_contenu = ""
    conserver = False
    compteur = 0

    for ligne in lignes:
        if "#define" in ligne or "int main(" in ligne:
            conserver = True
        elif "}" in ligne and conserver and compteur == 0:
            conserver = False

        if conserver:
            nouveau_contenu += transformer_assert(ligne) + '\n'

        if "{" in ligne and conserver:
            compteur += 1
        elif "}" in ligne and conserver:
            compteur -= 1

    return nouveau_contenu.strip()



def transformer_et_ecrire_fichier(nom_fichier):
    # Lire le contenu du fichier
    with open(nom_fichier, 'r') as f:
        contenu_original = f.read()

    # Transformer le contenu
    nouveau_contenu = transformer_contenu_fichier(contenu_original)

    # Écrire le nouveau contenu dans le fichier
    with open(nom_fichier, 'w') as f:
        f.write(nouveau_contenu)

def transformer_et_ecrire_dossier(chemin_dossier):
    # Parcours de tous les fichiers du dossier
    for nom_fichier in os.listdir(chemin_dossier):
        # Construction du chemin complet du fichier
        chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
        # Vérification s'il s'agit d'un fichier
        if os.path.isfile(chemin_fichier):
            # Application de la fonction transformer_et_ecrire_fichier à chaque fichier
            transformer_et_ecrire_fichier(chemin_fichier)


dossier_a_traiter = "./loop-crafted"  # Remplacez "chemin_vers_le_dossier" par le chemin de votre dossier
transformer_et_ecrire_dossier(dossier_a_traiter)
# fichier_a_traiter = "./loop-acceleration/array_1-1.c"  # Remplacez "chemin_vers_le_dossier" par le chemin de votre dossier
# transformer_et_ecrire_fichier(fichier_a_traiter)