# Nomenclatures et forfaits



## Forfaits


C'est un article non géré en stock 
 composé d'articles simples. Il 
 ne peut pas être composé d'autres articles de type forfait ou nomenclature.


 


Les composants sont déclarés dans l’onglet Composants mais la composition 
 (en quantité) peut être modifiée directement lors de l'utilisation du 
 forfait dans un document.


 


Le prix est défini uniquement en devise société.


 


Il est impossible de gérer [les 
 gammes](../../../Gammes/4/Articles.md) avec ce type.


### Mouvements de stock


Lors d'une commande client cela va impacter 
 le stock commandé des composants (Stock commandé par les clients (composants)).


 


Lors de la réservation dans un devis ou une 
 commande client cela va impacter le stock réservé (au devis ou à la commande) 
 des composants.


 


Lors de la sortie de stock (bon de livraison, 
 facture, ...) cela va impacter le stock actuel des composants et libérer 
 le stock réservé.


### Imputation comptable


En standard on va reprendre les informations des composants du premier 
 niveau (Comptes, TVA, TPF, ...) et pas du forfait.


 


Par défaut le prix du forfait correspond à la somme des prix des composants, 
 le calcul et la répartition de la TVA se base sur ces informations.


 


Lorsque le prix de vente à la ligne de document ne correspond pas à 
 la somme des prix des composants, un ratio est calculé pour actualiser 
 le prix des composants pour la composition du forfait dans le document, 
 le solde étant appliqué sur le dernier composant de la composition.


 


Une option dans les Préférences de Gestion permet de reprendre les informations 
 du forfait (Comptes, TVA, TPF, ...) et pas des composants.


 


Dans ce cas le calcul et la répartition de la TVA se base sur le prix 
 de la ligne du document.


## Nomenclatures


C'est un article qui peut être 
 ou non géré en stock, composé d'articles 
 simples, de nomenclatures 
 gérées en stock ou non gérée en stock. La nomenclature ne peut pas être 
 composée d'article de type forfait.


 


Il est impossible de gérer [les 
 gammes](../../../Gammes/4/Articles.md) avec ce type.


### Nomenclature non gérée en stock


Pour une nomenclature non gérée en stock 
 (nomenclature commerciale), les composants sont déclarés dans la fiche 
 nomenclature mais la composition (en quantité) peut être modifiée directement 
 lors de l'utilisation de la nomenclature non gérée en stock dans un document. 
 On ne gère pas d'information sur le stock de la nomenclature, les mouvements 
 de stock ont  pour effet de mettre à jour les quantités des articles 
 composants.


#### Mouvements de stock


Lors d'une commande client cela va impacter 
 le stock commandé des composants (Stock commandé par les clients (composants)).


 


Lors de la réservation dans un devis ou une 
 commande client cela va impacter le stock réservé (au devis ou à la commande) 
 des composants.


 


Lors de la sortie de stock (bon de livraison, 
 facture, ...) cela va impacter le stock actuel des composants et libérer 
 le stock réservé.


#### Imputation comptable


En standard on va reprendre les informations des composants du premier 
 niveau (Comptes, TVA, TPF, ...) et pas de la nomenclature.


Par défaut le prix de la nomenclature correspond à la somme des prix 
 des composants, le calcul et la répartition de la TVA se base sur ces 
 informations.


 


Lorsque le prix de vente à la ligne de document ne correspond pas à 
 la somme des prix des composants, un ratio est calculé pour actualiser 
 le prix des composants pour la composition de la nomenclature dans le 
 document, le solde étant appliqué sur le dernier composant de la composition.


Une option dans les Préférences de Gestion permet de reprendre les informations 
 de la nomenclature (Comptes, TVA, TPF, ...) et pas des composants.


Dans ce cas le calcul et la répartition de la TVA se base sur le prix 
 de la ligne du document.


### Nomenclature gérée en stock


Pour une nomenclature gérée en stock (nomenclature 
 de fabrication), les composants sont déclarés dans la fiche nomenclature. 
 La composition (article et/ou quantité) ne peut pas être modifiée directement 
 lors de l'utilisation de la nomenclature gérée en stock dans un document. 
 Pour les nomenclatures gérées en stock il est nécessaire de faire  une 
 [fiche 
 d'assemblage](../../../../Stocks/Documents/Fiche/Assemblage/FicheAssemblageNomenclatures.md) pour faire entrer du stock de la nomenclature et sortir 
 du stock des composants. Lors de la vente, seule la quantité de la nomenclature 
 sera mise à jour.


#### Mouvements de stock


Lors d'une commande client cela va impacter 
 le stock commandé de la nomenclature (Stock commandé par les clients (Articles)) 
 et le stock commandé des composants (Stock commandé par les clients (composants)).


 


Lors de la réservation dans un devis ou une 
 commande client cela va impacter le stock réservé (au devis ou à la commande) 
 de la nomenclature et des composants.


 


Lors de la sortie de stock (bon de livraison, 
 facture, ...) cela va impacter le stock actuel de la nomenclature et libérer 
 le stock réservé de la nomenclature et des composants.


#### Imputation comptable


On va reprendre les informations de la nomenclature 
 (Comptes, TVA, TPF, ...) et pas des composants.


## Création de l'article nomenclature ou forfait


Pour créer un article de type nomenclature ou 
 forfait allez dans le menu Articles / Articles puis "Nouveau".


 


Dans l’onglet général  pour "type 
 d’article" sélectionnez "Nomenclature" ou "Forfait".


 


Allez ensuite dans l’onglet "Composants" 
 afin d’y ajouter les articles qui composeront votre nomenclature ou forfait. 
 Vous pouvez saisir autant d’articles que vous souhaitez, ainsi que la 
 quantité nécessaire de chaque composant.


 


En bas de l'onglet Composants 
 vous avez 2 possibilités pour calculer le prix de vente de votre nomenclature 
 ou forfait l: 


* soit en cliquant 
 sur la calculatrice afin de calculer automatiquement votre prix,
* soit en cochant 
 la case "prix de vente de la nomenclature manuel" qui vous 
 permettra de choisir manuellement le prix de vente de votre nomenclature 
 ou forfait.


 


Pour une nomenclature gérée en stock, allez 
 dans l’onglet "Stock" afin de choisir le type de gestion de 
 stock à appliquer. Par défaut les articles de type nomenclature ou forfait 
 ne sont pas gérés en stock.


