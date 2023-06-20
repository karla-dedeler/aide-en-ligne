# Format EBP versions 200X, 5 et 3 à largeur variable


## Type de fichier


Fichier texte à largeur variable. Séparateur de champs : Virgule.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier contient des lignes d'écritures. Chaque ligne d'écriture peut être suivie d'une ou plusieurs lignes d'échéances, et d'une ou plusieurs lignes d'analytique.


 


Chaque ligne d'échéance doit commencer par le lettre "E".  Chaque ligne d'analytique doit commencer par le caractère ">".


## Dates


La seule différence entre les versions 3 et les versions 5 et 2000X est le format des dates.


* La date est de la forme JJMMAA dans les fichiers des versions 3
* La date est au format JJMMAAAA dans les fichiers des versions 5 et 200X.


## Structure des lignes d'écritures











| Ordre | Champ | Type | Longueur
maximale | Format | Présence |
| 1 | Numéro de ligne | Texte |   |   | Facultatif |
| 2 | Date d'écriture | Date |   | Format : JJMMAA ou JJMMAAAA | Obligatoire |
| 3 | Code journal | Texte | 4 |   | Obligatoire |
| 4 | Numéro de compte | Texte | 15 |   | Obligatoire |
| 5 | Code libellé automatique | Texte | 2 |   | Facultatif |
| 6 | Libellé | Texte | 40 | Entre guillemets | Obligatoire \* |
| 7 | Numéro de pièce | Texte | 10 | Entre guillemets | Obligatoire \*\* |
| 8 | Montant | Montant |   | Séparateur décimal : point | Obligatoire |
| 9 | Sens | Texte | 1 | Valeurs possibles :
D : Débit
C : Crédit | Facultatif |
| 10 | Date d'échéance | Date |   | Format : JJMMAA ou JJMMAAAA | Facultatif |
| 11 | Nature de TVA | Texte | 1 | Valeurs possibles :
E : Encaissement
D : Débit | Facultatif |
| 12 | Code mode de règlement  de la 1è échéance | Texte | 8 |   | Facultatif |


 


\* : Le libellé est obligatoire si l'option "Libellé obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


\*\* : Le numéro de pièce est obligatoire si l'option "N° de pièce obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


 


Exemple :


1,010103,VE,411ART,FA, "Ventes d’ordinateur ", "123 ",75.00,D,010303


## Structure des échéances












| Ordre | Champ | Type | Longueur
maximale | Format | Présence | Exemple |
| 1 | Type d'enregistrement : E | Texte | 1 |   | Obligatoire | E |
| 2 | Date d'échéance | Date |   | Format : JJMMAA ou JJMMAAAA
ou JJ/MM/AA ou JJ/MM/AAAA | Obligatoire | 10/03/2017 |
| 3 | Montant de l'échéance | Montant |   | Séparateur décimal : point | Obligatoire | 120.50 |
| 4 | Code mode de règlement | Texte | 8 |   | Facultatif | CHQ |


 


La date d'échéance en position 12 de la ligne d'écriture ne doit pas être renseignée. Si c'est le cas, les lignes d'échéances suivantes seront ignorées.


 


Si le montant total des échéances n'est pas égal au montant de la ligne d'écriture générale, l'écriture sera rejetée.


 


Exemple :


1,010103,VE,411ART,, "Ventes d’ordinateur ", "123 ",75.00,D,010303,D,EUR


E010303,75.00,T060


## Structure des ventilations analytiques












| Ordre | Champ | Type | Longueur
maximale | Format | Présence | Exemple |
| 1 | Type d'enregistrement : > | Texte | 1 |   | Obligatoire | > |
| 2 | Code section analytique | Texte | 15 |   | Obligatoire | S1 |
| 3 | Pourcentage du montant de la ligne d’écriture | Nombre à virgule |   | Séparateur décimal : point | Facultatif | 100.00 |
| 4 | Montant de le ventilation analytique | Montant |   | Séparateur décimal : point | Facultatif | 75.00 |


 


Si le montant total des ventilations analytiques n'est pas égal au montant de la ligne d'écriture générale, l'écriture sera rejetée.


 


Exemple :


1,01102013,VTE,707101,,"VIDAL","FAC12-0000168",23920.00,D,01102013,D,,EUR


>POSTE1,100.00,75.00


## Structure des comptes


L'import d'écritures comptables est capable de créer les comptes avant de créer les écritures, à partir d'un fichier texte nommé "Comptes.txt" placé dans le même dossier.


 











| Ordre | Champ | Type | Longueur
maximale | Format | Présence |
| 1 | Numéro de compte | Texte | 15 |   | Obligatoire |
| 2 | Intitulé du compte | Texte | 60 | Format : JJMMAA ou JJMMAAAA | Obligatoire |
| 3 | Raison sociale | Texte | 30 |   | Facultatif |
| 4 | Adresse | Texte | 100 |   | Facultatif |
| 5 | Code postal | Texte | 5 |   | Facultatif |
| 6 | Ville | Texte | 30 |   | Facultatif |
| 7 | Pays | Texte | 35 |   | Facultatif |
| 8 | Interlocuteur | Texte | 35 |   | Facultatif |
| 9 | Téléphone | Texte | 20 |   | Facultatif |
| 10 | Fax | Texte | 20 |   | Facultatif |


 


Exemple :


411DUPOND,DUPOND,,21 rue du bois,78120,Rambouillet,France,,0135698475,0135698475


 


En l'absence de ce fichier des comptes, le libellé des comptes créés sera "Compte créé pendant transfert".


