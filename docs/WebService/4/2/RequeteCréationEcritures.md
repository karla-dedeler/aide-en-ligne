# Requête de création d'écritures


## Disponibilité






Applications : ![](../GestionComptable32.png) 
Versions : 8 et +


## URL

``
api/rest/Ecritures/%22Importer%22
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
| format | Format d'import | GestimumComptaVariable <br>GestimumComptaFixe <br>GestimumComptaV15 <br>GestimumGescomV15 <br>EBPV5V2000 <br>EBPV3 | Obligatoire |   |
| fichier\_ecritures | Fichier d'écritures à importer |   | Facultatif | Non |
| fichier\_comptes | Fichier de comptes à importer |   | Facultatif | Non |
| tester | Tester seulement, sans réellement importer | Oui <br>Non | Facultatif | Non |
| simulation | Créer les écritures en simulation | Oui <br>Non | Facultatif | Non |
| creer\_sections\_analytiques | Créer les sections analytiques | Oui <br>Non | Facultatif | Non |
| plan\_analytique | Code plan analytique des sections à créer |   | Facultatif |   |


## Formats


Il existe 6 formats :

| N° | Format | Nom interne | Type | Séparateur |
|---|---|---|---|---|
| 1 | Gestimum Gestion Comptable à largeur variable | GestimumComptaVariable | Largeur variable | Virgule |
| 2 | Gestimum Gestion Comptable à largeur fixe | GestimumComptaFixe  | Largeur fixe |   |
| 3 | Gestimum Gestion Comptable version 1.5 | GestimumComptaV15 | Largeur fixe |   |
| 4 | Gestimum Gestion Commerciale version 1.5 | GestimumGescomV15 | Largeur variable | Virgule |
| 5 | EBP versions 5 et 2000 | EBPV5V2000 | Largeur variable | Virgule |
| 6 | EBP version 3 | EBPV3 | Largeur variable | Virgule |


## Exemples au format GestimumComptaVariable


### Création d'une écriture de 3 lignes

````
{
    "importer\_ecritures": {
        "societe": {
            "fichier": "DEMO.Gestimum",
            "utilisateur": "DEMO",
            "mot\_passe": "",
            "deconnecter": "Non",
            "exclusif": "Non"
        },
        "parametres": {
            "journal": "Oui",
            "statistiques": "Oui",
            "format": "GestimumComptaVariable",
            "fichier\_ecritures": [
                "1,19/02/2019,VTE,411C25,,Presta,FAC19-1100425,EUR,12000,D,,02/03/2019,,CHQ,EUR",
                "2,19/02/2019,VTE,445710,,Presta,FAC19-1100425,EUR,2400,C",
                "3,19/02/2019,VTE,707100,,Presta,FAC19-1100425,EUR,9600,C"
            ],
            "tester": "Oui"
        }
    }
}
````

 


Remarque : le fichier peut contenir plusieurs écritures


### Création d'une écriture de 3 lignes avec 2 échéances

````
{
    "importer\_ecritures": {
        "societe": {
            "fichier": "DEMO.Gestimum",
            "utilisateur": "DEMO",
            "mot\_passe": "",
            "deconnecter": "Oui",
            "exclusif": "Non"
        },
        "parametres": {
            "journal": "Oui",
            "statistiques": "Oui",
            "format": "GestimumComptaVariable",
            "fichier\_ecritures": [
                "1,19/02/2019,VTE,411C25,,Presta,FAC19-1100425,EUR,12000,D,,,,CHQ,EUR",
                "E10/04/2019,CHQ,40,4800",
                "E10/04/2019,CHQ,60,7200",
                "2,19/02/2019,VTE,445710,,Presta,FAC19-1100425,EUR,2400,C",
                "3,19/02/2019,VTE,707100,,Presta,FAC19-1100425,EUR,9600,C"
            ],
            "tester": "Non"
        }
    }
}
````

### Création d'une écriture de 3 lignes avec 1 ventilation analytique

