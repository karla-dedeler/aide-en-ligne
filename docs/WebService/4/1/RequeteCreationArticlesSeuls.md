# Requête de création d'articles seuls


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Articles/%22Importer%22
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
| fichier\_articles | Tableau d'articles seuls à importer | Obligatoire |


## Exemple

````
{
    "importer_articles": {
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
            "fichier_articles": [
                "ART_CODE;ART_LIB;ART_P_ACH;ART_P_COEF;ART_P_VTE",
                "A10;Article10;10;2;20",
                "A20;Article20;20;2;40"
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
                "13/09/2019 14:49:24 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 14:49:30 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 14:49:30 Lancement de la tâche ImporterArticles",
                "13/09/2019 14:49:30 L'import a été effectué avec succès.",
                "13/09/2019 14:49:30 Nombre de lignes importées : 2",
                "13/09/2019 14:49:30 Nombre de lignes non importées : 0",
                "13/09/2019 14:49:30 Tâche ImporterArticles",
                "13/09/2019 14:49:30 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````