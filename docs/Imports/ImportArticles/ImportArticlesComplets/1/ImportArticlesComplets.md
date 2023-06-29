# Import d'articles complets


L’import de la tables articles et des tables liées aux articles est 
 possible à partir du menu Outils/Importation/Autres données.


 


Un seul fichier suffit pour importer toutes les tables liées aux articles.


 


Pour cela, vous devez affecter devant chaque ligne importée un identifiant.


 


Chaque identifiant correspond à une table :


 







| Identifiant 
 de la table | Nom 
 de la table | Description |
| 001 | ARTICLES | Articles |
| 002 | ART\_PROD | Composants des nomenclatures et forfaits |
| 003 | ART\_PRIX | Tarifs |
| 004 | ART\_FOURN | Tarifs fournisseurs |
| 005 | ART\_CLIENT | Références clients |
| 006 | ART\_AUTRES | Équivalences |


 


Lors de l’import, suite à la sélection du fichier à importer, de la 
 table de destination Articles et du paramétrage du fichier à importer 
 (séparateur de champs, nom des champs en première ligne …), l’assistant 
 passera les tables successivement jusqu’à l’aperçu ou il ne sera visible 
 que les colonnes de la table articles (001).


 


Pour chaque import, il est obligatoire d’avoir au minimum la table 001 
 avec le code article et la désignation (même pour une mise à jour).


 


Les décimales doivent être définies avec des points (.) et non des virgules 
 (,).


 


Pour avoir un exemple de fichier cliquez [ici](../2/ExempleFichierArticlesComplets.md).


 


Pendant le traitement, une barre de progression permet de voir l’évolution 
 de l’import.


 


A la fin du traitement, vous avez la possibilité d’afficher un rapport 
 d’import qui contient les anomalies et erreurs de l’import.


