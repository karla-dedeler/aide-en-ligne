# Recopie automatique de champs personnalisés entre tables

## Création du champ


Certaines tables de la bases de données sont liées entre elles.


 


Lorsque vous souhaitez qu’un champ personnalisé d’une table soit recopié 
 dans une table liée, vous devez créer le champ personnalisé dans les deux 
 tables avec les mêmes caractéristiques. Les informations saisies seront 
 alors recopiées d’une table à l’autre.


## Exemple


Vous ajoutez un champ personnalisé dans la table "Articles" 
 susceptible d’être utilisée en saisie d’articles dans un document de vente.


 


Il faut alors créer ce même champ dans la table "Lignes de document 
 de vente".


## Tables recopiées


Les tables recopiées sont les suivantes :


 






| Source | Destination |
| --- | --- |
| Familles de tiers | Sous-familles de tiers |
| Familles de tiers | Tiers |
| Sous-famille de tiers | Tiers |
| Familles d’articles | Sous-familles d’articles |
| Familles d’articles | Articles |
| Sous-familles d’articles | Articles |
| Tiers | Documents |
| Affaires | Documents |
| Articles | Lignes de document |
| Comptes | Écritures |
| Journaux | Écritures |
| Lignes de guides | Écritures |


