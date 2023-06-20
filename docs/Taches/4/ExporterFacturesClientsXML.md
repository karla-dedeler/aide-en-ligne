# ExporterFacturesClientsXML
## Nom de la tâche


ExporterFacturesClientsXML


## Description de la tâche


Exporte des factures et avoirs clients au format XML


## Paramètres spécifiques de la tâche








| Nom | Description | Présence |
| DossierDestination | Dossier de destination | Obligatoire |
| DateDebut | Date de début | Obligatoire |
| DateFin | Date de fin | Obligatoire |


## Exemple


[Tâche]


Nom=ExporterFacturesClientsXML


Journal=ExporterFacturesClientsXML.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


DossierDestination=D:\FacturesClientsXML


DateDebut=01/01/2018


DateFin=31/12/2018


