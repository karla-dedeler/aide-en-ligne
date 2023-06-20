# Format Gestimum Gestion Comptable avec longueurs fixes

Le format spécifique de ce fichier est créé automatiquement par le transfert comptable de la gestion commerciale Gestimum.


 


La structure fixe du fichier est la suivante :


1 VT2003092020020930FA000013 707100 Vente client durand 45.73 C


 


Ci-après la description de chaque champ, dans l'ordre de la ligne :


* N ° de mouvement : il s’agit d’un numéro de ligne qui peut être aléatoire ou chronologique,
* Code journal : il est alphanumérique sur 10 caractères maximum,
* Date d’écriture : elle est de la forme AAAAMMJJ,
* Date d’échéance : elle est de la forme AAAAMMJJ,
* Numéro de pièce : il est alphanumérique sur 15 caractères maximum,
* Numéro de Compte : il est alphanumérique sur maximum 25 caractères,
* Libellé de l’écriture : il est alphanumérique sur maximum 60 caractères,,
* Montant : Numérique, avec le point comme séparateur de décimale maximum 20 caractères,
* Sens : D ou C pour Débit ou Crédit,
* N° de pointage : non repris,
* Libellé du compte : libellé du compte paramétré dans le plan comptable 60 caractères maximum. Si le compte n’existe pas le programme le crée avec l’intitulé "Compte à créer",
* Mode de règlement : Alphanumérique sur 8 caractères, il s'agit du mode de règlement de la première échéance du document,
* Code de la section analytiques : il est alphanumérique sur 15 caractères maximum,
* Libellé de la section analytiques : libellé de la section analytiques 60 caractères maximum.


