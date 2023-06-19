# Fichier CEGID Business Comptabilité 8 à largeur fixe
## Type de fichier


Fichier texte à largeur fixe.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures. Chaque ligne d'écriture 
 peut être suivie d'une ou plusieurs lignes d'analytique.


## Exemple de fichier


VTE09042015FC411000           X411C30 
           FAC15-00021 
                        DUBOIS 
                                09042015D 
             1394,64N 
        EUR1.00000000ED-             1394,64 
                           


VTE09042015FC4457220          X 
                 FAC15-00021 
                        DUBOIS 
                                        C 
              232,44N 
        EUR1.00000000ED-              232,44 
                           


VTE09042015FC707100           X 
                 FAC15-00021 
                        DUBOIS 
                                        C 
             1162,20N 
        EUR1.00000000ED-             1162,20 
                           


VTE09042015FC707100           AA1S3 
             FAC15-00021 
                        DUBOIS 
                                        C 
                0,00N 
        EUR1.00000000ED-                0,00 
                       S 
   


VTE09042015FC707100           AA2S3 
             FAC15-00021 
                        DUBOIS 
                                        C 
             1162,20N 
        EUR1.00000000ED-             1162,20 
                       S 
   


## Structure des lignes d'écritures









| Position | Champ | Type | Longueur |   |
| 1 | Code journal | Texte | 3 |   |
| 4 | Date de la ligne d'écriture | Date | 8 | Format : JJMMAAAA |
| 12 | Type de pièce |   | 2 | Valeurs possibles : 
 FC : Facture client 
 AC : Avoir client 
 FF : Facture fournisseur 
 AF : Avoir fournisseur |
| 14 | Numéro de compte comptable | Texte | 17 |   |
| 31 | Nature de la ligne : X | Texte | 1 | Valeurs possibles : 
 X : Auxiliaire 
 A : Analytique
H : Analytique + Général |
| 32 | Numéro de compte auxiliaire | Texte | 17 |   |
| 49 | Numéro de pièce | Texte | 35 |   |
| 84 | Libellé | Texte | 35 |   |
| 119 |   | Texte | 3 |   |
| 122 | Date d'échéance | Date | 8 | Format : JJMMAAAA |
| 130 | Sens | Texte | 1 | Valeurs possibles : 
 D : Débit 
 C : Crédit |
| 131 | Montant 1 | Montant | 20 | Séparateur décimal : Virgule |
| 151 | Type de ligne | Texte | 1 | Valeurs possibles : 
 S : Simulation 
 N : Normal |
| 152 |   | Texte | 8 |   |
| 160 | Code de la devise | Texte | 3 |   |
| 163 | Taux de la devise : 1.00000000 | Nombre à virgule | 10 |   |
| 173 | Codification des montants : ED- | Texte | 3 |   |
| 176 | Montant 2 | Montant | 20 | Séparateur décimal : Virgule |
| 196 |   | Montant | 20 |   |
| 216 |   | Texte | 3 |   |
| 219 | Code plan analytique | Texte | 2 |   |
| 221 |   | Texte | 2 |   |


## Structure des ventilations analytiques









| Position | Champ | Longueur | Type |   |
| 1 | Code journal | 3 | Texte |   |
| 4 | Date de la ligne d'écriture | 8 | Date | Format : JJMMAAAA |
| 12 | Type de pièce | 2 |   | Valeurs possibles : 
FC : Facture client 
AC : Avoir client 
FF : Facture fournisseur 
AF : Avoir fournisseur |
| 14 | Compte comptable | 17 | Texte |   |
| 31 | Nature de la ligne : A | 1 | Texte | Valeurs possibles : 
X = Auxiliaire 
A = Analytique
H = Analytique + Général |
| 32 | Code section analytique | 17 | Texte |   |
| 49 | Numéro de pièce | 35 | Texte |   |
| 84 | Libellé | 35 | Texte |   |
| 119 |   | 3 | Texte |   |
| 122 | Date d'échéance | 8 | Date | Format : JJMMAAAA |
| 130 | Sens | 1 | Texte | Valeurs possibles : 
D : Débit 
C : Crédit |
| 131 | Montant 1 | 20 | Montant | Séparateur décimal : Virgule |
| 151 | Type de ligne | 1 | Texte | Valeurs possibles : 
S : Simulation 
N : Normal |
| 152 |   | 8 | Texte |   |
| 160 | Code de la devise | 3 | Texte |   |
| 163 | Taux de la devise : 1.00000000 | 10 | Nombre à virgule |   |
| 173 | Codification des montants : ED- | 3 | Texte |   |
| 176 | Montant 2 | 20 | Montant | Séparateur décimal : Virgule |
| 196 |   | 20 | Montant |   |
| 216 |   | 3 | Texte |   |
| 219 | Code plan analytique | 2 | Texte |   |
| 221 |   | 2 | Texte |   |


