# Commander le réapprovisionnement



La génération des commandes fournisseurs (menu Achat) permet de rechercher 
 pour chacun des articles à réapprovisionner, le meilleur  fournisseur 
 puis de générer les commandes correspondantes.


 


Avant d’utiliser cette fonction, il faut préalablement [générer 
 les lignes d'articles à réapprovisionner](../1/Calculer.md).


## Mode d’application de la génération


La génération des commandes fournisseurs peut s’appliquer aux articles 
 d’un dépôt ou de tous les dépôts.


 


La sélection du fournisseur s’effectue en tenant compte ou non de la 
 priorité fournisseur et des trois critères suivants: meilleur délai de 
 livraison, meilleur prix ou plus petite quantité à commander.


 


Le choix du fournisseur de la commande est propre à [chaque 
 article](../../../Articles/1/Article/OngletFournisseurs/ArticleOngletFournisseurs.md) et dépend de la priorité défini (priorité fournisseur, délai 
 de livraison, quantité minimum et prix d’achat).


### Sélection du dépôt


Par défaut, la génération des commandes fournisseurs s’effectue sur 
 les articles à réapprovisionner sur la totalité des dépôts mais elle peut 
 être demandée pour un dépôt unique ou un intervalle de dépôts.


### Informations fournisseur


Dans chaque fiche article, [l'onglet 
 Fournisseur](../../../Articles/1/Article/OngletFournisseurs/ArticleOngletFournisseurs.md) contient la liste des fournisseurs possibles avec les 
 informations suivantes: le prix d’achat, le délai de livraison, la remise, 
 la quantité minimum à commander et la priorité. Le choix du fournisseur 
 auquel vous allez commander chaque article dépend du type de priorité 
 choisie.


 


Le classement des fournisseurs s’effectue sur les trois critères suivants 
 : prix d’achat, délai et quantité minimum.


 


Cochez la case Prise en compte de la "priorité fournisseur", 
 pour tenir compte en premier lieu de la priorité du fournisseur puis ensuite 
 des trois critères précédents, Autrement, le logiciel prendra en compte 
 uniquement les critères de prix, délai et quantité minimum.


## Détail des commandes à générer


A partir des critères définis dans la première étape, le logiciel affiche 
 pour chaque article, une liste de fournisseurs classés par ordre de priorité


Le meilleur fournisseur est coché et placé en premier et les autres 
 suivent selon leur priorité.


 


Les renseignements concernant la commande: délai de livraison, quantité 
 minimum à commander chez le fournisseur (en unité de conditionnement de 
 vente), prix, vous permettent de déterminer avec soin le fournisseur le 
 plus approprié.


 


La colonne "Devise" correspond à la devise de la fiche fournisseur 
 et celle "Prix brut" au prix de l’article dans la devise du 
 fournisseur.


La colonne "Franc" ou "Euro" ou "un autre nom 
 de devise" correspond au prix de l’article dans la devise société.


 


Pour éventuellement modifier le fournisseur proposé par défaut, il suffit 
 de double-cliquer sur la case à cocher du fournisseur que vous souhaitez 
 affecter à la commande de l’article.


 


Vous avez la possibilité de créer (F4+Ins) ou de modifier (F4+F2) les 
 [fiches fournisseurs](../../../Tiers/4/Introduction.md) 
 directement depuis cet onglet.


### Quantité mise en commande fournisseur


La quantité commandée sera égale à la quantité de réapprovisionnement 
 ou à la quantité minimum affichée ici (si Qté Besoins < Qté minimum).


La quantité devra toujours être au moins égale à une unité de conditionnement 
 d’achat.


 


### Particularités sur les articles gérant les gammes et les lots


Pour un article gérant [les 
 gammes](../../../Articles/Gammes/1/Introduction.md) et [les 
 numéros de lot](../../../Stocks/NumerosLots/2/Numéros_de_lots_de_A_à_Z.md), plusieurs lignes de commande peuvent être générées. 
 En effet, vous aurez plusieurs lignes avec des gammes et/ou des numéros 
 de lot différents pour un article à commander.


* Si sur le réapprovisionnement pour un article, 
 un numéro de lot ou une gamme est renseigné, la génération de commande 
 fournisseur affichera ces numéros/gammes. Sinon, le traitement ne 
 vus demandera pas de numéro de lot, ni de gamme, les colonnes resterons 
 vides,
* Sur vos commandes fournisseurs générées 
 vus n’aurez donc pas de numéro de lot ni de gamme. Lors du transfert 
 de ces commandes en bons de livraison, une fenêtre d'affectation de 
 numéro de lot/gamme vus sera proposée.


 


Lorsque vous cliquez sur le bouton Terminer, le logiciel génère les 
 commandes fournisseurs correspondantes


