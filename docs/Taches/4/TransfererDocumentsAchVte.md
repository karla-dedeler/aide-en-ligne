# TransfererDocumentsAchVte

## Nom de la tâche


TransfererDocumentsAchVte


## Description de la tâche


Transfère des documents d'achat ou de vente par import de fichier texte.


## Paramètres spécifiques de la tâche










| Nom | Description | Valeurs possibles | Présence | Valeur par défaut |
|---|---|---|---|---|
| FichierImporter | Fichier à importer |   | Obligatoire |   |
| TransfertPartiel | Transfert partiel | AvecReliquat <br>SansReliquat
PasDeTransfert | Facultatif | AvecReliquat |
| CreerLigneQuantite0 | Créer une ligne avec une quantité à 0 en cas de stock absent | Oui <br>Non | Facultatif | Non |
| RecopierLignesTextes | Recopier les lignes de texte du document source | Oui
Non | Facultatif | Non |
| RecopierLignesTotaux | Recopier les lignes de sous-total et total du document source | Oui <br>Non | Facultatif | Non |
| RenommerFichier | Renommer le fichier | Oui <br>Non | Facultatif | Non |


## Exemple

````
[Tâche]
Nom=TransfererDocumentsAchVte
Journal=TransfererDocumentsAchVte.log

[Société]
Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum
Utilisateur=DEMO

[Paramètres]
FichierImporter=D:\TransfererDocumentsAchVte.txt
TransfertPartiel=AvecReliquat
CreerLigneQuantite0=Non
RecopierLignesTextes=Oui
RecopierLignesTotaux=Oui
RenommerFichier=Non
````