# Structure du fichier de fournisseurs











| Champ | Description | Type | Longueur maximale | Valeurs possibles | Présence | Exemple |
|---|---|---|---|---|---|---|
| PCF\_CODE | Code fournisseur | Texte | 20 |   | Obligatoire |   |
| PCF\_RS | Raison sociale | Texte | 60 |   | Obligatoire |   |
| PCF\_CIVILE | Civilité | Texte | 25 |   | Facultatif |   |
| PCF\_DORT | En sommeil | Case à cocher |   |   | Facultatif |   |
| FAT\_CODE | Code famille | Texte | 10 |   | Facultatif |   |
| SFT\_CODE | Code sous-famille | Texte | 10 |   | Facultatif |   |
| PCF\_RS2 | Complément de raison sociale | Texte | 60 |   | Facultatif |   |
| PCF\_RUE | Rue (adresse de facturation) | Texte | 60 |   | Facultatif |   |
| PCF\_COMP | Complément de rue (adresse de facturation) | Texte | 60 |   | Facultatif |   |
| PCF\_ETAT | Etat (adresse de facturation) | Texte | 100 |   | Facultatif |   |
| PCF\_REG | Région (adresse de facturation) | Texte | 100 |   | Facultatif |   |
| PCF\_CP | Code postal (adresse de facturation) | Texte | 10 |   | Facultatif |   |
| PCF\_VILLE | Ville (adresse de facturation) | Texte | 200 |   | Facultatif |   |
| PAY\_CODE | Code pays (adresse de facturation) | Texte | 3 |   | Facultatif |   |
| PCF\_TEL1 | Téléphone 1 (adresse de facturation) | Texte | 20 |   | Facultatif |   |
| PCF\_TEL2 | Téléphone 2 (adresse de facturation) | Texte | 20 |   | Facultatif |   |
| PCF\_FAX | Fax (adresse de facturation) | Texte | 20 |   | Facultatif |   |
| PCF\_TELEX | Autre n° (adresse de facturation) | Texte | 10 |   | Facultatif |   |
| PCF\_EMAIL | Email (adresse de facturation) | Texte | 60 |   | Facultatif |   |
| PCF\_URL | Site web (adresse de facturation) | Texte | 128 |   | Facultatif |   |
| PCF\_ADRMEM | Commentaires (adresse de facturation) | Texte illimité |   |   | Facultatif |   |
| PCF\_NPAI | N'habite plus à l'adresse indiquée (adresse de facturation) | Case à cocher |   |   | Facultatif |   |
| PCF\_CBARAD | Code-barres (adresse de facturation) | Texte | 30 |   | Facultatif |   |
| PCF\_APE | APE (NAF) | Texte | 5 |   | Facultatif |   |
| PCF\_CMPAPE | Complément d'APE (NAF) | Texte | 100 |   | Facultatif |   |
| PCF\_STATUS | Statut | Texte | 15 |   | Facultatif |   |
| PCF\_INSC | Inscription | Texte | 15 |   | Facultatif |   |
| PCF\_SIRET | N° SIRET | Texte | 14 |   | Facultatif |   |
| PCF\_RCS | N° RCS | Texte | 200 |   | Facultatif |   |
| PCF\_SIREN | N° SIREN | Texte | 9 |   | Facultatif |   |
| PCF\_DATIMM | Date d'immatriculation | Date |   |   | Facultatif |   |
| PCF\_DATRAD | Date de radiation | Date |   |   | Facultatif |   |
| PCF\_NII | Numéro de TVA intracommunautaire | Texte | 14 |   | Facultatif |   |
| PCF\_ACCISE | N° d'accises | Texte | 15 |   | Facultatif |   |
| PCF\_CAPITA | Capital | Montant |   |   | Facultatif |   |
| PCF\_DATCLO | Date de clôture comptable | Date |   |   | Facultatif |   |
| PCF\_CASOC | Code chiffre d'affaires | Texte | 15 |   | Facultatif |   |
| PCF\_EFF | Code effectif | Texte | 15 |   | Facultatif |   |
| PCF\_EN\_TTC | Prix en TTC | Case à cocher |   |   | Facultatif |   |
| PCF\_BLOQUE | Bloqué | Case à cocher |   |   | Facultatif |   |
| PCF\_REMVAL | Taux de remise accordé | Nombre à virgule |   |   | Facultatif |   |
| PCF\_REMMIN | Remise accordée pour un minimum de | Montant |   |   | Facultatif |   |
| PCF\_TX\_RFA | Remise de fin d'année | Nombre à virgule |   |   | Facultatif |   |
| PCF\_TX\_ESC | Escompte | Nombre à virgule |   |   | Facultatif |   |
| REP\_CODE | Code commercial | Texte | 3 |   | Facultatif |   |
| SRV\_CODE | Code service | Texte | 3 |   | Facultatif |   |
| DIV\_CODE | Code division | Texte | 3 |   | Facultatif |   |
| DEP\_CODE | Code dépôt | Texte | 3 |   | Facultatif |   |
| PCF\_LANGUE | Code langue | Texte | 15 |   | Facultatif |   |
| PCF\_CBAR | Code-barres | Texte | 30 |   | Facultatif |   |
| FC1\_CODE | Code critère 1 | Texte | 15 |   | Facultatif |   |
| FC2\_CODE | Code critère 2 | Texte | 15 |   | Facultatif |   |
| FC3\_CODE | Code critère 3 | Texte | 15 |   | Facultatif |   |
| FC4\_CODE | Code critère 4 | Texte | 15 |   | Facultatif |   |
| FC5\_CODE | Code critère 5 | Texte | 15 |   | Facultatif |   |
| PCF\_URGENT | Priorité | Texte | 1 | 0 <br>1 <br>2 <br>3 <br>4 <br>5 <br>6 <br>7 <br>8 <br>9 | Facultatif |   |
| TAR\_CODE | Code grille de tarifs | Texte | 30 |   | Facultatif |   |
| PCF\_FPT\_01 | Code frais de port | Texte | 3 |   | Facultatif |   |
| PCF\_FPT\_02 | Code autres frais | Texte | 3 |   | Facultatif |   |
| PCF\_FPT\_03 | Code autres frais supplémentaires | Texte | 3 |   | Facultatif |   |
| PCF\_EDIIRC | Considérer le code-barres fourni lors de l'import EDI comme une référence client | Case à cocher |   |   | Facultatif |   |
| PCF\_EDICOM | Commentaires pour l'export EDI | Texte | 350 |   | Facultatif |   |
| PCF\_CHORUS | Exporter les factures vers la plateforme Chorus | Case à cocher |   |   | Facultatif |   |
| PCF\_CSCHRS | Code service destinataire Chorus | Texte | 100 |   | Facultatif |   |
| PCF\_NMCHRS | N° de marché Chorus | Texte | 50 |   | Facultatif |   |
| CPT\_NUMERO | N° de compte | Texte | 25 |   | Facultatif |   |
| NAT\_CODE | Code nature comptable | Texte | 3 |   | Facultatif |   |
| PCF\_PAYEUR | Code payeur | Texte | 20 |   | Facultatif |   |
| REG\_CODE | Code du mode de règlement | Texte | 8 |   | Facultatif |   |
| DEV\_CODE | Code devise | Texte | 3 |   | Facultatif |   |
| PCF\_TC\_DA | Document administratif pour les douanes | Texte | 3 |  
DSA <br>DAA | Facultatif |   |
| PCF\_REGBL | Règle de regroupement des bons de livraisons ou réceptions | Texte | 1 | T : Tous <br>1 : Un seul <br>C : Par commande <br>D : Par décade <br>M : Par mois | Facultatif |   |
| PCF\_PERIOD | Code périodicité de regroupement des bons de livraison | Texte | 15 |   | Facultatif |   |
| PCF\_EXCMDE | Nombre d'exemplaires d'impression pour les commandes | Texte | 1 |   | Facultatif |   |
| PCF\_EXBL | Nombre d'exemplaires d'impression pour les livraisons | Texte | 1 |   | Facultatif |   |
| PCF\_EXFACT | Nombre d'exemplaires d'impression pour les factures et avoirs | Texte | 1 |   | Facultatif |   |
| PCF\_FRAIS | Frais fourn. | Montant |   |   | Facultatif |   |
| PCF\_ENCMAX | Encours maximum | Montant |   |   | Facultatif |   |
| PCF\_ENCASS | Assurance crédit | Montant |   |   | Facultatif |   |
| PCF\_RISQUE | Risque | Texte | 15 |   | Facultatif |   |
| PCF\_MT\_REL | Seuil de relance | Montant |   |   | Facultatif |   |
| PCF\_MEMO | Commentaires | Texte illimité |   |   | Facultatif |   |
| PCF\_AFFMES | Afficher un message lors de la saisie d'un achat ou d'une vente | Case à cocher |   |   | Facultatif |   |
| PCF\_MESSAG | Message | Texte illimité |   |   | Facultatif |   |
| PCF\_HAUSSE | Hausse | Nombre à virgule |   |   | Facultatif |   |
| XXX\_... | Champs personnalisés |   |   |   | Facultatif |   |


