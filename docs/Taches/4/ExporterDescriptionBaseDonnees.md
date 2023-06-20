# ExporterDescriptionBaseDonnees

## Nom de la tâche


ExporterDescriptionBaseDonnees


## Description de la tâche


Exporte la description des tables, des champs, des clés primaires, des clés secondaires et des procédures stockées de la base de données dans un fichier XML avec une feuille de style XSL.


## Paramètre spécifique de la tâche








| Nom | Description | Présence |
| FichierDestination | Fichier de destination | Obligatoire |


## Exemple


[Tâche]


Nom=ExporterDescriptionBaseDonnees


Journal=ExporterDescriptionBaseDonnees.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


FichierDestination=D:\ExporterDescriptionBaseDonnees.xml


