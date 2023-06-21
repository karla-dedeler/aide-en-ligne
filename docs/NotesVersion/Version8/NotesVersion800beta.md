# Version 8.0.0 build 818 bêta du 07/12/2018
 


#### OPTIMISATION DE LA BASE DE DONNÉES


`#23377` - Mise en place de nouveaux 
 indexes, afin d'optimiser la base de donnée en lecture.


`#20327` - Ajout de la suppression 
 des tables "OLD\_" (créées par la migration) dans la fonction 
 de maintenance de base de donnée "Compacter/Optimiser".


`#23183` - Ajout d'une dé fragmentation 
 des indexes dans la fonction de maintenance de base de données "Compacter/Optimiser".


#### OUVERTURE DE SOCIÉTÉ & MIGRATION


`#23173` - Correction de la violation d'accès lors de la migration d'une 
 base de données de version <= 1207, sur l'ajout de 2 taxes parafiscales.


`#23174` - Correction de la violation d'accès lors de la migration en 
 ajoutant des états d'actions dans les tables de références.


`#23380` - Mise en place d'un message 
 d’alerte lorsque la taille de la base de donnée Sql Server 2017 Express 
 approche 90% de la taille limite.


`#24288` - Mise en place d'un contrôle 
 de la taille de la base de données avant migration en version Sql Express.


#### LOI ANTI-FRAUDE TVA


`#23762` - La progression du calcul 
 des clés d'inaltérabilité s'affiche dans la barre d'état lors d'une montée 
 de version.


`#23763` - Le calcul des clés d'inaltérabilité 
 lors d'une montée de version ne s'effectue qu'à partir du 01/01/2018.


`#24014` - Toutes les modifications 
 d'échéances sont historisées dans l'ERP.


#### ACHAT ET VENTE


`#20447` 
 - Ajout d'un contrôle dans la sélection des N° de séries après changement 
 d'affectation dans les documents de ventes.


`#20524` - Les quantité 
 livrées et les reliquats sont repris correctement, lors du regroupement 
 de commandes ayant un statut transfert partiellement.


`#21136` 
 - Optimisation du temps de traitement du ré-ordonnancement des lignes 
 d'un document d'achat / vente.


`#22407` - Mise en place d'un message 
 d'alerte, avant chaque demande d'envoi par email via Outlook, dans le 
 cas où la clé de registre "MAPI" avec la valeur "1", 
 n'est pas présente dans HKEY\_LOCAL\_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows 
 Messaging Subsystem, quand l'ERP tourne sous Windows 64 bits.


`#22860` - La duplication 
 en devis, d'un devis contenant des codes articles inexistant, est possible 
 avec l'option "contrôler la référence article dans le devis" 
 décochée.


`#22946` - Modification 
 des tests sur l'état du document dans les impressions d'historique des 
 achats et ventes.


`#23072` - Il est possible 
 de transférer les documents contenant des lignes avec des quantités à 
 0.


`#23092` - Les numéros 
 de série sont repris lors de la duplication d'un bon de retour en Bon 
 de Livraison.


`#23110` - Correction 
 du calcul des colonnes "Base" dans les modèles d'impressions 
 de journaux de vente dans le cas où l'option 'TTC' est activée dans les 
 documents.


`#23178` - Le transfert 
 d'un Bon de retour en Avoir n'est plus proposé, si l'utilisateur n'a pas 
 le droit de créer des documents de type avoir.


`#23404` - A l'affectation 
 d'un nouveau numéro de lot lors du transfert d'une commande d'achat en 
 bon de réception, sur un article gérés en lot avec conditionnement, la 
 quantité de la ligne n'est plus multipliée par son conditionnement.


`#23450` - Le transfert 
 de bon de retour antérieur à l'inventaire, en avoir, ne crée plus un autre 
 mouvement dans le stock.


`#23505` - Le stock 
 à terme à ligne de document et dans le volet d'information contextuel 
 n'est plus doublé lors de la saisie d'une commande.


`#23517` - Correction 
 du calcul de la différence dans l'échéancier des documents d'achats et 
 avoirs clients, lorsqu'il y a des échéances payées.


`#23576` - Les documents 
 d'achat / vente mouvementant le stock (BL, facture, bon de retour, avoir) 
 contenant une nomenclature gérée en stock n'impactent plus le stock de 
 ses composants gérés en stock.


