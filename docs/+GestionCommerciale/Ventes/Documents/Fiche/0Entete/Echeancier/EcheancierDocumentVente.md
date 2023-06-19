# Echéancier du document de vente



Si un mode de règlement est paramétré sur la fiche tiers, celui-ci sera 
 repris automatiquement lors de la [création 
 de la pièce](../Entête.md), ainsi vous aurez une ou plusieurs échéances créées automatiquement.


 


L’échéancier permet de répartir les échéances de la pièce.


## Entête


L’échéancier reprend le numéro de la pièce, la date de réalisation de 
 celle-ci et le nom du tiers concerné. Les montants totalisant la pièce 
 et les échéances saisies sont également indiqués.


Lorsque le total des lignes d’échéances ne correspond pas au montant 
 total de la pièce, la ligne "Montant des échéances" est en Rouge 
 et vous n’avez pas la possibilité de sortir de la fenêtre tant que l’équilibre 
 n’est pas établit (le bouton OK est grisé).


## Saisie des échéances


La saisie d’une ligne d’échéance consiste à sélectionner :


* Le domaine d’application de l’échéance,
* Le mode de règlement,
* Le pourcentage qui représente le montant de cette ligne d’échéance,
* Le choix du calcul de l’échéance sur le HT ou le TTC, (en gestion 
 commerciale uniquement)
* Le montant de l’échéance,
* La date d’échéance,
* Le commentaire de l’échéance (libellé).


 


La colonne Pièce sera renseignée automatiquement lors d’un transfert 
 de pièce.


Par exemple : lorsque vous réaliser un échéancier sur une commande et 
 que vous transférez celle-ci en bon de livraison/réception, la ligne de 
 l’échéancier sur commande affichera dans la colonne "Pièce" 
 le numéro de votre commande.


Lorsque vous avez plusieurs lignes d’échéance, le bouton ![image\Gest0033_wmf.gif](Echeancier_Solder.gif "image\Gest0033_wmf.gif") ou le raccourci clavier ALT+S, vous permet 
 de solder votre dernière ligne d’échéance.


Il est impossible de solder l’échéancier sur une ligne d’échéance calculée 
 sur le HT (champ HT sélectionné). La sélection du bouton "Solder" 
 affiche le message "Vous ne pouvez pas solder une échéance calculée 
 sur le HT".


 


Le menu contextuel vous permet :


* D’insérer une échéance,
* De supprimer une échéance,
* D’ accéder à toutes les fonctions générales d'une grille.


### Domaine d’application


Suivant les pièces réalisées en ventes ou achats, vous avez la possibilité 
 de créer un échéancier pour différents domaines.


 


Pour un Pro-forma ou un Devis ou une Demande de prix, les domaines possibles 
 sont :


* Avance,
* Commande,
* Livraison,
* Facture.


 


Pour un Accusé réception ou une Commande, les domaines possibles sont 
 :


* Commande,
* Livraison,
* Facture.


 


Pour un Bon de livraison/réception ou de retour, les domaines possibles 
 sont :


* Livraison,
* Facture.


 


Pour une Facture (financière ou non) ou un Avoir (financier ou non), 
 le domaine possible est la Facture.


### Date de l’échéance


Par défaut, la date d’échéance est la date de réalisation de la pièce.


Si un mode de règlement est affecté à la pièce, la date d’échéance sera 
 calculée d’après le paramétrage de la fiche de celui-ci. Cette date reste 
 toutefois modifiable.


## Cas particulier


### Saisie d’un acompte en pied de document


Lors de la saisie d’un acompte en pied de document, la fenêtre échéancier apparaît avec une ligne 
 d’échéance représentant le montant de l’acompte, le reste étant sur la 
 Facture par défaut


De plus, cet acompte est matérialisé par ![image\Gest0034_wmf.gif](Gest0034_wmf.gif "image\Gest0034_wmf.gif") dans la 
 colonne Acompte.


 


Lors de la saisie d’un acompte en pied de document de ventes ou d’achats, 
 le domaine de la génération d’une ligne d’échéance varie suivant le document 
 réalisé :


* Pour un Pro-Forma, un Devis, une Demande de prix, une Facture, 
 un Avoir, le domaine de la ligne d’acompte est Avance,
* Pour un Accusé réception, une Commande, le domaine de la ligne 
 d’acompte est Commande,
* Pour un Bon de livraison/réception, Bon de retour, le domaine 
 de la ligne d’acompte est Livraison.


 


Attention : Si vous saisissez 
 un acompte dans le document, nous vous conseillons de réaliser votre échéancier 
 uniquement à l’ouverture de la fenêtre, en effet votre échéancier est 
 modifié (recalculé) lors de la génération de la ligne d’échéance de l’acompte.


### Conséquence sur l’échéancier d’un document suite au règlement d’une 
 échéance


Lors du règlement d’une échéance du document, le règlement est matérialisé 
 par ![image\Gest0035_wmf.gif](Gest0035_wmf.gif "image\Gest0035_wmf.gif") dans la colonne réglé. 
 Cela signifie que l’échéance n’est pas modifiable.


### Conséquence sur l’échéancier d’un document suite à la modification 
 du document : Création d’une échéance négative


Si par la suite, vous effectuez une modification du document et que 
 le total de ce document est inférieur au montant déjà réglé, un message 
 vous informera qu’une échéance négative a été créée pour la différence 
 entre le montant initial du document (montant réglé) et le montant après 
 modification.


### Transfert partiel d’un Accusé Réception ou une Commande


Lors d’un transfert partiel d’un Accusé Réception ou d’une Commande, 
 la fenêtre Échéancier évolue en fonction du montant livré.


Suite à un transfert partie l’échéancier de l’Accusé Réception/Commande 
 affiche une colonne supplémentaire qui indique le montant transféré. Cette 
 colonne évolue en fonction des transferts effectués.


Lorsque le document est transféré entièrement (il est alors en état 
 Supprimé), les montants de la colonne "Transféré" sont identiques 
 aux montants de la colonne "Montant"


Pour voir un exemple cliquez [ici](ExempleEcheancierFractionneSuiteTransfertsPartiels.md).


