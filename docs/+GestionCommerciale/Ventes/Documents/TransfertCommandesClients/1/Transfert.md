# Transfert automatique des commandes clients



L’affectation de commandes vous permet de générer automatiquement les 
 bons de livraison ou factures des commandes client en attente de livraison. 
 Vous pouvez [également 
 transférer une commande précise](../../TransfertDuplicationDocument/2/Transfert.md), à partir de la liste des documents.


 


L’affectation des commandes s’effectue en deux temps : Choix et tri 
 des commandes puis Génération des bons de livraison ou factures.


## Présélection des commandes


A partir des renseignements que vous saisissez ici, le logiciel effectue 
 une recherche des commandes et les trie selon un classement très ordonné.


### Toutes les commandes prévues pour le


Le logiciel ne traitera que les commandes dont la date de livraison 
 prévue est antérieur ou identique à cette date.


### Date d’émissions


C’est la date de tous les documents qui vont être générés.


### En Bon de livraison ou Facture


Suivant la sélection de cette option, l’affectation de commande générera 
 des bons de livraison ou des factures.


Lorsque vous choisissez de générer des factures, il ne sera pas effectué 
 de regroupement : A une Commande correspond une facture.


### Présélections des documents


Une présélection des documents est possible par la sélection des fourchettes 
 des fichiers suivant :


* Clients,


Remarque 
 : Le tiers sélectionné doit être le tiers livré et non le tiers payeur. 
 Si le tiers est bloqué, le transfert n'est pas possible ni dans le module 
 Ventes/ Transfert automatique des commandes, ni dans la Multi 
 sélection des documents (à partir de la liste), ni dans la module Ventes/Portefeuille 
 de commandes . Si le tiers a un tiers payeur associé, le contrôle sera 
 effectué sur le tiers payeur,


* Familles de tiers,
* Sous-famille de tiers,
* Commerciaux/


 


De même, il est possible d’effectuer l’opération sur un, tous ou un 
 ensemble de dépôts.


### Pourcentage minimum de livraison ou facturation


Vous pouvez choisir d’effectuer des livraisons globales (minimum de 
 livraison/facturation = 100% ou partielles en indiquant un pourcentage 
 inférieur à100).


### Le pourcentage livrable/facturable minimum dépend du stock disponible


A la prochaine affectation de commande, le pourcentage saisi sera automatique 
 proposé.


Ce pourcentage peux s’effectuer sur les quantités ou sur le montant.


## Ordre de traitements des commandes


Il est possible de définir l’ordre de traitement des commandes en fonction 
 du délai de livraison suivie d’un classement précis et si ce délai est 
 dépassé, il est possible de définir un autre ordre.


 


Le tri par défaut, lorsqu’un délai de livraison est inférieur à un nombre 
 de jours, est :


* Priorité client,
* Date prévue,
* Date du document,
* Montant TTC décroissant.


 


Le tri par défaut, si le délai est dépassé,est :


* Date prévue,
* Date du document,
* Priorité client,
* Montant TTC décroissant.


 


Vous pouvez à tous moment changer la définition des tris par le bouton 
 définir.


 


Les autres champs de tri disponibles sont :


* Déjà livré partiellement ?,
* N° de pièce,
* Payeur,
* Client,
* Famille de client,
* Sous-famille de client,
* Commercial,
* Dépôt.


 


Suite à changement de tri, il est toujours possible de rétablir les 
 tris par défaut.


## Liste des commandes


La liste des commandes à affecter est triée par ordre de priorité.


 


Le logiciel signale les commandes pouvant être livrées en totalité et 
 celles qui répondent au pourcentage minimal de livraison (pour une éventuelle 
 livraison partielle).


 


Le menu contextuel ou les raccourcis claviers, vous permettent :


* D’inclure ou d’exclure certaines commandes de la génération 
 des bons de livraison, (la ligne de commande est alors barrée et grisée),
* Tout inclure ou tout exclure,
* De visualiser les documents non livrables pour le pourcentage 
 minimum: les documents seront affichés en italique, grisés et barrés,
* Ouvrir la pièce,
* Rafraîchir les documents,
* D’accéder aux fonctions générales d'une liste.


 


Note : le double-clic simplement sur la ligne de la commande et le fait 
 d’appuyez sur la barre espace permet également d’inclure et/ou exclure 
 les documents.


## Options supplémentaires


### Facturation/livraison sur


Il est possible de livrer/facturer sur le même dépôt que le document 
 d’origine ou sur un dépôt unique.


Si vous choisissez l’option dépôt unique, vous devez sélectionner celui-ci 
 à l’aide de la liste.


### Si transfert partiel du à un stock insuffisant


Dans le cas d’une livraison partielle, vous pouvez choisir de :


* Gérer en reliquat les quantités d’articles non livrés,
* Ne pas gérer en reliquat les quantités d’articles non livrés,
* Ne pas faire le transfert si les quantités en stock sont insuffisantes.


 


Dans le dernier cas, l’Accusé réception restera en état "En-cours" 
 et aucun Bon de livraison ne sera réalisé.


### Création d’une ligne avec une quantité à 0 si stock absent


Cette option vous permet d’afficher les reliquats sur les bons de livraison 
 sans avoir à affecter manuellement la quantité à livrer à 0.


### Création manuelle si inexistence


L’option "Création manuelle : 'articles' " vous permet de 
 [créer automatiquement l'article inexistant](../../TransfertDuplicationDocument/5/CréationArticleDuplicationTransfert.md) jusqu’à présent 
 dans la base.


* Article est inexistant,
* L’option est sélectionnée,
* La préférence oblige l'article d'exister pour le type du document 
 destinataire.


### Affectation manuelle (si non renseigné, stock périmé,…)


Lorsque vous avez sur votre document d’origine un article gérant les 
 gammes ou les numéros de lot et que vous n’avez pas renseigné la gamme 
 ou le numéro de lot sur celui-ci, vous devez sélectionner l’affectation 
 manuelle des gammes ou n° lot ou N° de série. Une fenêtre d'affectation 
 s’ouvrira lors du transfert d’un accusé réception dans un Bon de livraison 
 ou une Facture.


### Recopie des lignes


Texte : Lorsque vous sélectionnez 
 cette option, les lignes de ‘texte’ présentes sur vos "Accusés réceptions" 
 seront recopiées dans les "Bons de livraison" générés;


Total : Lorsque vous sélectionnez 
 cette option les lignes ‘sous-total’ et ‘total’ présentes sur vos "Accusés 
 réceptions" seront recopiées dans les "Bons de livraison" 
 générés.


## Génération des bons de livraison / factures


Pour la génération des bons de livraison / Factures, le logiciel traite 
 chaque commande et génère le bon de livraison ou facture correspondant 
 lorsque la quantité des articles livrables représente un pourcentage égal 
 ou supérieur au pourcentage demandé.


 


Pour chaque traitement, vous visualisez les commandes prises en compte 
 et le/les numéros de Bons de livraison ou Factures générés.


 


A la fin du traitement, vous avez la possibilité de visualiser et d’enregistrer 
 [un 
 rapport de traitement](../../TransfertDuplicationDocument/2/RapportFinTraitement.md).


 


Pour avoir un exemple de rapport cliquez ici .


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
//]]>
