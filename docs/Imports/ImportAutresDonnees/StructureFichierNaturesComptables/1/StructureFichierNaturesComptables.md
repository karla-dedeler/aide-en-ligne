# Structure du fichier de natures comptables












| Champ | Description | Type | Longueur
maximale | Valeurs possibles | Description des valeurs possibles | Présence | Valeur par défaut | Exemple |
| NAT\_TABLE | Code de table d'origine | Texte | 3 | ART
FAR
FPT
SFA
SOC | Article
Famille d'article
Frais
Sous-famille d''article
Société | Facultatif | SOC |   |
| NAT\_TYPE | Type ou domaine | Texte | 1 | V
A | Ventes Achats | Obligatoire |   |   |
| NAT\_ORIGIN | Code de la table d'origine | Texte | 30 | Code article
Code famille d'articles
Code frais
Code sous-famille d'articles |   | Facultatif |   |   |
| NAT\_CODE | Code de nature comptable | Texte | 3 |   |   | Obligatoire |   |   |
| NAT\_LIB | Libellé | Texte | 40 |   |   | Facultatif |   |   |
| CPT\_NUMERO | Compte général | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_CPTREM | Compte d'escompte | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_CPTRRR | Compte de remise en pied de facture | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_CPT\_RG | Compte de retenue de garantie | Texte | 25 |   |   | Facultatif |   |   |
| ANA\_CODE | Code section analytique | Texte | 15 |   |   | Facultatif |   |   |
| JRN\_CODE | Code journal | Texte | 10 |   |   | Facultatif |   |   |
| NAT\_TVACPT | Compte de TVA | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_TVATX | Taux de TVA | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_TVATYP | Nature de TVA | Texte | 1 | E
D
F
R
1
2 | Encaissements
Débits
Facturation
Décaissements
Collectée non perçue
Débits non perçu | Facultatif |   |   |
| NAT\_DTTVA | Date de changement du taux de TVA | Date |   |   |   | Facultatif |   |   |
| NAT\_TXTVA | Ancien taux de TVA | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_TPF1TX | Taux de TPF 1 | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_TPF1SQ | Calcul de la base de la TPF 1 | Texte | 1 | V
N
Q
O
A
G
P
B
C
H
I
J
K
L
M | Valeur
Valeur nette
Qté
Qté\*$Coefficient1
Qté\*$Coefficient2
Qté\*$Coefficient1\*$Coefficient2
Qté\*Conditionnement\*$Coefficient1
Qté\*Conditionnement\*$Coefficient2
Qté\*Conditionnement\*$Coefficient1\*$Coefficient2
Qté\*Poids\*$Coefficient1
Qté\*Poids\*$Coefficient2
Qté\*Surface\*$Coefficient1
Qté\*Surface\*$Coefficient2
Qté\*Volume\*$Coefficient1
Qté\*Volume\*$Coefficient2 | Facultatif |   |   |
| NAT\_TPF1CT | Compte de TPF 1 | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_TPF1ED | Classification EDI de la TPF 1 | Texte | 15 |   |   | Facultatif |   |   |
| NAT\_TPF1XT | Taux de TVA sur TPF 1 | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_TPF1XC | Compte de TVA de TPF 1 | Texte | 25 |   |   |   |   |   |
| NAT\_TPF2TX | Taux de TPF 2 | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_TPF2SQ | Calcul de la base de la TPF 2 | Texte | 1 | V
N
Q
O
A
G
P
B
C
H
I
J
K
L
M | Valeur
Valeur nette
Qté
Qté\*$Coefficient1
Qté\*$Coefficient2
Qté\*$Coefficient1\*$Coefficient2
Qté\*Conditionnement\*$Coefficient1
Qté\*Conditionnement\*$Coefficient2
Qté\*Conditionnement\*$Coefficient1\*$Coefficient2
Qté\*Poids\*$Coefficient1
Qté\*Poids\*$Coefficient2
Qté\*Surface\*$Coefficient1
Qté\*Surface\*$Coefficient2
Qté\*Volume\*$Coefficient1
Qté\*Volume\*$Coefficient2 | Facultatif |   |   |
| NAT\_TPF2CT | Compte de TPF 2 | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_TPF2ED | Classification EDI de la TPF 2 | Texte | 15 |   |   | Facultatif |   |   |
| NAT\_TPF2XT | Taux de TVA sur TPF 2 | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_TPF2XC | Compte de TVA de TPF 2 | Texte | 25 |   |   | Facultatif |   |   |
| NAT\_DTTPF1 | Date de changement du taux de TPF 1 | Date |   |   |   | Facultatif |   |   |
| NAT\_TXTPF1 | Ancien taux de TPF 1 | Nombre à virgule |   |   |   | Facultatif |   |   |
| NAT\_DTTPF2 | Date de changement du taux de TPF 2 | Date |   |   |   | Facultatif |   |   |
| NAT\_TXTPF2 | Ancien taux de TPF 2 | Nombre à virgule |   |   |   | Facultatif |   |   |


