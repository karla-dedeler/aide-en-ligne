# Paramétrage du pare-feu

Pour que Microsoft SQL Server 
 soit accessible depuis votre réseau, il faut paramétrer le pare-feu Windows 
 ou autre. Vous devez donc faire comme suit :


 


* Ouvrez le "Gestionnaire 
 de serveur"


![](../../assets/images/07/1/GestionnaireServeur.png)


 


* Cherchez dans le menu "Outils" 
 le Pare-feu Windows


![](../../assets/images/07/1/MenuOutils.png)


 


![](../../assets/images/07/1/AccueilPareFeu.png)


 


* Cliquez sur "Règle 
 de trafic entrant"


![](../../assets/images/07/1/ReglesTraficEntrant.png)


 


* Cliquez ensuite sur "Nouvelle 
 règle…" dans le menu à droite et dans la nouvelle fenêtre sélectionnez dans un premier temps 
 "Programme"


![](../../assets/images/07/1/NouvelleRegleProgramme.png)


 


* Allez dans parcourir et 
 cherchez "sqlserv.exe" 
 dans ce chemin (C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\Binn)


![](../../assets/images/07/1/NouvelleRegleProgrammeSelection.png)


 


![](../../assets/images/07/1/FenetreSelectionProgramme.png)


 


* Sélectionnez "Autoriser 
 la connexion"


![](../../assets/images/07/1/NouvelleRegleProgrammeAutorisation.png)


 


* Décochez "Public" 
 pour éviter que le serveur ne soit accessible en dehors de votre réseau


![](../../assets/images/07/1/NouvelleRegleProgrammeApplication.png)


 


* Nommez la règle comme vous 
 le voulez (vous pouvez mettre par exemple SQLServer.exe – Entrant)


![](../../assets/images/07/1/NouvelleRegleProgrammeNom.png)


 


* Refaites la même opération 
 mais cette fois en sélectionnant le port


![](../../assets/images/07/1/NouvelleReglePort.png)


 


* Tapez 1433 dans "Ports 
 Locaux spécifiques" qui correspond au port utilisé par SQL Server 
 pour communiquer en TCP.


![](../../assets/images/07/1/NouvelleReglePortSpecification.png)


 


* Sélectionnez "Autoriser 
 la connexion"


![](../../assets/images/07/1/NouvelleReglePortAutorisation.png)


 


* Décochez "Public"


![](../../assets/images/07/1/NouvelleReglePortApplication.png)


 


* Nommez la règle comme vous 
 le voulez (vous pouvez mettre par exemple Port SQLServer 1433 – Entrant)


![](../../assets/images/07/1/NouvelleReglePortNom.png)


 


Dans la liste des règles entrantes, vous devriez donc retrouver les 
 2 règles que nous venons de créer.


![](../../assets/images/07/1/ListeReglesEntrantes.png)


 


 


Il faut refaire les mêmes manipulations au niveau des règles de trafic 
 sortant.


### Source


<https://docs.microsoft.com/fr-fr/sql/sql-server/install/configure-the-windows-firewall-to-allow-sql-server-access> 


