# Requête de création d'équivalences d'articles seules


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/EquivalencesArticles/%22Importer%22
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
| fichier\_equivalences\_articles | Tableau d'équivalences d'articles seules à importer | Obligatoire |


## Exemple

````
{
    "importer_equivalences_articles": {
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
            "fichier_equivalences_articles": [
                "ART_CODE;ART_AUTRE;ART_PAUTRE",
                "A10;A20;5"
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
                "13/09/2019 16:03:44 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 16:03:50 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 16:03:50 Lancement de la tâche ImporterEquivalencesArticles",
                "13/09/2019 16:03:51 L'import a été effectué avec succès.",
                "13/09/2019 16:03:51 Nombre de lignes importées : 1",
                "13/09/2019 16:03:51 Nombre de lignes non importées : 0",
                "13/09/2019 16:03:51 Tâche ImporterEquivalencesArticles terminée",
                "13/09/2019 16:03:51 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````