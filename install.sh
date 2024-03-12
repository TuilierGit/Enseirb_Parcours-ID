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
