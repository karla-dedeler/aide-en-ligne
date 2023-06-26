# Structure du fichier de tarifs fournisseurs seuls









| Ordre | Champ       | Description                                                | Type            | Longueur maximale | Présence    |
|-------|-------------|------------------------------------------------------------|-----------------|-------------------|-------------|
| 1     | PCF_CODE    | Code tiers                                                 | Texte           | 20                | Obligatoire |
| 2     | ART_CODE    | Code article                                               | Texte           | 30                | Obligatoire |
| 3     | ART_GAMME   | Codes valeurs de gammes séparées par un \                  | Texte           | 98                | Facultatif  |
| 4     | ART_PFOURN  | Priorité                                                   | Texte           | 1                 | Facultatif  |
| 5     | ART_REFFRS  | Référence fournisseur                                      | Texte           | 30                | Facultatif  |
| 6     | ART_UC_ACH  | Unité de conditionnement d'achat                            | Texte           | 15                | Facultatif  |
| 7     | ART_CD_ACH  | Nombre d'unités de base dans l'unité de conditionnement d'achat | Nombre à virgule |                   | Facultatif  |
| 8     | ART_UB_ACH  | Unité de base d'achat                                      | Texte           | 15                | Facultatif  |
| 9     | ART_R_UAUV  | UA/UV                                                      | Nombre à virgule |                   | Facultatif  |
| 10    | DEV_CODE    | Devise                                                     | Texte           | 3                 | Facultatif  |
| 11    | ART_PACHUB  | Prix d'achat unitaire en unité de base                      | Case à cocher   |                   | Facultatif  |
| 12    | ART_P_ACH   | Prix d'achat unitaire                                      | Montant         |                   | Facultatif  |
| 13    | ART_P_VTE   | Prix public unitaire                                       | Montant         |                   | Facultatif  |
| 14    | ART_QTEMIN  | Quantité minimum                                           | Nombre à virgule |                   | Facultatif  |
| 15    | ART_CODREM  | Remise                                                     | Texte           | 10                | Facultatif  |
| 16    | ART_DELAI   | Délai de livraison                                         | Nombre entier    |                   | Facultatif  |


 


Attention, l'ordre des champs doit absolument être respecté.


 


 


