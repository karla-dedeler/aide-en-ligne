Comment le projet MkDocs fonctionne
===============================================

Organisation du dossier
---------------------

📚 **docs/** <br>
Le contenu même de l'aide en ligne est dans le dossier `docs/`, tous les fichiers  `*.md` font partie de la documentation.

⚠️ **mkdocs.yml** <br>
Ce fichier est divisé en plusieurs parties:
- La section `nav` est le sommaire et permet de voir la structure même du site. Pour avoir une meilleure vue, ne pas hésiter à cacher des parties avec les flèches sur le côté. 
- La section `theme` permet de choisir certains réglages. Le thème principal est [material](https://squidfunk.github.io/mkdocs-material/getting-started/). Ce thème comporte des options qui peuvent être utilisées en les important dans la sous section `features` ou `plugins` selon les cas (se référer à la documentation). 
- La section `extra_css` permet d'ajouter de la personnalisation, modifier le thème de base. Il faut faire les modifications dans le fichier `extra.css` qui se trouve dans `docs/stylesheets/`

⚙️ **docs/requirements.in** et **docs/requirements.txt** <br>
Ce sont deux fichiers avec les configurations et imports nécessaires à la bonne compliation. Si modification dans les extensions utiliséees dans `mkdocs.yml`, ajouter selon la documentation la ligne nécessaire dans `*docs/requirements.in` puis lancer la commande présente dans le fichier `*docs/requirements.txt` pour bien mettre à jour le fichier.

Modifier / compléter la doc
---------------------
Dans le sommaire (section `nav` du document `mkdocs.yml`) **ajouter la section à l'endroit voulu**.
Pour ce faire, effectuer les étapes suivantes :
- respecter la **bonne indentation** selon le niveau de sous partie dont il s'agit,  
- commencer avec un tiret - 
- écrire le titre de la section (qui apparaîtra dans le sommaire du site). 
- ajouter deux points :
- entre '' indiquer le chemin daccès du fichier correspondant. 

Ce fichier doit se trouver dans le dossier `docs\` et finir en `*.md`. Il sera donc écrit en markdown ([ici un guide avec les bases du markdown](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/markdown/)). Si vous utilisez Visual Studio Code, il y a des extensions pour visualiser ce que cela donne.



Générer le site
---------------------

```console

# Pour genérer en local, exécuter la commande suivante en étant dans le répertoire du projet
python -m mkdocs serve

# Pour avoir accès au site en mode offline, exécuter la commande suivante en étant dans le répertoire du projet. 
# Cela créera les pages html dans le dossier site/
python -m mkdocs build
```