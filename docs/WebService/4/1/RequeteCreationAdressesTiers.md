# Requête de création d'adresses de tiers



## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/AdressesTiers/%22Importer%22
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
| fichier\_adresses\_tiers | Tableau des adresses de tiers à importer | Obligatoire |


## Exemple

````
{
    "importer_adresses_tiers": {
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
            "fichier_adresses_tiers": [
                "ADR_CODE;ADR_NUMERO;ADR_RS;ADR_RUE;ADR_CP;ADR_VILLE;PAY_CODE",
                "CLIENT1;001;Client 1;5 rue Cugnot;78120;Rambouillet;FR",
                "CLIENT1;002;Client 1 - Adresse 2;7 rue Cugnot;78120;Rambouillet;FR",
                "CLIENT1;003;Client 1 - Adresse 3;9 rue Cugnot;78120;Rambouillet;FR",
                "CLIENT2;001;Client 2;Place du Jeu de Paume;78730;Saint-Arnoult-en-Yvelines;FR"
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
                "09/09/2019 18:47:26 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "09/09/2019 18:47:31 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "09/09/2019 18:47:31 Lancement de la tâche ImporterAdressesTiers",
                "09/09/2019 18:47:32 L'import a été effectué avec succès.",
                "09/09/2019 18:47:32 Nombre de lignes importées : 4",
                "09/09/2019 18:47:32 Nombre de lignes non importées : 0",
                "09/09/2019 18:47:32 Tâche ImporterAdressesTiers terminée",
                "09/09/2019 18:47:32 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "4",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````