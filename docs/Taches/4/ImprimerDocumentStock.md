# ImprimerDocumentStock

## Nom de la tâche


ImprimerDocumentStock


## Description de la tâche


Imprime un document de stock


## Paramètres spécifiques de la tâche










| Nom | Description | Valeurs possibles | Présence | Valeur par défaut |
| NumeroInterne | Numéro interne de document à imprimer |   | Obligatoire \* |   |
| NumeroPiece | Numéro de pièce de document à imprimer |   | Obligatoire \* |   |
| NomModele | Nom complet du modèle |   | Obligatoire |   |
| ImprimerVers | Imprimer vers |   | Obligatoire |   |
| DossierFichierPDF | Dossier de stockage du fichier PDF |   | Facultatif | Dossier des fichiers temporaires paramétré dans les préférences utilisateur |
| NomFichierPDF | Nom du fichier PDF |   | Facultatif | Numéro de pièce ou numéro interne passé en paramètre |
| NombreExemplaires | Nombre d'exemplaires |   | Facultatif | 1 |
| JoindreFichiersChampsPersonnalises | Joindre les fichiers des champs personnalisés | Oui
Non | Facultatif | Non |
| CreerAction | Créer une action | Oui
Non | Facultatif | Non |
| TypeAction | Type d'action |   | Facultatif |   |


 


\* : NumeroInterne et NumeroPiece ne sont pas obligatoires tous les deux. L'un des deux doit être renseigné.


## Exemple


[Tâche]


Nom=ImprimerDocumentStock


Journal=ImprimerDocumentStock.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


NumeroInterne=0004544785


NomModele=Entrees.DocStocks.rpm


ImprimerVers=Microsoft Print to PDF


