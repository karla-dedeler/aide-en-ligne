# ImporterFamillesArticles

## Nom de la tâche


ImporteFamillesArticles


## Description de la tâche


Crée des familles d'articles par import de fichier texte.


## Paramètres spécifiques de la tâche










| Nom | Description | Valeurs possibles | Présence | Valeur par défaut |
| FichierImporter | Fichier à importer |   | Obligatoire |   |
| SeparateurChamps | Séparateur de champs |   | Facultatif | ; |
| IdentificateurTexte | Identificateur de début et de fin de texte |   | Facultatif |   |
| PremiereLigneContientNomsChamps | Est-ce que la première ligne contient les noms des champs ? | Oui
Non | Facultatif | Oui |
| Champs | Liste des champs présents dans le fichier, dans le même ordre que dans le fichier, séparés par un point-virgule |   | Facultatif |   |
| RenommerFichier | Est-ce que le fichier doit être renommé une fois importé ? | Oui
Non | Facultatif | Non |


## Exemple


[Tâche]


Nom=ImporterFamillesArticles


Journal=ImporterFamillesArticles.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


Deconnecter=Non


Exclusif=Non


 


[Paramètres]


FichierImporter=ImporteFamillesArticles.txt


