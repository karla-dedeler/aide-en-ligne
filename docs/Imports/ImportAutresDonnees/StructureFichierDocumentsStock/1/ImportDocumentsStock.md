# Structure du fichier de documents de stock










| Champ | Description | Type | Longueur
maximale | Valeurs possibles | Présence | Valeur par défaut |
| DOC\_STYPE | Sous-type de document de stock | Texte | 1 | E = Entrée de stock
S = Sortie de stock
T = Transfert de stock
O = Assemblage de nomenclatures
M = Ecart de stock
X = Sortie pour perte | Obligatoire |   |
| DEP\_CODE | Code dépôt | Texte | 3 |   | Facultatif | Code dépôt des préférences |
| DOC\_TDEPOT | Code dépôt de destination de transfert | Texte | 3 |   | Facultatif |   |
| DOC\_DATE | Date au format JJ/MM/AAAA | Date |   |   | Facultatif | Date du jour |
| PCF\_CODE | Code tiers | Texte | 20 |   | Facultatif |   |
| DOC\_REFPCF | Référence | Texte | 100 |   | Facultatif |   |
| PRJ\_CODE | Code affaire | Texte | 40 |   | Facultatif |   |
| DOC\_MEMO | Commentaires | Texte illimité |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés des documents de stock |   |   |   | Facultatif |   |
| ART\_CODE | Code article | Texte | 30 |   | Obligatoire |   |
| ART\_GAMME | Codes des valeurs de gammes séparés par un \ | Texte | 98 |   | Facultatif |   |
| MVT\_NUMLOT | N° de lot | Texte | 25 |   | Facultatif |   |
| MVT\_DT\_FAB | Date de fabrication du lot | Date |   |   | Facultatif |   |
| MVT\_DT\_PER | Date de péremption du lot | Date |   |   | Facultatif |   |
| MVT\_ZONE | Zone de stockage | Texte | 100 |   | Facultatif |   |
| MVT\_QTE | Quantité | Nombre à virgule |   |   | Obligatoire |   |
| MVT\_TALTER | Code du type d'écart | Texte | 15 |   | Facultatif |   |
| MVT\_TPERTE | Code du type de perte | Texte | 15 |   | Facultatif |   |
| MVT\_LIB | Libellé du mouvement | Texte | 40 |   | Facultatif |   |
| MVT\_PACH | Prix unitaire | Montant |   |   | Facultatif |   |
| MVT\_IMPAFE | Charge dans le tableau de bord de l'affaire | Case à cocher |   |   | Facultatif |   |
| MVT\_IMPAFS | Produit dans le tableau de bord de l'affaire | Case à cocher |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés des lignes de documents de stock |   |   |   | Facultatif |   |


