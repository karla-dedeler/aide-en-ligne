# Préparer les paiements

La commande "Préparation des paiements" du menu Décaissements 
 permet :


* D’enregistrer les paiements 
 aux fournisseurs et de solder partiellement ou totalement les échéances 
 à payer en cours,
* De consulter les paiements 
 effectués sur une période donnée.


 


Lorsque la ligne d’un paiement est grisée, cela correspond à un paiement 
 effectué en Compta alors que vous consultez la liste en Gestion commerciale 
 et vice-versa.


## Liste des paiements


La liste affiche les paiements en cours (non émis) enregistrés pendant 
 la période définie en entête. Pour modifier un paiement, double-cliquez 
 sur sa ligne. Le détail du paiement apparaît alors dans le bas de la fenêtre 
 et peut être modifié.


 


Le menu contextuel de la liste vous permet :


* De créer un nouveau paiement 
 (Nouveau),
* De modifier un paiement,
* De supprimer un paiement,
* D’accéder aux fonctions de 
 toutes les grilles.


## Saisie d’un paiement


### Ligne de paiement


Une ligne de paiement est obligatoirement composée :


* D’une devise,
* D’un type de paiement,
* D’une date de règlement,
* D’un code fournisseur : vous 
 pouvez le saisir, le sélectionner dans la combo liste ou le rechercher 
 par l’icône,
* Du montant payé.


 


Suite à la sélection du code tiers, la raison sociale de celui-ci s’affichera 
 après le texte "payé à :".


 


Attention ! Si le journal est 
 défini en devise ou en devise société exclusivement, la devise du journal 
 est prioritaire sur la devise du tiers : le montant réglé est alors converti 
 dans la devise du journal de banque sélectionné.


 


Vous pouvez également :


* Saisir le numéro de pièce 
 (suite à la saisie du tiers, de la devise et du montant, le logiciel 
 pinte automatiquement sur la première pièce dont l’échéance crrespnd au montant du règlement),
* Saisir un numéro de chèque,
* Modifier la date d’échéance,
* Saisir une référence,
* Saisir une banque.


### Journal de banque


Le journal de banque est facultatif mais permet une présélection des 
 paiements qui seront automatiquement proposés en émission de paiements.


### Montant réglé et Échéancier


A la saisie du numéro de pièce, le logiciel 
 recherche automatiquement le montant à régler à partir des échéances en 
 cours.


 


Ce montant est modifiable manuellement, ou à partir du bouton Échéancier 
 si vous souhaitez affecter ce paiement à une autre ligne d’échéance.


 


Dans ce cas, sélectionnez la ligne et en colonne Affecté, saisissez 
 le montant payé.


 


Pour solder l’échéance, double-cliquez dans la ligne ou appuyez sur 
 la Barre Espace.


 


Le bouton OK permet d’enregistrer le montant affecté.


 


Par le bouton Modifier, il vous est possible de :


* Modifier l'affectation du 
 paiement sur une ou plusieurs échéances (bouton Échéancier),
* Modifier l'affectation de 
 l'écart de paiement,
* Modifier le RIB du tiers.


## Validation du paiement


Une fois toutes les informations du paiement saisies et le pointage 
 effectué, le bouton Valider permet d’enregistrer effectivement le paiement 
 qui s’affiche alors dans la liste.


### Écart de paiement


Suite à la validation, le logiciel peut ouvrir automatiquement la fenêtre 
 d’écarts de paiement, lorsque l’écart entre le montant saisi et l’échéance 
 correspond à un seuil défini dans les préférences.


## Conséquences de la validation


En gestion commerciale comme en comptabilité, le paiement que vous venez 
 de saisir reste modifiable tant que vous n’avez pas réaliser [d’émission 
 des paiements](../Emissions/EmissionPaimentsFiche.md).


## Impression


Par l’icône Imprimer de la barre d’outils ou la menu contextuel + "Imprimer", 
 vous pouvez éditer :


* La liste des paiements des 
 tiers [Modèle Liste(par Tiers)],
* Une lettre chèque : liste 
 des échéances payées par un Tiers avec un chèque en pied de document.


