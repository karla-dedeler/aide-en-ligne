# Structure du fichier de tarifs seuls










| Ordre | Champ        | Description                               | Type            | Longueur maximale | Présence    |
|-------|--------------|-------------------------------------------|-----------------|-------------------|-------------|
| 1     | ART_CODE     | Code article                              | Texte           | 30                | Obligatoire |
| 2     | DEV_CODE     | Code devise                               | Texte           | 3                 | Facultatif  |
| 3     | ART_GAMME    | Codes valeurs de gammes séparées par un \ | Texte           | 98                | Facultatif  |
| 4     | ART_P_ACH    | Prix d'achat unitaire                      | Montant         |                   | Facultatif  |
| 5     | ART_P_COEF   | Coefficient                               | Nombre à virgule |                   | Facultatif  |
| 6     | ART_P_VTE    | Prix public unitaire                       | Montant         |                   | Facultatif  |
| 7     | ART_DT_NEW   | Date de mise à jour                        | Date            |                   | Facultatif  |
| 8     | ART_N_ACH    | Nouveau prix d'achat unitaire              | Montant         |                   | Facultatif  |
| 9     | ART_N_COEF   | Nouveau coefficient                        | Nombre à virgule |                   | Facultatif  |
| 10    | ART_N_VTE    | Nouveau prix de vente unitaire             | Montant         |                   | Facultatif  |


 


Attention, l'ordre des champs doit absolument être respecté.


