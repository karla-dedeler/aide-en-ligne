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







| Code         | Libellé   |
|--------------|-----------|
| GDE_CODE     | Guide code, defined in the guide header. (1) |
| GDE_LIB      | Guide label, defined in the guide header. (1) |
| JRN_TYPE     | Journal type, defined in the guide header (V, A, T, O) for Sales, Purchases, Treasury, and General Ledger. (1) |
| GDE_LIBA     | Default automatic label, defined in the guide footer. This code (not the label) is derived from reference tables/automatic label). (1) |
| GDE_SENS     | Header direction. It can be left as C or D by default. (1) |
| CPT_NUMERO   | Account number appearing in the first line of the guide. (1) |
| JRN_CODE     | Default journal code. (1) |
| GDE_CONTRE   | Counterparty management (0 if false and 1 if true). (1) |
| GDL_NUMERO   | Guide line number (maximum 4 characters). All lines in a guide must be numbered in ascending order. Example: 0001, 0002, 0003 |
| CPT_NUMERO   | Account number for each guide line. It can be a defined account or a grouping account. They must exist in the chart of accounts. |
| GDL_LIB      | Writing label. It can be entered text or an equal sign (=) starting from the second line of the guide, or left empty. |
| GDL_SENS     | Amount direction in each writing line (C or D). |
| GDL_FORMUL   | Amount or formula for the writing line. It can be empty or in the form of a formula, for example, #1 - (#1 / (1 + $TV3)) |
| GDL_QTE      | Quantity (numerical value that will be proposed by default) |
| GDL_LIBSS    | Editable label (0 if false and 1 if true) |
| GDL_FORMSS   | Editable Amount/Formula (0 if false and 1 if true) |
| GDL_QTESS    | Editable Quantity (0 if false and 1 if true) |


#### Remarque


(1) Ce champ doit être recopié sur toutes les lignes du même guide