`#23635` - Correction 
 du regroupement de bons de réceptions fournisseurs.


`#23827` - Correction 
 du message d'erreur "stock insuffisant..." lors du transfert 
 de devis en Bon de Livraison, contenant une quantités négatives sur un 
 article non géré en stock.


`#23929` - La valorisation 
 du stock FIFO lors du transfert de BL/BR en Facture avec un article en 
 FIFO sans n° de lot se fait correctement.


`#24089` - L'archivage 
 via le menu contextuel de la liste des documents de ventes et d'achats 
 tient compte du paramétrage de droits utilisateurs dans Administration 
 / Archives.


`#24191` - La génération 
 de la facture suite au transfert d'un BL contenant au moins 2 articles 
 composés non gérés en stock, contenant des composants mouvementés sur 
 plusieurs dépôts et au moins 1 composant commun mouvementé sur un dépôt 
 unique n'est plus abandonnée.


`#24254` - Correction 
 de l'erreur à l'ouverture de la fenêtre de sélection des adresses dans 
 les documents.


`#24378` 
 - Les notions de Commercial et Division, sont maintenant disponibles dans 
 les documents d'achat / vente, les listes des documents d'achat / vente, 
 le regroupement automatique des bon de réceptions et retours fournisseurs, 
 le transfert automatique des commandes clients, le regroupement automatique 
 des bons de livraisons et de retours clients.


`#24428` 
 - Ajout dans l'onglet 'Autre' des documents d'achats et de ventes, de 
 la date de création, la date de modification, l'utilisateur ayant créé 
 le document, l'utilisateur ayant effectué la dernière modification du 
 document.


`#24432` 
 - Le transfert partiel d'une commande en Bon de livraison interdit, si 
 un acompte a été saisi sur la commande.


`#24440` - Mise à jour 
 de la requête SQL du modèle "Évolution chiffre d'affaires HT par 
 articles et par clients".


`#24441` - Mise à jour 
 de la requête SQL du modèle "Évolution chiffre d'affaires HT par 
 clients et par articles".


`#24442` - Mise à jour 
 de la requête SQL dans le modèle "Journal par famille clients".


`#24444` - Mise à jour 
 de la requête SQL dans le modèle "Journal par représentants lie au 
 document avec origine".


#### ACTIONS


`#23586` - Lors 
 de la duplication d'une action, la date de début est actualisée avec la 
 date du jour.


`#23744` - La création d'une action depuis 
 la fenêtre d'impression des documents remonte l'affaire du document dans 
 l'action.


`#24787` - Ajout de 2 boutons dans les 
 actions permettant d'accéder  à la fiche du contact et à la fiche 
 du tiers.


#### ARTICLES


`#23069` - Les 
 articles non gérés en stock ne remontent pas dans la sélection avancée 
 des articles de la fenêtre de mise à jour des tarifs articles.


`#23121` 
 - La valorisation du prix de revient de l'onglet général avec calcul du 
 prix de revient dans tous les dépôts s'alimente correctement.


`#23289` 
 - Correction du message d'erreur à la saisie d'un tiers dans l'onglet 
 client d'un article gammé, si la gamme n'a qu'une composante.


`#23898` - Il n'est plus possible de 
 créer un article non géré en stock, avec un n° de lot ou un n° de série.


`#23993` - La modification du code article 
 via ARTICLE / Modifier un code article alimente les colonnes "Modifié 
 le" et "Modifié par".


`#24430` - Ajout dans l'onglet 'Infos' 
 de l'article, de la date et l'utilisateur ayant effectué la dernière modification.


#### ASSEMBLAGE


`#23854` 
 - Correction du message "Champ 'ART\_AFFMES' non trouvé lors de l'ajout 
 d'un composant avec le même dépôt via un clic droit dans un document d'assemblage.


`#23948` 
 - La fenêtre de sélection de numéro de lot et de gamme ne s'ouvre plus 
 lors de la modification des composants simples dans les assemblages.


`#24622` 
 - Ajout des boutons 'OK' et 'Annuler' en bas à droite de la fenêtre d'assemblage 
 de nomenclature générée depuis une commande client.


#### BANQUES


`#22704` - Redéfinission 
 des formats de coordonnées bancaires dans l'onglet banque des tiers pour 
 l’Irlande, Malte, la Norvège et la Suède.


