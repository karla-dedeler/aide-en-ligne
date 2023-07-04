# Requête de création de natures comptables



## Disponibilité


Applications : ![](../GestionCommerciale32.png)
Versions : 8 et +


## URL

``
api/rest/NaturesComptables/%22Importer%22
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
| fichier\_natures\_comptables | Tableau de natures comptables à importer | Obligatoire |


## Exemple
````
{
    "importer_natures_comptables": {
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
            "fichier_natures_comptables": [
                "NAT_TYPE;NAT_CODE;NAT_LIB",
                "A;008;Achats Chine",
                "V;004;Ventes USA"
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
                "10/09/2019 16:18:53 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "10/09/2019 16:18:59 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "10/09/2019 16:18:59 Lancement de la tâche ImporterNaturesComptables",
                "10/09/2019 16:18:59 L'import a été effectué avec succès.",
                "10/09/2019 16:18:59 Nombre de lignes importées : 2",
                "10/09/2019 16:18:59 Nombre de lignes non importées : 0",
                "10/09/2019 16:18:59 Tâche ImporterNaturesComptables terminée",
                "10/09/2019 16:18:59 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_lignes_importées": "2",
                "nombre_lignes_non_importées": "0"
            }
        }
    ]
}
````