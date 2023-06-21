# Structure du fichier de tarifs seuls










| Ordre | Champ | Description | Type | Longueur
maximale | Présence |
| 1 | ART\_CODE | Code article | Texte | 30 | Obligatoire |
| 2 | DEV\_CODE | Code devise | Texte | 3 | Facultatif |
| 3 | ART\_GAMME | Codes valeurs de gammes séparées par un \ | Texte | 98 | Facultatif |
| 4 | ART\_P\_ACH | Prix d'achat unitaire | Montant |   | Facultatif |
| 5 | ART\_P\_COEF | Coefficient | Nombre à virgule |   | Facultatif |
| 6 | ART\_P\_VTE | Prix public unitaire | Montant |   | Facultatif |
| 7 | ART\_DT\_NEW | Date de mise à jour | Date |   | Facultatif |
| 8 | ART\_N\_ACH | Nouveau prix d'achat unitaire | Montant |   | Facultatif |
| 9 | ART\_N\_COEF | Nouveau coefficient | Nombre à virgule |   | Facultatif |
| 10 | ART\_N\_VTE | Nouveau prix de vente unitaire | Montant |   | Facultatif |


 


Attention, l'ordre des champs doit absolument être respecté.


