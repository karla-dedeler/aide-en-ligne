# Mouvements de stock des numéros de séries



La consultation des mouvements des numéros de série permet d’obtenir 
 pour un article sérialisé d’un dépôt, l’historique complet de ses mouvements 
 de stock sur une période précise.


## Entête: définition de la consultation


L’entête de la consultation des mouvements des n° de série donne la 
 possibilité de sélectionner un ensemble d’articles, de gammes, de dépôts 
 et de n° de série pour une période donnée.


### Article à consulter


La consultation peut être demandée pour :


* Un article précis 
 (Unique) : Vous avez le choix 
 de saisir le code article, de le sélectionner dans la liste déroulante 
 ou de le [rechercher](../../../Articles/1/Recherche/RechercheArticles.md).


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


### Gammes à consulter


Vous avez la possibilité de consulter :


* Toutes 
 les gammes,
* Un ensemble 
 de gammes : sélection multiple de gamme depuis la vue (Ctrl+clic pour 
 pouvoir sélectionner différents éléments pour une même gamme élémentaire),
* Une gamme unique : saisie d’une gamme ou sélection 
 depuis la vue.


### Choix du dépôt


Le dépôt principal (défini dans les préférences de la gestion) est automatiquement 
 proposé mais vous pouvez en sélectionner:


* Un autre (unique),
* Un ensemble 
 de dépôt,
* Tous 
 les dépôts.


### N° de série à consulter


Vous avez plusieurs possibilités pour [sélectionner les numéros 
 de série](../5/AffectationNumerosSeries.md) dont vous souhaitez consulter les mouvements.


### Période à consulter


Le logiciel propose par défaut de consulter les mouvements des 30 derniers 
 jours. La liste déroulante permet de sélectionner une autre période ou 
 d’introduire une période précise.


## Détail des mouvements


Chaque mouvement est détaillé et indique les numéros de série concernés


* Date 
 : C’est la date de la pièce à l’origine du mouvement,
* Pièce 
 N° : C'est le type et le numéro de la pièce à l'origine du 
 mouvement (facture client, bon de livraison, entrée, ...),
* Écarts 
 /Inventaire,
* Entrées,
* Sorties.


 


La quantité mouvementée s'inscrit dans une des trois colonnes en fonction 
 du type de mouvement :


* Du 
 N° de série : C’est le 1er numéro de série concerné par le 
 mouvement. Si le mouvement concerne qu’un numéro, seule cette colonne 
 sera renseignée
* Au 
 N° de série : C’est le dernier numéro de la série concerné 
 par le mouvement. Si le mouvement concerne qu’un numéro de série, 
 cette colonne n’aura aucun numéro
* Libellé 
 du mouvement : Libellé saisie lors de la création des pièces de stock
* Payeur 
 : Raison sociale de l’adresse de facturation
* Client 
 : Raison sociale de l’adresse de livraison
* Zone 
 stockage : Fonction non disponible actuellement
* [Date de péremption](../../NumerosLots/Trier/DatePeremption.md) : Disponible lors de la saisie des 
 numéros de lot


## Liste des mouvements


L'onglet Tous affiche la totalité 
 des mouvements d'un article. Les onglets Inventaire & Écarts, Entrées 
 ou Sorties affichent uniquement les mouvements d'inventaire et d’écart, 
 d'entrée (ventes, entrées, bons de livraison client, .. ) ou de sortie 
 (achats, sorties, pertes..).


 


Pour ouvrir automatiquement le document à l'origine du mouvement, sélectionnez 
 le mouvement puis cliquez sur l'icône Ouvrir de la barre d'outils (vous 
 pouvez également double-cliquer sur le mouvement ou utiliser la touche 
 Entrée). Le curseur est alors automatiquement placé sur la ligne de l'article 
 consulté.


 


Le menu contextuel permet également cette manipulation (Ouvrir la pièce) 
 ainsi que :


* L’impression de 
 la consultation,
* Le rafraîchissement 
 de la fenêtre,
* La possibilité 
 d’activer la recherche automatique,
* La possibilité 
 de paramétrer la grille de consultation (Propriétés).


 






//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
 FilePopupInit('a2');
//]]>
