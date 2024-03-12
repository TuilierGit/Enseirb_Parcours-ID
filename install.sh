#!/bin/bash

# Modules a installer
pip install --upgrade openai
pip install python-dotenv

# Fichier pour la clé API d'OpenAI
touch .env 
echo "OPENAI_API_KEY = 'your-api-key-here'" >> .env


