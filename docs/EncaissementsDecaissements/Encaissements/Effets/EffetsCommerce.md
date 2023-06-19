# Effets de commerce

La gestion des effets de commerce s’applique à toutes les échéances 
 dont le mode de règlement appartient à une catégorie de règlement définie 
 (dans les tables) avec un type de remise.


 


Toutes les échéances en devise société ou en devise locale (pour une 
 société appartenant à la zone Euro) sont prises en compte.


 


La gestion des effets de commerce permet :


* De répartir les 
 échéances de manière automatique sur les différents journaux de banque, 
 avec prise en compte de la priorité et du plafond de remise définis 
 dans la fiche du journal,
* D’enregistrer un 
 règlement par journal,
* D’effectuer une 
 remise en banque globale,
* De générer un fichier 
 ETEBAC.


## Recherche des effets de commerce


La gestion des effets de commerce est accessible à partir de la commande 
 "Échéances à recevoir" du menu Encaissements/Échéances clients 
 + le menu contextuel + la commande "Règlements et Remises"’.


 


Par défaut, le logiciel recherche dans la liste 
 des échéances courantes, celles dont le mode de règlement est défini avec 
 un type de remise LCR, Virement, Billet à ordre ou Prélèvements, et qui 
 sont définies en devise société ou Euro. (Devise euro après bascule).


 


Un [message 
 d'avertissement](../ReglementsRemises/AvertissementEcheancesSansModeSansType.md) affiche le nombre d’échéances ne répondant pas à ces 
 critères.


## La liste des effets de commerce


La fenêtre des effets affiche un onglet par type d’effets de commerce.


 


Pour chaque échéance, vous obtenez par défaut 
 : le numéro de la pièce, la date d’échéance, le tiers, le solde de l’échéance, 
 la devise, la première banque du client et son RIB, le journal sur lequel 
 vous souhaitez effectuer la remise en banque.


### Informations sur les journaux


Les informations concernant les journaux de trésorerie (affichage des 
 totaux par journal) peuvent être affichées ou masqués par le menu contextuel. 
 De plus, l’affichage peut ou non être activée dès l’ouverture de la liste 
 par le menu contextuel sur la partie grisée de la fenêtre.


### Modification du RIB du tiers


Le menu contextuel permet de compléter un RIB Tiers ou éventuellement 
 de [sélectionner 
 le RIB](../Reglements/Receptionner/SelectionCoordonneesBancaires.md) d’une autre banque du tiers.


### Rafraîchir les échéances


Pour annuler les modifications apportées aux échéances (modification 
 de RIB, affectation d’un journal de banque, .. ), Pensez au rafraîchissement 
 (menu contextuel ou touche F5)


## Répartition sur les journaux


La répartition sur les journaux (bouton Répartir ou menu contextuel) 
 permet d’affecter automatiquement les échéances à un journal de banque. 
 La répartition traite chaque échéance une à une par ordre croissant de 
 date en prenant en compte tout d’abord la priorité de la remise du journal, 
 puis son plafond.


 


Une affectation manuelle reste possible en sélectionnant directement 
 sur l’échéance le journal de banque. A l’enregistrement de la remise, 
 un message vous signalera si le plafond du journal est dépassé. [Exemple 
 de répartition](../ReglementsRemises/ExempleRepartition.md).


## Les règlements et la remise


L’enregistrement des règlements conserve obligatoirement 
 le mode de règlement par défaut associé à chaque échéance. Pour un règlement 
 dans un autre mode, vous devez passer par les commandes "[Réception 
 des règlements](../Reglements/Receptionner/ReceptionnerReglements.md)" du menu Encaissements.


 


Le [règlement 
 par journal](../ReglementsRemises/ReglementParCompteBancaire.md) permet de régler en une seule opération toutes les échéances 
 affectées au journal de l’échéance courante.


 


Cette opération est suivie généralement de l’opération de remise en 
 banque et d’impression avec possibilité de générer un fichier ETEBAC (fichier 
 de Transmission bancaire).


 


Un bordereau unique de remise en banque est généré pour la totalité 
 des règlements du journal.


## Impression


Il est possible d’imprimer la liste des échéances (Bouton Imprimer liste) 
 et, uniquement à partir des onglets Lettres de change, Traite et Virement, 
 d’imprimer une échéance (bouton Imprimer échéance).


 


[Voir aussi](javascript:RelatedTopic0.Click())


Voir aussi (espace réservé)
 

1. [Liste des rubriques](#)



