# Structure du fichier d'affaires









| Champ        | Description                                                              | Type           | Longueur maximale | Présence       | Exemple |
|--------------|--------------------------------------------------------------------------|----------------|-------------------|----------------|---------|
| PRJ_CODE     | Code affaire                                                             | Texte          | 40                | Obligatoire \* |         |
| PRJ_LIB      | Libellé                                                                  | Texte          | 100               | Obligatoire    |         |
| PRJ_ETAT     | Code état                                                                | Texte          | 15                | Facultatif     | C       |
| PRJ_GROUP1   | Code catégorie                                                           | Texte          | 15                | Facultatif     | STA     |
| PRJ_GROUP2   | Code sous-catégorie                                                       | Texte          | 15                | Facultatif     | STA2    |
| PRJ_DT_DEB   | Date de début                                                            | Date           |                   | Facultatif     |         |
| PRJ_DT_FIN   | Date de fin                                                              | Date           |                   | Facultatif     |         |
| PCF_CODE     | Code tiers                                                               | Texte          | 20                | Facultatif     |         |
| PRJ_DESC     | Descriptif                                                               | Texte illimité |                   | Facultatif     |         |
| PRJ_BUGLAC   | Montant budgété global pour tous les documents d'achat rattachés          | Montant        |                   | Facultatif     |         |
| ANA_CODE     | Code section analytique                                                   | Texte          | 15                | Facultatif     |         |
| XXX_...      | Champs personnalisés                                                      |                |                   | Facultatif     |         |

 


\* Dans le cas où la codification des affaires est définie comme automatique dans les préférences, le code affaire renseigné dans le fichier sera ignoré.


 
