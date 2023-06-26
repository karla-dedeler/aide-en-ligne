# Structure du fichier de devises








| Champ        | Description                        | Type             | Longueur maximale | Présence    |
|--------------|------------------------------------|------------------|--------------------|-------------|
| DEV_CODE     | Devise                             | Texte            | 3                  | Obligatoire |
| DEV_LIB      | Libellé                            | Texte            | 40                 | Obligatoire |
| DEV_MONEY    | Unité                              | Texte            | 12                 | Facultatif  |
| DEV_MONEYS   | Sous-unité                         | Texte            | 12                 | Facultatif  |
| DEV_FORMAT   | Format                             | Texte            | 20                 | Facultatif  |
| DEV_NB_DEC   | Décimales                          | Texte            | 1                  | Facultatif  |
| DEV_SYMBOL   | Symbole                            | Texte            | 3                  | Facultatif  |
| DEV_DT_ACT   | Date d'actualisation du cours       | Date             |                    | Facultatif  |
| DEV_INCERT   | A l'incertain ?                    | Case à cocher    |                    | Facultatif  |
| DEV_COURS    | Cours                              | Nombre à virgule |                    | Facultatif  |
| DEV_DTEURO   | Date d'application de l'Euro       | Date             |                    | Facultatif  |
| DEV_EURO     | Parité avec l'Euro                 | Nombre à virgule |                    | Facultatif  |


