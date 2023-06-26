# Structure du fichier de documents d'achat










| Champ       | Description                                   | Type             | Longueur maximale | Format                        | Présence    | Valeur par défaut |
|-------------|-----------------------------------------------|------------------|--------------------|-------------------------------|-------------|------------------|
| DOC_STYPE   | Sous-type de document de vente                 | Texte            | 1                  | D = Demande de prix, C = Commande, B = Livraison, R = Retour, F = Facture, A = Avoir, 0 = Avoir financier, 1 = Facture financière     | Obligatoire |                  |
| PCF_CODE    | Code tiers                                    | Texte            | 20                 |                               | Obligatoire |                  |
| DOC_PIECE   | N° de pièce                                   | Texte            | 15                 |                               | Facultatif  |                  |
| DOC_PIECE2  | N° de pièce complémentaire                     | Texte            | 60                 |                               | Facultatif  |                  |
| DOC_DATE    | Date de document                              | Date             |                    | JJ/MM/AAAA                    | Facultatif  | Date du jour     |
| DOC_DT_PRV  | Date de réception                             | Date             |                    | JJ/MM/AAAA                    | Facultatif  |                  |
| DOC_EN_TTC  | Prix en TTC ?                                 | Case à cocher    |                    |                               | Facultatif  |                  |
| PRJ_CODE    | Code affaire                                  | Texte            | 40                 |                               | Facultatif  |                  |
| REP_CODE    | Code commercial                               | Texte            | 3                  |                               | Facultatif  |                  |
| DEP_CODE    | Code dépôt                                    | Texte            | 3                  |                               | Facultatif  |                  |
| REG_CODE    | Code du mode de règlement                     | Texte            | 8                  |                               | Facultatif  | Mode de règlement du tiers |
| DOC_REFPCF  | Référence                                     | Texte            | 100                |                               | Facultatif  |                  |
| TRP_CODE    | Code transporteur                             | Texte            | 3                  |                               | Facultatif  |                  |
| DOC_REMFAC  | Montant de remise exceptionnelle              | Montant          |                    | Séparateur décimal : point ou virgule | Facultatif  |                  |
| DOC_TXRFAC  | Pourcentage de remise exceptionnelle          | Nombre à virgule |                    | Séparateur décimal : point ou virgule | Facultatif  |                  |
| DOC_FPYEUR  | Adresse de facturation au payeur ?             | Case à cocher    |                    |                               | Facultatif  |                  |
| DOC_F_TITL  | Titre de l'adresse de facturation              | Texte            | 60                 |                               | Facultatif  |                  |
| DOC_F_RS    | Raison sociale de l'adresse de facturation     | Texte            | 60                 |                               | Facultatif  |                  |
| DOC_F_RS2   | Complément de raison sociale de l'adresse de facturation | Texte            | 60                 |                               | Facultatif  |                  |
| DOC_F_RUE   | Rue de l'adresse de facturation                | Texte            | 60                 |                               | Facultatif  |                  |
| DOC_F_COMP  | Complément de rue de l'adresse de facturation  | Texte            | 60                 |                               | Facultatif  |                  |
| DOC_F_ETAT  | Etat de l'adresse de
| DOC\_L\_ETAT | Etat de l'adresse de livraison | Texte | 100 |   | Facultatif |   |
| DOC\_L\_REG | Région de l'adresse de livraison | Texte | 100 |   | Facultatif |   |
| DOC\_L\_CP | Code postal de l'adresse de livraison | Texte | 10 |   | Facultatif |   |
| DOC\_L\_VILL | Ville de l'adresse de livraison | Texte | 200 |   | Facultatif |   |
| DOC\_L\_PAYS | Code pays de l'adresse de livraison | Texte | 3 |   | Facultatif |   |
| DOC\_L\_CBAR | Code-barres de l'adresse de livraison | Texte | 30 |   | Facultatif |   |
| DOC\_L\_SIRET | N° SIRET de l'adresse de livraison | Texte | 14 |   | Facultatif |   |
| DOC\_L\_MEMO | Commentaires de l'adresse de livraison | Texte illimité |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés des documents d'achat |   |   |   | Facultatif |   |
| ART\_CODE | Code article  | Texte | 30 |   | Facultatif |   |
| LIG\_TYPE | Type de ligne texte | Texte | 1 | Valeur possible :
T = Texte | Facultatif |   |
| LIG\_QTE | Quantité  | Nombre à virgule |   | Séparateur décimal : point ou virgule | Obligatoire |   |
| ART\_GAMME | Codes valeurs de gammes séparées par un \ | Texte | 98 |   | Facultatif |   |
| LIG\_NUMLOT | N° de lot | Texte | 25 |   | Facultatif |   |
| LIG\_DT\_LIV | Date de réception (à la ligne ) | Date |   |   | Facultatif |   |
| LIG\_P\_BRUT | Prix brut unitaire | Montant |   | Séparateur décimal : point ou virgule | Facultatif |   |
| LIG\_P\_PRV | Prix de revient unitaire | Montant |   | Séparateur décimal : point ou virgule | Facultatif |   |
| LIG\_REMISE | Remise (à la ligne) | Texte | 30 |   | Facultatif |   |
| LIG\_LIB | Désignation | Texte | 1000 |   | Facultatif |   |
| LIG\_ZONE | Zone de stockage | Texte | 100 |   | Facultatif |   |
| LIG\_MEMO | Commentaires (à la ligne) | Texte illimité |   |   | Facultatif |   |
| LIG\_DT\_FAB | Date de fabrication du numéro de lot  | Date |   |   | Facultatif |   |
| LIG\_DT\_PER | Date de péremption du numéro de lot | Date |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés des lignes d'achat |   |   |   | Facultatif |   |


