# Requête de création de références clients d'articles seules


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/ReferencesClientsArticles/%22Importer%22
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
| fichier\_references\_clients\_articles | Tableau de références clients d'articles seules à importer | Obligatoire |


## Exemple

````
{
    "importer_references_clients_articles": {
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
            "fichier_references_clients_articles": [
                "ART_CODE;PCF_CODE;ART_PCLIENT;ART_REFCLI",
                "A10;C1;5;A10001",
                "A10;C2;5;A10002"
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
                "13/09/2019 16:16:56 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 16:17:02 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 16:17:02 Lancement de la tâche ImporterReferencesClientsArticles",
                "13/09/2019 16:17:02 Nombre de lignes importées : 0",
                "13/09/2019 16:17:02 Nombre de lignes non importées : 2",
                "13/09/2019 16:17:02 La ligne 1 n'a pas pu être importée :",
                "13/09/2019 16:17:02 Code manquant",
                "13/09/2019 16:17:02 La ligne 2 n'a pas pu être importée :",
                "13/09/2019 16:17:02 Code manquant",
                "13/09/2019 16:17:02 Tâche ImporterReferencesClientsArticles terminée",
                "13/09/2019 16:17:02 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "0",
                "nombre_lignes_non_importées": "2"
            }
        }
    ]
}
````