# Requête de création de pays


## Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/Pays/%22Importer%22
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
| fichier\_pays | Tableau de pays à importer | Obligatoire |


## Exemple


````
{
    "importer_pays": {
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
            "fichier_pays": [
                "PAY_CODE;PAY_NOM",
                "NEW;Nouveau"
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
                "10/09/2019 15:06:28 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 15:06:33 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 15:06:33 Lancement de la tâche ImporterPays",
                "10/09/2019 15:06:33 L'import a été effectué avec succès.",
                "10/09/2019 15:06:33 Nombre de lignes importées : 1",
                "10/09/2019 15:06:33 Nombre de lignes non importées : 0",
                "10/09/2019 15:06:33 Tâche ImporterPays terminée",
                "10/09/2019 15:06:33 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````