`#22705` - Redéfinission 
 du format de coordonnées bancaires dans l'onglet banque des tiers pour 
 le Danemark.


`#22706` 
 - Ajout de 15 formats de coordonnées bancaires dans l'onglet banque des 
 tiers : Arabie saoudite, Bosnie-Herzégovine, Brésil, Croatie, Îles Féroé, 
 Gibraltar, Groenland, Islande, Israël, Liechtenstein, Macédoine, Monaco, 
 Saint-Marin, Serbie, Turquie.


`#22917` 
 - On ne tient pas compte des espaces, lors d'un copier / coller ou une 
 saisie, dans la zone IBAN avec le type "Générique".


`#23200` 
 - Renommage du type de coordonnée bancaire "Grande Bretagne" 
 en "Royaume-uni".


`#23246` - Redéfinition 
 des formats de coordonnées bancaires dans l'onglet banque des tiers pour 
 l’Italie et Saint-Martin.


#### CHAMPS PERSONNALISÉS


`#24336` - Ajout d'un champs de type 
 'espacement' dans les champs personnalisés permettant d'effectuer une 
 séparation sans afficher de trait.


`#23620` 
 - Correction du message "Nom de colonne non valide" en boucle 
 après avoir renommé un champ personnalisé sur lequel on a un filtre personnalisé.


#### COMMERCIAUX ET BAREME


`#23546` - Correction 
 du calcul des commissions des commerciaux sur les échéances.


#### CONTACT


`#20492` - Ajout d'une zone numéro de 
 domicile dans la fiche contact.


`#20494` - Ajout des informations "Modifié 
 le" et "Modifié par" dans l'onglet général de la fiche 
 contact.


`#20495` - Ajout de l'option "Afficher 
 les éléments en sommeil" dans le menu contextuel de l'onglet contact 
 de la fiche tiers.


`#24338` 
 - Correction de la violation d'accès dans l'import des contacts et des 
 grilles de tarifs.


#### DÉPÔTS


`#18642` - Correction 
 du message "Indice de tableau de variants hors limites" en sélectionnant 
 un dépôt avec plus de 50 dépôts cochés dans le salarié et l'option de 
 mise en mémoire cochée.


#### ENCAISSEMENTS ET DECAISSEMENTS


`#21929` 
 – Le document à l'origine de l'échéance, est accessible depuis l'échéancier 
 clients/fournisseurs via à clic droit sur la ligne souhaitée.


`#23773` - Correction 
 du remplissage avec des 0 des champs Compte, Banque et Agence lors du 
 règlement & paiement des échéances dans Encaissement / Décaissement.


`#23790` - La liste 
 des paiements préparés est exportable au format Microsoft Excel depuis 
 la fenêtre 'Préparer les paiements'.


`#24570` 
 - Mise à jour du modèle de lettre traite utilisable depuis le menu Impressions/Encaissements/Règlements 
 reçus.


`#24574` 
 - Mise à jour modèle de lettre traite utilisable depuis le menu Impressions/Encaissements/Portefeuille 
 des effets.


#### ERGONOMIE


`#24294` 
 - Ajout d'un style "Gestimum blanc et gris" dans les paramétrages 
 d'affichage.


`#24323` 
 - Ajout de fonctionnalité dans le menu nouveau, permettant de créer des 
 documents de vente / achat, tiers, contact, action, affaire et article.


`#24738` 
 - Ajouter d'un bouton "Stat. vente" dans la barre d'outils de 
 'Données' en Gestion Commerciale.


#### EXPORT EXCEL


`#22295` 
 - Les commentaires dans les grilles sont exportables sous Excel.


#### GAMMES


`#23338` 
 - La sélection de gammes dans les documents via "sélectionner à partir 
 du stock" remonte bien le tarif associé.


#### GEOLOCALISATION


`#22425` - Mise sous option du géocodage 
 automatique des adresses. Par défaut cette option est désactivée lors 
 de la migration. Pour l'activer se rendre dans les Préférences de gestion, 
 Onglet Tiers.


#### IMPORTS


`#20444` - Lors de l'import d'achat vente, la remontée d'une ligne en 
 erreur n'empêche pas la création du document précédent cette ligne.


`#21804` - Le champ LIG\_P\_PRV 'Prix 
 de revient unitaire' est importable dans les lignes de documents.


`#23990` - Correction du message "Il existe déjà une fiche ayant 
 ce code" lors de l'import des équivalences d'articles.


