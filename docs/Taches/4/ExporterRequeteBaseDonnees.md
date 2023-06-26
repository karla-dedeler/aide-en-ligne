# ExporterRequeteBaseDonnees

## Nom de la tâche


ExporterRequeteBaseDonnees


## Description de la tâche


Exporte le contenu des tables de la base de données dans un fichier CSV.


## Paramètres spécifiques de la tâche








| Nom | Description | Présence |
|---|---|---|
| FichierDestination | Fichier de destination | Obligatoire |
| Requete | Requête à exécuter | Obligatoire |
| NomColonnes | Afficher les noms des colonnes en première ligne | Obligatoire |


## Exemple

````
[Tâche]
Nom=ExporterRequeteBaseDonnees
Journal=ExporterRequeteBaseDonnees.log

[Société]
Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum
Utilisateur=DEMO
Deconnecter=Non
Exclusif=Non

[Paramètres]
FichierDestination=C:\ProgramData\Gestimum
Requete=SELECT T.PCF\_RS, T.REG\_CODE, M.REG\_LIB FROM TIERS T LEFT OUTER JOIN MODE\_REG M ON M.REG\_CODE = T.REG\_CODE WHERE T.PCF\_TYPE = 'C'
NomColonnes=Oui
````