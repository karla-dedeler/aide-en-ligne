# Requête de création de composants d'articles seuls


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/ComposantsNomenclatures/%22Importer%22
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
| fichier\_composants\_nomenclatures | Tableau de composants d'articles seuls à importer | Obligatoire |


## Exemple


````
{
    "importer_composants_nomenclatures": {
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
            "fichier_composants_nomenclatures": [
                "ART_CODE;PRD_CODE",
                "N30;A10",
                "N30;A20"
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
                "13/09/2019 16:01:51 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "13/09/2019 16:01:57 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "13/09/2019 16:01:57 Lancement de la tâche ImporterComposantsNomenclatures",
                "13/09/2019 16:01:58 L'import a été effectué avec succès.",
                "13/09/2019 16:01:58 Nombre de lignes importées : 2",
                "13/09/2019 16:01:58 Nombre de lignes non importées : 0",
                "13/09/2019 16:01:58 Tâche ImporterComposantsNomenclatures terminée",
                "13/09/2019 16:01:58 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````