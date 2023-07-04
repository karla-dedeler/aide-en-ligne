# Requête de création de salariés

## Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/Salaries/%22Importer%22
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
| fichier\_salaries | Tableau de salariés à importer | Obligatoire |


## Exemple

````
{
    "importer_salaries": {
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
            "fichier_salaries": [
                "SAL_CODE;SAL_PRENOM;SAL_NOM",
                "BSP;Bastien;SPANGHERO",
                "MBL;Mélodie;BLONDEAU",
                "EGA;Esther;GAUDIN"
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
                "10/09/2019 11:02:35 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 11:02:41 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 11:02:41 Lancement de la tâche ImporterSalaries",
                "10/09/2019 11:02:41 L'import a été effectué avec succès.",
                "10/09/2019 11:02:41 Nombre de lignes importées : 3",
                "10/09/2019 11:02:41 Nombre de lignes non importées : 0",
                "10/09/2019 11:02:41 Tâche ImporterSalaries terminée",
                "10/09/2019 11:02:41 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "3",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````