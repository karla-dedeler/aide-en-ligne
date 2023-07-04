# Requête de création de glossaires


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Glossaires/%22Importer%22
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
| fichier\_glossaires | Tableau de glossaires à importer | Obligatoire |


## Exemple

````
{
    "importer_glossaires": {
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
            "fichier_glossaires": [
                "TXT_CODE;TXT_MEMO",
                "SERVICELIVRAISON;Information : Nous avons un nouveau service de livraison ...",
                "LOREMIPSUM;Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
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
                "12/09/2019 10:27:25 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "12/09/2019 10:27:31 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "12/09/2019 10:27:31 Lancement de la tâche ImporterGlossaires",
                "12/09/2019 10:27:31 L'import a été effectué avec succès.",
                "12/09/2019 10:27:31 Nombre de lignes importées : 2",
                "12/09/2019 10:27:31 Nombre de lignes non importées : 0",
                "12/09/2019 10:27:31 Tâche ImporterGlossaires terminée",
                "12/09/2019 10:27:31 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````