````
{
    "importer_ecritures": {
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
            "format": "GestimumComptaVariable",
            "fichier_ecritures": [
                "1,19/02/2019,VTE,411C25,,Presta,FAC19-1100425,EUR,12000,D,,02/03/2019,,CHQ,EUR",
                "2,19/02/2019,VTE,445710,,Presta,FAC19-1100425,EUR,2400,C",
                "3,19/02/2019,VTE,707100,,Presta,FAC19-1100425,EUR,9600,C",
                ">P1,S1,100,9600,100,1"
            ],
            "tester": "Oui"
        }
    }
}
````

## Exemple au format EBPV5V2000


### Création d'une écriture de 3 lignes et d'1 compte comptable

````
{
    "importer_ecritures": {
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
            "format": "EBPV5V2000",
            "fichier_ecritures": [
                "1,11/02/2019,VTE,411C24,,Presta,FAC19-1100422,12000,D,13/03/2019,,CHQ,EUR",
                "2,11/02/2019,VTE,445710,,Presta,FAC19-1100425,2400,C,,,,",
                "3,11/02/2019,VTE,707100,,Presta,FAC19-1100425,9600,C,,,,"
            ],
            "fichier_comptes": [
                "411BETATEST0404,BETA TEST 0404,BETATEST0404,5 rue Cugnot;ZA du Patis,78120,Rambouillet,FR,,0134840901,0134840902"      
            ],
            "tester":"Oui"
        }
    }
}
````

## Retour

```
{
    "result": [
        {
            "resultat": "succès",
            "message": "terminé",
            "journal": [
                "23/09/2019 11:47:22 Ouverture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum",
                "23/09/2019 11:47:25 Société C:\\ProgramData\\Gestimum\\DEMO.Gestimum ouverte",
                "23/09/2019 11:47:25 Lancement de la tâche ImporterEcritures",
                "23/09/2019 11:47:25 Ci-dessous le rapport d'import :",
                "23/09/2019 11:47:25 ############################################################",
                "23/09/2019 11:47:25 Résumé",
                "23/09/2019 11:47:25 Lignes d'écritures importables : 3",
                "23/09/2019 11:47:25 Lignes d'écritures rejetables : 0",
                "23/09/2019 11:47:25 Lignes d'échéances importables : 0",
                "23/09/2019 11:47:25 Lignes d'échéances rejetables : 0",
                "23/09/2019 11:47:25 ERREURS : 0",
                "23/09/2019 11:47:25 AVERTISSEMENTS : 0",
                "23/09/2019 11:47:25 ############################################################",
                "23/09/2019 11:47:25 Fichier d'écritures importé : D:\\Temp\\ImporterEcritures\\2019-09-23-11-47-22-048\\Ecritures.txt",
                "23/09/2019 11:47:25 Légende :",
                "23/09/2019 11:47:25 ERR : Erreur provoquant le rejet de la ligne",
                "23/09/2019 11:47:25 AV : Avertissement ne provoquant pas le rejet de la ligne",
                "23/09/2019 11:47:25 E : Ligne d'écriture",
                "23/09/2019 11:47:25 S : Section analytique",
                "23/09/2019 11:47:25 H : Ligne d'échéance",
                "23/09/2019 11:47:25 Tâche ImporterEcritures terminée",
                "23/09/2019 11:47:25 Fermeture de la société C:\\ProgramData\\Gestimum\\DEMO.Gestimum"
            ],
            "statistiques": {
                "nombre_erreurs": "0",
                "nombre_avertissements": "0",
                "nombre_lignes_écritures_importées": "3",
                "nombre_lignes_écritures_rejetées": "0",
                "nombre_lignes_échéances_importées": "0",
                "nombre_lignes_échéances_rejetées": "0",
                "nombre_lignes_analytiques_importées": "0",
                "nombre_lignes_analytiques_rejetées": "0"
            }
        }
    ]
}
````