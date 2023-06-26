# Structure du fichier de références clients seules











| Ordre | Champ       | Description                               | Type           | Longueur maximale | Présence    | Exemple |
|-------|-------------|-------------------------------------------|----------------|-------------------|-------------|---------|
| 1     | PCF_CODE    | Code client                               | Texte          | 20                | Obligatoire |         |
| 2     | ART_CODE    | Code article                              | Texte          | 30                | Obligatoire |         |
| 3     | ART_GAMME   | Codes valeurs de gammes séparées par un \ | Texte          | 98                | Facultatif  |         |
| 4     | ART_PCLIENT | Priorité client                           | Texte          | 1                 | Facultatif  |         |
| 5     | ART_REFCLI  | Référence client                          | Texte          | 30                | Facultatif  |         |
| 6     | ART_PAYEUR  | Payeur                                    | Case à cocher  |                   | Facultatif  |         |

Attention, l'ordre des champs doit absolument être respecté.


