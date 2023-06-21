# Structure du fichier de banques de tiers

 












| Champ | Description | Type | Longueur
maximale | Format | Présence | Exemple |
| PCF\_CODE | Code tiers | Texte | 20 |   | Obligatoire | 5100004 |
| RIB\_ORDRE | Numéro d’ordre | Texte | 2 |   | Obligatoire | 1 |
| RIB\_BQ\_NOM | Nom de la banque | Texte | 40 |   | Facultatif | CA |
| RIB\_BQ\_ADR | Adresse | Texte | 40 |   | Facultatif | Agence de la Gare |
| RIB\_BQ\_NUM | Numéro de RIB | Texte | 6 |   | Facultatif | 1 |
| RIB\_ASWIFT | BIC (SWIFT) | Texte | 20 |   | Facultatif | CAFRPP01 |
| RIB\_IBAN | Préfixe IBAN | Texte | 4 |   | Facultatif | FR76 |
| RIB\_TYPE | Type de coordonnées bancaires | Texte | 3 | Valeurs possibles :
GEN : Générique
DE : Allemagne
AD : Andorre
SA : Arabie saoudite
AT : Autriche
BE : Belgique
BA : Bosnie-Herzégovine
BR : Brésil
BG : Bulgarie
CA : Canada
RCB : Carte Bancaire
CCP : CCP
CN : Chine
CY : Chypre
HR : Croatie
DK : Danemark
ES : Espagne
EE : Estonie
US : États-Unis
FI : Finlande
FR : France
GI : Gibraltar
GR : Grèce
GL : Groenland
HU : Hongrie
FO : Îles Féroé
IE : Irlande
IS : Islande
IL : Israël
IT : Italie
LV : Lettonie
LI : Liechtenstein
LT : Lituanie
LU : Luxembourg
MK : Macédoine
MT : Malte
MA : Maroc
MC : Monaco
NO : Norvège
NL : Pays-Bas
PL : Pologne
PT : Portugal
CZ : République tchèque
RO : Roumanie
GB : Royaume-Uni
SM : Saint-Marin
RS : Serbie
SK : Slovaquie
SI : Slovénie
SE : Suéde
CH : Suisse
DTA : Suisse DTA
LSV : Suisse LSV
TN : Tunisie
TR : Turquie
ZZZ : Autre | Facultatif | FR |
| RIB\_AGENCE | Banque | Texte | 12 |   | Facultatif | 2 |
| RIB\_GUICHE | Agence | Texte | 12 |   | Facultatif | 1 |
| RIB\_COMPTE | Compte | Texte | 24 |   | Facultatif | 12345678901 |
| RIB\_CLE | Clé | Texte | 2 |   | Facultatif | 12 |
| RIB\_CB\_TYP | Type de carte bancaire | Texte |   |   | Facultatif | VIS |
| RIB\_CB\_DTF | Date d’expiration de la carte bancaire | Date |   | Format : JJ/MM/AAAA | Facultatif | 10/09/2018 |
| RIB\_TEXTE | Commentaire | Texte illimité |   |   | Facultatif |   |
| RIB\_RUM | Référence unique du mandat | Texte | 35 |   | Facultatif | BTCA22 |
| RIB\_DT\_SM | Date de signature du mandat | Date |   | Format : JJ/MM/AAAA | Facultatif | 10/09/2016 |
| RIB\_SEQPRE | Séquence de présentation | Texte | 4 | Valeurs possibles :
OOFF : Prélèvement unique
FRST : Premier prélèvement d'une série
RCUR : Prélèvement récurrent
FNAL : Dernier prélèvement d'une série | Facultatif |   |


