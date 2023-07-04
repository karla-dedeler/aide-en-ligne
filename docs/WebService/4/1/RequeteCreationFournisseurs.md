# Requête de création de fournisseurs


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Fournisseurs/%22Importer%22
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
| fichier\_fournisseurs | Fichie de fournisseurs à importer |   | Obligatoire |   |
| tester | Tester seulement, sans réellement importer | Oui <br>Non | Facultatif | Non |


## Exemple

````
{
    "importer_fournisseurs": {
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
            "fichier_fournisseurs": [
                "PCF_CODE;CPT_NUMERO;PCF_RS;PCF_RUE;PCF_COMP;PCF_CP;PCF_VILLE",
                "F42;401F42;NIKE;5 rue Cugnot;ZA Du Pâtis;78120;RAMBOUILLET"
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
                "10/09/2019 18:58:58 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 18:59:03 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 18:59:03 Lancement de la tâche ImporterFournisseurs",
                "10/09/2019 18:59:04 L'import a été effectué avec succès.",
                "10/09/2019 18:59:04 Nombre de lignes importées : 1",
                "10/09/2019 18:59:04 Nombre de lignes non importées : 0",
                "10/09/2019 18:59:04 Tâche ImporterFournisseurs terminée",
                "10/09/2019 18:59:04 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````