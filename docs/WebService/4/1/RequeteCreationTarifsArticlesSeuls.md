# Requête de création de tarifs articles seuls


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/TarifsArticles/%22Importer%22
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
| fichier\_tarifs\_articles | Tableau de tarifs d'articles seuls à importer | Obligatoire |


## Exemple

````
{
    "importer_tarifs_articles": {
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
            "fichier_tarifs_articles": [
                "ART_CODE;ART_P_ACH;ART_P_COEF;ART_P_VTE;DEV_CODE",
                "A10;10;2;20;EUR",
                "A20;20;2;40;EUR"
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
                "13/09/2019 16:24:56 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 16:25:01 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 16:25:02 Lancement de la tâche ImporterTarifsArticles",
                "13/09/2019 16:25:03 L'import a été effectué avec succès.",
                "13/09/2019 16:25:03 Nombre de lignes importées : 2",
                "13/09/2019 16:25:03 Nombre de lignes non importées : 0",
                "13/09/2019 16:25:03 Tâche ImporterTarifsArticles terminée",
                "13/09/2019 16:25:03 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````