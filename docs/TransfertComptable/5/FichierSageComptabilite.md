# Fichier Sage Comptabilité à largeur variable
## Type de fichier


Fichier texte à largeur variable.


 


Séparateur de champs : Tabulation.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures uniquement.


## Exemple de fichier


VTE 09/04/15 411000 C30 DUBOIS 09/04/15 1394,64 0,00 
 FAC15-00021


VTE 09/04/15 4457220 DUBOIS 09/04/15 0,00 232,44 
 FAC15-00021


VTE 09/04/15 707100 DUBOIS 09/04/15 0,00 1162,20 
 FAC15-00021


## Structure des lignes d'écritures










| Ordre | Champ | Type | Longueur
maximale |   | Exemple |
| 1 | Code journal | Texte | 10 |   | VTE |
| 2 | Date de pièce | Date | 6 | Format : JJ/MM/AA | 09/04/15 |
| 3 | Numéro de compte | Texte | 13 |   | 411000 |
| 4 | Numéro de compte auxiliaire, sans la racine | Texte | 10 |   | C30 |
| 5 | Référence du document | Texte | 17 |   |   |
| 6 | Libellé d'écriture | Texte | 35 |   | DUBOIS |
| 7 | Libellé du mode de règlement | Texte | 35 |   |   |
| 8 | Date d'échéance | Date | 6 | Format : JJ/MM/AA | 09/04/15 |
| 9 | Montant au débit | Montant |   | Séparateur décimal : Virgule | 1394,64 |
| 10 | Montant au crédit | Montant |   | Séparateur décimal : Virgule | 232,44 |
| 11 | Numéro de pièce | Texte | 17 |   | FAC15-00021 |


