# Structure du fichier de documents de vente










| Champ | Description | Type | Longueur
maximale | Format | Présence | Valeur par défaut |
| DOC\_STYPE | Sous-type de document de vente | Texte | 1 | Valeurs possibles :
P = Pro-Forma
D = Devis
C = Commande
B = Livraison
R = Retour
F = Facture
A = Avoir
0 = Avoir financier
1 = Facture financière | Obligatoire |   |
| PCF\_CODE | Code tiers | Texte | 20 |   | Obligatoire |   |
| DOC\_PIECE | N° de pièce | Texte | 15 |   | Facultatif |   |
| DOC\_PIECE2 | N° de pièce complémentaire | Texte | 60 |   | Facultatif |   |
| DOC\_DATE | Date de document | Date |   | Format : JJ/MM/AAAA | Facultatif | Date du jour |
| DOC\_DT\_PRV  | Date de livraison | Date |   | Format : JJ/MM/AAAA | Facultatif |   |
| DOC\_EN\_TTC  | Prix en TTC ? | Case à cocher |   |   | Facultatif |   |
| PRJ\_CODE | Code affaire | Texte | 40 |   | Facultatif |   |
| REP\_CODE | Code commercial | Texte | 3 |   | Facultatif |   |
| DEP\_CODE | Code dépôt  | Texte | 3 |   | Facultatif |   |
| REG\_CODE | Code du mode de règlement | Texte | 8 |   | Facultatif | Mode de règlement du tiers |
| DOC\_REFPCF | Référence | Texte | 100 |   | Facultatif |   |
| TRP\_CODE | Code transporteur | Texte | 3 |   | Facultatif |   |
| DOC\_REMFAC | Montant de remise exceptionnelle | Montant |   | Séparateur décimal : point ou virgule | Facultatif |   |
| DOC\_TXRFAC | Pourcentage de remise exceptionnelle | Nombre à virgule |   | Séparateur décimal : point ou virgule | Facultatif |   |
| DOC\_FPYEUR | Adresse de facturation au payeur ? | Case à cocher |   |   | Facultatif |   |
| DOC\_F\_TITL | Titre de l'adresse de facturation | Texte | 60 |   | Facultatif |   |
| DOC\_F\_RS | Raison sociale de l'adresse de facturation | Texte | 60 |   | Facultatif |   |
| DOC\_F\_RS2 | Complément de raison sociale de l'adresse de facturation | Texte | 60 |   | Facultatif |   |
| DOC\_F\_RUE | Rue de l'adresse de facturation | Texte | 60 |   | Facultatif |   |
| DOC\_F\_COMP | Complément de rue de l'adresse de facturation | Texte | 60 |   | Facultatif |   |
| DOC\_F\_ETAT | Etat de l'adresse de facturation | Texte | 100 |   | Facultatif |   |
| DOC\_F\_REG | Région de l'adresse de facturation | Texte | 100 |   | Facultatif |   |
| DOC\_F\_CP | Code postal de l'adresse de facturation | Texte | 10 |   | Facultatif |   |
| DOC\_F\_VILL | Ville de l'adresse de facturation | Texte | 200 |   | Facultatif |   |
| PAY\_CODE | Code pays de l'adresse de facturation | Texte | 3 |   | Facultatif |   |
| DOC\_F\_CBAR | Code-barres de l'adresse de facturation | Texte | 30 |   | Facultatif |   |
| DOC\_F\_SIRET | N° SIRET de l'adresse de facturation | Texte | 14 |   | Facultatif |   |
| DOC\_F\_MEMO | Commentaires de l'adresse de facturation | Texte illimité |   |   | Facultatif |   |
| DOC\_L\_TITL | Titre de l'adresse de livraison | Texte | 60 |   | Facultatif |   |
| DOC\_L\_RS | Raison sociale de l'adresse de livraison | Texte | 60 |   | Facultatif |   |
| DOC\_L\_RS2 | Complément de raison sociale de l'adresse de livraison | Texte | 60 |   | Facultatif |   |
| DOC\_L\_RUE | Rue de l'adresse de livraison | Texte | 60 |   | Facultatif |   |
| DOC\_L\_COMP | Complément de rue de l'adresse de livraison | Texte | 60 |   | Facultatif |   |
| DOC\_L\_ETAT | Etat de l'adresse de livraison | Texte | 100 |   | Facultatif |   |
| DOC\_L\_REG | Région de l'adresse de livraison | Texte | 100 |   | Facultatif |   |
| DOC\_L\_CP | Code postal de l'adresse de livraison | Texte | 10 |   | Facultatif |   |
| DOC\_L\_VILL | Ville de l'adresse de livraison | Texte | 200 |   | Facultatif |   |
| DOC\_L\_PAYS | Code pays de l'adresse de livraison | Texte | 3 |   | Facultatif |   |
| DOC\_L\_CBAR | Code-barres de l'adresse de livraison | Texte | 30 |   | Facultatif |   |
| DOC\_L\_SIRET | N° SIRET de l'adresse de livraison | Texte | 14 |   | Facultatif |   |
| DOC\_L\_MEMO | Commentaires de l'adresse de livraison | Texte illimité |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés des documents de vente |   |   |   | Facultatif |   |
| ART\_CODE | Code article  | Texte | 30 |   | Facultatif |   |
| LIG\_TYPE | Type de ligne texte | Texte | 1 | Valeur possible :
T = Texte | Facultatif |   |
| LIG\_QTE | Quantité  | Nombre à virgule |   | Séparateur décimal : point ou virgule | Obligatoire |   |
| ART\_GAMME | Codes valeurs de gammes séparées par un \ | Texte | 98 |   | Facultatif |   |
| LIG\_NUMLOT | N° de lot | Texte | 25 |   | Facultatif |   |
| LIG\_DT\_LIV | Date de livraison (à la ligne ) | Date |   |   | Facultatif |   |
| LIG\_P\_BRUT | Prix brut unitaire | Montant |   | Séparateur décimal : point ou virgule | Facultatif |   |
| LIG\_P\_PRV | Prix de revient unitaire | Montant |   | Séparateur décimal : point ou virgule | Facultatif |   |
| LIG\_REMISE | Remise (à la ligne) | Texte | 30 |   | Facultatif |   |
| LIG\_LIB | Désignation | Texte | 1000 |   | Facultatif |   |
| LIG\_ZONE | Zone de stockage | Texte | 100 |   | Facultatif |   |
| LIG\_MEMO | Commentaires (à la ligne) | Texte illimité |   |   | Facultatif |   |
| LIG\_DT\_FAB | Date de fabrication du numéro de lot  | Date |   |   | Facultatif |   |
| LIG\_DT\_PER | Date de péremption du numéro de lot | Date |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés des lignes de vente |   |   |   | Facultatif |   |


