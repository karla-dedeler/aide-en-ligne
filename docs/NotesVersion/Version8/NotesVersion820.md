# Version 8.2.0 build 836 du 01/04/2019

 


\* Les numéros de tickets en orange 
 correspondent à des évolutions de l'ERP.


 


#### LOI ANTI-FRAUDE TVA


`#24919` - Toutes les modifications 
 effectuées sur les lignes de documents de vente de type facture, facture 
 financière, avoir, avoir financier sont tracées.


`#24921` - Mise en place d'un état 
 d'impression de détail des encaissements par tiers et par document, accessible 
 depuis le menu Impressions / Encaissements / Règlements reçus.


`#24922` - Mise en place d'un format 
 d'export des documents de vente au format -CSV, accessible depuis le menu 
 Outils / Exporter / Factures et avoirs clients au format CSV pour l'administration 
 fiscale.


Cet export 
 crée 4 fichiers : documents, lignes, échéances et règlements ; Structurés 
 comme suit :


* Le fichier Documents contient les 
 colonnes suivantes : NumeroPiece(DOC\_PIECE);Date(DOC\_DATE);MontantTTC(DOC\_MT\_TTC),
* Le fichier Lignes contient les colonnes 
 suivantes : NumeroPiece(DOC\_PIECE);CodeArticle(ART\_CODE);Libelle(LIG\_LIB);Quantite(LIG\_QTE);PrixUnitaire(LIG\_P\_NET);TotalHT(LIG\_TOTAL);TauxTVA(NAT\_TVATX),
* Le fichier Échéances contient les 
 colonnes suivantes : NumeroPiece(DOC\_PIECE);Date(ECH\_DATE);ModeReglement(REG\_CODE);ARecevoir(ECH\_ARECEV);APayer(ECH\_APAYER),
* Le fichier Règlements contient les 
 colonnes suivantes : NumeroPiece(DOC\_PIECE);Date(REG\_DATE);TypeReglement(REG\_TYPE);Recu(REG\_RECU);Paye(REG\_DONNEE).


#### ACHAT ET VENTE


`#24821` 
 - Mise en place du champ DOC\_PIECE2 "N° de pièce complémentaire" 
 dans les documents d'achat, permettant d'y renseigner le n° de document 
 du système du fournisseur. 


Ce champs se situe dans l'onglet général 
 du document, et est visible dans la liste des documents d'achats et dans 
 les échéances fournisseurs.


Lors du transfert comptable, 
 le contenu de ce champ est affecté au champ ECR\_PIECE2 "Numéro de 
 pièce complémentaire" des écritures.


`#24834` 
 - Le numéro de lot saisie dans une commande client est pris en compte 
 lors du transfert en BL, la fenêtre de sélection à partir du stock ne 
 s'ouvre plus.


`#24842` - Avec l'option  multi-lots 
 à la ligne d'activée, le numéro de lot s'importe lors d'un transfert de 
 document avec un import de fichier, à l'aide des éléments suivants :


*  LLD\_NUMLOT 
 => le ou les numéros de lot à importer,
* LLD\_QTE => 
 la ou les quantités par numéro de lot importé.


Avec 
 l'option  mono-lots à la ligne 
 d'activée, le numéro de lot s'importe lors d'un transfert de document 
 avec un import de fichier, à l'aide des éléments suivants :


* LIG\_NUMLOT => 
 le numéro de lot à importer,
*  LIG\_QTE 
 => la quantité par numéro de lot importé.


`#25037` - Correction 
 de l'erreur "Syntaxe incorrecte vers '('" dans le regroupement 
 de BL lorsque l'utilisateur à un salarié ayant des droits sur plusieurs 
 dépôts.


`#25043` - Lors du transfert 
 d'une commande contenant des articles gérés par lots, le total de la sélection 
 à partir du stock ne double plus lorsque l'on désélectionne un lot pour 
 en sélectionner un autre.


`#25117` - Le message 
 d'avertissement "Le prix de vente de l'article est inférieur au prix 
 de revient" n'apparaît plus dans le transfert automatique des commandes.


`#25342` - Correction 
 de l'erreur : "Les types de données text et varchar sont incompatibles 
 dans l'opérateur equal to." en cliquant sur le bouton "tout 
 effacer" de la fenêtre de sortie de numéros de séries depuis un document 
 de vente.


#### CHAMPS PERSONNALISÉS


`#24742` 
 - Ajout des colonnes FLD\_SEPRTR (séparateur) et FLD\_ESPCMT (Espacement), 
 dans la personnalisation du paramétrage des champs personnalisés permettant 
 d'afficher la nature des champs.


#### ENCAISSEMENTS ET DÉCAISSEMENTS


`#25333` - Correction de l'erreur "Champ 
 'ECH\_DTMAJ.' non trouvé" lors de la création d'échéances d'avance 
 via les échéancier clients / fournisseurs.


`#25348` - Correction 
 de l'erreur dans la requête SQL du modèle "Suivi des echeances des 
 tiers en liste.Reglements.rpm".


#### ERGONOMIE


`#24627` 
 - Modification de la fonction de recherche en utilisant '\*' dans les listes 
 et fenêtres de recherche : 


* "commence 
 par" avec la syntaxe suivante : GEST\*,
* "contient" 
 avec la syntaxe suivante : \*ESTI\*,
* "fini par" 
 avec la syntaxe suivante : \*MUM.


`#25217` 
 - Harmonisation du fonctionnement des différentes zones de recherche, 
 avec l'utilisation du caractère "\*".


`#24997` - Modification de l'ergonomie 
 des Préférences de Société, Préférences de Gestion, Préférences de comptabilité 
 et Préférences utilisateurs.


#### GEOLOCALISATION


`#25083` - L'outil de géo-codage des adresses dans la mise à jour des 
 tiers prend bien en compte le dernier lot de 100 adresses.


#### IMPORTS / EXPORTS


`#25059` - Correction de l'erreur "(la ligne 1 n'a pas pu être importée) 
 : Le contenu du champ ADR\_MEMO est trop grand, il sera ignoré" dans 
 l'import des adresses de tiers.