#### MODES DE RÈGLEMENTS


`#23310` - Il est possible de 
 créer un mode de règlement contenant un type de règlement sans type de 
 remise.


#### PORTEFEUILLE DES COMMANDES


`#15750` - Ajout de la colonne "Affaire 
 à la ligne" dans les portefeuilles de commandes achats et ventes.


#### STOCKS


`#22515` - Le calcul du stock dans les lignes de mouvement de stock s'effectue 
 correctement, lorsqu'un article est présent plusieurs fois dans un BL 
 transféré en facture.


`#23368` - Le code-barres du lot peut contenir jusqu'à 30 caractères.


`#23398` - Correction du message "Paramètre pDepCode non trouvé" 
 lors de la poursuite de la validation d'un inventaire.


`#23513` - Correction du message d'erreur "Champ 'DOC\_MT\_TTC' non 
 trouvé" lors de la suppression d'un document de stock.


`#23524` - Lors d'un transfert de stock, la valorisation de départ de 
 l'article est bien reprise dans le dépôt de destination.


`#23761` - Mise en place d'un message d'alerte lorsque l'on essaie de 
 créer une action à l'impression d'un document de stock alors que le code 
 tiers ou le numéro de contact ou le code affaire de la pièce est manquant.


`#23792` - Lors de l'ajout d'un nouvel article dans un document d'entrée 
 existant, le prix unitaire de ce nouvel article est bien remonté dans 
 le document.


`#24002` - Le stock à terme à la ligne de document dans un Bon de livraison 
 client, tient compte des quantités saisies dans la première ligne d'article.


`#24162` - Ajout d'un contrôle sur le stock lorsque l'on transfert une 
 facture d'achat en avoir d'achat.


`#24726` - Correction du message d'erreur généré lors de l'affectation 
 automatique par code ou par date des numéros de série dans les documents 
 achats / ventes.


#### TARIFS & PROMOTIONS


`#24533` - Suppression du bouton "Recopier" dans les grilles 
 de tarifs.


#### TRANSFERT COMPTABLE


`#22863` - Ajout du code postal du 
 tiers dans le fichier d'export au format QuadraCompta.


`#24074` - Remplacement des '...' 
 présents dans le numéro de pièce de l'écriture d'une remise en portefeuille 
 des effets contenant plusieurs factures réglées pour un même tiers, par 
 le numéro de la remise en portefeuille.


#### TIERS


`#19311` - Le Pays et le Code-barres du tiers sont repris dans l'adresse 
 des contacts.


`#20728` - Les commentaires des adresses du tiers sont conservés lorsque 
 l'on modifie la fiche du compte tiers en Comptabilité.


`#23109` - Mise en place d'une option "Étendre aux contacts" 
 dans la recherche de tiers permettant de rechercher un tiers par le contact.


`#23687` - Correction des filtres dans le modèle d'étiquettes de Tiers 
 en Report Builder.


`#24161` - Le code affaire de l'action remonte dans la liste des actions 
 du tiers et dans la liste des actions du contact.


#### UTILISATEURS


`#24035` 
 - Mise en place d'une option 'Web service et Tâches en ligne de commande 
 uniquement' dans les droits utilisateurs. Cette option empêche la connexion 
 de l'utilisateur aux écrans Gestimum ERP.


#### AFFAIRES


`#17060` 
 - Les documents de type devis et demande de prix, remontent dans l'onglet 
 "Réalisé" de l'affaire.


`#19061` 
 - Lors de l'ajout les lignes d'un document dans le budgété de l'affaire, 
 les lignes de texte sont ignorées.


`#21180` 
 - Il est possible d'ajouter les lignes d'un document ou le pied d'un document 
 dans le Budgété Achats des Affaires 


`#21910` - "Ajouter le pied d'un document" 
 dans le budgété ventes de l'affaire renseigne le libellé du document ainsi 
 que le montant HT.


`#23337` 
 - Il est possible d'ajouter les lignes d'un document contenant des lignes 
 de texte vides, dans le budget des affaires en achat et en vente.


`#23705` - Suppression du contrôle sur le 
 champs DOC\_NUMERO lors de l'intégration de lignes dans le budgété des 
 affaires.


`#24786` 
 - Ajout d'un bouton permettant d'accéder à la fiche du tiers depuis l'affaire.


