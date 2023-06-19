# Remise à l'encaissement
L’icône Ouvrir ou le menu contextuel permet d’accéder à la liste des 
 remises à l'encaissement ou à l'escompte en cours ou non.


 


En gestion commerciale, la remise à l’encaissement/l’escompte est obligatoire 
 pour pouvoir transférer vos encaissements et escomptes.


## Conditions pour réaliser une remise à l’encaissement ou à l’escompte


Une remise à l’encaissement ou à l’escompte est possible uniquement 
 si [une mise en portefeuille](../Portefeuille/MisePortefeuilleEffets.md) 
 a été réalisée.


 


Le journal de remise à l’encaissement ou à l’escompte doit obligatoirement 
 avoir un compte de contrepartie dans sa fiche.


## Encaissement / escompte à remettre


L’entête de la fenêtre permet de sélectionner le journal de remise à 
 l‘encaissement ou escompte dans lequel vous allez remettre vos effets 
 à l’encaissement ou à l’escompte.


 


La sélection des effets à remettre s’effectue sur la période d’enregistrement 
 et le type (LCR, BOR,...). Toutefois si des effets ont déjà été rattachés 
 au journal sélectionné, ils apparaissent automatiquement.


 


Le logiciel affiche uniquement les effets enregistrés dans la devise 
 de la banque. Le choix de cette devise est modifiable uniquement si le 
 journal a été défini en devise société et multidevises.


### Sélection des effets


Pour sélectionner (ligne de couleur, bleue par défaut) ou désélectionner 
 une ligne d’effets, il suffit de double-cliquer dessus ou d’utiliser le 
 menu contextuel + Inverser la sélection.


 


Une encoche ![image\Gest0090_wmf.gif](../../assets/images/Effets/RemisesEncaissement/CaseCocher.gif "image\Gest0090_wmf.gif") vous 
 permet de distinguer les lignes sélectionnées ou non.


 


Ce même menu permet de sélectionner tous les effets affichés.


### RIB du tiers


Ces informations sont nécessaires pour la réalisation du [fichier 
 ETEBAC](../../Fichiers/ETEBAC/FichiersBancairesETEBAC.md).


 


Les informations RIB de la première banque du tiers sont récupérées 
 à partir de la fiche de ce dernier. Pour les modifier ou changer la banque 
 du tiers, utilisez le menu contextuel + [Modifier 
 le RIB](../../Reglements/Receptionner/ModificationCoordonneesBancaires.md) sur la ligne du règlement.


 


La liste des différentes banques du tiers est disponible à partir du 
 bouton [Sélectionner 
 un RIB](../../Reglements/Receptionner/SelectionCoordonneesBancaires.md) de la fenêtre Relevé d’identité bancaire.


## Validation de la remise à l’encaissement ou à l’escompte


Pour valider une remise, cliquez sur l’icône Enregistrer, vous avez 
 alors la possibilité d’imprimer un bordereau de remises.


 


Avant de valider la remise, le logiciel contrôle le plafond de remise 
 éventuellement indiqué dans la fiche du journal (onglet Banque). Si celui-ci 
 est dépassé un message vous le signale mais vous pouvez passer outre.


 


Une fois la remise validée, par le menu contextuel "Remise magnétique", 
 vous avez la possibilité de générer un [fichier 
 ETEBAC](../../Fichiers/ETEBAC/FichiersBancairesETEBAC.md).


## Conséquences de la validation de la remise


En gestion commerciale, vous devez effectuer le transfert comptable 
 de vos remises d'effets depuis l’option ‘’remise de règlements et remissions 
 de paiements’’ pour qu’une écriture soit générée.


 


En comptabilité, la validation de la remise à l’encaissement ou à l’escompte 
 génère une écriture dans le journal de remise à l’encaissement ou à l’escompte 
 correspondant à la remise.


 


Ces écritures ne sont pas modifiables. Seule la suppression de la remise 
 supprimera les écritures.


 


Exemple d’écriture de remise à l’encaissement : Débit 5113 / Crédit 
 413000


Exemple d’écriture de remise à l’escompte : Débit 5114 / Crédit 413000


## Modification/ suppression d’une remise a l’encaissement ou a l’escompte


A partir de la liste des remises à l'encaissement ou à l'escompte, double-cliquez 
 sur la remise à consulter ou à modifier. La modification permet de désélectionner 
 certains effets.


### Conditions pour pourvoir supprimer la remise


La suppression d’une remise à l’encaissement/à l’escompte n’est possible 
 que si aucun avis d’encaissement/d’escompte a été effectué sur cette remise.


 


En gestion commerciale, la suppression d’une remise à l’encaissement/escompte 
 n’est possible que si le transfert comptable des remises n’a pas été réalisé.


### Comment supprimer la remise ?


A partir de la liste des remises à l’encaissement ou à l’escompte, sélectionnez 
 la remise à supprimer puis par le menu contextuel choisissez l’option 
 ‘’Supprimer’’. Un message vous demande de confirmer la suppression ou 
 non de la remise.


## Conséquences de la suppression d’une remise à l’encaissement ou a l’escompte


En gestion commerciale et comptabilité, l’effet est remis à disposition 
 pour une prochaine remise à l’encaissement ou à l’escompte.


 


En comptabilité, la suppression de la remise à l’encaissement ou à l’escompte 
 supprimera les écritures générées dans le journal.


