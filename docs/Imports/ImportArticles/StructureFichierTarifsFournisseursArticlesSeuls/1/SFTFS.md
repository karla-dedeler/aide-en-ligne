# Structure du fichier de tarifs fournisseurs seuls









| Ordre | Champ | Description | Type | Longueur
maximale | Présence |
| 1 | PCF\_CODE | Code tiers | Texte | 20 | Obligatoire |
| 2 | ART\_CODE | Code article | Texte | 30 | Obligatoire |
| 3 | ART\_GAMME | Codes valeurs de gammes séparées par un \ | Texte | 98 | Facultatif |
| 4 | ART\_PFOURN | Priorité | Texte | 1 | Facultatif |
| 5 | ART\_REFFRS | Référence fournisseur | Texte | 30 | Facultatif |
| 6 | ART\_UC\_ACH | Unité de conditionnement d'achat | Texte | 15 | Facultatif |
| 7 | ART\_CD\_ACH | Nombre d'unités de base dans l'unité de conditionnement d'achat | Nombre à virgule |   | Facultatif |
| 8 | ART\_UB\_ACH | Unité de base d'achat | Texte | 15 | Facultatif |
| 9 | ART\_R\_UAUV | UA/UV | Nombre à virgule |   | Facultatif |
| 10 | DEV\_CODE | Devise | Texte | 3 | Facultatif |
| 11 | ART\_PACHUB | Prix d'achat unitaire en unité de base | Case à cocher |   | Facultatif |
| 12 | ART\_P\_ACH | Prix d'achat unitaire | Montant |   | Facultatif |
| 13 | ART\_P\_VTE | Prix public unitaire | Montant |   | Facultatif |
| 14 | ART\_QTEMIN | Quantité minimum | Nombre à virgule |   | Facultatif |
| 15 | ART\_CODREM | Remise | Texte | 10 | Facultatif |
| 16 | ART\_DELAI | Délai de livraison | Nombre entier |   | Facultatif |


 


Attention, l'ordre des champs doit absolument être respecté.


 


 


