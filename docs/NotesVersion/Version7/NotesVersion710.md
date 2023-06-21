# Version 7.1.0 build 797 du 18/05/2018

 


#### LOI ANTI-FRAUDE 
 TVA


`#23769` – Le calcul des clés d'inaltérabilité 
 lors d'une montée de version ne s'effectue qu’à partir du 01/01/2018.


#### ACHAT ET VENTE


`#23751` 
 – A l'affectation d'un nouveau numéro de lot lors du transfert d'une commande 
 d'achat en bon de réception, sur un article géré en lot avec conditionnement, 
 la quantité de la ligne n'est plus multipliée par son conditionnement.


`#23789` 
 – Le stock à terme à la ligne de document et dans le volet d'information 
 contextuel n'est plus doublé lors de la saisie d'une commande.


`#23806` – 
 Le stock des composants gérés en stock d'une nomenclature gérée 
 en stock, n'est pas impactés à la saisie de document d'achat/vente, mouvementant 
 le stock (bon de livraison, bon de retour, facture, avoir).


#### GAMME


`#23713` 
 – La sélection de gammes dans les documents via "sélectionner à partir 
 du stock" remonte bien le tarif associé.


#### GEOLOCALISATION


`#23770` – Le géocodage des adresses 
 de tiers est désactivé lors de la migration. Après migration, il est possible 
 de lancer un géocodage en masse par type de tiers, via le menu "Tiers 
 \ Mettre à jour les tiers".


#### OUVERTURE DE SOCIETE


`#23750` 
 – Mise en place d'un message d’alerte lorsque la taille de la base de 
 donnée SQL Server Express approche 90 % de la taille limite.


#### STOCK


`#23768` – Lors d'un transfert de stock, 
 la valorisation de départ de l'article est bien reprise dans le dépôt 
 de destination.


`#23791` – Le calcul du stock dans les lignes 
 de mouvement de stock s'effectue correctement, lorsqu'un article est présent 
 plusieurs fois dans un bon de livraison transféré en facture.


`#23852` – Correction du message "Champ 
 'ART\_AFFMES' non trouvé lors de l'ajout d'un composant avec le même dépôt 
 via un clic droit dans un document d'assemblage.


#### AFFAIRES


`#23483` 
 – Il est possible d'ajouter les lignes d'un document ou le pied d'un document 
 dans le budgété Achats des affaires.


`#23490` – Il est possible d'ajouter les 
 lignes d'un document contenant des lignes de texte vide, dans le budget 
 des affaires en achat et en vente.


`#23710` – Suppression du contrôle sur le 
 champ DOC\_NUMERO lors de l'intégration de lignes dans le budgété des affaires.


#### G-CHANGE


`#23484` 
 – Impression de documents d'achat, vente et stock par tâche en ligne de 
 commande.


#### ÉCRITURES


`#23616` – L'échéance s'actualise correctement 
 dans l'échéancier lors d'une modification de l'écriture comptable.


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


 


