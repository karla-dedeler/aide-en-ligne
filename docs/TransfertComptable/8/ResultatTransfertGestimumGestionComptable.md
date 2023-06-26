# Résultat du transfert Gestimum Gestion Comptable


Suivant les paramètres que vous avez sélectionner dans votre dossier Gestimum Gestion Commerciale, vous obtiendrez des résultats différents en Gestimum Gestion Comptable. Nous allons ci dessous lister un certain nombre de cas résultant du transfert comptable.


## Libellé automatique


Le libellé automatique de l’écriture par défaut est à définir sur chaque fiche journal.


Suite au transfert des pièce, dans la colonne "LibA" de la saisie standard, vous trouverez différents résultats en fonction de la pièce que vous avez transféré.


Ce libellé automatique est renseigné en fonction du paramétrage des préférences de la société (onglet "Comptabilité").


## Libellé de l'écriture


Le libellé de l’écriture par défaut se paramètre à plusieurs niveaux :


* Les paramètres de la société (onglet "Comptabilité"),
* L'onglet "Général" de la fiche du journal.


 


Suite au transfert des pièces, dans la colonne "Libellé" de la saisie standard, vous aurez différents résultats en fonction de l’option choisie dans les paramètres de la société et dans la fiche du journal :


 








| Paramétrage des préférences de la société | Paramétrage du journal | Résultat |
|---|---|---|
| A saisir | A saisir | Rien |
| Reprendre libellé compte saisi | A saisir | Libellé compte |
| Reprendre libellé 1ère écriture | A saisir | Libellé 1ère écriture |
| Le journal est prioritaire | Reprendre l’intitulé du compte saisi | Libellé compte |
| Le journal est prioritaire | Reprendre le libellé de la 1ère écriture | Libellé 1ère écriture |


### Transfert de règlement avec écart


Le libellé de l’écriture du journal d’OD provenant d’un transfert de règlement avec écart est noté "Écart de règlement sur remise RB XXX".


## Gestion des échéances


Pour récupérer la gestion des échéances lors du transfert comptable, vous devez au préalable :


* paramétrer la société (onglet "Comptabilité"),
* sélectionner la gestion des échéances sur le journal et le compte.


 


Suite au transfert des pièces, dans la colonne "échéances" de la saisie standard, vous aurez :


* soit une date,
* soit "Multiples" qui signifie qu’il y a plusieurs échéances pour cette pièce. Par un double clic dans la colonne, vous obtiendrez l’échéancier.


L’échéancier de l’écriture est disponible par le menu contextuel de la saisie standard + Échéancier ou le bouton "Échéancier".


## Gestion des quantités


Pour récupérer la gestion des quantités lors du transfert comptable, vous devez au préalable :


* paramétrer la société (onglet "Comptabilité"),
* sélectionner la gestion des quantités sur le compte (Possible /Obligatoire).


 


Suite au transfert des pièces, dans la colonne "Qté" de la saisie standard, vous aurez un nombre.


En fonction de la pièce que vous transférez, ce nombre pourra être positif ou négatif, si vous transférez une pièce avec des quantités négatives, le nombre de la colonne quantité sera négatif et inversement pour une pièce positive.


## Gestion de l'analytique


Pour récupérer la gestion de l’analytique lors du transfert comptable, vous devez au préalable :


* paramétrer la société (onglet  "Comptabilité"),
* créer le plan analytique dans les tables en comptabilité,
* créer les sections analytiques en comptabilité (menu SOCIETE/Comptabilité),
* sélectionner la gestion de l'analytique sur le compte (Possible/Obligatoire),
* affecter les sections analytiques par défaut au compte.


 


Suite au transfert des pièces, dans la colonne "A", vous aurez "une croix" signalisant qu’une ou des sections analytiques sont affectées à cette ligne d’écriture. Par le bouton "Analyt…" ou le menu contextuel + Analytique de la saisie standard, vous pourrez visualiser cette affectation et éventuellement la modifiée.


Si vous possédez 2 plans analytiques (par exemple, un pour la gestion (renseignement de la section du plan 1 sur la nature comptable) et un pour la comptabilité (renseignement de la section du plan 2 dans le compte comptable)], suite au transfert comptable, les 2 plans seront renseignés.


## Gestion de la TVA sur encaissement


Pour récupérer la gestion de la TVA sur encaissement lors du transfert comptable des remises en banque, vous devez au préalable paramétrer :


* la société (onglet "Comptabilité"),
* les comptes de TVA sur encaissement.


 


Lors de la demande du transfert comptable, vous avez la possibilité de sélectionner ou non l’option "TVA sur encaissement automatique" .


Suite au transfert des pièces vous aurez la possibilité de voir la TVA sur encaissement par le menu contextuel de la saisie standard.


## Gestion des écarts


Pour récupérer la gestion des écarts lors du transfert comptable des remises en banque, vous devez sélectionner au préalable  dans les paramètres de la société (onglet "Comptes") :


* les comptes et les montants d’écart accordés au maximum,
* le journal des opérations diverses (OD) dans lequel les écritures seront transférées.


 


Suite au transfert comptable des opérations de trésorerie, vos écritures d’écart (règlement, conversion, change et escompte) seront consultables dans le journal d’opérations diverses paramétré dans les préférences de la société.


