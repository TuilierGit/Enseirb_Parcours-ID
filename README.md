# Enseirb_Parcours-ID

Espace de travail pour le module SE205 “Initiation à la recherche” de l'Enseirb-Matmeca. Le but de ce projet est d'analyser les expériences de la thèse suivante :

**[Can ChatGPT support software verification?
](https://arxiv.org/pdf/2311.02433.pdf)**

Réalisé par Christian Janßen, Cedric Richter et Heike Wehrheim.

## Installation et mise en place de l'API d'OpenAI

On va dans un premier temps installer et mettre en place un environement de travail pour les s'occuper des différents modules python nécessaire à ce projet. Pour faire cela il suffit d'utiliser la commande suivante :

```
  python -m venv pid-env
```

Puis de l'activer avec la commande :

```
  source pid-env/bin/activate
```

Une fois cela réaliser, on va installer les différents packages avec

```
  ./install.sh
```

Maintenant il faut ajouter une clé API, pour réaliser cela on va se rendre sur le [site d'OpenAI](https://platform.openai.com/api-keys) dans la partie des clés API
