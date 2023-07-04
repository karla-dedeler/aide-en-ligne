# Requête de création de banques de tiers


## Disponibilité






Applications : ![](../GestionCommerciale32.png)![](../GestionComptable32.png)
Versions : 8 et +


## URL

``
api/rest/BanquesTiers/%22Importer%22
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
| fichier\_banques\_tiers | Tableau de banques de tiers à importer |   | Obligatoire |   |
| tester | Tester seulement, sans réellement importer | Oui 
Non | Facultatif | Non |


## Exemple

````
{
    "importer_banques_tiers": {
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
            "fichier_banques_tiers": [
                "PCF_CODE;RIB_ORDRE;RIB_BQ_NUM;RIB_BQ_NOM;RIB_TYPE;RIB_IBAN;RIB_GUICHE;RIB_AGENCE;RIB_COMPTE;RIB_CLE;RIB_DT_SM;RIB_RUM;RIB_SEQPRE",
                "CLIENT1;01;001;CA;FR;FR76;12345;67890;12345678901;11;15/10/2016;TCA20;FRST",
                "CLIENT1;02;002;BNP;FR;FR76;12345;67890;12345678901;12;16/10/2016;BTCA21;FRST",
                "CLIENT1;03;003;LCL;FR;FR76;12345;67890;12345678901;13;17/10/2016;BTCA22;FRST"
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
                "10/09/2019 12:02:42 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 12:02:48 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 12:02:48 Lancement de la tâche ImporterBanquesTiers",
                "10/09/2019 12:02:48 L'import a été effectué avec succès.",
                "10/09/2019 12:02:48 Nombre de lignes importées : 3",
                "10/09/2019 12:02:48 Nombre de lignes non importées : 0",
                "10/09/2019 12:02:48 Attention ! Le numéro BBAN 67890123451234567890111 n'est pas valide.",
                "10/09/2019 12:02:48 Attention ! Le numéro BBAN 67890123451234567890112 n'est pas valide.",
                "10/09/2019 12:02:48 Attention ! Le numéro BBAN 67890123451234567890113 n'est pas valide.",
                "10/09/2019 12:02:48 Tâche ImporterBanquesTiers terminée",
                "10/09/2019 12:02:48 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "3",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````