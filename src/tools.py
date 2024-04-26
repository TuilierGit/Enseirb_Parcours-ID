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


def extraire_arguments(declaration):
    # Diviser la déclaration de fonction en fonction du premier parenthèse ouvrante
    index_parenthese = declaration.find("(")
    if index_parenthese == -1:
        return None  # La déclaration est invalide, retourner None
    
    # Extraire la partie des arguments entre les parenthèses
    arguments_part = declaration[index_parenthese+1:-1].strip()
    
    # Diviser les arguments en fonction des virgules
    arguments = [arg.strip() for arg in arguments_part.split(",")]
    
    # Modifier le dernier argument pour enlever une parenthèse fermante
    arguments[-1] = arguments[-1][:arguments[-1].find(")")] + arguments[-1][arguments[-1].find(")")+1:]

    # Retourner les arguments séparés par des virgules
    return ", ".join(arguments)


def extraire_contenu(fichier_entree, fichier_sortie, include_list):
    # Ouvrir le fichier d'entrée en lecture
    with open(fichier_entree, 'r') as file_in:
        contenu = file_in.read()

    # Extraire la déclaration de la fonction
    declaration = contenu.split("{")[0].strip() + " ;\n"

    # Écrire dans le fichier de sortie
    with open(fichier_sortie, 'w') as file_out:
        # Écrire l'inclusion des fichiers
        file_out.write(include_list + "\n\n")
        
        # Écrire les conditions
        file_out.write("/*\n")
        file_out.write(f"  @ assigns {extraire_arguments(declaration)}\n")
        file_out.write("*/\n\n")
        
        # Écrire la déclaration de la fonction
        file_out.write(declaration)

