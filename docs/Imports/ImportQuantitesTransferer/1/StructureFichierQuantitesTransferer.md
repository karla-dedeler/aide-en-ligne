# Structure du fichier de quantités à transférér
S'il n'y a pas de numéro de lot ou un seul par ligne :


 











| Champ | Description | Type | Longueur
maximale | Présence | Exemple |
| DOC\_NUMERO | Numéro interne du document d'achat ou vente | Texte | 10 | Obligatoire |   |
| LIG\_NUMERO | Numéro de ligne | Texte | 5 | Obligatoire si code article absent |   |
| ART\_CODE | Code article | Texte | 30 | Obligatoire si numéro de ligne absent |   |
| ART\_GAMME | Codes des valeurs de gamme, séparés par un **\** | Texte | 98 | Obligatoire pour les articles gammés |   |
| LIG\_NUMLOT | Numéro de lot | Texte |   | Obligatoire pour les articles lottés |   |
| LIG\_DT\_FAB | Date de fabrication du lot | Date |   |   |   |
| LIG\_DT\_PER | Date de péremption du lot | Date |   |   |   |
| LIG\_QTE | Quantité |   |   | Obligatoire |   |
| LIG\_ZONE | Zone de stockage | Texte |   |   |   |
| PRJ\_CODE | Code affaire | Texte |   |   |   |
| LIG\_MEMO | Commentaires | Texte illimité |   |   |   |


 


S'il y a plusieurs numéros de lots par ligne :


 











| Champ | Description | Type | Longueur
maximale | Présence | Exemple |
| DOC\_NUMERO | Numéro interne du document d'achat ou vente | Texte | 10 | Obligatoire |   |
| LIG\_NUMERO | Numéro de ligne | Texte | 5 | Obligatoire si code article absent |   |
| ART\_CODE | Code article | Texte | 30 | Obligatoire si numéro de ligne absent |   |
| ART\_GAMME | Codes des valeurs de gamme, séparés par un **\** | Texte | 98 | Obligatoire pour les articles gammés |   |
| LLD\_NUMLOT | Numéros de lots, séparées par un **|** | Texte | 25 | Obligatoire pour les articles lottés |   |
| LLD\_QTE | Quantités des lots, séparées par un **|** | Texte |   |   |   |
| LLD\_DT\_FAB | Dates de fabrication des lots, séparées par un **|** | Texte |   |   |   |
| LLD\_DT\_PER | Dates de péremption des lots, séparées par un **|** | Texte |   |   |   |
| LIG\_QTE | Quantité |   |   | Obligatoire |   |
| LIG\_ZONE | Zone de stockage | Texte |   |   |   |
| PRJ\_CODE | Code affaire | Texte |   |   |   |
| LIG\_MEMO | Commentaires | Texte illimité |   |   |   |


