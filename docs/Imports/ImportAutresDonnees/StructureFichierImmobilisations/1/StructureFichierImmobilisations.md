# Structure du fichier d'immobilisations











| Champ | Description | Type | Longueur
maximale | Valeurs possibles | Description des valeurs possibles | Présence | Exemple |
| IMO\_CODE | Code immobilisation | Texte | 15 |   |   | Obligatoire |   |
| IMO\_LIB | Libellé | Texte | 60 |   |   | Obligatoire |   |
| IMO\_LIBLON | Description longue | Texte | 200 |   |   | Facultatif |   |
| FAI\_CODE | Code famille d'immobilisation | Texte | 10 |   |   | Facultatif |   |
| IMO\_ETAT | Etat | Texte | 1 |  
E
A
S | Non amortie
En cours
Amortie
Sortie | Facultatif |   |
| IMO\_TYPE | Type | Texte | 1 | A
B
C
L | Aucun
Bien
Crédit-bail
Location | Facultatif |   |
| IMO\_CAT | Catégorie | Texte | 1 | A
I
C
F | Aucune
Incorporelle
Corporelle
Financière | Facultatif |   |
| LII\_CODE | Code lieu d'immobilisation | Texte | 3 |   |   | Facultatif |   |
| IMO\_CBAR | Code-barres | Texte | 30 |   |   | Facultatif |   |
| IMO\_SERIE | N° de série | Texte | 30 |   |   | Facultatif |   |
| IM1\_CODE | Code critère 1 | Texte | 15 |   |   | Facultatif |   |
| IM2\_CODE | Code critère 2 | Texte | 15 |   |   | Facultatif |   |
| IM3\_CODE | Code critère 3 | Texte | 15 |   |   | Facultatif |   |
| IM4\_CODE | Code critère 4 | Texte | 15 |   |   | Facultatif |   |
| IM5\_CODE | Code critère 5 | Texte | 15 |   |   | Facultatif |   |
| IMO\_DTACQ | Date d'acquisition | Date |   |   |   | Facultatif |   |
| IMO\_DTSERV | Date de mise en service | Date |   |   |   | Facultatif |   |
| IMO\_REPRISE | Reprise d'immobilisation | Case à cocher |   |   |   | Facultatif |   |
| IMO\_PIEFRN | N° de pièce de l'acquisition | Texte | 15 |   |   | Facultatif |   |
| IMO\_PRXACH | Prix d'achat HT | Montant |   |   |   | Facultatif |   |
| IMO\_FRAISA | Frais inclus dans le prix d'achat HT | Montant |   |   |   | Facultatif |   |
| IMO\_TVAPXA | Montant de TVA sur le prix d'achat | Montant |   |   |   | Facultatif |   |
| IMO\_PRATTC | Prix d'achat TTC | Montant |   |   |   | Facultatif |   |
| IMO\_JRNACQ | Code journal d'acquisition | Texte | 10 |   |   | Facultatif |   |
| IMO\_CPT | Compte d'immobilisation | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTVAA | Compte de TVA sur les achats | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTFRN | Compte fournisseur | Texte | 25 |   |   | Facultatif |   |
| IMO\_MDAMO | Mode d'amortissement | Texte | 1 |  
L
D | Aucun
Linéaire
Dégressif | Facultatif |   |
| IMO\_BSEAMO | Base amortissable | Montant |   |   |   | Facultatif |   |
| IMO\_VALVTE | Valeur de revente | Montant |   |   |   | Facultatif |   |
| IMO\_DREAMO | Durée en mois de l'amortissement | Nombre entier |   |   |   | Facultatif |   |
| IMO\_NBJAMO | Nombre de jours dans une année pour l'amortissement | Texte | 3 | 360
365 | 360 jours
365 jours | Facultatif |   |
| IMO\_DTFINA | Date de fin d'amortissement | Date |   |   |   | Facultatif |   |
| IMO\_COAMDE | Coefficient d'amortissement dégressif | Nombre à virgule |   |   |   | Facultatif |   |
| IMO\_JRNDOT | Code journal de dotations aux amortissements | Texte | 10 |   |   | Facultatif |   |
| IMO\_CPTDAM | Compte de dotations aux amortissements | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTAM | Compte d'amortissement | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTDEP | Compte de dépréciation | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTDDE | Compte de dotations aux dépréciations | Texte | 25 |   |   | Facultatif |   |
| IMO\_TYPSOR | Type de cession | Texte | 1 |  
C
R | Aucun
Cession
Mise au rebut | Facultatif |   |
| IMO\_DTSOR | Date de cession | Date |   |   |   | Facultatif |   |
| IMO\_PIESOR | N° de pièce de la sortie | Texte | 15 |   |   | Facultatif |   |
| IMO\_PRXVTE | Prix de vente | Montant |   |   |   | Facultatif |   |
| IMO\_TVARVT | TVA de revente | Montant |   |   |   | Facultatif |   |
| IMO\_PVCCT | Plus-value de cession à court terme | Montant |   |   |   | Facultatif |   |
| IMO\_PVCLT | Plus-value de cession à long terme | Montant |   |   |   | Facultatif |   |
| IMO\_MVCCT | Moins-value de cession à court terme | Montant |   |   |   | Facultatif |   |
| IMO\_MVCLT | Moins-value de cession à long terme | Montant |   |   |   | Facultatif |   |
| IMO\_JRNCES | Code journal de cession | Texte | 10 |   |   | Facultatif |   |
| IMO\_CPTCES | Compte de cession | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTCRE | Compte de créance | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTVAV | Compte de TVA sur les ventes | Texte | 25 |   |   | Facultatif |   |
| IMO\_CPTVNC | Compte de valeur nette comptable | Texte | 25 |   |   | Facultatif |   |
| MVN\_CODE | Code modèle analytique | Texte | 15 |   |   | Facultatif |   |
| IMO\_MEMO | Commentaires | Texte illimité |   |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés |   |   |   |   | Facultatif |   |


