# Fenêtre d'affectation d'une gamme et/ou numéro de lot



La fenêtre d’affectation d’une gamme et/u d’un 
 numéro de lot vous est proposée :


* Lors d’un transfert 
 de document,
* Lors de la duplication 
 de document ,
* Lors de la génération 
 des abonnements,
* Lors de la réalisation 
 d'une fiche d'assemblage


 


La fenêtre d’affectation de la gamme et/u du 
 numéro de lot est identique à la fenêtre de consultation du stock d'un 
 article à l’exception :


* De la partie ‘article 
 à consulter’ présente sur l’entête de la consultation de stock d’un 
 article et est remplacé par les informations de la pièce d'origine,
* Des colonnes par 
 défaut dans la grille de sélection,
* Du traitement réalisé.


## Informations de la pièce d’origine


Les informations de la pièce d’origine sont de 2 types :


### Informations générales


* Type de traitement 
 : Transfert ou Duplication,
* Numéro de la pièce,
* Date de réalisation 
 de la pièce,
* Code du tiers.


### Informations liées à l’article


* Libellé court de 
 l’article (Pour une fiche d’assemblage, le code tiers est remplacé 
 par le code de l’article assemblé et le composant),
* Quantité saisie 
 sur la pièce d’origine.


## Grille de sélection


L’affectation affiche par défaut, par dépôt pour l’article, les colonnes 
 suivantes :


* Quantités actuel,
* Quantités à terme,
* Quantités sélectionnée.


 


Lorsque l’article gère les lots, la grille d’affectation des numéros 
 de lot tient compte de [l'ancienneté 
 de celui-ci](Gestion_des_lots_par_anciennete.md).


 


Lorsque l’article gère les gammes et/ou les lots, les colonnes du même 
 nom sont renseignées.


 


Ces champs et beaucoup d’autres peuvent être afficher ou non par l’appel 
 des propriétés du menu contextuel.


 


Ce menu vous permet également de choisir l’option ‘Sélection explicite 
 des quantités’. Celle-ci vous permet d'effectuer une affectation multiple 
 des numéros de lots. Exemple : Cliquez [ici](../../../Achats/Documents/TransfertDuplicationDocument/4/ExempleAffectationGammeLot.md).


 


Lorsque vous gérez les articles [périssables](ArticlePerissable.md), vous 
 disposez dans les propriétés de la grille de plusieurs [champs 
 spécifiques](Champs_disponibles_pour_la_gestion_de_la_p_remption.md).


 


Les autres options de ce menu sont identiques à celui de la fenêtre 
 de consultation du [stock d'un article](../../Stock/1-1/Stock.md).


## Traitement réalisé


Plusieurs possibilités vous sont proposées pour [sélectionner 
 une ligne](../../../Ventes/Documents/Fiche/3Corps/SelectionPartirStockArticle.md). Si les lignes présentes ne vous conviennent pas vous pouvez 
 [créer une nouvelle 
 ligne de stock](../../Trier/CreationLigneStockArticle.md).


### Validation de la ligne


A la validation de la ligne, le traitement :


* Peut vous informer qu’il n’y a pas assez 
 de stock pour la ligne sélectionnée avec le nom du dépôt, l’article 
 et la gamme ou le numéro de lot ainsi que la quantité disponible,
* Peut passer à la 
 ligne suivante. Si celle-ci gère les lots ou les gammes, la fenêtre 
 d'affectation sera de nouveau proposée pour sélectionner la gamme 
 ou le numéro de lot à affecter à la pièce,
* Passe à la réalisation 
 du document. Un message vous informera :
* + De la réalisation 
	 du transfert ou de la duplication avec le numéro de pièce généré,
	+ De la non réalisation 
	 du document avec les raisons possibles (uniquement lorsque vous 
	 êtes en transfert de document).


### Annulation de l’affectation


En cliquant sur le bouton Annuler, vus pouvez 
 arrêter l’affectation d’une gamme ou un numéro de lot.


 


Un message vus demande alors de confirmer si 
 vous ne souhaitez pas transférer/dupliquer la ligne en-cours. Si vous 
 confirmer, le traitement passe à la ligne suivante ou à la fin de l’opération, 
 sinon il reste sur la fenêtre dans l’attente de la sélection d’une gamme 
 ou d’un numéro de lot.


 


### Si vous n’affectez aucune ligne, en fin de traitement


Pour un transfert de document : vous aurez un 
 message vous informant qu’aucune ligne n’a pu être transférer, les raisons 
 de ce non traitement ainsi que la pièce non transférer.


 


Pour une duplication de document : vous resterez 
 sur la fenêtre de duplication.


 






