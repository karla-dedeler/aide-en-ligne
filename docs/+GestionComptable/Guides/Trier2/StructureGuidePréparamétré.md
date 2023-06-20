# Structure du guide pré-paramétré






Gestimum propose un ensemble de modèles guides par défaut qui seront initialisés dans le menu Données/Guides lors de la création de la société.


 


Néanmoins, vous pouvez créer vous même vos propres guides en modifiant le fichier guides.txt disponible dans le répertoire \Bases\ qui sera utilisé pour la création de vos prochaines sociétés.


 


Ce fichier disponible lors de l’installation du logiciel peut être pré-paramétré. Quelques exemples sont déjà disponibles par défaut.


## PARAMÉTRAGE


Pour pouvoir initialiser les Guides du menu Données lors de la création d'une nouvelle société, il faut :


* Lors de la création de la société cocher les données par défaut : Tables de référence, plan comptable, journaux et guides,
* Le paramétrage effectué dans le fichier guides.txt doit contenir des journaux, des comptes et de libellés automatiques des tables de références existants respectivement dans chaque fichier.


 


La structure du fichier guides.txt est la suivante :


Nombre=9


// GDE\_CODE; GDE\_LIB; JRN\_TYPE; GDE\_LIBA; GDE\_SENS; CPT\_NUMERO; JRN\_CODE; GDE\_CONTRE; GDL\_NUMERO; CPT\_NUMERO; GDL\_LIB; GDL\_SENS; GDL\_FORMUL; GDL\_QTE; GDL\_LIBSS; GDL\_FORMSS; GDL\_QTESS


A001;Achats de marchandises en France;A;FAC;C;401; ACH;0;001;401;;C;;0;1;1;0


A001;Achats de marchandises en France;A;FAC;C;401; ACH;0;002;445661;=;D;#1-(#1/(1+$TV3));0;0;0;0


A001;Achats de marchandises en France;A;FAC;C;401;ACH;0;003;607201;=;D;#1-#2;0;0;0;0


V001;Ventes de marchandises en France;v;FAC;C;411;VTE;0;001;411;;D;;0;1;1;0


V001;Ventes de marchandises en France;V;FAC;C;411;VTE;0;002;445711;=;C;#1-(#1/(1+$TV3));0;0;0;0


V001;Ventes de marchandises en France;V;FAC;C;411;VTE;0;003;707101;=;C;#1-#2;,0;0;0;0


A011;Crédit-bail;A;FAC;C;401;ACH;0;001;401;;C;;0;1;1;0


A011;Crédit-bail;A;FAC;C;401;ACH;0;002;445661;=;D;#1-(#1/(1+$TV3));0;0;0;0


A011;Crédit-bail;A;FAC;C;401;ACH;0;003;612;=;D;#1-#2;0;0;0;0


// Fin du fichier


 


La première ligne contient le nombre total de toutes les lignes des guides : "Nombre=9".


 


La deuxième ligne contient les noms des champs du fichier précédés par un double anti-slash :


"//GDE\_CODE;GDE\_LIB;JRN\_TYPE;GDE\_LIBA;GDE\_SENS;CPT\_NUMERO;JRN\_CODE;GDE\_CONTRE;GDL\_NUMERO;CPT\_NUMERO;GDL\_LIB;GDL\_SENS;GDL\_FORMUL;GDL\_QTE;GDL\_LIBSS;GDL\_FORMSS;GDL\_QTESS ".


 


Les autres lignes doivent respecter le format défini dans la deuxième ligne, les champs ont un séparateur point virgule (;).


 


La dernière ligne contient un double anti-slash suivi du texte : "// Fin du fichier "


## Détail de champs







| Code | Libellé |
| GDE\_CODE | Code du guide, défini dans l'entête du guide. (1) |
| GDE\_LIB | Libellé du guide, défini dans l'entête du guide. (1) |
| JRN\_TYPE | Type de journal, défini dans l'entête du guide (V, A, T, O) pour les Ventes, Achats, Trésorerie et OD. (1) |
| GDE\_LIBA | Libellé automatique par défaut, défini dans le pied du guide. Ce code (et non le libellé) est issu des tables de références/libellé automatique). (1) |
| GDE\_SENS | Sens dans l'entête. Il peut être laissé à C ou D par défaut. (1) |
| CPT\_NUMERO | Compte comptable figurant dans la première ligne du guide. (1) |
| JRN\_CODE | Journal par défaut. Il s'agit du code. (1) |
| GDE\_CONTRE | Gestion de la contrepartie (0 si faux et 1 si vrai). (1) |
| GDL\_NUMERO | N° de ligne du guide (Maxi 4 caractères). Toutes les lignes d'un guide doivent être numérotées dans un ordre ascendant. Exemple : 0001, 0002, 0003 |
| CPT\_NUMERO | Compte comptable pour chaque ligne du guide. Il s'agit d'un compte comptable défini ou d'un compte de regroupement. Ils doivent exister dans le plan comptable. |
| GDL\_LIB | Libellé de l'écriture. Il s'agit d'un texte saisi, d'un signe égal (=) à partir de la deuxième ligne du guide, ou vide. |
| GDL\_SENS | Sens du montant dans chaque ligne d'écriture (C ou D). |
| GDL\_FORMUL | Montant ou Formule de la ligne d'écriture. Il peut être vide, ou en forme de formule, par exemple #1 - (#1 / (1 + $TV3)) |
| GDL\_QTE | Qte (valeur numérique qui sera proposée par défaut) |
| GDL\_LIBSS | Libellé saisissable (0 si faux et 1 si vrai) |
| GDL\_FORMSS | Montant / Formule saisissable (0 si faux et 1 si vrai) |
| GDL\_QTESS | Qté saisissable (0 si faux et 1 si vrai) |


#### Remarque


(1) Ce champ doit être recopié sur toutes les lignes du même guide


