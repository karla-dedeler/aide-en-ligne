# Impayés de A à Z

L’option "Impayé" permet de remettre à disposition une échéance 
 réglée mais qui est retournée par la banque comme étant impayée.


## Comment réaliser l’impayé ?


Pour réaliser un impayé, vous devez :


* Depuis les règlements 
 reçus sélectionner la ligne pour laquelle vous souhaitez réaliser 
 un impayé,
* Par le menu contextuel, 
 sélectionner l’option "Impayé", la saisie de la fenêtre 
 Impayé vous sera alors proposée.


 


Conditions d'affichage de cette option :


* L'échéance doit 
 obligatoirement être remise en banque,
* Le type de règlement 
 doit être Chèque, Billet à ordre ou LCR,
* Aucun impayé ne 
 doit être déjà généré pour cette échéance (champ RIP\_NUMERO).


## Fenêtre de saisie de l’impayé


Cette fenêtre permet de saisir :


* La date,
* La sélection d’un 
 motif est obligatoire,
* Les frais : le 
 montant ainsi que le compte dont la racine est définie dans les préférences 
 de la société/Racines/Onglet charges et produits/Services bancaires,
* La TVA sur frais 
 : le montant ainsi que le compte dont la racine est définie dans les 
 préférences de la société/Racines/Taxes/TVA sur biens et services.


 


La liste des motifs d’impayés peut être alimentée par le menu Société/Paramétrage/Tables 
 de Références/Motifs d'impayés.


 


Dans l’onglet Compteurs des préférences de la société, vous pouvez visualiser 
 le nombre d’impayés effectués sur le dossier.


 


Par le menu contextuel du menu Encaissements/[Impayés](ImpayésEnregistrés.md) 
 vous pouvez [consulter les impayés](FicheImpaye.md).


## Conséquences de la validation d’un impayé


Dans le cas ou l’impayé est saisi en comptabilité, une écriture est 
 générée automatiquement.


 


Si toutefois l’impayé est réalisé en gestion commerciale, vous devez 
 effectuer un transfert comptable du "Règlement impayé" pour 
 que l’écriture comptable se génère.


## Modification d’un impayé


Un Impayé ne peut être modifié, vous devez supprimer l’impayé.


## Suppression de l’impayé


### Conditions pour pourvoir supprimer l’impayé


En gestion commerciale, la suppression d’un impayé n’est possible que 
 si le transfert comptable des règlements impayés n’a pas été réalisé.


 


Il n’y a pas de contrainte de suppression dans la comptabilité.


### Comment supprimer l’impayé ?


A partir de l’historique des impayés, sélectionnez l’impayé à supprimer 
 puis par le menu contextuel choisissez l’option "Supprimer". 
 Un message vous demande de confirmer la suppression ou non de l’impayé.


## Conséquences de la suppression d’un impayé


En gestion commerciale, le règlement est remis à disposition pour un 
 prochain impayé.


 


En comptabilité, la suppression de l’impayé supprimera les écritures 
 générées et le règlement est remis à disposition pour un prochain impayé.


