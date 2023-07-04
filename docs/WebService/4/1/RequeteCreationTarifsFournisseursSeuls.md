# Requête de création de tarifs fournisseurs seuls


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/TarifsFournisseursArticles/%22Importer%22
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
| fichier\_tarifs\_fournisseurs\_articles | Tableau de tarifs fournisseurs d'articles seuls à importer | Obligatoire |


## Exemple
````
{
    "importer_tarifs_fournisseurs_articles": {
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
            "fichier_tarifs_fournisseurs_articles": [
                "ART_CODE;ART_P_ACH;DEV_CODE;PCF_CODE;ART_PFOURN",
                "A10;8;EUR;F10;5"
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
                "13/09/2019 16:30:15 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 16:30:21 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 16:30:21 Lancement de la tâche ImporterTarifsFournisseursArticles",
                "13/09/2019 16:30:22 L'import a été effectué avec succès.",
                "13/09/2019 16:30:22 Nombre de lignes importées : 1",
                "13/09/2019 16:30:22 Nombre de lignes non importées : 0",
                "13/09/2019 16:30:22 Tâche ImporterTarifsFournisseursArticles terminée",
                "13/09/2019 16:30:22 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````