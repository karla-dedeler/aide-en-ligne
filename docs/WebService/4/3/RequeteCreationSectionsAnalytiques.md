# Requête de création de sections analytiques


### Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/SectionsAnalytiques/%22Importer%22
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
| fichier\_sections\_analytiques | Tableau de sections analytiques à importer | Obligatoire |


## Exemple

````
{
    "importer_sections_analytiques": {
        "societe": {
            "fichier": "DEMO.Gestimum",
            "utilisateur": "DEMO",
            "mot_passe": "",
            "deconnecter": "Non",
            "exclusif": "Non"
        },
        "parametres": {
            "journal": "Oui",
            "statistiques": "Oui",
            "entete": "Oui",
            "noms_champs": "",
            "separateur_champs": ";",
            "identificateur_texte": "",
            "fichier_sections_analytiques": [
                "ANA_CODE;ANA_LIB;ANA_TYPE;ANA_PLAN;ANA_COUT",
                "15;Pack Equipement 15;G;001;SC"
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
                "10/09/2019 18:10:23 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 18:10:28 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 18:10:28 Lancement de la tâche ImporterSectionsAnalytiques",
                "10/09/2019 18:10:28 L'import a été effectué avec succès.",
                "10/09/2019 18:10:28 Nombre de lignes importées : 1",
                "10/09/2019 18:10:28 Nombre de lignes non importées : 0",
                "10/09/2019 18:10:28 Tâche ImporterSectionsAnalytiques terminée",
                "10/09/2019 18:10:28 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````