#### CONNECTEUR PRESTASHOP


`#23113` 
 - Lors de la synchronisation des commandes PrestaShop, on affiche 'Synchronisation 
 PrestaShop', dans le champs 'Traitement ayant créé le document' dans la 
 liste des documents.


#### EDI


`#24211` - Ajout du champs ADR\_SIRET dans les différents imports EDI.


`#24209` - Correction de l'import d'ORDERS au format LogisEDICOT.


#### EDI CHORUS


`#21860` 
 - Mise en place d'un champ SIRET à l'adresse de livraison dans les tiers.


`#22196` 
 - Mise en place d’un contrôle, lors de l’export au format Chorus, sur 
 les éléments renseignés dans l’adresse de livraison du document


`#24513` 
 - Les lignes de document de type texte sont reprises dans le fichier d'export 
 au format CHORUS.


`#24532` 
 - Les conditions de pénalités présentes dans les Préférences de Gestion 
 onglet 'Modèles' sont reprises dans l'export au format Chorus.


#### G-CHANGE


`#21645` - Import des équivalences d'articles, tarifs fournisseurs, références 
 clients, composants de nomenclature par tâche en ligne de commande.


`#21531` - Impression de documents d'achat, 
 vente et stock par tâche en ligne de commande


`#22510` 
 - Ajout des champs personnalisés dans l'import de compte, via Outils/import, 
 tâche en ligne de commande et WebService.


`#22670` 
 - Import des utilisateurs par tâche en ligne de commande.


`#23346` 
 - Implémentation d’un paramètre « statistiques » dans toutes les tâches 
 en ligne de commande d’import.


`#24462` - Le transfert d'un Accusé de Réception 
 en Bon de Livraison via la tâche ligne de commande ne crée plus une seconde 
 échéance.


`#24538` 
 - Mise en place du champs ECH\_NUOREX 'N° d'origine externe' à la ligne 
 d'échéance sur les écritures permettant de stocker le n° d'échéance d'origine 
 d'une application tierce. C'est un champs de type chaîne de caractères 
 limité à 10 caractères, pouvant être renseigné via le web service, les 
 tâches en ligne de commande et l'import.


#### ANALYTIQUE


`#24113` - Les pourcentages de la répartition 
 analytique paramétrée dans le compte est bien appliqué dans les lignes 
 d'écritures.


`#24731` - La répartition analytique paramétrée 
 dans le compte est bien appliquée dans les lignes d'écritures sur chacun 
 des plans pré définis. 


#### CLÔTURE & VALIDATION


`#22878` - Lors de la clôture comptable, 
 le champs date d'émission 'ECH\_DTEMIS' n'est plus modifié pour être remplacé 
 par la date du premier jour du nouvel exercice.


#### DÉCLARATION DE TVA


`#24485` - Mise à jour des fichiers CA3 France.TVARegroupements 
 et CA3 France.TVALignes utilisés dans le paramétrage de la déclaration 
 de TVA avancée.


#### ÉCRITURES


`#18245` - Correction de l'erreur 'Paramètre 
 ECR\_DT\_CRE non trouvé' dans la recherche d'écritures par date de création.


`#21411` - Ajout de contrôle lors du transfert 
 comptable de documents émis en devises différentes que la devise du dossier 
 évitant que l'écriture soit considérée comme déséquilibrée lors de la 
 clôture si elle est équilibrée en devise mais pas en conversion euro / 
 local.


`#22477` 
 - Mise en place dans les préférences de comptabilité/onglet Fiscalité 
 de 2 options:  rendre obligatoire la saisie du n° de pièce et/ou 
 du libellé dans les écritures comptables.


`#22560` 
 - A l'ouverture d'un journal de saisie,  un message indique à l'utilisateur 
 si le journal est déjà verrouillé par un autre utilisateur.


`#22813` - On ne peut plus supprimer des 
 écritures lettrées ou issues des règlements, via le menu de recherche 
 des écritures.


`#22830` - Correction du message "La 
 date doit être dans la période en cours de saisie au kilomètre !" 
 lors de la sélection d'un guide d'écriture en saisie des écritures au 
 kilomètre, par clic droit, alors que les dates sélectionnées sont cohérentes.


`#23070` - Les filtres sur les écritures 
 dans la fenêtre de recherche d'écritures s'enregistrent correctement et 
 sont pris en compte lors de la recherche.


