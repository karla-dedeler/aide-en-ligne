# Structure du fichier d'articles seuls










| Champ | Description | Type | Longueur maximale | Valeurs possibles | Description des valeurs possibles | Présence |
|--------------|--------------------------------------------|----------------|-------------------|----------------------------------------------|-----------------------------------|-------------|
| ART\_CODE | Code article | Texte | 30 |   |   | Obligatoire \* |
| ART\_LIB | Libellé | Texte | 250 |   |   | Obligatoire |
| ART\_TGAMME | Type de gamme | Texte | 10 |   |   | Facultatif |
| ART\_DORT | En sommeil | Case à cocher |   |   |   | Facultatif |
| FAR\_CODE | Famille | Texte | 10 |   |   | Facultatif |
| ART\_FARNAT |   | Texte | 10 |   |   | Facultatif |
| SFA\_CODE | Code sous-famille | Texte | 10 |   |   | Facultatif |
| ART\_SFANAT |   | Texte | 10 |   |   | Facultatif |
| ART\_TYPE | Type d'article | Texte | 1 | P C N F V | Pièce, Consigne, Nomenclature, Forfait, Service | Facultatif |
| ART\_CATEG | Catégorie | Texte | 1 | F S M O T A | Produits finis, Produits semi-finis, Matières premières, Main d'oeuvre, Sous-traitance, Autre | Facultatif |
| ART\_QTEDFT | Quantité par défaut | Nombre à virgule |   |   |   | Facultatif |
| ART\_PRIXAU | Par combien ? | Nombre à virgule |   |   |   | Facultatif |
| ART\_T\_APP | Formule de frais d'approche de vente 1 | Texte | 15 |   |   | Facultatif |
| ART\_F\_APP | Frais d'approche de vente 1 | Montant |   |   |   | Facultatif |
| ART\_T\_APP2 | Formule de frais d'approche de vente 2 | Texte | 15 |   |   | Facultatif |
| ART\_F\_APP2 | Frais d'approche de vente 2 | Montant |   |   |   | Facultatif |
| ART\_T\_APP3 | Formule de frais d'approche de vente 3 | Texte | 15 |   |   | Facultatif |
| ART\_F\_APP3 | Frais d'approche de vente 3 | Montant |   |   |   | Facultatif |
| ART\_T\_ACH | Formule de frais d'approche d'achat 1 | Texte | 15 |   |   | Facultatif |
| ART\_F\_ACH | Frais d'approche d'achat 1 | Montant |   |   |   | Facultatif |
| ART\_T\_ACH2 | Formule de frais d'approche d'achat 2 | Texte | 15 |   |   | Facultatif |
| ART\_F\_ACH2 | Frais d'approche d'achat 2 | Montant |   |   |   | Facultatif |
| ART\_T\_ACH3 | Formule de frais d'approche d'achat 3 | Texte | 15 |   |   | Facultatif |
| ART\_F\_ACH3 | Frais d'approche d'achat 3 | Montant |   |   |   | Facultatif |
| ART\_M\_PRV | Calcul du prix de revient | Texte | 1 | M P A D | Manuel, Dans le dépot principal, Dans tous les dépots, Celui du dernier mouvement d'entrée | Facultatif |
| ART\_I\_PRV | Si modification prix de revient | Texte | 1 | P C | Recalcul du prix de vente, Recalcul du coefficient | Facultatif |
| ART\_V\_ARR | Arrondir à | Nombre à virgule |   |   |   | Facultatif |
| ART\_T\_ARR | Type d'arrondi | Texte | 1 | 1 2 3 4 5 6 | Inférieur, Proche, Supérieur, Fixe inférieur, Fixe proche, Fixe supérieur | Facultatif |
| ART\_REMMAX | Pourcentage de remise maximum | Montant |   |   |   | Facultatif |
| ART\_RMXDOC | Pourcentage de remise maximum au document ? | Case à cocher |   |   |   | Facultatif |
| ART\_TRENDU | Type de frais rendus | Texte | 15 |   |   | Facultatif |
| ART\_FRENDU | Frais rendus | Montant |   |   |   | Facultatif |
| ART\_P\_ACH | Prix d'achat unitaire | Montant |   |   |   | Facultatif |
| ART\_P\_PRV | Prix de revient unitaire | Montant |   |   |   | Facultatif |
| ART\_P\_COEF | Coefficient | Nombre à virgule |   |   |   | Facultatif |
| ART\_P\_VTE | Prix public unitaire | Montant |   |   |   | Facultatif |
| ART\_P\_EURO | Prix de vente unitaire en Euro | Montant |   |   |   | Facultatif |
| ART\_LIBC | Libellé court | Texte | 20 |   |   | Facultatif |
| ART\_CBAR | Code-barres | Texte | 30 |   |   | Facultatif |
| ART\_REF | Référence constructeur | Texte | 30 |   |   | Facultatif |
| ART\_NII | Nomenclature DEB | Texte | 14 |   |   | Facultatif |
| ART\_MFACT | Facturation à la vente | Texte | 1 | D B V L P | Au débit unitaire, Au débit total, Au volume unitaire, Au volume total, Au poids | Facultatif |
| ART\_MACHAT | Facturation à l'achat | Texte | 1 | D B V L P | Au débit unitaire, Au débit total, Au volume unitaire, Au volume total, Au poids | Facultatif |
| ART\_DELAI | Délai de livraison | Entier |   |   |   | Facultatif |
| ART\_CONSIG | Consigne | Texte | 30 |   |   | Facultatif |
| GAR\_CODE | Garantie | Texte | 3 |   |   | Facultatif |
| FA1\_CODE | Critère 1 | Texte | 15 |   |   | Facultatif |
| FA2\_CODE | Critère 2 | Texte | 15 |   |   | Facultatif |
| FA3\_CODE | Critère 3 | Texte | 15 |   |   | Facultatif |
| FA4\_CODE | Critère 4 | Texte | 15 |   |   | Facultatif |
| FA5\_CODE | Critère 5 | Texte | 15 |   |   | Facultatif |
| ART\_NIMP | Non imprimable | Case à cocher |   |   |   | Facultatif |
| ART\_NSTAT | Hors statistiques | Case à cocher |   |   |   | Facultatif |
| ART\_NCOM | Hors commissions | Case à cocher |   |   |   | Facultatif |
| ART\_CONTRM | Géré en contremarque | Case à cocher |   |   |   | Facultatif |
| ART\_INTV | Interdit à la vente | Case à cocher |   |   |   | Facultatif |
| ART\_INTA | Interdit à l'achat | Case à cocher |   |   |   | Facultatif |
| ART\_MSUPPTPF1 | Coefficient 1 de TPF | Nombre à virgule |   |   |   | Facultatif |
| ART\_MSUPPTPF2 | Coefficient 2 de TPF | Nombre à virgule |   |   |   | Facultatif |
| ART\_UC\_ACH | Unité de conditionnement d'achat | Texte | 15 |   |   | Facultatif |
| ART\_CD\_ACH | Nombre d'unités de base dans l'unité de conditionnement d'achat | Nombre à virgule |   |   |   | Facultatif |
| ART\_UB\_ACH | Unité de base d'achat | Texte | 15 |   |   | Facultatif |
| ART\_UC\_STK | Unité de conditionnement de stock | Texte | 15 |   |   | Facultatif |
| ART\_CD\_STK | Nombre d'unités de base dans l'unité de conditionnement de stock | Nombre à virgule |   |   |   | Facultatif |
| ART\_UB\_STK | Unité de base de stock | Texte | 15 |   |   | Facultatif |
| ART\_UC\_VTE | Unité de conditionnement de vente | Texte | 15 |   |   | Facultatif |
| ART\_CD\_VTE | Nombre d'unités de base dans l'unité de conditionnement de vente | Nombre à virgule |   |   |   | Facultatif |
| ART\_UB\_VTE | Unité de base de vente | Texte | 15 |   |   | Facultatif |
| ART\_R\_UAUV | UA/UV | Nombre à virgule |   |   |   | Facultatif |
| ART\_R\_USUV | US/UV | Nombre à virgule |   |   |   | Facultatif |
| ART\_NCOLIS | Articles par colis | Nombre à virgule |   |   |   | Facultatif |
| ART\_POIDSN | Poids net | Nombre à virgule |   |   |   | Facultatif |
| ART\_POIDST | Tare | Nombre à virgule |   |   |   | Facultatif |
| ART\_POIDSB | Poids brut | Nombre à virgule |   |   |   | Facultatif |
| ART\_LONG | Longueur | Nombre à virgule |   |   |   | Facultatif |
| ART\_LARG | Largeur | Nombre à virgule |   |   |   | Facultatif |
| ART\_HAUT | Hauteur | Nombre à virgule |   |   |   | Facultatif |
| ART\_VOLUME | Volume | Nombre à virgule |   |   |   | Facultatif |
| ART\_PACHUB | Prix d'achat unitaire en unité de base | Case à cocher |   |   |   | Facultatif |
| ART\_PVTEUB | Prix de vente unitaire exprimé en unité de base | Case à cocher |   |   |   | Facultatif |
| ART\_PV\_MAN | Prix de vente de la nomenclature manuel | Case à cocher |   |   |   | Facultatif |
| ART\_STOCK | Type de stock | Texte | 1 | N C M X A I F | Non géré, Non valorisé, Prix moyen pondéré, Prix moyen d'achat, Dernier prix d'achat, FIFO/FEFO, LIFO | Facultatif |
| ART\_TLOT | Lot ou série | Texte | 1 | S L | Série, Lot | Facultatif |
| ART\_LCSNSH | Limiter les n° de série aux caractères hexadécimaux (0123456789ABCDEF) | Case à cocher |   |   |   | Facultatif |
| ART\_PERIMA | Lot périssable | Case à cocher |   |   |   | Facultatif |
| ART\_DELCOM | Délai de commercialisation du lot en jours | Entier |   |   |   | Facultatif |
| ART\_S\_PRV | Mise à jour du prix de revient dans les stocks | Texte | 1 | A M | Automatique
Manuelle | Facultatif |
| ART\_D\_PRV | Prix de revient dans les documents de vente | Texte | 1 | A S | Prix de revient commercial de l'onglet "Général", Prix de revient unitaire de l'onglet "Stock" | Facultatif |
| ART\_GROUPE | Groupe d'équivalence | Texte | 10 |   |   | Facultatif |
| ART\_REMPL | Article de rempl. | Texte | 30 |   |   | Facultatif |
| ART\_AUCFS | Acheter uniquement chez les fournisseurs sélectionnés | Case à cocher |   |   |   | Facultatif |
| ART\_MEMO | Commentaires | Texte illimité |   |   |   | Facultatif |
| ART\_AFFMES | Afficher un message lors de la saisie d'un document | Case à cocher |   |   |   | Facultatif |
| ART\_MESSAG | Message | Texte illimité |   |   |   | Facultatif |
| ART\_FMTIMG | Format d'image | Texte | 255 |   |   | Facultatif |
| ART\_DTCREE | Créé le | Date |   |   |   | Facultatif |
| ART\_USRCRE | Créé par | Texte | 20 |   |   | Facultatif |
| ART\_OLDCOD | Ancien code article | Texte | 30 |   |   | Facultatif |
| ART\_RENPAR | Renommé par | Texte | 20 |   |   | Facultatif |
| ART\_RENLE | Renommé le | Date |   |   |   | Facultatif |
| PCF\_CODE | Code tiers | Texte | 20 |   |   | Facultatif |
| XXX\_... | Champs personnalisés |   |   |   |   | Facultatif |


   


\* Dans le cas où la codification des articles est définie comme automatique, le code article présent dans le fichier sera ignoré.


