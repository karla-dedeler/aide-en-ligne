# Requête de création de familles d'articles


#
## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/FamillesArticles/%22Importer%22
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
| fichier\_familles\_articles | Tableau de familles d'articles à importer | Obligatoire |


## Exemple

````
{
    "importer_familles_articles": {
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
            "fichier_familles_articles": [
                "FAR_CODE;FAR_LIB;FAR_TYPE;FAR_CATEG",
                "FAR1;Famille d'articles 1;P;F",
                "FAR2;Famille d'articles 2;P;F"
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
                "12/09/2019 11:51:38 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "12/09/2019 11:51:44 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "12/09/2019 11:51:44 Lancement de la tâche ImporterFamillesArticles",
                "12/09/2019 11:51:44 L'import a été effectué avec succès.",
                "12/09/2019 11:51:44 Nombre de lignes importées : 2",
                "12/09/2019 11:51:44 Nombre de lignes non importées : 0",
                "12/09/2019 11:51:44 Tâche ImporterFamillesArticles terminée",
                "12/09/2019 11:51:44 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````