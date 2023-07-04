# Requête de création de contacts


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 9 et +


## URL

``
api/rest/Contacts/%22Importer%22
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
| fichier\_contacts | Tableau de contacts à importer | Obligatoire |


## Exemple


````
{
    "importer_contacts": {
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
            "fichier_contacts": [
                "CCT_CODE;CCT_NOM;CCT_ORIGIN",
                "CONTACT1;Contact1;CLIENT1",
                "CONTACT2;Contact2;CLIENT1",
                "CONTACT3;Contact3;CLIENT2"
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
                "13/09/2019 14:30:38 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 14:30:43 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 14:30:43 Lancement de la tâche ImporterContacts",
                "13/09/2019 14:30:44 L'import a été effectué avec succès.",
                "13/09/2019 14:30:44 Nombre de lignes importées : 3",
                "13/09/2019 14:30:44 Nombre de lignes non importées : 0",
                "13/09/2019 14:30:44 Tâche ImporterContacts terminée",
                "13/09/2019 14:30:44 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "3",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````