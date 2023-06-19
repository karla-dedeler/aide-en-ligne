# Fichier QuadraCOMPTA à largeur fixe
## Type de fichier


Fichier texte à largeur fixe.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de 5 types de lignes ou enregistrements.


 


Chaque ligne commence par un caractère spécifique identifiant le type 
 de ligne ou enregistrement :


* C pour les comptes
* N pour les plans analytiques
* A pour les sections analytiques
* M pour les lignes d'écritures
* I pour les ventilations analytiques
* R pour les règlements


## Exemple de fichier


C01CLIENTClient1                       CLIENT10000000000000000000000000000000000000000000000000000411000 
                                                                                                                                    CNCA                            67890123451234567890111 
                                                                                                          France 
                                                 FR76 
             BTC


C01CLIENTClient1                       CLIENT10000000000000000000000000000000000000000000000000000411000 
                                                                                                                                    CNBNP                           67890123451234567890112 
                                                                                                          France 
                                                 FR76 
             BTC


C01CLIENTClient1                       CLIENT10000000000000000000000000000000000000000000000000000411000 
                                                                                                                                    CNLCL                           67890123451234567890113 
                                                                                                          France 
                                                 FR76 
             BTC


C01EXEMPLExemple1                      EXEMPLE0000000000000000000000000000000000000000000000000000411000 
  5 rue Cugnot                                                78120Rambouillet 
                                                      CNCA                            67890123451234567890112 
                                                                                                          France 
                                                 FR76AGRIFRPP78 
   BTC


C01EXEMPLExemple1                      EXEMPLE0000000000000000000000000000000000000000000000000000411000 
  5 rue Cugnot                                                78120Rambouillet 
                                                      CNBNP                           67890123451234567890112 
                                                                                                          France 
                                                 FR76BNPPFRPP75 
   BTC


C01EXEMPLExemple1                      EXEMPLE0000000000000000000000000000000000000000000000000000411000 
  5 rue Cugnot                                                78120Rambouillet 
                                                      CNLCL                           67890123451234567890112 
                                                                                                          France 
                                                 FR76LCLFFRPP92 
   BTC


M01C30   VT000090415 DUBOIS              D+000000139464411000 
  090415     FAC15                    FAC15-00 
   VTEN                                  FAC15-0002 
          +000000139464                                    08112019100837 
 


M4457220 VT000090415 DUBOIS              C+0000000232444457220 
            FAC15 
                    FAC15-00 
   VTEN                                  FAC15-0002 
          +000000023244                                    08112019100837 
 


M707100  VT000090415 DUBOIS              C+000000116220707100 
             FAC15 
                    FAC15-00 
   VTEN                                  FAC15-0002 
          +000000116220                                    08112019100837 
 


I   50+000000000000A1S3      S 
         


I   50+000000116220A2S3      S 
         


## Structure des comptes







| Position | Champ | Longueur |
| 1 | Type d'enregistrement : C | 1 |
| 2 | Numéro de compte | 8 |
| 10 | Libellé de compte | 30 |
| 40 | Clé alpha | 7 |
| 47 |   | 13 |
| 60 |   | 13 |
| 73 |   | 13 |
| 86 |   | 13 |
| 99 | Compte collectif | 8 |
| 107 | Rue 1 | 30 |
| 137 | Rue 2 | 30 |
| 167 | Ville | 30 |
| 197 | Téléphone | 20 |
| 217 | Flag "Mise à jour du compte si existant" | 1 |
| 218 | Type de compte | 1 |
| 219 | Compte à centraliser | 1 |
| 220 | Domiciliation bancaire | 30 |
| 250 | RIB | 30 |
| 280 | Mode de règlement sur 2 positions | 2 |
| 282 | Nombre de jours d'échéance | 2 |
| 284 | Terme échéance | 2 |
| 286 |   | 2 |
| 288 |   | 2 |
| 290 |   | 8 |
| 298 | Nombre de jours d'échéance | 3 |
| 301 |   | 1 |
| 302 | Fax | 20 |
| 322 | Mode de règlement sur 4 positions | 4 |
| 326 |   | 8 |
| 334 | SIRET | 14 |
| 348 |   | 1 |
| 349 |   | 30 |
| 379 | Pays | 50 |
| 429 |   | 3 |
| 432 |   | 1 |
| 433 |   | 1 |
| 434 | IBAN | 4 |
| 438 | BIC (SWIFT) | 11 |
| 449 |   | 2 |
| 451 | Numéro de mandate de prélèvement SEPA | 3 |


 


Les comptes ne seront exportés que s'ils ont été modifiés depuis le 
 dernier export.


## Structure des plans analytiques







| Position | Champ | Longueur |
| 1 | Type d'enregistrement : N | 1 |
| 2 | Code du plan analytique | 10 |
| 12 | Libellé du plan analytique | 30 |


 


Les plans analytiques ne seront exportés que s'ils ont été modifiés 
 depuis le dernier export.


## Structure des sections analytiques







| Position | Champ | Longueur |
| 1 | Type d'enregistrement : A | 1 |
| 2 | Code de la section analytique | 10 |
| 12 | Libellé du plan analytique | 30 |


 


Les sections analytiques ne seront exportées que si elles ont été modifiées 
 depuis le dernier export.


## Structure des lignes d'écritures







| Position | Champ | Longueur |
| 1 | Type d'enregistrement : M | 1 |
| 2 | Numéro de compte | 8 |
| 10 | Code journal | 2 |
| 12 | Folio | 3 |
| 15 | Date d'écriture au format JJMMAA | 6 |
| 21 | Code libellé | 1 |
| 22 | Libellé | 20 |
| 42 | Sens : D ou C | 1 |
| 43 | Montant | 13 |
| 56 | Compte de contrepartie | 8 |
| 64 | Date d'échéance au format JJMMAA | 6 |
| 70 |   | 2 |
| 72 |   | 3 |
| 75 | Numéro de pièce du document dans Gestimum | 5 |
| 80 |   | 10 |
| 90 |   | 10 |
| 100 | Numéro de pièce du document dans Gestimum | 8 |
| 108 | Code devise | 3 |
| 111 | Code journal | 3 |
| 114 | Code flag TVA | 1 |
| 115 |   | 1 |
| 116 |   | 1 |
| 117 |   | 30 |
| 147 |   | 2 |
| 149 | Numéro de pièce du document dans Gestimum | 10 |
| 159 | ? | 10 |
| 169 | Montant en devise | 13 |
| 182 |   | 12 |
| 194 |   | 10 |
| 204 |   | 10 |
| 214 |   | 4 |
| 218 | Date système | 14 |


## Structure des ventilations analytiques







| Position | Champ | Longueur |
| 1 | Type d'enregistrement : I | 1 |
| 2 | Pourcentage | 5 |
| 7 | Montant | 13 |
| 20 | Code de section analytique | 10 |
| 30 | Code de plan analytique | 10 |


## Structure des règlements







| Position | Champ | Longueur |
| 1 | Type d'enregistrement : R | 1 |
| 2 | Date d'échéance au format JJMMAA | 6 |
| 8 | Montant de l'échéance | 13 |
| 21 | Mode de règlement | 2 |
| 23 | Code journal de banque | 2 |
| 25 | Référence tiré | 10 |
| 35 | RIB tiré | 23 |
| 58 | Domiciliation bancaire | 20 |
| 78 | Code journal blanc | 3 |
| 81 | N° de compte d'origine | 8 |
| 89 | Mode de règlement | 4 |
| 93 | Bon à payer | 1 |
| 94 | IBAN | 4 |
| 98 | BIC | 11 |
| 109 | N° de mandat SEPA | 3 |


