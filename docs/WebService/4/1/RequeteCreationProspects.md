# Requête de création de prospects



## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Prospects/%22Importer%22
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
| fichier\_prospects | Fichier de prospects à importer |  | Obligatoire |  |
| tester | Tester seulement, sans réellement importer | Oui <br>Non | Facultatif | Non |


## Exemple

````
{
    "importer_prospects": {
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
            "fichier_prospects": [
                "PCF_CODE;CPT_NUMERO;PCF_RS;PCF_RUE;PCF_CP;PCF_VILLE",
                "P42;411P42;DECAT5;6 rue de la paix;78120;RAMBOUILLET"
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
                "10/09/2019 18:59:14 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 18:59:20 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 18:59:20 Lancement de la tâche ImporterProspects",
                "10/09/2019 18:59:20 L'import a été effectué avec succès.",
                "10/09/2019 18:59:20 Nombre de lignes importées : 1",
                "10/09/2019 18:59:20 Nombre de lignes non importées : 0",
                "10/09/2019 18:59:20 Tâche ImporterProspects terminée",
                "10/09/2019 18:59:20 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````