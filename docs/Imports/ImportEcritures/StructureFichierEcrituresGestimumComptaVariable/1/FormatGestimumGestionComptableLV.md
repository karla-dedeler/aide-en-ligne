# Format Gestimum Gestion Comptable à largeur variable


## Type de fichier


Fichier texte à largeur variable. Séparateur de champs : Virgule.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier contient des lignes d'écritures. Chaque ligne d'écriture peut être suivie d'une ou plusieurs lignes d'échéances, et d'une ou plusieurs lignes d'analytique.


 


Chaque ligne d'échéance doit commencer par le lettre "E". Chaque ligne d'analytique doit commencer par le caractère ">".


## Exemple de fichier

````
1,31/12/2019,VTE,411070001,FA12,"Vente d'ordinateurs FAC19-000482",42,EUR,120.00,C,,,0,,"TEST","test variable"
E31/12/2019,CB,0,120.00,125
2,31/12/2019,VTE,445710,FA12,"Vente d'ordinateur FAC19-000482",42,EUR,20.00,D,,,0,,"TEST","test variable"
3,31/12/2019,VTE,707100,FA12,"Vente d'ordinateurs FAC19-000482",42,EUR,100.00,D,,,0,,"TEST","test variable"
>P1,S1,100,100.00,100,1.0
````


Ce fichier contient une écriture de 3 lignes :


- La 1è ligne d'écriture est suivie d'une ligne d'échéance.


- La 2è ligne d'écriture  est seule.


- La 3è ligne est suivi d'une ligne d'analytique.


## Structure des lignes d'écritures












| Ordre | Champ | Type | Longueur maximale | Format | Présence | Exemple |
|---|---|---|---|---|---|---|
| 1 | Numéro de ligne | Numéro |   |   | Facultatif | 1 |
| 2 | Date d'écriture | Date |   | Format :  JJMMAA ou JJMMAAAA ou JJ/MM/AA ou JJ/MM/AAAA | Obligatoire | 10/03/2017 |
| 3 | Code journal | Texte | 10 |   | Obligatoire | VTE |
| 4 | Numéro de compte | Texte | 25 |   | Obligatoire | 411160001 |
| 5 | Code libellé automatique | Texte | 15 |   | Facultatif | FAC |
| 6 | Libellé | Texte | 60 | Entre guillemets | Obligatoire \* | Facture de prestation FAC16-100004 |
| 7 | Numéro de pièce | Texte | 15 | Entre guillemets | Obligatoire \*\* | 25115 |
| 8 | Code devise | Texte | 3 |   | Facultatif | EUR |
| 9 | Montant | Montant |   | Séparateur décimal : point | Obligatoire | 120 |
| 10 | Sens | Texte | 1 | Valeurs possibles : <br>D : Débit <br>C : Crédit | Facultatif | D |
| 11 | Code lettrage | Texte | 3 |   | Facultatif | AAB |
| 12 | Date d'échéance | Date |   | Format :  JJMMAA ou JJMMAAAAou JJ/MM/AA ou JJ/MM/AAAA | Facultatif | 10/03/2017 |
| 13 | Quantité | Nombre à virgule |   |   | Facultatif |   |
| 14 | Code mode de règlement | Texte | 8 |   | Facultatif | CHQ |
| 15 | Numéro de pièce complémentaire | Texte | 15 | Entre guillemets | Facultatif |   |
| 16 | Référence | Texte | 60 | Entre guillemets | Facultatif |   |
| 17 | Date de pièce complémentaire | Date |   | Format :  JJMMAA ou JJMMAAAA ou JJ/MM/AA ou JJ/MM/AAAA | Facultatif |   |


 


\* : Le libellé est obligatoire si l'option "Libellé obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


\*\* : Le numéro de pièce est obligatoire si l'option "N° de pièce obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


## Structure des échéances












| Ordre | Champ | Type | Longueur maximale | Format | Présence | Exemple |
|---|---|---|---|---|---|---|
| 1 | Type d'enregistrement : E | Texte | 1 |   | Obligatoire |   |
| 2 | Date | Date |   | Format : JJMMAA ou JJMMAAAA ou JJ/MM/AA ou JJ/MM/AAAA | Obligatoire | 10/03/2017 |
| 3 | Code mode de règlement | Texte | 8 |   | Facultatif | CHQ |
| 4 | Pourcentage | Nombre à virgule |   | Séparateur décimal : point | Facultatif | 100 |
| 5 | Montant | Montant |   | Séparateur décimal : point | Facultatif | 120 |
| 6 | Numéro d'origine externe | Texte | 10 |   | Facultatif |   |


 


La date d'échéance en position 12 de la ligne d'écriture ne doit pas être renseignée. Si c'est le cas, les lignes d'échéances suivantes seront ignorées.


 


Si le montant total des échéances n'est pas égal au montant de la ligne d'écriture générale, l'écriture sera rejetée.


## Structure des ventilations analytiques












| Ordre | Champ | Type | Longueur maximale | Format | Présence | Exemple |
|---|---|---|---|---|---|---|
| 1 | Type d'enregistrement : > | Texte | 1 |   | Obligatoire |   |
| 2 | Code plan analytique | Texte | 15 |   | Obligatoire | P1 |
| 3 | Code section analytique | Texte | 15 |   | Obligatoire | S1 |
| 4 | Pourcentage du montant de la ligne d’écriture | Nombre à virgule |   | Séparateur décimal : point | Facultatif | 80 |
| 5 | Montant | Montant |   | Séparateur décimal : point | Facultatif | 100 |
| 6 | Pourcentage de la quantité de la ligne d'écriture | Nombre à virgule |   | Séparateur décimal : point | Facultatif | 80 |
| 7 | Quantité | Nombre à virgule |   | Séparateur décimal : point | Facultatif | 5 |


 


Si le montant total des ventilations analytiques n'est pas égal au montant de la ligne d'écriture générale, l'écriture sera rejetée.


