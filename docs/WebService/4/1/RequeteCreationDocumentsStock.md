# Requête de création de documents de stock


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/DocumentsStock/%22Importer%22
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
| fichier\_documents\_stock | Tableau de documents d'achat à importer | Obligatoire |


## Exemple

````
{
    "importer_documents_stock": {
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
            "fichier_documents_stock": [
                "DOC_STYPE;DEP_CODE;ART_CODE;MVT_QTE",
                "E;001;ELS;20"
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
                "12/09/2019 16:28:06 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "12/09/2019 16:28:11 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "12/09/2019 16:28:11 Lancement de la tâche ImporterDocumentsStock",
                "12/09/2019 16:28:11 L'import a été effectué avec succès.",
                "12/09/2019 16:28:11 Nombre de lignes importées : 1",
                "12/09/2019 16:28:11 Nombre de lignes non importées : 0",
                "12/09/2019 16:28:11 La pièce ENT17-00017 a été créée",
                "12/09/2019 16:28:11 Tâche ImporterDocumentsStock terminée",
                "12/09/2019 16:28:11 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````