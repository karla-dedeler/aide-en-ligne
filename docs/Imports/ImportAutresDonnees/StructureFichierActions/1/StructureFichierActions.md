# Structure du fichier d'actions










| Champ       | Description                     | Type            | Longueur maximale | Valeurs possibles                                         | Présence    | Exemple |
|-------------|---------------------------------|-----------------|-------------------|-----------------------------------------------------------|-------------|---------|
| ACT_NUMERO  | Numéro interne de l'action      | Texte           | 10                |                                                           | Facultatif  |         |
| ACT_DATE    | Date et heure de début          | Date et heure   |                   |                                                           | Facultatif  |         |
| ACT_HEURE   | Heure                           | Texte           | 6                 |                                                           | Facultatif  |         |
| ACT_DATECH  | Date d'échéance                  | Date            |                   |                                                           | Facultatif  |         |
| PCF_CODE    | Code tiers                      | Texte           | 20                |                                                           | Facultatif  |         |
| CCT_NUMERO  | N° interne de contact           | Texte           | 10                |                                                           | Facultatif  |         |
| ACT_OBJET   | Objet                           | Texte           | 80                |                                                           | Facultatif  |         |
| ACT_TYPE    | Type                            | Texte           | 15                |                                                           | Obligatoire |         |
| ACT_ETAT    | Etat                            | Texte           | 15                |                                                           | Facultatif  |         |
| ACT_LEVEL   | Priorité                        | Texte           | 1                 | F : Faible, N : Normale, H : Haute                   | Facultatif  |         |
| ACT_RAPPEL  | Rappel                          | Case à cocher   |                   |                                                           | Facultatif  |         |
| ACT_JRNENT  | Journée entière                 | Case à cocher   |                   |                                                           | Facultatif  |         |
| ACT_TERMINE | Terminée                        | Case à cocher   |                   |                                                           | Facultatif  |         |
| ACT_DATRAP  | Date et heure de rappel         | Date et heure   |                   |                                                           | Facultatif  |         |
| ACT_DATFIN  | Date et heure de fin            | Date et heure   |                   |                                                           | Facultatif  |         |
| ACT_POUREA  | % réalisé                       | Nombre entier   |                   |                                                           | Facultatif  |         |
| ACT_DMNDPR  | Demandée par                    | Texte           | 3                 |                                                           | Facultatif  |         |
| SAL_CODE    | Assignée à                      | Texte           | 3                 |                                                           | Facultatif  |         |
| PRJ_CODE    | Code affaire                    | Texte           | 40                |                                                           | Facultatif  |         |
| DOC_NUMERO  | N° interne de document          | Texte           | 10                |                                                           | Facultatif  |         |
| ACT_DESC    | Descriptif                      |                 |                   |                                                           | Facultatif  |         |
| ACT_FILE    | Fichier                         | Texte           | 260               |                                                           | Facultatif  |         |
| XXX_...     | Champs personnalisés            |                 |                   |                                                           | Facultatif  |         |

