# Avis d'encaissement de A à Z

L’[avis d'encaissement](../AvisEncaissement/EffetEncaissement.md) est généré par le menu contextuel 
 de la liste des remises à l'encaissement / à l'escompte.


 


Suite à la réception de l’avis d’encaissement de la banque, vous pouvez 
 générer votre avis d’encaissement afin de solder votre compte d’effet 
 à l’encaissement


## Comment réaliser l'avis d'encaissement ?


Pour réaliser un avis d’encaissement, vous devez :


* Depuis la liste 
 des remises, sélectionner la ligne pour laquelle vous souhaitez réaliser 
 un avis d’encaissement,
* Par le menu contextuel, 
 sélectionner l’option ‘’Avis d’encaissement’’, la saisie de la fenêtre 
 avis d’encaissement vous sera alors proposée.


## Fenêtre de saisie de l’avis d’encaissement


Cette fenêtre permet de saisir :


* La date de l’avis,
* Le journal de banque: 
 il peut être pré-paramétrer dans les préférences de la société (onglet 
 Encaissements),
* Le montant et le 
 compte associé des frais d’encaissement,
* Le montant et le 
 compte associé de la TVA sur frais d’encaissement.


 


Ensuite, vous devez sélectionner les règlements concernés par l’avis 
 d’encaissement (menu contextuel + ‘sélectionner’ ou ‘sélectionner tous’, 
 barre d’espace, double clic …).


 


Une fois ces informations saisies, vous devez cliquer sur le bouton 
 Ok pour valider l’avis d’encaissement.


 


Par le menu contextuel du menu Encaissements/[Avis 
 d'encaissement reçus](../AvisEncaissement/AvisEncaissementRecus.md) vous pouvez [consulter 
 les avis d'encaissement](../AvisEncaissement/AvisEncaissementRecus.md).


## Conséquences de la validation de l’avis d’encaissement


En gestion commerciale, vous devez effectuer le transfert comptable 
 de vos avis d'encaissements depuis l’option ‘’avis d’encaissement et avis 
 d’escompte’’ pour qu’une écriture soit générée.


 


En comptabilité, la validation de l’avis d’encaissement génère une écriture 
 dans le journal de banque correspondant à l’avis.


 


Ces écritures ne sont pas modifiables. Seule la suppression de l’avis 
 supprimera les écritures.


 


Exemple d’écriture simple : Débit 512 / Crédit 5113.


Exemple d’écriture avec frais : Débit 512. Débit 627. Débit 44566 / 
 Crédit 5113.


## Modification de l’avis d’encaissement


Un avis d’encaissement ne peut être modifié, vous devez supprimer l’avis 
 d’encaissement.


## Suppression de l’avis d’encaissement


### Conditions pour pourvoir supprimer l’avis


En gestion commerciale, la suppression d’un avis d’encaissement n’est 
 possible que si le transfert comptable des avis d’encaissement n’a pas 
 été réalisé


Il n’y a pas de contrainte de suppression dans la comptabilité.


### Comment supprimer l’avis ?


A partir de [l'historique 
 des avis d'encaissement](../AvisEncaissement/AvisEncaissementRecus.md), sélectionnez l’avis à supprimer puis par 
 le menu contextuel choisissez l’option "Supprimer". Un message 
 vous demande de confirmer la suppression ou non de l’avis.


## Conséquences de la suppression d’un avis d’encaissement


En gestion commerciale, la remise à l’encaissement est remise à disposition 
 pour un prochain avis d’encaissement.


 


En comptabilité, la suppression de l’avis d’encaissement supprimera 
 les écritures générées et la remise à l’encaissement est remise à disposition 
 pour un prochain avis d’encaissement.


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
//]]>
