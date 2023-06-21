# Structure du fichier d'affaires









| Champ | Description | Type | Longueur
maximale | Présence | Exemple |
| PRJ\_CODE | Code affaire | Texte | 40 | Obligatoire \* |   |
| PRJ\_LIB | Libellé | Texte | 100 | Obligatoire |   |
| PRJ\_ETAT | Code état | Texte | 15 | Facultatif | C |
| PRJ\_GROUP1 | Code catégorie | Texte | 15 | Facultatif | STA |
| PRJ\_GROUP2 | Code sous-catégorie | Texte | 15 | Facultatif | STA2 |
| PRJ\_DT\_DEB | Date dé début | Date |   | Facultatif |   |
| PRJ\_DT\_FIN | Date de fin | Date |   | Facultatif |   |
| PCF\_CODE | Code tiers | Texte | 20 | Facultatif |   |
| PRJ\_DESC | Descriptif | Texte illimité |   | Facultatif |   |
| PRJ\_BUGLAC | Montant budgété global pour tous les documents d'achat rattachés | Montant |   | Facultatif |   |
| ANA\_CODE | Code section analytique | Texte | 15 | Facultatif |   |
| XXX\_... | Champs personnalisés |   |   | Facultatif |   |


 


\* Dans le cas où la codification des affaires est définie comme automatique dans les préférences, le code affaire renseigné dans le fichier sera ignoré.


 
