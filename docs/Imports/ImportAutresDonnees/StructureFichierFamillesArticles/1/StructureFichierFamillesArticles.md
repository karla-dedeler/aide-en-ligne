# Structure du fichier de familles d'articles










| Champ | Description | Type | Longueur maximale | Valeurs possibles | Description des valeurs possibles | Présence |
|-------|-------------|------|-------------------|------------------|---------------------------------|----------|
| FAR\_CODE | Code | Texte | 10 | - | - | Obligatoire |
| FAR\_LIB | Libellé | Texte | 40 | - | - | Obligatoire |
| FAR\_DORT | En sommeil | Case à cocher | - | - | - | Facultatif |
| FAR\_TYPE | Type d'article | Texte | 1 | P, C, N, F, V | Pièce, Consigne, Nomenclature, Forfait, Service | Facultatif |
| FAR\_CATEG | Catégorie | Texte | 1 | F, S, M, O, T, A | Produits finis, Produits semi-finis, Matières premières, Main d'oeuvre, Sous-traitance, Autre | Facultatif |
| FAR\_QTEDFT | Quantité par défaut | Nombre à virgule | - | - | - | Facultatif |
| FAR\_PRIXAU | Par combien ? | Nombre à virgule | - | - | - | Facultatif |
| FAR\_T\_APP | Formule de frais d'approche de vente 1 | Texte | 15 | - | - | Facultatif |
| FAR\_T\_APP2 | Formule de frais d'approche de vente 2 | Texte | 15 | - | - | Facultatif |
| FAR\_T\_APP3 | Formule de frais d'approche de vente 3 | Texte | 15 | - | - | Facultatif |
| FAR\_F\_APP | Frais d'approche de vente 1 | Montant | - | - | - | Facultatif |
| FAR\_P\_COEF | Coefficient | Nombre à virgule | - | - | - | Facultatif |
| FAR\_V\_ARR | Arrondir à | Nombre à virgule | - | - | - | Facultatif |
| FAR\_T\_ARR | Type d'arrondi | Texte | 1 | 1, 2, 3, 4, 5, 6 | Inférieur, Proche, Supérieur, Fixe inférieur, Fixe proche, Fixe supérieur | Facultatif |
| FAR\_M\_PRV | Calcul du prix de revient | Texte | 1 | M, P, A, D | Manuel, Dans le dépôt principal, Dans tous les dépôts, Celui du dernier mouvement d'entrée | Facultatif |
| FAR\_I\_PRV | Si modification prix de revient | Texte | 1 | P, C | Recalcul du prix de vente, Recalcul du coefficient | Facultatif |
| FAR\_MFACT | Mode de facturation | Texte | 1 | - , D, B, V, L, P | - , Au débit unitaire, Au débit total, Au volume unitaire, Au volume total, Au poids | Facultatif |
| FAR\_NII | Nomenclature DEB | Texte | 14 | - | - | Facultatif |
| FAR\_NIMP | Non imprimable | Case à cocher | - | - | - | Facultatif |
| FAR\_NSTAT | Hors statistiques | Case à cocher |   |   |   | Facultatif |
| FAR\_NCOM | Hors commissions | Case à cocher |   |   |   | Facultatif |
| FAR\_CONTRM | Géré en contremarque | Case à cocher |   |   |   | Facultatif |
| FAR\_INTV | Interdit à la vente | Case à cocher |   |   |   | Facultatif |
| FAR\_INTA | Interdit à l'achat | Case à cocher |   |   |   | Facultatif |
| FAR\_STOCK | Type de stock | Texte | 1 | N, C, M, X, A, I, O | Non géré, Non valorisé, Prix moyen pondéré, Prix moyen d'achat, Dernier prix d'achat, FIFO/FEFO, LIFO | Facultatif |
| FAR\_TLOT | Lot ou série | Texte | 1 |  S, L | Série, Lot | Facultatif |
| FAR\_LCSNSH | Limiter les n° de sérieaux caractères hexadécimaux (0123456789ABCDEF) | Case à cocher |   |   |   | Facultatif |
| FAR\_PERIMA | Lot périssable | Case à cocher |   |   |   | Facultatif |
| FAR\_DELCOM | Délai de commercialisation du lot en jours | Nombre entier |   |   |   | Facultatif |
| FAR\_S\_PRV | Mise à jour du prix de revient dans les stocks | Texte | 1 | A
M | Automatique
Manuelle | Facultatif |
| FAR\_D\_PRV | Prix de revient dans les documents de vente | Texte | 1 | A
S | Prix de revient commercial de l'onglet "Général"
Prix de revient unitaire de l'onglet "Stock" | Facultatif |
| FAR\_GROUPE | Groupe d'équivalence | Texte | 10 |   |   | Facultatif |
| FAR\_AUCFS | Acheter uniquement chez les fournisseurs sélectionnés | Case à cocher |   |   |   | Facultatif |
| FAR\_TGAMME | Type de gamme | Texte | 10 |   |   | Facultatif |
| XXX\_... | Champs personnalisés |   |   |   |   | Facultatif |


