# Structure du fichier de sous-familles d'articles











| Champ | Description | Type | Longueur
maximale | Valeurs possibles | Description des valeurs possibles | Présence | Exemple |
| SFA\_CODE | Code | Texte | 10 |   |   | Obligatoire |   |
| SFA\_LIB | Libellé | Texte | 40 |   |   | Facultatif |   |
| FAR\_CODE | Famille | Texte | 10 |   |   | Facultatif |   |
| SFA\_DORT | En sommeil | Case à cocher |   |   |   | Facultatif |   |
| SFA\_TYPE | Type d'article | Texte | 1 | P
C
N
F
V | Pièce
Consigne
Nomenclature
Forfait
Service | Facultatif |   |
| SFA\_CATEG | Catégorie | Texte | 1 | F
S
M
O
T
A | Produits finis
Produits semi-finis
Matières premières
Main d'oeuvre
Sous-traitance
Autre | Facultatif |   |
| SFA\_QTEDFT | Quantité par défaut | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_PRIXAU | Par combien ? | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_T\_APP | Formule de frais d'approche de vente 1 | Texte | 15 |   |   | Facultatif |   |
| SFA\_T\_APP2 | Formule de frais d'approche de vente 2 | Texte | 15 |   |   | Facultatif |   |
| SFA\_T\_APP3 | Formule de frais d'approche de vente 3 | Texte | 15 |   |   | Facultatif |   |
| SFA\_F\_APP | Frais d'approche de vente 1 | Montant |   |   |   | Facultatif |   |
| SFA\_P\_COEF | Coefficient | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_V\_ARR | Arrondir à | Nombre à virgule |   |   |   | Facultatif |   |
| SFA\_T\_ARR | Type d'arrondi | Texte | 1 | 1
2
3
4
5
6 | Inférieur
Proche
Supérieur
Fixe inférieur
Fixe proche
Fixe supérieur | Facultatif |   |
| SFA\_M\_PRV | Calcul du prix de revient | Texte | 1 | M
P
A
D | Manuel
Dans le dépot principal
Dans tous les dépots
Celui du dernier mouvement d'entrée | Facultatif |   |
| SFA\_I\_PRV | Si modification prix de revient | Texte | 1 | P
C | Recalcul du prix de vente
Recalcul du coefficient | Facultatif |   |
| SFA\_MFACT | Mode de facturation | Texte | 1 |  
D
B
V
L
P |  
Au débit unitaire
Au débit total
Au volume unitaire
Au volume total
Au poids | Facultatif |   |
| SFA\_NII | Nomenclature DEB | Texte | 14 |   |   | Facultatif |   |
| SFA\_NIMP | Non imprimable | Case à cocher |   |   |   | Facultatif |   |
| SFA\_NSTAT | Hors statistiques | Case à cocher |   |   |   | Facultatif |   |
| SFA\_NCOM | Hors commissions | Case à cocher |   |   |   | Facultatif |   |
| SFA\_CONTRM | Géré en contremarque | Case à cocher |   |   |   | Facultatif |   |
| SFA\_INTV | Interdit à la vente | Case à cocher |   |   |   | Facultatif |   |
| SFA\_INTA | Interdit à l'achat | Case à cocher |   |   |   | Facultatif |   |
| SFA\_STOCK | Type de stock | Texte | 1 | N
C
M
X
A
I
O | Non géré
Non valorisé
Prix moyen pondéré
Prix moyen d'achat
Dernier prix d'achat
FIFO/FEFO
LIFO | Facultatif |   |
| SFA\_TLOT | Lot ou série | Texte | 1 |  
S
L |  
Série
Lot | Facultatif |   |
| SFA\_LCSNSH | Limiter les n° de série aux caractères hexadécimaux (0123456789ABCDEF) | Case à cocher |   |   |   | Facultatif |   |
| SFA\_PERIMA | Lot périssable | Case à cocher |   |   |   | Facultatif |   |
| SFA\_DELCOM | Délai de commercialisation du lot en jours | Nombre entier |   |   |   | Facultatif |   |
| SFA\_S\_PRV | Mise à jour du prix de revient dans les stocks | Texte | 1 | A
M | Automatique
Manuelle | Facultatif |   |
| SFA\_D\_PRV | Prix de revient dans les documents de vente | Texte | 1 | A
S | Prix de revient commercial de l'onglet "Général"
Prix de revient unitaire de l'onglet "Stock" | Facultatif |   |
| SFA\_GROUPE | Groupe d'équivalence | Texte | 10 |   |   | Facultatif |   |
| SFA\_AUCFS | Acheter uniquement chez les fournisseurs sélectionnés | Case à cocher |   |   |   | Facultatif |   |
| SFA\_TGAMME | Type de gamme | Texte | 10 |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés |   |   |   |   |   |   |


