# Réceptionner les règlements

La "Réception des règlements" du menu Encaissements permet 
 :


* D’enregistrer les règlements 
 clients avec ou sans écart de règlement et de solder partiellement 
 ou totalement les échéances à recevoir en cours,
* De consulter les règlements 
 en cours (non remis en banque) sur une période donnée.


 


Lorsque la ligne d’un règlement est grisée, cela correspond à un règlement 
 effectué en Compta alors que vous consultez la liste en Gestion commerciale 
 et vice-versa


## Liste des règlements


La liste affiche les règlements en cours (non remis en banque) enregistrés 
 pendant la période définie en entête. Pour modifier un règlement, double-cliquez 
 sur sa ligne. Le détail du règlement apparaît alors dans le bas de la 
 fenêtre et peut être modifié.


 


Le menu contextuel de la liste vous permet :


* De créer un nouveau règlement 
 (Nouveau),
* De modifier un règlement,
* De supprimer un règlement,
* D’accéder aux fonctions de 
 toutes les grilles.


## Saisie d’un règlement


### Ligne de règlement


Une ligne de règlement est obligatoirement composée :


* D’un code tiers : vous pouvez 
 le saisir, le sélectionner dans la combo liste ou le rechercher par 
 l’icône,
* D’un type de règlement,
* D’une date d’enregistrement,
* D’un montant,
* D’une devise.


 


Suite à la sélection du code tiers, la raison sociale de celui-ci s’affichera 
 après le texte "réglé par:".


 


Attention ! ! si le journal 
 est défini en devise ou en devise société exclusivement, la devise du 
 journal est prioritaire sur la devise du tiers : le montant réglé est 
 alors converti dans la devise du journal de banque sélectionné.


 


Vous pouvez également :


* Saisir le numéro de pièce 
 (suite à la saisie du tiers, de la devise et du montant, le logiciel 
 pinte automatiquement sur la première pièce dont l’échéance correspond 
 au montant du règlement). La fonction de recherche ou Ctrl + F permet 
 de retrouver une ou des échéances répondant à des critères particuliers 
 (période, code tiers ou raison sociale, numéro de pièce, montant restant, 
 devise),
* Saisir un numéro de chèque,
* Modifier la date d’échéance,
* Saisir une référence,
* Saisir une banque.


### Choix de la banque


Le journal de banque est facultatif mais permet une présélection des 
 règlements qui seront automatiquement proposés en Remise en banque.


### Pointage automatique de l’échéance


Lorsque vous validez (Entrée) le montant du règlement, le logiciel recherche 
 automatiquement dans les échéances du tiers ce montant d’échéance.


 


Par le bouton Modifier, il vous est possible de :


* Modifier l'affectation du 
 règlement sur une ou plusieurs échéances (bouton Échéancier),
* Modifier l'affectation de 
 l'écart de règlement,
* Modifier le RIB du tiers.


## Validation du règlement


Une fois toutes les informations du règlement saisies et le pointage 
 effectué, le bouton Valider permet d’enregistrer effectivement le règlement 
 qui s’affiche alors dans la liste.


### Écart de règlement


Suite à la validation, le logiciel peut ouvrir automatiquement la fenêtre 
 d’[écarts de règlement](EcartsReglement.md), lorsque l’écart 
 entre le montant saisi et l’échéance correspond à un seuil défini dans 
 les préférences.


## Conséquences de la validation


En gestion commerciale comme en comptabilité, le règlement que vous 
 venez de saisir reste modifiable tant que vous ne l’avez pas [remis 
 en banque](../../Remises/RemisesBanque.md).


## Impression


Par l’icône Imprimer de la barre d’outils ou la menu contextuel + "Imprimer", 
 vous pouvez éditer :


* La liste des règlements des 
 tiers [Modèle Liste(par Tiers)],
* Une lettre traite : liste 
 des échéances réglées par un Tiers avec une traite en pied de document.


## Modification d’un règlement


La modification d’un règlement est possible pour le type, la date, la 
 devise, le montant mais pas le tiers.


 






