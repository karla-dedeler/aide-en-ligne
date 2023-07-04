# Requête de création d'affaires


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Affaires/%22Importer%22
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
| fichier\_affaires | Tableau des affaires à importer | Obligatoire |


## Exemple

````
{
    "importer_affaires": {
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
            "fichier_affaires": [
                "PRJ_CODE;PRJ_LIB;PRJ_ETAT;PRJ_GROUP1;PRJ_GROUP2;PRJ_DT_DEB;PRJ_DT_FIN",
                "COA2019;COA2019;ENC;COA;COA1;01/09/2019;15/19/2019",
                "STA2019;STA2019;ENC;STA;STA2;01/10/2019;15/10/2019"
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
                "10/09/2019 13:59:46 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 13:59:52 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 13:59:52 Lancement de la tâche ImporterAffaires",
                "10/09/2019 13:59:52 L'import a été effectué avec succès.",
                "10/09/2019 13:59:52 Nombre de lignes importées : 2",
                "10/09/2019 13:59:52 Nombre de lignes non importées : 0",
                "10/09/2019 13:59:52 Tâche ImporterAffaires terminée",
                "10/09/2019 13:59:52 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````