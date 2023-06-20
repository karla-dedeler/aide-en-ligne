# Purger les écritures


La purge des écritures est accessible à partir du menu Outils/Purge 
 les écritures.


 


La purge des écritures permet de supprimer de manière définitive certaines 
 écriture et les tables associées (analytique, échéances …) appartenant 
 à des exercices antérieurs.


 


Une sauvegarde de votre dossier sera faite automatiquement avant de 
 lancer ce traitement.


## Modalités pour pouvoir effectuer la purge des écritures


### Exclusivité


La base doit être ouverte de manière exclusive.


 


Si un seul utilisateur travaille sur le dossier, le logiciel connecte 
 automatiquement le dossier en ouverture exclusive. Dans le cas contraire, 
 un message d’avertissement informe qu’un autre utilisateur est sur la 
 base et donc que la purge est impossible.


### Droit


Dans la gestion des utilisateur, vous devez avoir sélectionné dans la 
 branche Administration + Purge, les droits pour pouvoir lancer ce traitement.


### Obligation


Pour pouvoir purger les écritures, vous devez avoir au moins 2 exercices 
 de clôturés. Seul le premier de ces 2 exercices clôturés pourra être purgé.


 


La purge peut-être lancer que si :


* L’exercice est 
 clôturé et qu’il n’est pas le dernier,
* L’exercice n’est 
 pas déjà purgé.


## Traitement de la purge des écritures


Un assistant vous guide dans les différentes étapes de la purge des 
 écritures.


 


[Purger les écritures : Informations](PurgerEcrituresInfos.md)


Cette purge réalise la suppression des écritures ainsi que les informations 
 des tables liées à celle-ci : écriture analytiques, échéances sur écriture, 
 échéances, écriture de TVA sur encaissement …


 


Les écritures supprimables sont celles antérieures au dernier exercice 
 clôturé.


 


[Purger les écritures : Options](PurgerEcrituresOptions.md)


Le 2ème écran vous permet de saisir les informations de paramétrage 
 de la purge :


* Sélection de l’exercice 
 pour lequel le traitement effectuera la purge des Écritures antérieures 
 à celui-ci,
* Sélection de l’option 
 Purger les cumuls périodiques : lors de la consultation des écritures 
 dans le centralisateur, celles purgées n’apparaîtront plus,
* Sélection de l’option 
 Purger les cumuls par compte et par exercice: Lors de la consultation 
 du cumul du compte, il y aura aucun montant pour l’exercice purgé.


 


Rappel :


Une sauvegarde sera faite avant que le traitement soit lancé. Elle sera 
 stockée sur le serveur avec le nom :


Nom de la société + "\_" + Date du jour au 
 format AAAAMMJJ\_HHMM + "\_SauvegardeAvantPurgeEcritures.bak"


 


Suite au lancement du traitement (bouton ‘’Terminer’’), le traitement 
 affiche ‘‘Purge en cours …’’


 


Lorsque le traitement est achevé, un message vous informe que la purge 
 s’est déroulée avec succès et du nombre d’écriture supprimées par rapport 
 au total des écritures du dossier


## Conséquences de la purge des écritures


Les écritures supprimées par la purge ne sont plus consultables dans 
 les centralisateurs, la recherche d’écriture, export liasses fiscales…


