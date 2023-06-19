# Sélection à partir du stock d'un article


La fenêtre vous est proposée à partir du menu contextuel de la grille 
 de saisie des document de ventes et achats.


 


La fenêtre de sélection à partir du stock d’un article est identique 
 à la fenêtre de consultation du [stock 
 d'un article](../../../../Stocks/Stock/1-1/Stock.md) à l’exception :


* Qu’il n’y a pas 
 de décomposition possible,
* Des colonnes par 
 défaut dans la grille de sélection,
* Du traitement réalisé,
* Cette fenêtre peut 
 être différente pour l’affectation d'une gamme et/ou d'un numéro de 
 lot lors d’un transfert de document, lors de la duplication de document 
 , lors de la génération des abonnements, ou de la réalisation d'une 
 fiche d'assemblage/


## Grille de sélection


L’affichage par défaut est un dépôt pour l’article de la ligne courante 
 du document et les colonnes suivantes :


* Priorités
* Code article
* Libellé de l’article
* Gammes
* Numéro de lot
* Quantités actuelles
* Quantités à terme
* Quantités sélectionnées


 


Ces champs et beaucoup d’autres peuvent être afficher ou non par l’appel 
 des propriétés du menu contextuel.


 


Celle-ci vous permet d'effectuer une affectation multiple des articles, gammes, numéros 
 de lots… Exemple 
 ! Cliquez [ici](../../../../Achats/Documents/TransfertDuplicationDocument/4/ExempleAffectationGammeLot.md).


 


Lorsque vous gérez les articles [périssables](../../../../Stocks/NumerosLots/Trier/ArticlePerissable.md), vous 
 disposez dans les propriétés de la grille de plusieurs [champs 
 spécifiques](../../../../Stocks/NumerosLots/Trier/Champs_disponibles_pour_la_gestion_de_la_p_remption.md).


 


Les autres options de ce menu sont identiques à celui de la fenêtre 
 de consultation du [stock 
 d'un article](../../../../Stocks/Stock/1-1/Stock.md).


## Traitement réalisé


Plusieurs possibilités vous sont proposées pour [sélectionner 
 une ligne](SelectionPartirStockArticle.md). Si les lignes présentes ne vous conviennent pas vous pouvez 
 [créer 
 une nouvelle ligne de stock](../../../../Stocks/Trier/CreationLigneStockArticle.md).


### Validation de la ligne


A la validation de la ligne, le traitement :


* Peut vous informer 
 qu’il n’y a pas assez de stock pour la ligne sélectionnée avec le 
 nom du dépôt, l’article et la gamme ou le numéro de lot ainsi que 
 la quantité disponible,
* Peut passer à la 
 ligne suivante. Si celle-ci gère les lots ou les gammes, la fenêtre 
 d'affectation sera de nouveau proposée pour sélectionner la gamme 
 ou le numéro de lot à affecter à la pièce.


### Annulation de l’affectation


En cliquant sur le bouton Annuler, vous pouvez arrêter la sélection 
 à partir du stock de l’article.


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
 FilePopupInit('a2');
//]]>
