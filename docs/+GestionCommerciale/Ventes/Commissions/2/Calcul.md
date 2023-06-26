# Calcul des commissions sur les ventes



Le calcul des commissions (menu VENTES) consiste à retrouver tous les documents, toutes les échéances en cours, tous les règlements qui donne lieu à un commissionnement sur la période de référence pour le ou la sélection de commerciaux.


 


Avant de lancer le calcul des commissions commerciaux, il est indispensable qu’un [paramétrage correct](../1/Parametrage.md) soit effectué.


## Entête


#### Définir le calcul


Avant de lancer le calcul des commissions (bouton Calcul), vous devez définir dans votre entête :


* Le ou l’intervalle des commerciaux pour lesquels vous souhaitez obtenir le commissionnement,
* La période sur laquelle vous souhaitez calculer ce commissionnement,
* Le type d’information à afficher : détail ou non des articles, des tiers ou encore de la marge.


#### Lancer le calcul


Permet de calculer les montants en fonction des paramètres définis dans l’entête. Dès que vous modifiez l’un de ces paramètres, une note en rouge vous signale qu’il est indispensable de relancer le calcul des commissions.


## Lignes de commissions


Le contenu qui s'affiche est le résultat fidèle du paramétrage effectué dans les fiches des barèmes, des commerciaux et des lignes d’articles.


Vous obtenez pour chaque commercial, le détail des pièces entrant dans le domaine d’application de chaque barème.


Un détail des articles, des tiers ou de la marge peut ou non être affiché à partir des cases à cocher de l’entête.


### Lignes de pièce


Les lignes courantes contiennent le détail de chacune des pièces (N° de pièce, Date de la pièce, Domaine, Commercial, Client, Quantité vendue, Chiffre d’affaires, Marge, Article vendu) concernée par un barème.


Lorsqu’un article fait l’objet d’une commission particulière, il apparaît sur une ligne distincte.


### Lignes de barème


Les lignes sous-total (par défaut en caractère gras de couleur noir Sous-total) affichent le détail de chaque barème (domaine, objectif, formule, intéressement).


Lorsque le barème est de type Tranche, le logiciel affiche autant de lignes de barème que de lignes d’objectif entrant en compte dans le calcul de la commission.


### Lignes commercial


Les lignes Total (par défaut en caractère gras rouge Total) affichent le montant total de la commission commercial sur la période, tout barèmes confondus.


## Comment se calculent les commissions ?


Sur chaque document rattaché à un commercial, le logiciel calcule les commissions dans l’ordre de priorité suivant:


* La commission par article lorsqu’un taux de commission a été saisi directement sur une ligne d’article,
* La commission déterminée par un barème ou la commission globale du commercial.


### Commission sur ligne d’article


Pour saisir le taux de commission sur une ligne d’article, la colonne correspondante doit exister. S’il est nécessaire de l’ajouter, utilisez le menu contextuel + Personnaliser la liste et sélectionner la colonne REP\_TX\_COM.


### Commission sur barème


Lorsque le barème et la facture sont en devises, le logiciel convertit automatiquement le montant de la commission en devise société.


La commission s’appliquera sur tous les articles de la sélection du barème à l’exception des articles sur lesquels une commission particulière (voir plus haut commission sur ligne d’article) a été appliquée dans le document.


### Domaine du barème


Du domaine du barème dépend le déclenchement du calcul de la commission :


 







| Domaine      | Déclenchement du calcul de la commission                                          |
|--------------|-------------------------------------------------------------------------------------|
| Facturation  | Factures et avoirs                                                                 |
| Commande     | Commandes et tout autre document résultant de leur transfert.                       |
| Livraison    | Bons de livraison, Bons de retour, Factures et Avoirs (transférés ou non)            |
| Encaissement | Au moment du règlement sur les commandes, bons de livraison et factures.             |
| Échéance     | A la date d’échéance des factures et des avoirs                                      |



### Commission Globale


La commission globale du commercial s’applique à tous les articles à l’exception des articles pour lesquels une commission particulière est appliquée dans le document .


## Impression des commissions


L’impression se lance par le bouton Imprimer de votre barre d’outils et permet de choisir le modèle que vous souhaitez imprimer.


Par le menu contextuel de la grille de commission, vous pouvez également choisir un modèle ou imprimer suivant une liste.


## Exploiter le calcul des commissions


A partir du moment où toutes les lignes sont calculées, il vous est possible de récupérer ces lignes dans le tableur Excel afin d’exploiter les informations qu’elles contiennent.


Pour cela, cliquez simplement sur le bouton ![image\Gest0052_wmf.gif](BoutonExportExcel.gif "image\Gest0052_wmf.gif").Le logiciel ouvre alors l’application Excel et crée une feuille contenant les informations de votre état.


