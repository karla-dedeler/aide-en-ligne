# Format Gestimum Gestion Comptable 1.5 à largeur fixe

## Type de fichier


Fichier texte à largeur fixe


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier contient uniquement des lignes d'écritures.


## Exemple de fichier


1 VT2003092020020930FA000013 707100 Vente client Durand 45.73 C


## Structure des lignes d'écritures












| Position | Champ | Type | Longueur | Format | Présence | Exemple |
| 1 | Code journal | Texte | 3 |   | Obligatoire |   |
| 4 | Date d'écriture | Date | 8 | Format : JJMMAA ou JJMMAAAA | Obligatoire |   |
| 12 | Numéro de pièce | Texte | 8 |   | Obligatoire \* |   |
| 20 | Numéro de compte | Texte | 10 | Entre guillemets | Obligatoire |   |
| 30 | Libellé | Texte | 35 | Entre guillemets | Obligatoire \*\* |   |
| 65 | Nature de TVA | Texte | 1 |   | Facultatif |   |
| 66 | Date d'échéance | Date | 8 | Format : JJMMAA ou JJMMAAAA | Facultatif |   |
| 74 | Code lettrage | Texte | 2 |   | Facultatif |   |
| 76 | Montant au débit | Montant | 15 | Séparateur décimal : point | Obligatoire |   |
| 91 | Montant au crédit | Montant | 15 | Séparateur de décimal : point | Obligatoire |   |
| 106 | Code mode de règlement | Texte | 8 |   | Facultatif |   |


 


\* : Le numéro de pièce est obligatoire si l'option "N° de pièce obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


\*\* : Le libellé est obligatoire si l'option "Libellé obligatoire dans les écritures comptables" est cochée dans les préférences de comptabilité


