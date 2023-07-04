# Requête de création d'immobilisations


## Disponibilité


Applications : ![](../GestionComptable32.png) 
Versions : 9 et +


## URL

``
api/rest/Immobilisations/%22Importer%22
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
| fichier\_immobilisations | Tableau d'immobilisations à importer | Obligatoire |


## Exemple

````
{
    "importer_immobilisations": {
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
            "fichier_immobilisations": [
                "IMO_CODE;IMO_LIB;IMO_TYPE;IMO_CAT;IMO_DTACQ;IMO_DTSERV",
                "IMMEUBLE1;Immeuble1;B;C;01/09/2019;05/09/2019"
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
                "11/09/2019 17:51:56 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "11/09/2019 17:52:02 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "11/09/2019 17:52:02 Lancement de la tâche ImporterImmobilisations",
                "11/09/2019 17:52:02 L'import a été effectué avec succès.",
                "11/09/2019 17:52:02 Nombre de lignes importées : 1",
                "11/09/2019 17:52:02 Nombre de lignes non importées : 0",
                "11/09/2019 17:52:02 Tâche ImporterImmobilisationsterminée",
                "11/09/2019 17:52:02 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````