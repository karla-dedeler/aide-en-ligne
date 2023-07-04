# Requête de création de comptes


## Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/Comptes/%22Importer%22
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
| fichier\_comptes | Tableau de comptes de tiers à importer |   | Obligatoire |   |
| calculer\_code\_tiers |   | Oui <br>Non | Facultatif | Non |
| calculer\_numero\_compte |   | Oui <br>Non | Facultatif | Non |
| tester | Tester seulement, sans réellement importer | Oui <br>Non | Facultatif | Non |


## Exemple

````
{
    "importer_comptes": {
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
            "fichier_comptes": [
                "CPT_NUMERO;CPT_LIB;CPT_TYPE;PCF_CODE;CPT_TVA_NC",
                "411JOHNDOE;John Doe;C;JOHNDOE",
                "70700202;Ventes de produits finis;G;;445660"
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
                "16/09/2019 17:39:43 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "16/09/2019 17:39:49 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "16/09/2019 17:39:49 Lancement de la tâche ImporterComptes",
                "16/09/2019 17:39:49 L'import a été effectué avec succès.",
                "16/09/2019 17:39:49 Nombre de lignes importées : 2",
                "16/09/2019 17:39:49 Nombre de lignes non importées : 0",
                "16/09/2019 17:39:49 Tâche ImporterComptes terminée",
                "16/09/2019 17:39:49 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````