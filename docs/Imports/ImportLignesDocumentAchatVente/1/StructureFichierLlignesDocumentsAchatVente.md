# Structure du fichier de lignes de documents d'achat et vente
S'il n'y a pas de numéro de lot ou un seul par ligne :


 











| Champ | Description | Type | Longueur
maximale | Présence | Exemple |
| ART\_CODE | Code de l'article | Texte | 30 |   |   |
| ART\_GAMME | Codes des valeurs de gamme, séparés par un \ | Texte | 98 |   |   |
| LIG\_NUMLOT | Numéro de lot | Texte |   |   |   |
| LIG\_DT\_FAB | Date de fabrication | Date |   |   |   |
| LIG\_DT\_PER | Date de péremption | Date |   |   |   |
| LIG\_QTE | Quantité |   |   |   |   |
| LIG\_P\_BRUT | Prix unitaire brut | Montant |   |   |   |
| LIG\_REMISE | Remise | Texte |   |   |   |
| LIG\_TYPE |   | Texte |   |   |   |
| NAT\_TVATX |   |   |   |   |   |
| LIG\_LIB |   | Texte |   |   |   |
| LIG\_ZONE |   | Texte |   |   |   |
| PRJ\_CODE | Code de l'affaire | Texte | 40 |   |   |
| LIG\_P\_PRV |   | Montant |   |   |   |


 


S'il y plusieurs numéros de lots par ligne :


 











| Champ | Description | Type | Longueur
maximale | Présence | Exemple |
| ART\_CODE | Code de l'article | Texte | 30 |   |   |
| ART\_GAMME | Codes des valeurs de gamme, séparés par un \ | Texte | 98 |   |   |
| LLD\_NUMLOT | Numéros de lots, séparés par un | | Texte | 25 |   |   |
| LLD\_QTE | Quantités des lots, séparées par un | | Texte |   |   |   |
| LLD\_DT\_FAB | Dates de fabrication des lots, séparées par un | | Texte |   |   |   |
| LLD\_DT\_PER | Dates de péremption des lots, séparées par un | | Texte |   |   |   |
| LIG\_QTE | Quantité |   |   |   |   |
| LIG\_P\_BRUT |   | Montant |   |   |   |
| LIG\_REMISE |   | Texte |   |   |   |
| LIG\_TYPE |   | Texte |   |   |   |
| NAT\_TVATX |   |   |   |   |   |
| LIG\_LIB |   | Texte |   |   |   |
| LIG\_ZONE |   | Texte |   |   |   |
| PRJ\_CODE | Code de l'affaire | Texte | 40 |   |   |
| LIG\_P\_PRV |   | Montant |   |   |   |


