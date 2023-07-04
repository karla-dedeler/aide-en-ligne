# Requête de création d'utilisateurs

## Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/Utilisateurs/%22Importer%22
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
| fichier\_utilisateurs | Tableau d'utilisateurs à importer | Obligatoire |


## Exemple

````
{
    "importer_utilisateurs": {
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
            "fichier_utilisateurs": [
                "USR_NAME;USR_GROUPE;SAL_CODE",
                "BSP;ADMIN;BSP",
                "MBL;ADMIN;MBL",
                "EGA;ADMIN;EGA"
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
                "10/09/2019 11:25:32 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 11:25:38 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 11:25:38 Lancement de la tâche ImporterUtilisateurs",
                "10/09/2019 11:25:38 L'import a été effectué avec succès.",
                "10/09/2019 11:25:38 Nombre de lignes importées : 3",
                "10/09/2019 11:25:38 Nombre de lignes non importées : 0",
                "10/09/2019 11:25:38 Tâche ImporterUtilisateurs terminée",
                "10/09/2019 11:25:38 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "3",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````