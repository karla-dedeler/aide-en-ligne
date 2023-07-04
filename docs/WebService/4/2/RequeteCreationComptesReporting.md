# Requête de création de comptes de reporting


## Disponibilité

Applications : ![](../GestionComptable32.png) 
Versions : 8 et + 


## URL

``
api/rest/ComptesReporting/%22Importer%22
``

## Méthode

``
POST
``

## Paramètres


Cette requête prend des paramètres sous la forme d'un [objet JSON](../ObjetJSONParametreRequetes.md).


### Paramètres spécifiques







| Paramètre | Description | Présence |
|---|---|---|
| fichier\_comptes\_reporting | Tableau de comptes de reporting à importer | Obligatoire |


## Exemple

````
{
    "importer\_comptes\_reporting": {
        "societe": {
            "fichier": "DEMO.Gestimum",
            "utilisateur": "DEMO",
            "mot\_passe": "",
            "deconnecter": "Non",
            "exclusif": "Non"
        },
        "parametres": {
            "journal": "Oui",
            "statistiques": "Oui",
            "entete": "Oui",
            "noms\_champs": "",
            "separateur\_champs": ";",
            "identificateur\_texte": "",
            "fichier\_comptes\_reporting": [
                "RPT\_COMPTE;RPT\_LIB;RPT\_TYPE",
                "6;Charges;R",
                "600;Charges Commerciales;G"
            ]
        }
    }
}
````

## Retour

````
{
    "result": [
        {
            "resultat": "succès",
            "message": "terminé",
            "journal": [
                "10/09/2019 17:34:36 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 17:34:42 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 17:34:42 Lancement de la tâche ImporterComptesReporting",
                "10/09/2019 17:34:42 L'import a été effectué avec succès.",
                "10/09/2019 17:34:42 Nombre de lignes importées : 2",
                "10/09/2019 17:34:42 Nombre de lignes non importées : 0",
                "10/09/2019 17:34:42 Tâche ImporterComptesReporting terminée",
                "10/09/2019 17:34:42 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre\_lignes\_importées": "2",
                "nombre\_lignes\_non\_importées": "0"
            }
        }
    ]
}
````