# Requête de création de grilles de tarifs



## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/GrillesTarifs/%22Importer%22
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
| fichier\_grilles\_tarifs | Tableau de grilles de tarifs à importer | Obligatoire |


## Exemple

````
{
    "importer_grilles_tarifs": {
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
            "fichier_grilles_tarifs": [
                "TAR_CODE;TAR_LIB;ART_CODE;TAR_PRIX;TAR_REMISE",
                "GT1;GT1;ELS;59",
                "GT1;GT1;GBLD;;10",
                "GT1;GT1;GBLG;;20"
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
                "16/09/2019 14:46:21 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "16/09/2019 14:46:27 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "16/09/2019 14:46:27 Lancement de la tâche ImporterGrillesTarifs",
                "16/09/2019 14:46:27 Nombre de lignes importées : 3",
                "16/09/2019 14:46:27 Nombre de lignes non importées : 0",
                "16/09/2019 14:46:27 Tâche ImporterGrillesTarifs terminée",
                "16/09/2019 14:46:27 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "3",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````