`#23278` 
 - Les champs ECR\_PIECE2 & ECR\_REFERE sont affichables dans : l'extrait 
 de compte, l'extrait de comptes simplifiés, l'extrait de compte par échéance, 
 l'échéancier clients et l'échéancier fournisseurs


`#23584` - La contre-passation d'une écriture 
 crée bien une nouvelle échéance associée.


`#23597` 
 - Mise en place d'un contrôle de cohérence dans l'import d'écritures, 
 entre le montant de la ligne d'écriture et les échéances qui y sont rattachées. 
 En cas d'erreur, l'écriture sera rejetée.


`#23603` 
 - Mise en place d'un contrôle de cohérence dans l'import d'écritures, 
 entre le montant de la ligne d'écriture et la répartition analytique qui 
 y est rattachée. En cas d'erreur, l'écriture sera rejetée.


`#23617` - L'échéance s'actualise correctement 
 dans l'échéancier lors d'une modification de l'écriture comptable.


`#23731` - Dans la saisie d'écriture, la 
 modification d'un compte rattaché à une échéance, ne crée plus d'échéance 
 en double.


`#23995` 
 - Intégration d'un numéro de pièce sur les écritures automatiques générées 
 par l'ERP (OD écart de règlement, écart de conversion, etc....) à condition 
 que le journal de saisie ait un paramétrage de numérotation de pièces 
 Continue ou Périodique.


`#23996` 
 - Les chaînes de caractère sont nettoyées lors de l'export du fichier 
 FEC afin d'exclure les tabulations, retours lignes et espaces insécables, 
 interprétés pas l'outil de contrôle des fichiers de l'administration fiscale, 
 comme un séparateur de colonne rendant la structure non conforme.


`#24025` 
 - Mise en place d'un champ de type date dans la table des écritures permettant 
 de saisir la date d'origine du document lorsqu'il ne peut être saisi sur 
 sa période d'origine.


`#24114` - La numérotation "Continue" 
 et la numérotation "Périodique" paramétrable dans le journal 
 s'initialise dès la première ligne d'écriture.


`#24431` 
 - Activation par défaut des options rendant obligatoires le numéro de 
 pièce et le libellé dans les écritures comptables. (Préférences de comptabilité, 
 onglet Fiscalité)


`#24689` - Le numéro interne d'échéance dans 
 l'échéancier de l'écriture et des documents d'achat / vente n'est plus 
 saisissable.


`#24690` 
 - La suppression d'une ligne d'écriture comptable rattachée à une échéance 
 soldée n'est plus autorisée.


#### ENCAISSEMENTS ET DÉCAISSEMENTS


`#21929` 
 - L'écriture comptable à l'origine de l'échéance, est accessible depuis 
 l'échéancier clients/fournisseurs via à clic droit sur la ligne souhaitée.


`#23624` 
 - Les champs ECR\_PIECE2 & ECR\_REFERE peuvent être affichés dans les 
 grilles d'échéanciers.


`#23994` 
 - Remplacement des '...' présents dans le numéro de pièce de l'écriture 
 d'une remise en banque contenant plusieurs factures réglées pour un même 
 tiers, par le numéro de la remise en banque.


#### ERGONOMIE


`#24457` 
 - Ajout de fonctionnalité dans le menu nouveau, permettant de créer comptes 
 généraux, fournisseurs et clients.


`#24739` 
 - Ajouter de 2 boutons  "Ech. clients" et "Ech. fourniss." 
 dans la barre d'outils de 'Données'.


`#24740` - Ajouter d'un bouton "S.I.G." 
 dans la barre d'outils de 'Données'.


#### EXPORT DES ÉCRITURES COMPTABLES (FEC)


`#23999` - 
 Mise en place d'un outil de pré-contrôle du fichier des écritures comptables 
 (FEC) disponible depuis le menu Outils / Exporter / Écritures pour l'administration 
 fiscale / "Contrôler". Cet outil vérifie les points suivants 
 : présence du n° de pièce sur les écritures (champ PIECEREF => ECR\_NUMERO) 
 ; présence du libellé dans les écritures (champ ECRITURELIB => ECR\_LIB) 
 ; le numéro de compte comptable doit commencer par trois chiffres(champ 
 COMPTENUM => ECR\_COMPTE).


