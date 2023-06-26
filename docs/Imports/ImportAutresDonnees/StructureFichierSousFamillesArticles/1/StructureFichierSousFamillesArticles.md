# Structure du fichier de sous-familles d'articles











| Champ | Description | Type | Longueur maximale | Valeurs possibles | Description des valeurs possibles | Présence | Exemple |
|---|---|---|---|---|---|---|---|
| SFA\_CODE | Code | Texte | 10 |   |   | Obligatoire |   |
| SFA\_LIB | Libellé | Texte | 40 |   |   | Facultatif |   |
| FAR\_CODE | Famille | Texte | 10 |   |   | Facultatif |   |
| SFA\_DORT | En sommeil | Case à cocher |   |   |   | Facultatif |   |
| SFA\_TYPE | Type d'article | Texte | 1 | P <br>C <br>N <br>F <br>V | Pièce <br>Consigne <br>Nomenclature <br>Forfait <br>Service | Facultatif |   |
| SFA\_CATEG | Catégorie | Texte | 1 | F <br>S <br>M <br>O <br>T <br>A | Produits finis <br>Produits semi-finis <br>Matières premières <br>Main d'oeuvre <br>Sous-traitance <br>Autre | Facultatif |   |
| SFA\_QTEDFT | Quantité par défaut | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_PRIXAU | Par combien ? | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_T\_APP | Formule de frais d'approche de vente 1 | Texte | 15 |   |   | Facultatif |   |
| SFA\_T\_APP2 | Formule de frais d'approche de vente 2 | Texte | 15 |   |   | Facultatif |   |
| SFA\_T\_APP3 | Formule de frais d'approche de vente 3 | Texte | 15 |   |   | Facultatif |   |
| SFA\_F\_APP | Frais d'approche de vente 1 | Montant |   |   |   | Facultatif |   |
| SFA\_P\_COEF | Coefficient | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_V\_ARR | Arrondir à | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_T\_ARR | Type d'arrondi | Texte | 1 | 1 <br>2 <br>3 <br>4 <br>5 <br>6 | Inférieur <br>Proche <br>Supérieur <br>Fixe inférieur <br>Fixe proche <br>Fixe supérieur | Facultatif |   |
| SFA\_M\_PRV | Calcul du prix de revient | Texte | 1 | M <br>P <br>A <br>D | Manuel <br>Dans le dépot principal <br>Dans tous les dépots <br>Celui du dernier mouvement d'entrée | Facultatif |   |
| SFA\_I\_PRV | Si modification prix de revient | Texte | 1 | P
C | Recalcul du prix de vente
Recalcul du coefficient | Facultatif |   |
| SFA\_MFACT | Mode de facturation | Texte | 1 | D <br>B <br>V <br>L <br>P | Au débit unitaire <br>Au débit total <br>Au volume unitaire <br>Au volume total <br>Au poids | Facultatif |   |
| SFA\_NII | Nomenclature DEB | Texte | 14 |   |   | Facultatif |   |
| SFA\_NIMP | Non imprimable | Case à cocher |   |   |   | Facultatif |   |
| SFA\_NSTAT | Hors statistiques | Case à cocher |   |   |   | Facultatif |   |
| SFA\_NCOM | Hors commissions | Case à cocher |   |   |   | Facultatif |   |
| SFA\_CONTRM | Géré en contremarque | Case à cocher |   |   |   | Facultatif |   |
| SFA\_INTV | Interdit à la vente | Case à cocher |   |   |   | Facultatif |   |
| SFA\_INTA | Interdit à l'achat | Case à cocher |   |   |   | Facultatif |   |
| SFA\_STOCK | Type de stock | Texte | 1 | N <br>C <br>M <br>X <br>A <br>I <br>O | Non géré <br>Non valorisé <br>Prix moyen pondéré <br>Prix moyen d'achat <br>Dernier prix d'achat <br>FIFO/FEFO <br>LIFO | Facultatif |   |
| SFA\_TLOT | Lot ou série | Texte | 1 | S <br>L | Série <br>Lot | Facultatif |   |
| SFA\_LCSNSH | Limiter les n° de série aux caractères hexadécimaux (0123456789ABCDEF) | Case à cocher |   |   |   | Facultatif |   |
| SFA\_PERIMA | Lot périssable | Case à cocher |   |   |   | Facultatif |   |
| SFA\_DELCOM | Délai de commercialisation du lot en jours | Nombre entier |   |   |   | Facultatif |   |
| SFA\_S\_PRV | Mise à jour du prix de revient dans les stocks | Texte | 1 | A <br>M | Automatique
Manuelle | Facultatif |   |
| SFA\_D\_PRV | Prix de revient dans les documents de vente | Texte | 1 | A <br>S | Prix de revient commercial de l'onglet "Général" <br>Prix de revient unitaire de l'onglet "Stock" | Facultatif |   |
| SFA\_GROUPE | Groupe d'équivalence | Texte | 10 |   |   | Facultatif |   |
| SFA\_AUCFS | Acheter uniquement chez les fournisseurs sélectionnés | Case à cocher |   |   |   | Facultatif |   |
| SFA\_TGAMME | Type de gamme | Texte | 10 |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés |   |   |   |   |   |   |


