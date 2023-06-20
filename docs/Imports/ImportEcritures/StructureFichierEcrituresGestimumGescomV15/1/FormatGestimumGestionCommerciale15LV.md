# Format Gestimum Gestion Commerciale 1.5 à largeur variable
## Type de fichier


Fichier texte à largeur variable. Séparateur de champs : Virgule.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier contient uniquement des lignes d'écritures.


## Exemple


"VTE",14/01/2003,"411020002","FA 0000066","BUDUM SA",14/01/2003,"",2001.69,0.00


## Structure des lignes d'écritures












| Ordre | Champ | Type | Longueur
maximale | Format | Présence | Exemple |
| 1 | Code journal | Texte | 10 | Entre guillemets | Obligatoire | "VTE" |
| 2 | Date de l'écriture | Date |   | Format : JJMMAA ou JJMMAAAA | Obligatoire | 14/01/2003 |
| 3 | Numéro de compte | Texte | 10 | Entre guillemets | Obligatoire | "411020002" |
| 4 | Numéro de pièce | Texte | 8 | Entre guillemets | Obligatoire \* | "FA 0000066" |
| 5 | Libellé de l'écriture | Texte | 35 | Entre guillemets | Obligatoire \*\* | "BUDUM SA" |
| 6 | Date d'échéance | Date |   | Format : JJMMAA ou JJMMAAAA |   | 14/01/2003 |
| 7 | Nature de TVA | Texte | 1 |   |   |   |
| 8 | Code lettrage | Texte | 2 |   |   |   |
| 9 | Montant au débit | Montant |   | Séparateur décimal : point |   | 2001.69 |
| 10 | Montant au crédit | Montant |   | Séparateur décimal : point |   |   |
| 11 | Mode de règlement de la 1è échéance | Texte | 8 |   |   |   |


 


\* : Le numéro de pièce est obligatoire si l'option "N° de pièce obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


\*\* : Le libellé est obligatoire si l'option "Libellé obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


