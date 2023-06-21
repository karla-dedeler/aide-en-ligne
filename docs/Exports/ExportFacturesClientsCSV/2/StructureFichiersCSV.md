# Structure des fichiers CSV générés
4 fichiers sont créés :


* Documents
* Lignes
* Échéances
* Règlements


## Documents


Ce fichier contient les colonnes suivantes : 


NumeroPiece(DOC\_PIECE);Date(DOC\_DATE);MontantTTC(DOC\_MT\_TTC)


## Lignes


Ce fichier contient les colonnes suivantes :


NumeroPiece(DOC\_PIECE);CodeArticle(ART\_CODE);Libelle(LIG\_LIB);Quantite(LIG\_QTE);PrixUnitaire(LIG\_P\_NET);TotalHT(LIG\_TOTAL);TauxTVA(NAT\_TVATX)


## Échéances


Ce fichier contient les colonnes suivantes :


NumeroPiece(DOC\_PIECE);Date(ECH\_DATE);ModeReglement(REG\_CODE);ARecevoir(ECH\_ARECEV);APayer(ECH\_APAYER)


## Règlements


Ce fichier contient les colonnes suivantes :


NumeroPiece(DOC\_PIECE);Date(REG\_DATE);TypeReglement(REG\_TYPE);Recu(REG\_RECU);Paye(REG\_DONNEE)


