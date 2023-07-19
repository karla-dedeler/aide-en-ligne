# Défragmenter les index de vos tables

Un index est un objet complémentaire (mais non indispensable) à la base 
 de données permettant d'indexer certaines colonnes dans le but d'améliorer 
 l'accès aux données par Microsoft SQL Server, 
 au même titre qu'un index dans un livre ne vous est pas indispensable 
 mais vous permet souvent d'économiser du temps lorsque vous recherchez 
 une partie spécifique de ce dernier...


 


La fragmentation intervient lorsque des index possèdent des pages dans 
 lesquelles l'organisation logique (reposant sur la valeur de la clé) ne 
 correspond pas à l'organisation physique dans le fichier de données. Une 
 fragmentation importante des index peut diminuer les performances des 
 requêtes et ralentir la vitesse de réponse de votre application.


## Connaître le taux de fragmentations table par table


* Tapez 
 le nom de la base contenant la table


USE
[Nom de la base 
 de données];


 


* Modifiez le nom de la table 
 à vérifier (ici TIERS)


DBCC SHOWCONTIG
('dbo.TIERS')
WITH 
 FAST, TABLERESULTS, 
 ALL\_INDEXES, NO\_INFOMSGS;



## Défragmenter une table


* Tapez 
 le nom de la base contenant la table


USE
[Nom de la base 
 de données];


 


* Modifiez le nom de la table 
 à défragmenter (ici TIERS)


ALTER
INDEX
ALL ON 
 dbo.TIERS


REBUILD
WITH
(FILLFACTOR
= 80,
SORT\_IN\_TEMPDB =
ON,
STATISTICS\_NORECOMPUTE =
ON);


## Script complet à exécuter étape 
 par étape


/\* Etape 1 \*/


USE
[Nom de la base 
 de données];


 


/\* Etape 2 \*/


DBCC
SHOWCONTIG ('dbo.TIERS')
WITH
FAST, TABLERESULTS,
ALL\_INDEXES, NO\_INFOMSGS;


 


/\* Etape 3 \*/


USE
[Nom de la base 
 de données];


 


/\* Etape 4 \*/


ALTER
INDEX
ALL ON 
 dbo.TIERS


REBUILD
WITH
(FILLFACTOR
= 80,
SORT\_IN\_TEMPDB =
ON,
STATISTICS\_NORECOMPUTE =
ON);


## Pour en savoir plus


<https://msdn.microsoft.com/fr-fr/library/ms189858%28v=sql.120%29.aspx> 