`#25124` - L'import de documents de vente effectue une rupture lorsqu'il 
 passe sur une ligne n'ayant pas la même date que la précédente.


`#25125` - Mise en place d'un export 
 des documents de vente au format .xml accessible depuis le menu Outils 
 / Exporter / Factures et Avoirs clients au format XML.


`#25148` - L'import de documents de vente effectue une rupture lorsqu'il 
 passe sur une ligne n'ayant pas la même référence commande (DOC\_REFPCF) 
 que la précédente.


#### STOCKS


`#24547` - La personnalisation de la liste de la fenêtre "Stock des 
 articles des lignes" accessible depuis le menu contextuel d'un document 
 d'achat / vente est sauvegardée après fermeture de la fenêtre.


`#24726` - Correction du message d'erreur généré lors de l'affectation 
 automatique par code ou par date des numéros de série dans les documents 
 achats / ventes.


`#24776` - Mise en place de contrôles sur les numéros de séries lors de 
 la suppression de lignes dans les documents d'achat / vente.


`#24882` - Les commentaires des documents d'inventaire sont sauvegardés.


`#24963` - Mise en place d'un contrôle sur le stock manquant dans la fenêtre 
 de sélection des lots, lorsque l'option de sélection à partir du stock 
 est activée avec le multi-lots à la ligne.


#### TIERS


`#25001` 
 - Le tiers est accessible depuis la liste des documents de stock, via 
 un clic droit dans la liste.


#### AFFAIRES


`#24374` 
 - L'affaire est accessible depuis la liste des documents d'achat et de 
 vente, via un clic droit dans la liste, si l'affaire est renseignée dans 
 l'en-tête du document sélectionné.


`#24375` 
 - L'affaire est accessible depuis les lignes des documents d'achat et 
 de vente, via un clic droit sur la ligne.


`#24474` 
 - Ajout d'une option dans les Préférences de Gestion, permettant de rendre 
 obligatoire la saisie de l'affaire dans les documents de ventes et d'achats.


`#25001` 
 - L'affaire est accessible depuis la liste des documents de stock, via 
 un clic droit dans la liste.


`#25008` - La permission de voir ou modifier 
 les affaires est contrôlée dans chaque clic droit "Affaire".


`#25112` 
 - Ajout de filtres dans l'en-tête de la fenêtre de liste des affaires, 
 permettant d'effectuer des recherches sur : Tiers, Libellé, Descriptif, 
 État, Catégorie, Sous-Catégorie et Date de début / fin.


#### EDI CHORUS


`#25085` - Les sauts de lignes, tabulations et espaces insécables présents 
 dans les textes saisis dans Gestimum sont supprimés le l'export des documents 
 au format Chorus Pro.


`#25086` - Le numéro de marché Chorus (DOC\_NMCHRS) 
 est maintenant exporté dans la balise <ContractDocumentReference> 
 du fichier d'export au format Chorus au lieu de la balise <OrderReference>.


`#25127` 
 - La raison sociale présente dans les préférences de Société est maintenant 
 exportée dans la balise <cac:AccountingContact> <cbc:Name>"RAISON 
 SOCIALE"</cbc:Name> du fichier d'export au format Chorus.


`#25129` 
 - Lorsque le numéro de marché Chorus n'est pas renseigné dans DOC\_NMCHRS, 
 la balise <ContractDocumentReference> du fichier d'export au format 
 Chorus reste vide.


`#25144` 
 - Ajout d'un contrôle sur la présence du code pays dans les adresses des 
 documents exportables au format Chorus.


En 
 cas d'erreur lors de la génération des fichier, le message suivant apparaît 
 : "Code pays manquant de l'adresse de facturation dans la facture 
 client %s".


`#25145` 
 - La fenêtre de sélection des factures et avoirs à exporter au format 
 Chorus exclut les documents non éligibles. La raison de l'exclusion est 
 accessible via un double clic sur la ligne concernée.


