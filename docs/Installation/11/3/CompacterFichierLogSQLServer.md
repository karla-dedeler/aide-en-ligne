# Compacter le fichier LOG de la base de données

Les fichiers de log sont en fait ce que l'on appelle en français les 
 "fichiers de journalisation".


 


Ils contiennent toutes les transactions effectuées dans la base de données 
 (INSERT, UPDATE, DELETE...) enregistrées en séquence.


 


Par exemple si, partant d'une base vide, on ajoute et supprime un millier 
 de lignes dans une table, et cela plusieurs centaines de fois, la base 
 sera quasi vide et le journal des transactions important. Il se peut donc 
 que le journal des transactions vienne donc à occuper un espace disque 
 important et si l'administrateur n'y prend pas garde, saturer les disques...


 


Les remèdes sont les suivants :


* Surveillez l’espace disque 
 via l'OS (alertes administratives)
* Videz les journaux de transactions
* Limitez la croissance du 
 fichier de transaction (dangereux)


 


Il se peut que vous ayez du mal à vider votre journal de transaction. 
 En effet les différentes sauvegardes : base complète, base différentielle 
 ou journal des transactions permettent de récupérer une base corrompue. 
 Tant que ces fichiers ne sont pas tronqués, la récupération est en principe 
 toujours possible. C'est pourquoi tant que la sauvegarde base + journal 
 n'a pas eu lieu, il n'est pas possible de tronquer les fichiers.


 


Les fichiers logs sont des fichiers en croissance forte qui peuvent 
 parfaitement dépasser de beaucoup la taille des données. Ces fichiers 
 peuvent provoquer la saturation du disque dur du serveur, dans ce cas 
 vous serez dans l’obligation soit de réduire la taille de ces fichiers 
 soit les déplacer sur un autre disque dur local.


## Compacter vos logs


* Tapez le nom de votre base 
 de données


USE
[Nom de la base 
 de données]


 


* Effectuez une sauvegarde 
 de votre base de données


BACKUP
DATABASE 
 [Nom de la base de données] TO DISK='Chemin où 
 sera stocké la sauvegarde. Par exemple, C:\MonBackUp.bak' WITH INIT,
STATS


 


* Exécutez ce script avec 
 le nom de votre base qui passe change temporairement le mode de récupération 
 de la base de donnée


ALTER DATABASE [Nom 
 de la base de données] SET 
 RECOVERY SIMPLE


 


* Exécutez cette procédure 
 stockée système "sp\_helpfile" qui liste les fichiers et 
 leurs noms pour la base de données courante et vous renvoie le nom 
 logique dont on a besoin plus loin


EXEC
sp\_helpfile


 


* Ce script qui va compacter 
 le fichier log


DBCC
SHRINKFILE ('NomLogique\_Log','TRUNCATEONLY')


 


* Repassez la base en mode 
 RECOVERY FULL


ALTER DATABASE [Nom de 
 la base de données]
SET RECOVERY FULL


## Script complet à exécuter étape 
 par étape


/\* Etape 1 \*/


USE 
 [Nom de la base de données]


 


/\* 
 Etape 2 \*/


BACKUP
DATABASE [Nom de la base de données] 
 TO DISK='Chemin où 
 sera stocké la sauvegarde. Par exemple, C:\MonBackUp.bak' WITH INIT, STATS


 


/\* 
 Etape 3 \*/


ALTER 
 DATABASE [Nom de la base de données] SET 
 RECOVERY SIMPLE


 


/\* 
 Etape 4 \*/


EXEC
sp\_helpfile


 


/\* 
 Etape 5 \*/


DBCC 
 SHRINKFILE ('NomLogique\_Log','TRUNCATEONLY')


 


/\* 
 Etape 6 \*/


ALTER 
 DATABASE [Nom de la base de données] SET 
 RECOVERY FULL


