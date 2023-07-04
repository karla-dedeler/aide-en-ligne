# Requête de création de clients


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Clients/%22Importer%22
``

## Méthode

``
POST
``

## Paramètres


Cette requête prend des paramètres sous la forme d'un [objet JSON](../ObjetJSONParametreRequetes.md).


### Paramètres spécifiques


| Paramètre | Description | Valeurs possibles | Présence | Valeur par défaut |
|---|---|---|---|---|
| fichier\_clients | Tableau de clients à importer |   | Obligatoire |   |
| tester | Tester seulement, sans réellement importer | Oui <br>Non | Facultatif | Non |


## Exemple

````
{
    "importer_clients": {
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
            "fichier_clients": [
                "PCF_CODE;CPT_NUMERO;PCF_RS;PCF_RUE;PCF_COMP;PCF_CP;PCF_VILLE",
                "C42;411C42;SPORT25;5 rue Cugnot;ZA Du Pâtis;78120;RAMBOUILLET"
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
                "10/09/2019 18:57:29 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 18:57:35 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 18:57:35 Lancement de la tâche ImporterClients",
                "10/09/2019 18:57:35 L'import a été effectué avec succès.",
                "10/09/2019 18:57:35 Nombre de lignes importées : 1",
                "10/09/2019 18:57:35 Nombre de lignes non importées : 0",
                "10/09/2019 18:57:35 Tâche ImporterClients terminée",
                "10/09/2019 18:57:35 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````