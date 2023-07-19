# Configuration minimale recommandée pour le serveur


Gestimum ERP requiert le serveur de bases de données Microsoft SQL Server 2019 ou une version inférieure.


 


Pour une installation possédant déjà une version de Microsoft SQL Server, il n’est pas nécessaire d’évoluer vers une installation plus récente.


Si vous voulez installer quand même la dernière version, il faut au préalable désinstaller l’ancienne version en prenant soin de sauvegarder vos bases de données.


 


Nous recommandons d'exécuter Microsoft SQL Server sur des ordinateurs dotés du format de fichier NTFS. L'installation de Microsoft SQL Server sur un système de fichiers FAT32 est prise en charge mais n'est pas recommandée car elle est moins sécurisée que le système de fichiers NTFS.


 


Attention, le programme d'installation de Microsoft SQL Server bloquera les installations sur les lecteurs en lecture seule, mappés ou compressés. L’installation échoue si vous lancez le programme d’installation par le biais d’une connexion Bureau à distance en utilisant un support sur une ressource locale du client Connexion Bureau à distance. Pour effectuer une installation à distance, le support doit se trouver sur un partage réseau ou être installé en local sur l’ordinateur physique ou la machine virtuelle. Le support d’installation de SQL Server peut soit se trouver sur un partage réseau, sur un lecteur mappé ou sur un lecteur local, soit être présenté à une machine virtuelle sous la forme d’un fichier ISO.


 


Pour des raisons de sécurité, nous recommandons de ne pas installer Microsoft SQL Server sur un **contrôleur de domaine**. Le programme d'installation ne bloquera pas l'installation sur un ordinateur qui est contrôleur de domaine, mais les limitations suivantes s'appliquent :


 


* Vous ne pouvez pas exécuter les services Microsoft SQL Serverr sur un contrôleur de domaine sous un compte de service local.
* Après avoir installé sur un ordinateur Microsoft SQL Server, vous ne pouvez pas modifier l'ordinateur d'un membre de domaine en un contrôleur de domaine. Vous devez désinstaller Microsoft SQL Server avant de modifier l'ordinateur hôte en un contrôleur de domaine.
* Les instances de cluster de basculement Microsoft SQL Server ne sont pas prises en charge lorsque les nœuds du cluster sont des contrôleurs de domaine.
* Microsoft SQL Server n’est pas pris en charge sur un contrôleur de domaine en lecture seule. Le programme d'installation de Microsoft SQL Server ne peut pas créer de groupes de sécurité ni configurer de comptes de service Microsoft SQL Server sur un contrôleur de domaine en lecture seule. Dans ce scénario, le programme d'installation échoue.


 


Une base de données migrée vers Microsoft SQL Server plus récente ne peut être **rétrogradée** vers une version antérieure.


### **Disque Dur**


* 6 Go pendant l’installation


 


puis :


* 1.48 Go pour le moteur de base de données
* 1.8 Go pour les composants clients (SSMS …)


 


Sur l'édition Microsoft SQL Server Express, la taille de la base de données ne pourra pas excéder **10 Go**. Au-dessus il faut passer en version Standard.


## **Mémoire**


* 1 Go minimum


 


Attention avec l'édition Express, ce seuil ne sera jamais dépassé.


## **Processeur**


* **64 bits**
* 1,4 GHz minimum / 2 GHz ou plus recommandé
* AMD Opteron, AMD Athlon 64, Intel Xeon avec prise en charge d'Intel EM64T, Intel Pentium IV avec prise en charge d'EM64T


 


L'édition Express ne prendra pas en charge plus d’un processeur et plus de **4 cœurs** sur ce dernier.


## **Système d’exploitation**


* Windows Server 2016 ou ultérieur
* Windows 10 version 1507 minimum


 


Pour l’installation de Microsoft SQL Server, il est important de faire toutes les mises à jour Microsoft, et installer :


* Framework .NET 4.6.1
* PowerShell 2.0


## Internet


Une connexion Internet est nécessaire lors de l’installation.


## Compatibilité avec Windows Server


Le tableau suivant indique la compatibilité des éditions de SQL Server 2019 avec chaque version de Windows Server :


 











|   | SQL Server 2019 Enterprise | SQL Server 2019 Développeur | SQL Server 2019 Standard | SQL Server 2019 Web | SQL Server 2019 Express |
|---|---|---|---|---|---|
| Windows Server 2019 Datacenter | Oui | Oui | Oui | Oui | Oui |
| Windows Server 2019 Standard | Oui | Oui | Oui | Oui | Oui |
| Windows Server 2019 Essentials | Oui | Oui | Oui | Oui | Oui |
| Windows Server 2016 Datacenter | Oui | Oui | Oui | Oui | Oui |
| Windows Server 2016 Standard | Oui | Oui | Oui | Oui | Oui |
| Windows Server 2016 Essentials | Oui | Oui | Oui | Oui | Oui |


## Microsoft SQL Server Management Studio (SSMS)


Il n’est plus inclus dans l’installateur de Microsoft SQL Server. Il faut l’installer séparement.


## Sources


Vous retrouverez les sources de ces informations ici :


<https://docs.microsoft.com/fr-fr/sql/sql-server/install/hardware-and-software-requirements-for-installing-sql-server-ver15>


<https://docs.microsoft.com/fr-fr/sql/sql-server/compute-capacity-limits-by-edition-of-sql-server>


