# Paramétrage du serveur Microsoft SQL Server

Vous pouvez faire d’autres paramétrages sur votre serveur Microsoft SQL Server.


 


Pour ouvrir la fenêtre de paramétrage, il faut faire clic-droit sur 
 le nom du serveur puis "Propriétés" 
 en bas du menu contextuel.


![](../../assets/images/07/5/MenuProprietes.png)


 


Cette fenêtre nous donne des informations générales sur le serveur SQL 
 et sur son hôte (version, nom, …).


![](../../assets/images/07/5/OngletGeneral.png)


 


Quand vous cliquez sur "Mémoire", vous accédez au paramétrage 
 qui permettent de limiter ou d’augmenter l’accès à la mémoire du serveur. 
 Attention pour SQL Express, la taille maximale sera de **1Go** de mémoire 
 vive.


![](../../assets/images/07/5/OngletMemoire.png)


 


Le menu processeur permet d’accorder plus de "privilèges" 
 à SQL Server par rapport aux autres applications. Il permet d’augmenter 
 l’affinité cœur par cœur de votre processeur.


![](../../assets/images/07/5/OngletProcesseurs.png)


 


Le menu "Sécurité" permet de revenir sur le mode d’authentification 
 au serveur. On peut revenir à un mode où on utilise que les comptes Windows 
 comme moyen d’authentification (attention dans le cas d’un réseau en **WORKGROUP** 
 sans AD ).


![](../../assets/images/07/5/OngletSecurite.png)


 


Le menu "Connexions" permet notamment de limiter le nombre 
 de connexion et d’autoriser les accès distants.


![](../../assets/images/07/5/OngletConnexions.png)


 


Le menu Paramètres de base de données nous permet de compresser ou pas 
 la sauvegarde et de changer les chemins de stockage des bases de données 
 et de leur sauvegarde.


![](../../assets/images/07/5/OngletParametresBdd.png)


