# Structure du fichier de documents de stock










| Champ | Description | Type | Longueur maximale | Valeurs possibles | Présence | Valeur par défaut |
| --- | --- | --- | --- | --- | --- | --- |
| DOC_STYPE | Sous-type de document de stock | Texte | 1 | E = Entrée de stock <br> S = Sortie de stock <br> T = Transfert de stock <br> O = Assemblage de nomenclatures <br> M = Écart de stock <br> X = Sortie pour perte | Obligatoire |  |
| DEP_CODE | Code dépôt | Texte | 3 |  | Facultatif | Code dépôt des préférences |
| DOC_TDEPOT | Code dépôt de destination de transfert | Texte | 3 |  | Facultatif |  |
| DOC_DATE | Date au format JJ/MM/AAAA | Date |  |  | Facultatif | Date du jour |
| PCF_CODE | Code tiers | Texte | 20 |  | Facultatif |  |
| DOC_REFPCF | Référence | Texte | 100 |  | Facultatif |  |
| PRJ_CODE | Code affaire | Texte | 40 |  | Facultatif |  |
| DOC_MEMO | Commentaires | Texte illimité |  |  | Facultatif |  |
| XXX_... | Champs personnalisés des documents de stock |  |  |  | Facultatif |  |
| ART_CODE | Code article | Texte | 30 |  | Obligatoire |  |
| ART_GAMME | Codes des valeurs de gammes séparés par un \ | Texte | 98 |  | Facultatif |  |
| MVT_NUMLOT | N° de lot | Texte | 25 |  | Facultatif |  |
| MVT_DT_FAB | Date de fabrication du lot | Date |  |  | Facultatif |  |
| MVT_DT_PER | Date de péremption du lot | Date |  |  | Facultatif |  |
| MVT_ZONE | Zone de stockage | Texte | 100 |  | Facultatif |  |
| MVT_QTE | Quantité | Nombre à virgule |  |  | Obligatoire |  |
| MVT_TALTER | Code du type d'écart | Texte | 15 |  | Facultatif |  |
| MVT_TPERTE | Code du type de perte | Texte | 15 |  | Facultatif |  |
| MVT_LIB | Libellé du mouvement | Texte | 40 |  | Facultatif |  |
| MVT_PACH | Prix unitaire | Montant |  |  | Facultatif |  |
| MVT_IMPAFE | Charge dans le tableau de bord de l'affaire | Case à cocher |  |  | Facultatif |  |
| MVT_IMPAFS | Produit dans le tableau de bord de l'affaire | Case à cocher |  |  | Facultatif |  |
| XXX_... | Champs personnalisés des lignes de documents de stock |  |  |  | Facultatif |  |