# Mouvements de stock



## Consultation des mouvements de stock


La consultation des mouvements permet d’obtenir pour un article d’un 
 dépôt, l’historique complet de ses mouvements de stock sur une période 
 précise.


## Entêté : définition de la consultation


### Article à consulter


La consultation des mouvements de stock peut être demandé pour :


* Un article précis (Unique)


Vous avez le choix de saisir le code article, 
 de le sélectionner dans la liste déroulante ou de le [rechercher](../../../Articles/1/Recherche/RechercheArticles.md).


De plus, vous disposerez des informations 
 suivantes :


* + Le type de 
	 l’article,
	+ Le type de 
	 gestion de stock,
	+ Le mode de 
	 gestion de stock ("sérialisé", "lot" ou "rien"),
* Une sélection d'articles 
 (Avancée),
* La totalité des 
 articles (Tous).


 


Grâce aux boutons Suivant et Précédent de la barre d’outils, il est 
 ensuite très facile de consulter respectivement, les mouvements de l’article 
 suivant et précédent.


 


Lorsque l’article gère les numéros de lot et/u 
 les gammes, la sélection du numéro de lot et/u la gamme peut-être précisée.


### Dépôt


La sélection du dépôt peut être pour :


* Un dépôt précis 
 (Unique),
* Une sélection manuelle 
 (Ensemble),
* La totalité des 
 dépôts (Tous).


### Tiers


La sélection de tiers peut-être :


* Unique 
 : Vous avez la possibilité de saisir le code tiers, de le sélectionner 
 dans la liste déroulante ou de le rechercher,
* Tous 
 : Les mouvements de stock concernant tous les tiers seront affichés.


### Période à consulter


Le logiciel propose par défaut de consulter les mouvements des 30 derniers 
 jours. La liste déroulante permet de sélectionner une autre période ou 
 d’introduire une période précise.


 


La quantité des différents stocks pour l’article courant s’affiche en 
 unité de conditionnement de vente.


## Liste des mouvements


L'onglet Tous affiche la totalité des mouvements d'un article.


 


Les onglets Inventaire & Écarts, Entrées ou Sorties affiche uniquement 
 les mouvements d'inventaire et d’écart, d'entrée (ventes, entrées, bons 
 de livraison client, .. ) Ou de sortie (achats, sorties, pertes..).


 


Le logiciel signale une ligne erronée par une couleur particulière (par 
 défaut le rouge) lorsque :


* Une ligne de mouvement 
 est erronée sur un article de type Lot ou de type Série. Vérifiez 
 dans ce cas, l’affectation des numéros de série ou de lots sur ce 
 mouvement,
* Qu’aucun prix n’aura 
 été affecté à un mouvement d’entrée de stock (inventaire, entrée, 
 bon de réception achat,..).


 


Pour ouvrir automatiquement le document à l'origine du mouvement, sélectionnez 
 le mouvement puis cliquez sur l'icône Ouvrir de la barre d'outils (vous 
 pouvez également double-cliquer sur le mouvement ou utiliser la touche 
 Entrée ou le menu contextuel). Le curseur est alors automatiquement placé 
 sur la ligne de l'article consulté.


 


Lorsque vous gérez les articles [périssables](../../NumerosLots/Trier/ArticlePerissable.md), vous 
 disposez dans les propriétés de la grille de plusieurs champs spécifiques. 
 De plus, les champs suivants vous permettent d’affiner le suivi de stock 
 :


* Le stock de la 
 ligne article (MVA\_STOCK),
* Le stock précédent 
 le mouvement (MVA\_PSTOCK),
* La valeur du stock 
 (MVA\_VALSTOCK).


 


Le menu contextuel permet également :


* De consulter les 
 numéros de série affectés à l'article,
* D’ imprimer la 
 consultation,
* De rafraîchir la 
 fenêtre,
* D’activer la recherche 
 automatique,
* De paramétrer la 
 grille de consultation (Propriétés).


## Détail des mouvements


Pour chacun des mouvements vous pouvez trier par :


* Date,
* Dépôt (sauf dans 
 le cas d’une sélection de dépôt unique),
* Article (sauf dans 
 le cas d’une sélection d'article unique),
* Libellé,
* N° de pièce.


 


Chaque mouvement est détaillé et indique la nouvelle valeur du stock 
 :


* Date : C’est la 
 date de la pièce à l’origine du mouvement,
* Pièce N° : C'est 
 le type et le numéro de la pièce à l'origine du mouvement (facture 
 client, bon de livraison, entrée, ...),
* Écarts /Inventaire,
* Entrées,
* Sorties,


La quantité mouvementée dans le conditionnement 
 s'inscrit dans une des trois colonnes en fonction du type de mouvement


* Conditionnement 
 : C'est le conditionnement du mouvement (Boite, Carton, Litre,..),
* Nb U. V : C'est 
 le nombre d'unités de conditionnement de vente calculé automatiquement 
 en fonction de la quantité et du conditionnement mouvementés,
* Prix Moyen / FIFO\LIFO 
 : En mode FIFO, LIFO, le logiciel affiche un prix moyen car il n’y 
 a pas de prix unique,
* Stock : C'est la 
 quantité physique ou Stock Actuel au moment du mouvement,
* Prix d'achat : 
 C'est le prix d'achat saisi lors d'un mouvement de stock,
* PUMP/D.P.A. /P.M.A 
 : En fonction du type de stock, c'est soit le PUMP, le Dernier PA, 
 le PMA,
* Valeur du stock 
 : C'est la valeur du stock qui correspond à : PUMP \* Quantité en stock 
 sauf en mode FIFO ou LIFO,
* Type de perte/ 
 écart : Pour une pièce de Perte/d’Écart, affiche le type de la perte/écart,
* Libellé du mouvement 
 : Libellé saisie lors de la création des pièces de stock,
* Payeur : Raison 
 sociale de l’adresse de facturation,
* Client : Raison 
 sociale de l’adresse de livraison,
* Zone stockage : 
 Fonction non disponible actuellement,
* [Date de péremption](../../NumerosLots/Trier/DatePeremption.md) : Disponible 
 lors de la saisie des numéros de lot.


 