`#24156` - 
 Mise à jour de la requête de génération du Fichier des Écritures Comptables 
 (FEC).


#### IMPORT DES ÉCRITURES COMPTABLES


`#22642` - Le fichier d'import n'est pas renommé si l'import en ligne 
 de commande échoue.


`#23732` - Le code journal et le nom de la période sont affichés dans 
 le récapitulatif en fin de rapport d'import d'écritures.


`#23983` - L'option de création de journaux gérants les échéances dans 
 l'outil d'import d'écriture multi-échéances active la gestion d'échéances 
 du journal.


 


#### LETTRAGE


`#16431` - Ajout du champs 'Date 
 d'échéance' ECR\_DT\_ECH dans la fenêtre de lettrage.


`#19073` - Ajout d'une option dans 
 les Préférences de la société / Onglet Encaissements, pour le lettrage 
 automatique lors de transfert comptable des règlements en portefeuille.


`#21852` - Le filtre "Lettrées" 
 et "Non lettrées" dans le lettrage manuel et pris en compte 
 lorsque l'on utilise les boutons "Précédent" et "Suivant".


`#23997` - Ajout de l'option "Solder 
 automatiquement les échéances correspondantes" dans la fenêtre de 
 lettrage automatique.


#### MODES DE RÈGLEMENTS


`#23310` - Il est possible de créer un mode de règlement contenant un 
 type de règlement sans type de remise.


#### PLAN COMPTABLE


`#20277` - Ajout dans la personnalisation 
 de liste du plan comptable, de la date du dernier lettrage et l'utilisateur 
 qui a effectué le lettrage/dé-lettrage.


`#22808` - Dans les plans comptables clients et fournisseurs, l'impression 
 d'une fiche via un clic droit n'ouvre plus une fenêtre d'impression sur 
 le plan comptable général mais bien du plan comptable clients/fournisseurs.


`#24810` - Ajout des nouveaux comptes 
 liés au prélèvement à la source dans le PCG dans les nouvelles sociétés.


#### SOLDES INTERMÉDIAIRES DE GESTION (SIG)


`#19106` - Le total des extraits de comptes ouverts 
 depuis les SIG est cohérent avec le montant présent dans la rubrique sélectionnée.


`#21716` - 
 L'extrait de compte depuis les SIG  fonctionne lorsque plusieurs 
 comptes ou plusieurs racines de comptes dont présents dans le paramétrage 
 de la zone.


`#23348` - 
 A l'ouverture de l'extrait de compte depuis les SIG, La zone "Compte" 
 est grisée.


`#22688` - Il est possible de lancer l'ouverture 
 des extraits de compte contenus dans le paramétrage d'une cellule des 
 SIG.


`#24554` - L'extrait de compte depuis les SIG tient 
 compte de la période de la cellule dans laquelle on a double-cliqué.


#### IMMOBILISATIONS


`#22986` - Correction du message d'erreur 
 "Aucune écriture n'a été trouvée" en cliquant sur le bouton 
 "Voire l'écriture d'acquisition", après avoir validé l'écriture 
 de simulation.


`#23083` - Correction du message d'erreur 
 "Division par zéro en virgule flottante" lors de la comptabilisation 
 mensuelle d'une dotation, pour une immobilisation acquise le dernier mois 
 de l'exercice.


`#23175` 
 - Correction du message Nom d'objet 'IMMOBILISATIONS' non valide lors 
 de la migration d'une 4.7.13 vers une 7.0.0 ;


`#23979` 
 - Ajout d'un champ dans les immobilisations permettant de stocker le numéro 
 de pièce d'achat et de vente/cession.


`#23980` 
 - Ajouter d'un numéro de pièce dans les écritures de dotations, générées 
 depuis le module immobilisations.


`#24055` - Le mode d'amortissement Dégressif 
 tient compte des coefficients d'amortissement dégressifs renseignés dans 
 les tables de références.


#### IMPORT BANCAIRE & RAPPROCHEMENT


`#23974` 
 - Ajout d'un numéro de pièce dans les écritures générées via le module 
 d’import bancaire & rapprochement. Pour cela, il faut que le journal 
 utilisé soit paramétré avec une numérotation des pièces différente de 
 "Manuelle".


`#24039` 
 - Ajouter l'option "Écriture en simulation" dans la fenêtre 
 de création des écritures comptables depuis le module d’import bancaire 
 & rapprochement.


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


 


