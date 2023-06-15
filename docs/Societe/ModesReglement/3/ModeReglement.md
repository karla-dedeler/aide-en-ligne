# Mode de règlement



Un [mode de règlement](../1/Introduction.md) est décrit par son code (voir la [règle de codification conseillée](../4/ReglesCodification.md)), son intitulé, son type, le mode de calcul de la date d’échéance de facture et l’échelonnement du règlement.


## Code et libellé


La saisie d’un code (8 caractères maximum) et d’un libellé est obligatoire. Nous vous conseillons de suivre cette codification.
## Type de règlement


Le choix d’un type du mode de règlement est obligatoire et permet de distinguer les règlements selon le moyen de paiement utilisé. Les types (chèque, LCR, Carte Bleue, …) sont à définir dans les tables « types de règlement ». En remise en banque, vous pourrez sélectionner les règlements d’un certain type et obtenir des opérations particulières en fonction du type (fichiers ETEBAC, lettre chèque, ...).


## Journal et compte comptable


Ces zones sont juste informative et ne sont pas utilisées pour lors de la comptabilisation des règlements. Elles peuvent par exemple servir à faire un lien entre avec un compte bancaire.


## Règlement sur relevé


Cette zone est juste informative.


## Échéance


La date d’échéance de la facture est calculée classiquement en nombres de jours ou en mois, net ou fin de mois, tel(s) jour(s).


 


Pour définir un nombre de mois, il suffit de cocher la case « 30 j équivalent à 1 mois » et d’indiquer 30 pour un mois, 60 pour deux mois, 90 pour trois mois, etc


 


Pour un date d’échéance avec indication d’un jour précis « Le », trois jours peuvent être paramétrés.


 


Exemple : Si vous indiquez le 10, le 15 et le 20 et que le calcul en nombre de mois ou de jours donne la date du 16 Avril. Le logiciel ne prendra pas comme date d’échéance le 10 ou le 15 Avril mais le 20 Avril.
## % à la commande / livraison


Les règlements/paiements à la commande et/ou sur bon de livraison/réception peuvent être automatisés ici pour un pourcentage du HT ou du TTC du document.


En réalisation de l’accusé de réception et/ou du bon de livraison/réception, la ligne d’échéance sera automatiquement générée dans l’échéancier.


Cette option permet également d’automatiser la demande d’acompte à la commande ou à la livraison/réception.


## Test de la date d'échéance


Permet d’effectuer un test. Saisissez une date (qui correspondrait à la date de facture), le logiciel calcule automatiquement la date d’échéance.


 



