# Structure du fichier de lignes d'amortissement











| Ordre | Champ | Description | Type | Longueur  maximale | Présence | Exemple |
|---|---|---|---|---|---|---|
| 1 | IMO\_CODE | Code d'une immobilisation existante | Texte | 15 | Obligatoire |  |
| 2 | LIG\_NUMERO | N° d'une ligne existante à modifier, ou rien du tout pour une ligne à créer | Nombre entier |   | Facultatif |   |
| 4 | LIG\_DTDEB | Date de début d'amortissement pour la ligne en cours | Date |   | Obligatoire |   |
| 5 | LIG\_DTFIN | Date de fin d'amortissement pour la ligne en cours | Date |   | Obligatoire |   |
| 6 | LIG\_MTBSE | Montant de base à amortir | Montant |   | Facultatif |   |
| 7 | LIG\_MTDOT | Montant de la dotation | Montant |   | Obligatoire |   |
| 8 | LIG\_MTCDOT | Cumul des montants de dotation | Montant |   | Facultatif |   |
| 9 | LIG\_MTVNC | Montant de la VNC | Montant |   | Facultatif |   |
| 10 | LIG\_TXGAMO | Taux d'amortissement | Nombre à virgule |   | Obligatoire |   |
| 11 | LIG\_SLDEE | Ligne soldée | Texte | 3 | Facultatif | Oui <br>Non |


 


Attention, l'ordre des champs doit absolument être respecté.


