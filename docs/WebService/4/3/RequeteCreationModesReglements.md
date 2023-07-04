# Requête de création de modes de règlements


## Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/ModesReglements/%22Importer%22
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
| fichier\_modes\_reglements | Tableau de modes de règlements à importer | Obligatoire |


## Exemple

````
{
    "importer_modes_reglements": {
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
            "fichier_modes_reglements": [
                "REG_CODE;REG_LIB;REG_TYPE;REG_NBJ;REG_FDM",
                "CHQ45;Chèque 45 jours fin de mois;CHQ;45;1"
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
                "10/09/2019 16:38:53 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 16:38:59 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 16:38:59 Lancement de la tâche ImporterModesReglements",
                "10/09/2019 16:38:59 L'import a été effectué avec succès.",
                "10/09/2019 16:38:59 Nombre de lignes importées : 1",
                "10/09/2019 16:38:59 Nombre de lignes non importées : 0",
                "10/09/2019 16:38:59 Tâche ImporterModesReglements terminée",
                "10/09/2019 16:38:59 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````