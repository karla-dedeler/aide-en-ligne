# Requête de création de villes


## D## Disponibilité


Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/Villes/%22Importer%22
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
| fichier\_villes | Tableau de villes à importer | Obligatoire |


## Exemple

````
{
    "importer_villes": {
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
            "fichier_villes": [
                "VIL_CODE;VIL_NOM;PAY_CODE",
                "78333;Rambouillet Cedex 333;FR"
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
                "10/09/2019 14:25:35 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 14:25:42 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 14:25:42 Lancement de la tâche ImporterVilles",
                "10/09/2019 14:25:42 L'import a été effectué avec succès.",
                "10/09/2019 14:25:42 Nombre de lignes importées : 1",
                "10/09/2019 14:25:42 Nombre de lignes non importées : 0",
                "10/09/2019 14:25:42 Tâche ImporterVilles terminée",
                "10/09/2019 14:25:42 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "1",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````