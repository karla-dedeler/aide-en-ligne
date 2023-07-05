# Version 8.3.0 build 852 du 01/07/2019

 




 


#### OUVERTURE DE SOCIÉTÉ


`#25485` - L'option 
 de connexion exclusive via IHM bloque la connexion des autres utilisateurs 
 quelque soit le 
 module utilisé.


#### ACHAT ET VENTE


`#24993` 
 - Suppression du contrôle empêchant un transfert partiel sans reliquat 
 d'une commande contenant un acompte.


`#25213` - Lors d'un 
 regroupement de bon de commande en bon de livraison, la quantité livrée 
 est renseignée dans le bon de livraison créé.


`#25241` 
 - Mise en place d’une fonction permettant d'abandonner les reliquats d'une 
 commande, d'achat ou de vente, et de la passer au statut « transféré ». 
 Accessible depuis la liste des documents, via un clic droit.


`#25454` 
 - Augmentation de la taille du champ "Réf." (DOC\_REFPCF) à 100 
 caractères dans les documents d'achat, vente et stock.


#### ARTICLES


`#14755` - Le Prix de 
 revient dans l'onglet stock de la fiche article est modifiable si l'option 
 "Manuelle" est choisie.


`#25522` - La création 
 d'une nouvelle fiche article depuis un menu déroulant est possible avec 
 la touche clavier "insert".


#### CONTACTS


`#25449` - L'adresse 
 Bureau du tiers sélectionnable dans l'adresse "Bureau" du contact 
 est sauvegardée à l'enregistrement du contact.


#### IMPORTS


`#25538` - L'import de  date de livraison au document et à la ligne 
 de document, en d'achats et en ventes est prise en compte.


#### STOCKS


`#25301` - Création d'une fenêtre 
 de stock prévisionnel, permettant de piloter les livraisons client et 
 les réapprovisionnements en achat, en ayant une visibilité sur le stock 
 à terme de l'article en fonction des différentes dates de livraison. Cette 
 fenêtre est également accessible depuis la saisie d'une commande en vente.


`#25401` - Correction de l'erreur "conversion de type variante incorrecte" 
 lors de l'impression de l'état du stock avec sélection article avancée 
 pour tous les dépôts.


`#25413` - Mise en place d’un contrôle 
 de disponibilité du stock à la date sélectionnée dans la fenêtre de sélection 
 d’une date de livraison accessible depuis le menu contextuel de la grille 
 d'une commande client.


`#25470` - Correction de l'affichage du total des mouvements en entrée 
 et en sortie dans l onglet "mouvements de stock".


`#25502` - Correction de l'erreur "il n'y a aucune donnée !" 
 lors de l'impression du stock avec une sélection sur tous les dépôts, 
 et que l'utilisateur est rattaché à un salarié.


`#25509` - L'abandon des reliquats sur les commandes n'impacte plus le 
 stock réservé à la commande en négatif, quand le stock n'a pas été réservé 
 à la commande.


#### TIERS


`#25448` - La colonne "Demandée par" 
 (ACT\_DMNDPR) s'alimente dans l'onglet des actions des tiers et des contacts.


`#25450` 
 - Ajout du code postal et de la ville de l'adresse "Bureau" 
 du contact, dans la liste des contacts du tiers.


#### TRANSFERT AUTOMATIQUE DES COMMANDES


`#25576` - Le montant net du bon de livraison se calcule correctement 
 si, lors du transfert automatique des commandes, on annule l'une des fenêtres 
 de sélection de lot, gamme ou n° de série.


#### EDI CHORUS


`#25484` - Ajout d'une colonne dans 
 les tables de références des unités de conditionnement pour gérer l'«unitCode 
 » de l’InvoicedQuantity de l'UBL. Si cette donnée est renseignée dans 
 la table de référence et sélectionnée dans l'article alors elle est reprise 
 dans le fichier UBL sinon c'est le code "EA" qui est renseigné 
 par défaut.


#### ÉCRITURES


`#25435` - L'échéance de la ligne d'écriture 
 est renseignée de manière automatique, en fonction du paramétrage du compte 
 auquel elle est rattachée.


#### IMPORT DES ÉCRITURES COMPTABLES


`#25474` - Les écritures importées portent un numéro de pièce distinct 
 par écriture comptable, dans le cas où le journal est paramétré en numérotation 
 périodique et que le numéro n'a pas été initialisé par une première saisie 
 manuelle.


#### SOLDES INTERMÉDIAIRES DE GESTION


`#25531` - Le rafraîchissement de la grille des Soldes Intermédiaires 
 de Gestion s'effectue correctement lorsque l'on veut restaurer les données 
 par défaut d'une cellule.


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


 


