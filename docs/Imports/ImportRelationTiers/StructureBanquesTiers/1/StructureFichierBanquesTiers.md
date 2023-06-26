# Structure du fichier de banques de tiers

 












| Champ | Description | Type | Longueur maximale | Format | Présence | Exemple |
|---|---|---|---|---|---|---|
| PCF\_CODE | Code tiers | Texte | 20 |   | Obligatoire | 5100004 |
| RIB\_ORDRE | Numéro d’ordre | Texte | 2 |   | Obligatoire | 1 |
| RIB\_BQ\_NOM | Nom de la banque | Texte | 40 |   | Facultatif | CA |
| RIB\_BQ\_ADR | Adresse | Texte | 40 |   | Facultatif | Agence de la Gare |
| RIB\_BQ\_NUM | Numéro de RIB | Texte | 6 |   | Facultatif | 1 |
| RIB\_ASWIFT | BIC (SWIFT) | Texte | 20 |   | Facultatif | CAFRPP01 |
| RIB\_IBAN | Préfixe IBAN | Texte | 4 |   | Facultatif | FR76 |
| RIB\_TYPE | Type de coordonnées bancaires | Texte | 3 | Valeurs possibles : <br>GEN : Générique <br>DE : Allemagne <br>AD : Andorre <br>SA : Arabie saoudite <br>AT : Autriche <br>BE : Belgique <br>BA : Bosnie-Herzégovine <br>BR : Brésil <br>BG : Bulgarie <br>CA : Canada <br>RCB : Carte Bancaire <br>CCP : CCP <br>CN : Chine <br>CY : Chypre <br>HR : Croatie <br>DK : Danemark <br>ES : Espagne <br>EE : Estonie <br>US : États-Unis <br>FI : Finlande <br>FR : France <br>GI : Gibraltar <br>GR : Grèce <br>GL : Groenland <br>HU : Hongrie <br>FO : Îles Féroé <br>IE : Irlande <br>IS : Islande <br>IL : Israël <br>IT : Italie <br>LV : Lettonie <br>LI : Liechtenstein <br>LT : Lituanie <br>LU : Luxembourg <br> MK : Macédoine<br>MT : Malte <br>MA : Maroc <br>MC : Monaco <br>NO : Norvège <br>NL : Pays-Bas <br>PL : Pologne <br>PT : Portugal <br>CZ : République tchèque <br>RO : Roumanie <br>GB : Royaume-Uni <br>SM : Saint-Marin <br>RS : Serbie <br>SK : Slovaquie <br>SI : Slovénie <br>SE : Suède <br>CH : Suisse <br>DTA : Suisse DTA <br>LSV : Suisse LSV <br>TN : Tunisie <br>TR : Turquie <br>ZZZ : Autre<br> | Facultatif | FR |
| RIB\_AGENCE | Banque | Texte | 12 |   | Facultatif | 2 |
| RIB\_GUICHE | Agence | Texte | 12 |   | Facultatif | 1 |
| RIB\_COMPTE | Compte | Texte | 24 |   | Facultatif | 12345678901 |
| RIB\_CLE | Clé | Texte | 2 |   | Facultatif | 12 |
| RIB\_CB\_TYP | Type de carte bancaire | Texte |   |   | Facultatif | VIS |
| RIB\_CB\_DTF | Date d’expiration de la carte bancaire | Date |   | Format : JJ/MM/AAAA | Facultatif | 10/09/2018 |
| RIB\_TEXTE | Commentaire | Texte illimité |   |   | Facultatif |   |
| RIB\_RUM | Référence unique du mandat | Texte | 35 |   | Facultatif | BTCA22 |
| RIB\_DT\_SM | Date de signature du mandat | Date |   | Format : JJ/MM/AAAA | Facultatif | 10/09/2016 |
| RIB\_SEQPRE | Séquence de présentation | Texte | 4 | Valeurs possibles : <br>OOFF : Prélèvement unique <br>FRST : Premier prélèvement d'une série <br>RCUR : Prélèvement récurrent <br>FNAL : Dernier prélèvement d'une série | Facultatif |   |


