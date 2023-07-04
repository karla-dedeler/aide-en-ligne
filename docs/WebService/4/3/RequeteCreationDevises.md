# Requête de création de devises


## Disponibilité




Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +

## URL

``
api/rest/Devises/%22Importer%22
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
| fichier\_devises | Tableau de devises à importer | Obligatoire |


## Exemple

````
{
    "importer_devises": {
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
            "fichier_devises": [
                "DEV_CODE;DEV_LIB;DEV_COURS",
                "AUD;Dollar Australien;1,60",
                "CAD;Dollar Canadien;1,5101"
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
                "10/09/2019 18:25:02 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 18:25:08 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 18:25:08 Lancement de la tâche ImporterDevises",
                "10/09/2019 18:25:08 L'import a été effectué avec succès.",
                "10/09/2019 18:25:08 Nombre de lignes importées : 2",
                "10/09/2019 18:25:08 Nombre de lignes non importées : 0",
                "10/09/2019 18:25:08 La ligne 1 comporte les avertissements suivants :",
                "10/09/2019 18:25:08 La date d'actualisation et le cours de la devise ne sont modifiables que par l'assistant d'actualisation des devises.",
                "10/09/2019 18:25:08 La ligne 2 comporte les avertissements suivants :",
                "10/09/2019 18:25:08 La date d'actualisation et le cours de la devise ne sont modifiables que par l'assistant d'actualisation des devises.",
                "10/09/2019 18:25:08 Tâche ImporterDevises terminée",
                "10/09/2019 18:25:08 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````