# Requête de création de documents de vente


## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/DocumentsVente/%22Importer%22
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
| fichier\_documents\_vente | Tableau de documents d'achat à importer | Obligatoire |


## Exemple

````
{
    "importer_documents_vente": {
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
            "fichier_documents_vente": [
                "DOC_STYPE;DOC_DATE;DOC_DT_PRV;DOC_REFPCF;PCF_CODE;REP_CODE;PRJ_CODE;ART_CODE;LIG_QTE;LIG_P_BRUT;LIG_REMISE",
                "C;25/12/2018;25/12/2018;CC20181225;MA0001;CO1;A11;NL;10;20;2",
                "C;25/12/2018;25/12/2018;CC20181225;MA0001;CO1;A11;EV;2;15;2"
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
                "12/09/2019 15:54:03 Ouverture de la société C:\\ProgramData\\Gestimum\\ET-TEST.Gestimum",
                "12/09/2019 15:54:07 Société C:\\ProgramData\\Gestimum\\ET-TEST.Gestimum ouverte",
                "12/09/2019 15:54:07 Lancement de la tâche ImporterDocumentsVente",
                "12/09/2019 15:54:11 L'import a été effectué avec succès.",
                "12/09/2019 15:54:11 Nombre de lignes importées : 2",
                "12/09/2019 15:54:11 Nombre de lignes non importées : 0",
                "12/09/2019 15:54:11 La pièce ARC17-00051 a été créée",
                "12/09/2019 15:54:11 Tâche ImporterDocumentsVente terminée",
                "12/09/2019 15:54:11 Fermeture de la société C:\\ProgramData\\Gestimum\\ET-TEST.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````