# ExporterFacturesChorus

## Nom de la tâche


ExporterFacturesChorus


## Description de la tâche


Exporte des factures clients au format Chorus


## Paramètres spécifiques de la tâche










| Nom | Description | Valeurs possibles | Présence | Valeur par défaut |
| DossierDestination | Dossier de destination |   | Obligatoire |   |
| DateDebut | Date de début |   | Obligatoire |   |
| DateFin | Date de fin |   | Obligatoire |   |
| ReexporterFactures | Y compris les factures déjà exportées | Oui
Non | Facultatif | Non |


## Exemple


[Tâche]


Nom=ExporterFacturesChorus


Journal=ExporterFacturesChorus.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


DossierDestination=D:\FacturesChorus\2020\09


DateDebut=01/09/2020


DateFin=30/09/2020


