# Fichier Gestimum Gestion Comptable à largeur fixe
## Type de fichier


Fichier texte à largeur fixe.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures uniquement.


## Exemple de fichier


```
1VTE       2015040920150409FAC15-00021    411C30                   DUBOIS                                                            1394.64D                  DUBOIS                                                      

1VTE       20150409        FAC15-00021    4457220                  DUBOIS                                                             232.44C                  TVA 20 % collectée sur les débits                           

1VTE       20150409        FAC15-00021    707100                   DUBOIS                                                            1162.20C                  Marchandise (ou groupe) A - France 
````



## Structure des lignes d'écritures









| Position | Champ | Type | Longueur |   |
|---|---|---|---|---|
| 1 | Numéro de ligne | Numéro | 5 |   |
| 6 | Code journal | Texte | 10 |   |
| 16 | Date d'écriture | Date | 8 | Format : AAAAMMJJ |
| 24 | Date d'échéance | Date | 8 | Format : AAAAMMJJ |
| 32 | Numéro de pièce | Texte | 15 |   |
| 47 | Numéro de compte | Texte | 25 |   |
| 72 | Libellé d'écriture | Texte | 60 |   |
| 132 | Montant d'écriture | Montant | 13 |   |
| 145 | Sens d'écriture | Texte | 1 |   |
| 146 |   |   | 12 |   |
| 158 |   |   | 6 |   |
| 164 | Libellé du compte | Texte | 60 |   |
| 224 | Mode de règlement | Texte | 8 |   |


