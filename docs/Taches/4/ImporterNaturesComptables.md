# ImporterNaturesComptables

## Nom de la tâche


ImporterNaturesComptables


## Description de la tâche


Crée des natures comptables par import de fichier texte.


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


Nom=ImporterNaturesComptables


Journal=ImporterNaturesComptables.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


FichierImporter=ImporterNaturesComptables.txt


