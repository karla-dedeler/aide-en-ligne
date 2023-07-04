# Requête de création de sous-familles d'articles


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/SousFamilles/%22Importer%22
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
| fichier\_sousfamilles\_articles | Tableau de sous-familles d'articles à importer | Obligatoire |


## Exemple

````
{
    "importer_sousfamilles_articles": {
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
            "fichier_sousfamilles_articles": [
                "SFA_CODE;SFA_LIB;SFA_TYPE;SFA_CATEG",
                "SFAR1;Sous-famille d'articles 1;P;F",
                "SFAR2;Sous-famille d'articles 2;P;F"
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
                "12/09/2019 11:42:25 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "12/09/2019 11:42:30 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "12/09/2019 11:42:30 Lancement de la tâche ImporterSousFamillesArticles",
                "12/09/2019 11:42:30 L'import a été effectué avec succès.",
                "12/09/2019 11:42:30 Nombre de lignes importées : 2",
                "12/09/2019 11:42:30 Nombre de lignes non importées : 0",
                "12/09/2019 11:42:30 Tâche ImporterSousFamillesArticles terminée",
                "12/09/2019 11:42:30 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````