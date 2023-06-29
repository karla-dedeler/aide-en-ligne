# Frais



La création d’un frais consiste à saisir un code frais, un libellé et 
 à sélectionner un type de frais (port ou autres).


## Base de calcul


### Livraison et Transporteur


Le mode de Livraison 
 et de transport sont à sélectionner dans la liste déroulante. Ces informations 
 seront utilisées lors de la réalisation de la déclaration d'échanges 
 de biens (DEB).


### Montant du frais


Un frais peut être :


* Un montant à saisir 
 en pied de document (zone Montant fixe vierge),
* Un montant fixe.
* En fonction du montant de la facture.


 


Montant Fixe permet de paramétrer un montant de frais à saisir en pied 
 de document (ne saisir aucune valeur dans la zone Montant) ou de définir 
 un montant fixe de frais non modifiable en pied de document.


### Pourcentage du HT


A partir du pourcentage saisi, le frais sera calculé sur le Montant 
 Total brut du document ![image\Gest0000.gif](../../assets/images/Frais/2/BoutonDossier.gif) .


### Par palier


Le seuil correspond au montant du document.


Lorsque le montant du document est inférieur ou égal au Seuil établit, 
 il sera appliqué le montant de frais correspondant, au-delà il faudra 
 faire référence au palier supérieur.


 


Exemple :






| Seuil | Montant |
| 0 | 100 |
| 50 | 80 |
| 100 | 50 |


 


Si le montant du document est 50.00, Le frais sera de 100.


Si le montant du document est 50.01, Le frais sera de 80.


## Comptabilité


Le logiciel propose par défaut les informations paramétrées dans la 
 fiche de [chaque 
 nature comptable](../../NaturesComptable/1/NaturesComptables.md). Ces informations étant modifiables, il est possible 
 de paramétrer un traitement comptable particulier pour chaque frais et 
 chaque type de vente et d’achat.


 


Exemple : Le compte comptable proposé pour traiter les frais est le 
 compte général indiqué dans la fiche de la nature comptable (par exemple 
 707100 pour les ventes). Pour distinguer le montant des frais du montant 
 brut des ventes, il suffit d’indiquer un autre compte (par exemple 708500)


 






