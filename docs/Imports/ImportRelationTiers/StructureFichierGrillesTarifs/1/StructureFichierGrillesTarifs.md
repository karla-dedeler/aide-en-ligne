# Structure du fichier de grilles de tarifs










| Champ | Description | Type | Longueur maximale | Présence | Exemple |
|---|---|---|---|---|---|
| TAR\_CODE | Code de la grille de tarifs | Texte | 30 | Obligatoire |   |
| TAR\_LIB | Libellé de la grille de tarifs | Texte | 40 | Obligatoire \* |   |
| FAR\_CODE | Code famille d'articles de la ligne de grille de tarifs | Texte | 10 | Obligatoire \*\* |   |
| SFA\_CODE | Code sous-famille d'articles | Texte | 10 | Obligatoire \*\* |   |
| ART\_CODE | Code article de la ligne de grille de tarifs | Texte | 30 | Obligatoire \*\* |   |
| ART\_GAMME | Codes valeurs de gammes de la ligne de grille de tarifs séparées par un \ | Texte | 98 | Facultatif |   |
| DEV\_CODE | Code devise de la ligne de grille de tarifs | Texte | 3 | Facultatif |   |
| TAR\_BORNE | Seuil de la ligne de grille de tarifs | Nombre à virgule |   | Facultatif |   |
| TAR\_REMISE | Remise de la ligne de grille de tarifs | Texte | 30 | Facultatif |   |
| TAR\_PRIX | Prix de la ligne de grille de tarifs | Montant |   | Facultatif \*\*\* |   |
| TAR\_CMMNTR | Commentaires de la ligne de grille de tarifs | Texte | 200 | Facultatif |   |
| TAR\_CMNTR2 | Commentaires supplémentaires de la ligne de grille de tarifs | Texte | 200 | Facultatif |   |


 


\* : Le libellé est obligatoire si la grille de tarifs est à créer, et facultatif si la grille de tarifs est juste à modifier


\*\* : Le code article ou le code famille ou le code sous-famille doit être renseigné.


\*\*\* : Le prix doit être renseigné à 0 si le champs est considéré comme vide.


