# Structure du fichier de comptes











| Nom | Description | Type | Longueur
maximale | Valeurs possibles | Présence | Exemple |
| CPT\_NUMERO | Numéro | Texte | 25 |   | Obligatoire | 70700202 |
| CPT\_LIB | Libellé | Texte | 60 |   | Obligatoire | Ventes de Produits Finis |
| PCF\_CODE | Code tiers | Texte | 20 |   | Obligatoire | 5100004 |
| CPT\_TYPE | Type de compte | Texte |   | G : Général
R : Regroupement
C : Client
F : Fournisseur | Obligatoire | G |
| CPT\_COLLEC | Numéro du compte collectif | Texte | 25 |   | Facultatif | 411000 |
| RPT\_COMPTE | Numéro de compte de reporting | Texte | 15 |   | Facultatif | 700 |
| DEV\_CODE | Code devise | Texte | 3 |   | Facultatif | EUR |
| CPT\_DEVOBG | Devise unique | Case à cocher |   | 0 : Non
1 : Oui | Facultatif | 0 |
| CPT\_GROUPE | Centralisé | Case à cocher |   | 0 : Non
1 : Oui | Facultatif | 0 |
| CPT\_ECH | Echéances | Case à cocher |   | 0 : Non
1 : Oui | Facultatif | 1 |
| CPT\_LET | Lettrable | Case à cocher |   | 0 : Non
1 : Oui | Facultatif | 1 |
| CPT\_SENS | Sens par défaut | Texte | 1 | D : Débit
C : Crédit | Facultatif | D |
| CPT\_ANA | Saisie de l’analytique | Texte | 1 | I : Interdit
O : Obligatoire
P : Possible | Facultatif | I |
| CPT\_QTE | Saisie de la quantité | Texte | 1 | I : Interdit
O : Obligatoire
P : Possible | Facultatif | I |
| CPT\_SAL | Saisie du salarié | Texte | 1 | I : Interdit
P : Possible | Facultatif | I |
| CPT\_TVA\_NC | Compte de TVA | Texte | 25 |   | Facultatif | 445660 |
| CPT\_TVA\_L1 | Code ventilation CA | Texte | 15 |   | Facultatif | 33 |
| CPT\_LIADEB | Code débit liasse fiscale | Texte | 3 |   | Facultatif | 101 |
| CPT\_LIACRE | Code crédit liasse fiscale | Texte | 3 |   | Facultatif | 202 |


 


Pour les comptes auxiliaires (Clients et Fournisseurs), vous avez 2 possibilités pour le code tiers (PCF\_CODE) en fonction de paramétrage de la génération du code tiers dans les préférences de gestion (en Gestion Commerciale) et dans les préférences de comptabilité (en Comptabilité).


 


En codification manuelle, le code tiers doit être obligatoirement indiqué dans le fichier d'import.


 


Dans les 2 autres modes de codification, il n'est pas obligatoire, par contre vous pouvez l'indiquer dans le fichier et sera donc repris.


