def copier_fichier(fichier_A, fichier_B):
    # Lire le contenu du fichier B
    with open(fichier_B, 'r') as file_B:
        contenu_B = file_B.read()

    # Écrire le contenu de B dans le fichier A
    with open(fichier_A, 'w') as file_A:
        file_A.write(contenu_B)


def extraire_invariant(chaine):
    # Supprimer les espaces inutiles et diviser la chaîne en fonction de ":"
    chaine = chaine.strip()
    chaine = chaine.split(":")
    
    # Vérifier si la chaîne commence par "//@ loop invariant mask:"
    if chaine[0] == "//@ loop invariant mask":
        # Retourner la partie après le ":"
        return chaine[1].strip()
    


def remplacer_invariant(fichier_A, invariant):
    # Lire le contenu du fichier A
    with open(fichier_A, 'r') as file_A:
        contenu_A = file_A.read()

    # Remplacer [mask] par l'invariant dans le contenu du fichier A
    contenu_A_modifie = contenu_A.replace("[mask]", invariant)

    # Écrire le contenu modifié dans le fichier A
    with open(fichier_A, 'w') as file_A:
        file_A.write(contenu_A_modifie)