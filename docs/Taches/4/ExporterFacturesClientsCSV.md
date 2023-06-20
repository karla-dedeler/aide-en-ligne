# ExporterFacturesClientsCSV
## Nom de la tâche


ExporterFacturesClientsCSV


## Description de la tâche


Exporte des factures et avoirs clients au format CSV pour l'administration fiscale


## Paramètres spécifiques de la tâche








| Nom | Description | Présence |
| DossierDestination | Dossier de destination | Obligatoire |
| DateDebut | Date de début | Obligatoire |
| DateFin | Date de fin | Obligatoire |


## Exemple


[Tâche]


Nom=ExporterFacturesClientsCSV


Journal=ExporterFacturesClientsCSV.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


DossierDestination=D:\FacturesClientsCSV


DateDebut=01/01/2018


DateFin=31/12/2018


