# Requête de création de documents d'achat



## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/DocumentsAchat/%22Importer%22
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
| fichier\_documents\_achat | Tableau de documents d'achat à importer | Obligatoire |


## Exemple

````
{
    "importer_documents_achat": {
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
            "fichier_documents_achat": [
                "DOC_STYPE;DOC_DATE;DOC_DT_PRV;PCF_CODE;ART_CODE;LIG_QTE",
                "C;20/12/2018;22/12/2018;HU0001;NL;1",
                "C;28/12/2018;29/12/2018;HU0001;TRA;2",
                "C;28/12/2018;29/12/2018;HU0001;NL;3"
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
                "12/09/2019 15:39:45 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "12/09/2019 15:39:51 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "12/09/2019 15:39:51 Lancement de la tâche ImporterDocumentsAchat",
                "12/09/2019 15:39:56 L'import a été effectué avec succès.",
                "12/09/2019 15:39:56 Nombre de lignes importées : 3",
                "12/09/2019 15:39:56 Nombre de lignes non importées : 0",
                "12/09/2019 15:39:56 La pièce BCF17-00008 a été créée",
                "12/09/2019 15:39:56 La pièce BCF17-00009 a été créée",
                "12/09/2019 15:39:56 Tâche ImporterDocumentsAchat terminée",
                "12/09/2019 15:39:56 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "3",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````