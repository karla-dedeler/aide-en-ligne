# Requête de création de commerciaux


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/Commerciaux/%22Importer%22
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
| fichier\_commerciaux | Tableau de commerciaux à importer | Obligatoire |


## Exemple

````
{
    "importer_commerciaux": {
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
            "fichier_commerciaux": [
                "REP_CODE;REP_CIVILE;REP_PRENOM;REP_NOM;REP_TELB;REP_TELM",
                "GLE;Monsieur;Grégoire;LETERTRE;0134840984;0613257896"
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
                "10/09/2019 17:51:56 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 17:52:02 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 17:52:02 Lancement de la tâche ImporterCommerciaux",
                "10/09/2019 17:52:02 L'import a été effectué avec succès.",
                "10/09/2019 17:52:02 Nombre de lignes importées : 1",
                "10/09/2019 17:52:02 Nombre de lignes non importées : 0",
                "10/09/2019 17:52:02 Tâche ImporterCommerciaux terminée",
                "10/09/2019 17:52:02 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````