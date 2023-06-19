# Fichier EBP 3 à largeur variable
## Type de fichier


Fichier texte à largeur variable.


 


Séparateur de champs : Virgule.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures. Chaque ligne d'écriture 
 peut être suivie d'une ou plusieurs lignes d'échéances, et d'une ou plusieurs 
 lignes d'analytique.


 


Chaque ligne d'échéance commence par le caractère "E". Chaque 
 ligne d'analytique commence par le caractère ">".


## Exemple de fichier


1,090415,VTE,411C30,FA,"DUBOIS","FAC15-00021",1394.64,D,090415,D,,EUR


2,090415,VTE,4457220,FA,"DUBOIS","FAC15-00021",232.44,C,,D,,EUR


3,090415,VTE,707100,FA,"DUBOIS","FAC15-00021",1162.20,C,,D,,EUR


>A1S3,50,00,0.00


>A2S3,50,00,1162.20


## Structure des lignes d'écritures










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Numéro de ligne | Numéro |   |   |   |
| 2 | Date d'écriture | Date |   | Format : JJMMAA |   |
| 3 | Code journal | Texte | 4 |   |   |
| 4 | Numéro de compte | Texte | 15 |   |   |
| 5 | Libellé automatique | Texte | 2 | Valeurs possibles : FA=Facture, AV=Avoir |   |
| 6 | Libellé manuel | Texte | 40 | Entre guillemets |   |
| 7 | Numéro de pièce | Texte | 10 | Entre guillemets |   |
| 8 | Montant | Montant |   | Séparateur décimal : Point |   |
| 9 | Sens | Texte | 1 | Valeurs possibles : D=Débit, C=Crédit |   |
| 10 | Date d'échéance | Date |   | Format : JJMMAA |   |
| 11 | Nature de TVA | Texte | 1 | Valeurs possibles : E=Encaissement, D=Débit |   |
| 12 | Code mode de règlement de la 1è échéance du document | Texte | 8 |   |   |


## Structure des échéances










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Type d'enregistrement : E | Texte | 1 |   | E |
| 2 | Date | Date |   | Format : JJMMAA | 100317 |
| 3 | Montant | Montant |   | Séparateur décimal : Point | 120.50 |
| 4 | Code mode de règlement | Texte | 8 |   | CHQ |


## Structure des ventilations analytiques










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Type d'enregistrement : > | Texte | 1 |   | > |
| 2 | Code section analytique | Texte | 15 |   | S1 |
| 3 | Pourcentage du montant de la ligne d’écriture | Nombre à virgule |   | Séparateur décimal : Point | 100.00 |
| 4 | Montant | Montant |   | Séparateur décimal : Point | 75.00 |


## Différences


Il y a 2 différences entre le fichier "EBP 3 à largeur variable" 
 et le fichier "EBP 200X et 5 à largeur variable" :


- le format des dates est JJMMAA dans 
 le premier, et JJMMAAAA dans le second


- un libellé automatique FA ou AV est 
 présent dans la ligne d'écriture du premier, mais pas dans la ligne d'écriture 
 du second


