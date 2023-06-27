# Structure du fichier de main d'oeuvre réalisée d'affaires










| Ordre | Champ | Description | Type | Longueur maximale | Présence | Exemple |
|---|---|---|---|---|---|---|
| 1 | PRJ\_CODE | Code d'une affaire existante | Texte | 40 | Obligatoire |  |
| 2 | LPJ\_NUMERO | N° d'une ligne existante à modifier, ou rien du tout pour une ligne à créer | Texte | 5 | Facultatif | 00003 |
| 3 | LPJ\_ID | Identifiant d'une ligne existante à modifier, ou rien du tout pour une ligne à créer | Texte | 38 | Facultatif | {2583DE57-AFB9-4760-9CEF-EB2889E43484} |
| 4 | LPJ\_DATE | Date | Date |   | Facultatif |   |
| 5 | LPJ\_TYPE | Code d'un type de main d'oeuvre existant dans "Affaires : Types de main d'œuvre" (TMP) dans les tables de référence | Texte | 15 | Facultatif |   |
| 6 | LPJ\_STYPE | Code d'un sous-type de main d'œuvre existant dans "Affaires : Sous-Types de main d'œuvre" (SMP) dans les tables de référence | Texte | 15 | Facultatif |   |
| 7 | SAL\_CRITE1 | Code d'un critère salarié 1 existant dans "Salariés : Critères 1" (CS1) dans les tables de référence | Texte | 15 | Facultatif |   |
| 8 | SAL\_CRITE2 | Code d'un critère salarié 2 existant dans "Salariés : Critères 2" (CS2) dans les tables de référence | Texte | 15 | Facultatif |   |
| 9 | SAL\_CRITE3 | Code d'un critère salarié 3 existant dans "Salariés : Critères 3" (CS3) dans les tables de référence | Texte | 15 | Facultatif |   |
| 10 | SAL\_CODE | Code d'un salarié existant, pas en sommeil | Texte | 3 | Facultatif |   |
| 11 | LPJ\_LIB | Libellé | Texte | 100 | Facultatif |   |
| 12 | LPJ\_QTE | Quantité | Nombre à virgule |   | Facultatif |   |
| 13 | LPJ\_PRIXUN | Prix unitaire | Montant |   | Facultatif |   |
| 14 | LPJ\_PRIXTO | Prix total | Montant |   | Facultatif |   |
| 15 | LPJ\_AVANCE | Pourcentage d'avancement | Nombre à virgule |   | Facultatif |   |
| 16 | ART\_CODE | Code d'un article existant, pas en sommeil, de catégorie "Main d'œuvre" (O) ou "Sous-traitance" (T) | Texte | 30 | Facultatif |   |


 


Attention, l'ordre des champs doit absolument être respecté.


