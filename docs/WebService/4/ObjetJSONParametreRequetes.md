# Objet JSON en paramètre des requêtes


Toutes les requêtes de création de données requièrent un objet JSON, 
 contenant des paramètres et leurs valeurs.


## Exemple

```
{
    "importer\_immobilisations": {
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
            "entete": "Oui",
            "noms\_champs": "",
            "separateur\_champs": ";",
            "identificateur\_texte": "",
            "fichier\_glossaires": [
                "IMO\_CODE;IMO\_LIB;IMO\_TYPE;IMO\_CAT;IMO\_DTACQ;IMO\_DTSERV",
                "IMMEUBLE1;Immeuble1;B;C;01/09/2019;05/09/2019"
            ]
        }
    }
}
```

## Structure


La plupart des objets JSON ont la même structure.


 


Ils se composent de 2 parties :


* une première décrivant la société dans laquelle la requête doit 
 être exécutée, ainsi que les informations pour s'y connecter
* une deuxième décrivant les données à importer, ainsi que les 
 options d'import


 


Les paramètres de la première partie sont les mêmes dans toutes les 
 requêtes.


 


Les paramètres de la deuxième partie peuvent varier d'une requête à 
 l'autre. Cette partie peut contenir des paramètres spécifiques.


### Société









| Paramètre | Description | Valeurs possibles | Présence | Valeur par défaut |
|---|---|---|---|---|
| fichier | Chemin et nom du fichier de connexion .Gestimum <br>Si le chemin n'est pas précisé, le fichier doit se trouver dans le dossier C:\ProgramData\Gestimum |   | Obligatoire |   |
| utilisateur | Code utilisateur ERP |   | Obligatoire |   |
| mot\_passe | Mot de passe de l'utilisateur ERP |   | Facultatif |   |
| deconnecter | Déconnecter l'utilisateur déjà connecté avec ce nom | Oui <br>Non | Facultatif | Non |
| exclusif | Interdire aux autres utilisateurs de se connecter | Oui <br>Non | Facultatif | Non |


### Import









| Paramètre | Description | Valeurs possibles | Présence | Valeur par défaut |
|---|---|---|---|---|
| journal | Créer un [fichier Journal.log](ExempleFichierJournal.md) dans le dossier temporaire d'exécution de la tâche et renvoyer le [contenu de  ce fichier dans le JSON retourné](ExempleJournalRetour.md) pour la requête. <br>Ce fichier contient un journal détaillé du déroulement de l'exécution de la tâche. | Oui <br>Non | Facultatif | Non |
| statistiques | Créer un [fichier Statistiques.txt](ExempleFichierStatistiques.md) dans le dossier temporaire d'exécution de la tâche et renvoyer le [contenu de ce fichier dans le JSON retourné](ExempleStatistiquesRetour.md) par la requête. <br>Ce fichier contient le nombre de lignes importées et le nombre de lignes non importées, sous une forme plus lisible par d'autres logiciels  | Oui <br>Non | Facultatif | Non |
| entete | Est-ce que le fichier contient une première ligne avec le nom des champs ? | Oui <br>Non | Facultatif | Non |
| noms\_champs | Liste des champs présents dans le fichier, dans le même ordre que dans le fichier, séparés par un point-virgule |   | Facultatif |   |
| separateur\_champs | Séparateur de champs |   | Facultatif |   |
| identificateur\_texte | Identificateur de début et de fin de texte |   | Facultatif |   |
| fichier\_... | Tableau de lignes à importer |   | Obligatoire |   |
| ... | Paramètres spécifiques |   |   |   |



