Comment le projet MkDocs fonctionne
===============================================


📚 **docs/** <br>
Le contenu même est dans le dossier `docs/`, tous les fichiers  `*.md` sont des sections de la documentation.

⚙️ **mkdocs.yml** <br>
Ce fichier est divisé en plusieurs partie. 
La section `nav` est le sommaire et la structure même du site.
La section `theme` permet de choisir certains réglages. Le thème principal est [material](https://squidfunk.github.io/mkdocs-material/getting-started/). Ce thème comporte des options qui peuvent être utilisées en les important dans la sous section `features` ou `plugins` selon les cas (se référer à la documentation).
La section `extra_css` permet d'ajouter de la personnalsiation, modifier le thème de base. Il faut faire les modifications dans le fichier `extra.css` qui se trouve dans `docs/stylesheets/`


Générer le site
---------------------

```console

# Pour genérer en local, exécuter la commande suivante en étant dans le répertoire du projet
python -m mkdocs serve

# Pour avoir accès au site en mode offline, exécuter la commande suivante en étant dans le répertoire du projet. 
# Cela créera les pages html dans le dossier site/
python -m mkdocs build
```


