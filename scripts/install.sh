#!/bin/bash

# Modules a installer
echo "Installation des modules python."
pip install --upgrade openai
pip install --upgrade python-dotenv


# Fichier pour la clé API d'OpenAI
fichierEnv=".env"
echo "Creation du fichier .env"
if [ -e "$fichierEnv" ];
then
	echo "--Le fichier .env existe déjà."
else
	touch .env
	echo "OPENAI_API_KEY = 'your-api-key-here'" >> .env
	echo "--Creation : OK"

fi


# Installation de Frama-C

read -p "Faire l'installation de Frama-C ? (oui/non) : " reponseFC
case "$reponseFC" in
    oui)
		echo "Creation du fichier .profile"
		if [ -e "$fichierEnv" ];
		then
			echo "--Le fichier .profile existe déjà."
		else
			touch ./frama-c/.profile
			echo "--Creation : OK"
		fi
		sudo apt install opam


		read -p "Voulez-vous déjà installé opam ? (oui/non) : " reponse

		# Vérifier la réponse de l'utilisateur
		case "$reponse" in
			oui)
				echo "Vous avez choisi de continuer."
				# Action à effectuer si la réponse est "oui"
				# Exemple : exécuter une commande ou un script
				;;
			non)
				echo "Vous avez choisi de ne pas continuer."
				# Action à effectuer si la réponse est "non"
				opam init --compiler 4.14.1 f ./.profile
				opam install frama-c
				;;
			*)
				echo "Réponse invalide. Veuillez répondre par 'oui' ou 'non'."
				# Action à effectuer si la réponse n'est ni "oui" ni "non"
				;;
		esac
		;;
    *)
        echo "Ne pas installer Frama-C"
        ;;
esac




echo "Fin de l'installation"