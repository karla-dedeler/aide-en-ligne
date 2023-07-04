# Requête de création d'actions



## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Actions/%22Importer%22
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
| fichier\_actions | Tableau d'actions à importer | Obligatoire |


## Exemple

````
{
    "importer_actions": {
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
            "fichier_actions": [
                "ACT_DATE;ACT_TYPE;ACT_OBJET;ACT_FILE;PRJ_CODE",
                "05/09/2019;IMPORT;Import d'actions;D:\\ImporterActions.txt;AFFAIRE1",
                "09/09/2019;IMPORT;Suite de l'import d'actions;D:\\ImporterActions2.txt;AFFAIRE1"
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
                "10/09/2019 11:04:40 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 11:04:46 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 11:04:46 Lancement de la tâche ImporterActions",
                "10/09/2019 11:04:46 L'import a été effectué avec succès.",
                "10/09/2019 11:04:46 Nombre de lignes importées : 2",
                "10/09/2019 11:04:46 Nombre de lignes non importées : 0",
                "10/09/2019 11:04:46 Tâche ImporterActions terminée",
                "10/09/2019 11:04:46 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````