`#25158` 
 - Actualisation des valeurs possibles renseignables dans la balise  <PaymentMeansCode> 
 du fichier d'export au format Chorus :


* 01 Instrument 
 not defined (correspond à la donnée générique « Autres »),
* 10 Cash (correspond 
 à la donnée générique « Espèce »),
* 20 Check (correspond 
 à la donnée générique « Chèque »),
* 30 Credit Transfert 
 (correspond à la donnée générique « Virement »),
* 31 Debit transfert 
 (correspond à la donnée générique « Virement »),
* 42 Payment to 
 Bank account (correspond à la donnée générique « Virement »),
* 48 Bank Card 
 (correspond à la donnée générique « Prélèvement »),
* 49 Direct Debit 
 (correspond à la donnée générique « Prélèvement »)
* 97 Clearing 
 between partners (correspond à la donnée générique « Report »).


`#25228` - Le montant HT 
 des frais saisi en pied de document, est bien exporté dans le récapitulatif 
 des taxes du fichier d'export au format Chorus.


`#25233` 
 - Le complément raison sociale de l'adresse de facturation et de l'adresse 
 de livraison sont concaténés dans la balise <cac:Delivery> <cac:DeliveryLocation> 
 du fichier d'export au format Chorus. 


Attention 
 les données contenues dans cette balise sont tronquées à 99 caractères.


#### G-CHANGE


`#24833` 
 - La tâche en ligne de commande de transfert de documents d'achat / vente 
 ne remonte plus de message "Prix de Vente inférieur au Prix de Revient" 
 comme via l'IHM.


`#24835` - L'erreur "Code manquant" 
 ou "n'a pas pu être calculé" lorsque les champs ne sont pas 
 dans le bon ordre dans les imports autour des articles, ne sont plus affichées 
 via IHM, mais inscrites dans le log.


`#24922` - Mise en place d'une tâche 
 en ligne de commande permettant d'exporter les factures et avoirs clients 
 au format CSV pour l'administration fiscale. 4 
 fichiers sont alors générés :


* Le fichier Documents contient les 
 colonnes suivantes : NumeroPiece(DOC\_PIECE);Date(DOC\_DATE);MontantTTC(DOC\_MT\_TTC),
* Le fichier Lignes contient les colonnes 
 suivantes : NumeroPiece(DOC\_PIECE);CodeArticle(ART\_CODE);Libelle(LIG\_LIB);Quantite(LIG\_QTE);PrixUnitaire(LIG\_P\_NET);TotalHT(LIG\_TOTAL);TauxTVA(NAT\_TVATX),
* Le fichier Échéances contient les 
 colonnes suivantes : NumeroPiece(DOC\_PIECE);Date(ECH\_DATE);ModeReglement(REG\_CODE);ARecevoir(ECH\_ARECEV);APayer(ECH\_APAYER),
* Le fichier Règlements contient les 
 colonnes suivantes : NumeroPiece(DOC\_PIECE);Date(REG\_DATE);TypeReglement(REG\_TYPE);Recu(REG\_RECU);Paye(REG\_DONNEE).


`#25125` 
 - Mise en place d'une tâche en ligne de commande permettant d'exporter 
 des documents de vente au format xml.


#### ANALYTIQUE


`#24819` - Le paramétrage de l'analytique du compte est appliqué lors 
 de la génération d'écriture automatique via le menu lettré manuellement 
 / lettrage approche.


#### DÉCLARATION DE TVA


`#25161` - Affichage de l'état de 
 la déclaration en clair dans la liste des déclarations de TVA de la TVA 
 avancée.


`#25179` - La fenêtre "Récapitulatif par comptes" de la déclaration 
 de TVA avancée, ne reprend que les comptes nécessaires au calcul de la 
 provision.


#### ÉCRITURES


`#24681` - Dans un journal, il n'est plus 
 possible de sortir d'une ligne d'écriture, si le compte comptable n'est 
 pas renseigné.


`#25310` - Modification du contrôle effectué 
 sur la présence du n° de pièce et du libellé dans l'import d'écritures.


#### RAPPROCHEMENT BANCAIRE


`#25034` - La fonction "Valider tous les rapprochements jusqu'à ce 
 rapprochement" accessible depuis un clic droit dans la liste des 
 rapprochements bancaires prend en compte les rapprochements précédents.


#### SOLDES INTERMÉDIAIRES DE GESTION (SIG)


`#24761` - Correction de la Violation d'accès présente 
 dans les SIG en cliquant sur le bouton 'Valider' sans avoir sélectionné 
 de ligne dans la grille au préalable.


#### IMPORT BANCAIRE & RAPPROCHEMENT


`#25155` - La création d'écritures depuis le module de rapprochement bancaire 
 automatique ne génère plus d'écritures déséquilibrées si le compte d'attente 
 sélectionné ne comporte pas de devise dans son paramétrage.


 


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


 


