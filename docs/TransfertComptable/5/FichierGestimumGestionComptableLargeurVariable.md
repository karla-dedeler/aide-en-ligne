# Fichier Gestimum Gestion Comptable à largeur variable
## Type de fichier


Fichier texte à largeur variable.


 


Séparateur de champs : Virgule.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures. Chaque ligne d'écriture 
 peut être suivie d'une ou plusieurs lignes d'échéances, et d'une ou plusieurs 
 lignes d'analytique.


 


Chaque ligne d'échéance commence par le lettre "E".  Chaque 
 ligne d'analytique commence par le caractère ">".


## Exemple de fichier


1,09/04/2015,VTE,411C30,F,"DUBOIS","FAC15-00021",EUR,1394.64,D,,09/04/2015,,


2,09/04/2015,VTE,4457220,F,"DUBOIS","FAC15-00021",EUR,232.44,C,,,


3,09/04/2015,VTE,707100,F,"DUBOIS","FAC15-00021",EUR,1162.20,C,,,


>S,A1S3,50,00,0.00


>S,A2S3,50,00,1162.20


 


Ce fichier contient une écriture de 3 lignes. La 3è ligne d'écriture 
 est suivie de 2 lignes d'analytique.


## Structure des lignes d'écritures










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Numéro de ligne | Numéro |   |   | 1 |
| 2 | Date d'écriture | Date |   | Format :  JJ/MM/AAAA | 10/03/2017 |
| 3 | Code journal | Texte | 10 |   | VTE |
| 4 | Numéro de compte | Texte | 25 |   | 411160001 |
| 5 | Code libellé automatique | Texte | 15 |   | FAC |
| 6 | Libellé | Texte | 60 | Entre guillemets | Facture de prestation FAC16-100004 |
| 7 | Numéro de pièce | Texte | 15 | Entre guillemets | 25115 |
| 8 | Code devise | Texte | 3 |   | EUR |
| 9 | Montant | Montant |   | Séparateur décimal : point | 120 |
| 10 | Sens | Texte | 1 | Valeurs possibles : 
D : Débit 
C : Crédit | D |
| 11 |   |   |   |   |   |
| 12 | Date d'échéance | Date |   | Format : JJ/MM/AAAA | 10/03/2017 |
| 13 | Quantité | Nombre à virgule |   |   |   |
| 14 | Code mode de règlement | Texte | 8 |   | CHQ |


## Structure des échéances










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Type 
 d'enregistrement : E | Texte | 1 |   |   |
| 2 | Date 
 d'échéance | Date |   | Format 
 : JJMMAA ou JJMMAAAA 
ou 
 JJ/MM/AA ou JJ/MM/AAAA | 10/03/2017 |
| 3 | Code mode de règlement | Texte | 8 |   | CHQ |
| 4 | Pourcentage du montant de la ligne d'écriture | Nombre à virgule |   | Séparateur décimal : point | 100 |
| 5 | Montant de l'échéance | Montant |   | Séparateur décimal : point | 120 |


## Structure des ventilations analytiques










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Type d'enregistrement : > | Texte | 1 |   |   |
| 2 | Code plan analytique | Texte | 15 |   | P1 |
| 3 | Code section analytique | Texte | 15 |   | S1 |
| 4 | Pourcentage du montant de la ligne d’écriture | Nombre à virgule |   | Séparateur décimal : point | 80 |
| 5 | Montant de la ventilation analytique | Montant |   | Séparateur décimal : point | 100 |
| 6 | Pourcentage de la quantité de la ligne d'écriture | Nombre à virgule |   | Séparateur décimal : point | 80 |


