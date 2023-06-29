# Calcul de TVA



La déclaration de TVA diffère d’un pays à l’autre. C’est pourquoi, le 
 logiciel vous permet de programmer votre propre état préparatoire à la 
 déclaration de TVA.


 


Pour cela, vous devez :


* Définir 
 dans les tables un code Ventilation pour chacun des montants que vous 
 souhaitez suivre dans votre état préparatoire,
* Paramétrer 
 la fiche des comptes de TVA, de charges et de produits et les ventiler 
 sur le code Ventilation TVA ou CA correspondant,
* Lancer 
 le calcul de l’état préparatoire et éventuellement le modifier,
* Exploiter 
 les informations de l’état préparatoire.


## Paramétrage des ventilations


Pour chacun des montants que vous souhaitez visualiser dans votre état 
 préparatoire, vous devez paramétrer un code Ventilation dans les tables 
 de références du dossier.


 


Chaque ligne de ventilation est composée d’un code, d’un libellé et 
 d’un booléen "saisissable".


### Code


Vous devez indiquer ici le numéro de la ligne 
 présent sur la déclaration de TVA.


### Libellé


Ce champ permet de saisir la désignation de 
 la ligne.


### Saisissable


La sélection de cette case vous donne la possibilité 
 de saisir une valeur au moment du calcul de la préparation à la déclaration 
 de TVA.


### Exemple de codes Ventilation (sur la base d’une Déclaration de TVA 
 France)


01 Ventes, prestations de services


…


08 Taux à 20


13 TVA antérieurement déduite à reverser


 


Pour avoir un exemple de création dans les tables cliquez [ici](ExempleVentilationTVA.md).


## Paramétrage des comptes


Pour tous les comptes de TVA, de charges et de produits utiles au calcul 
 de vos ventilations, vous devez paramétrer l’onglet Informations.


### Comptes de TVA


Sur chaque fiche de compte de TVA, vous devez définir dans l’onglet 
 général le sens du compte.


 


Dans l’onglet information de la fiche du compte de TVA, vous devez indiquer 
 :


* Le taux 
 de TVA désiré pour le compte,
* Le type 
 de TVA,
* La ventilation 
 de TVA (à paramétrer dans les tables de références) : Cette ventilation 
 vous permet de déterminer l’intitulé de la ligne correspondant au 
 montant de TVA des lignes de produits ou charges,
* Le type 
 d’opération (France ou UE).


 


Pour avoir un exemple de création dans les tables cliquez [ici](ExempleParametrageCompteTVA.md).


### Comptes de produit et de charge


Sur chaque fiche de compte de produit ou de charge, vous devez définir 
 dans l’onglet général le sens du compte.


 


Dans l’onglet information de la fiche du compte, vous devez indiquer 
 :


* Le compte de TVA 
 correspondant au compte de produits ou de charges,
* La ventilation 
 de CA (à paramétrer dans les tables de références) : Cette ventilation 
 vous permet de déterminer l’intitulé de la ligne correspondant au 
 montant HT des produits ou charges.


 


La Ventilation sur CA des montants de vos comptes de produits et de 
 charges n’est pas obligatoire mais est vivement conseillée pour vérifier 
 la cohérence entre le montant de la base HT calculé à partir du montant 
 de TVA (par la ventilation TVA) et le montant de la base HT calculé à 
 partir de la ventilation CA.


 


Pour avoir un exemple de création dans les tables cliquez [ici](ExempleParametrageCompteChargesProduits.md).

