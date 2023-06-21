# Version 5.6.6 build 707 du 03/12/2015
 


Un nouveau code de débridage est nécessaire : Pour l’obtenir, solliciter 
 debridage@gestimum.com via le menu "Société\Paramétrage\Débrider 
 mon ERP".


 






|   
 | Gestimum ERP a été testé avec succès sous Windows 8, Windows 
 8.1, Windows 10 et SQL Server 2014 et 2016.
Gestimum ERP est certifié Windows Server 2012 R2. |


 


ReportBuilder est compatible avec Windows XP, Windows 8, Windows 8.1 
 et Windows 10.


### Mise en garde


Si vous utilisez un système d’exploitation 
 Windows XP ou antérieur, vous devez installer la police d’écriture Segoe 
 UI pour utiliser Gestimum ERP. Sans cette police d’écriture vous risquez 
 de rencontrer des anomalies d’affichage.


 


Attention, 
 depuis la version 5.6.0 de nombreux changements dans la gestion des numéros 
 de lots ont été apportés.


 


Pour 
 les clients gérant les numéros de lots et utilisant une version 4.8 ou 
 5, une intervention sur la base peut être nécessaire avant utilisation 
 des versions 5.6 et supérieures, dans 
 ce cas contactez-nous avant migration.


 


Par défaut nous proposons un fonctionnement 
 mono lot à la ligne de document (fonctionnel similaire à la 4.7.13) et 
 en option la possibilité de sélectionner plusieurs lots dans la sélection 
 à partir du stock avec création ou non d’autant de lignes que de lots 
 sélectionnés. La fenêtre de sélection à partir du stock étant également 
 utilisée pour les gammes, cela permet soit la sélection d’une gamme par 
 ligne de document, soit une sélection de plusieurs gammes, ce qui va créer 
 autant de lignes que de gammes sélectionnées.


 





| Gestion des numéros de lots |
|  
**CIBLE : Les PME ayant 
 besoin de gérer en stocks des articles avec numéro de lot.** 
 
**BÉNÉFICE :** **Une seule et même fenêtre de 
 sélection des numéros de lots pour l’ensemble de l’application 
 avec plusieurs méthodes de sélection et d’affectation.**
 
**PRATIQUE :**** Possibilité 
 d’importer l’ensemble des informations du lot, saisie multiple 
 possible avec détail des lots par ligne, calcul du stock et du 
 besoin à l’article et non au lot.**
  |


 


#### Evolutions principales





| **Préférences 
 de gestion**
-          **Ajout 
 d’une option permettant la saisie de la quantité et la sélection 
 multiple dans la sélection à partir du stock.**
-          **Ajout 
 d’une option permettant la création d’autant de lignes que de 
 lots et gammes.**
-          **Ajout 
 d’une option interdisant la création de lot sans date de fabrication.**
-          **Prise 
 en compte de l’option demandant le regroupement des lots lors 
 du réapprovisionnement.**
  |
| **Documents 
 d’achat, vente et stock**
-          **Sélection 
 du lot par saisie manuelle, dans la liste déroulante « N° 
 de lot 1 », par double-clic dans la fenêtre de sélection 
 à partir du stock de l’article ou en cliquant sur « Sélectionner » 
 dans le menu contextuel de la fenêtre de sélection à partir du 
 stock.**
-          **Affectation 
 du lot des composants de nomenclatures ou forfaits.**
-          **Affichage 
 d’un message d’avertissement ou bloquant lorsque la date limite 
 de commercialisation est dépassée.**
-          **Affichage 
 de la quantité totale à affecter au(x) lot(s) dans la fenêtre 
 de sélection à partir du stock de l’article.**
-          **Date 
 de péremption obligatoire lors de la création du lot pour un article 
 périssable.**
-          **Option 
 lors de la création du lot permettant d’être alerté à la mi-vie 
 du lot.**
-          **Contrôle 
 du stock réel et du stock à terme directement depuis la fenêtre 
 de sélection à partir du stock de l’article.**
-          **Import 
 possible de la date de fabrication, de la date de péremption, 
 du délai de commercialisation et de la zone de stockage du lot.**
  |
| **Abonnements**
-          **Sélection 
 du lot lors de la génération de la facture**
  |
| **Articles**
-          **Saisie 
 possible du stock mini, stock maxi et seuil d’alerte à l’article 
 pour calcul du réapprovisionnement.** |


 


#### Autres 
 évolutions & correctifs (n° de ticket)








| Cible | Catégorie | Description | N° |
| 5.6.6 | Achats & Ventes | La fenêtre de sélection à partir du stock ne 
 s’ouvre plus pour les articles non gérés lors de la duplication | 20244 |
| 5.6.5 | Analytique | Modification de la répartition bien conservée 
 après changement d’une section | 20154 |
| 5.6.5 | Achats & Ventes | Plus d’import partiel de document que le numéro 
 de pièce soit indiqué ou pas dans le fichier | 20132 |
| 5.6.5 | Achats & Ventes | On peut transférer un devis en commande même 
 si l’article n’a pas assez de stock et qu’on n’interdit pas le 
 stock à terme négatif | 20164 |
| 5.6.5 | Achats & Ventes | Stock du lot bien actualisé et plus doublé 
 lors de la suppression d’une ligne de document | 20174 |
| 5.6.5 | Achats & Ventes | On peut sélectionner un article de remplacement 
 ou une équivalence dans la sélection à partir du stock | 20182 |
| 5.6.5 | Achats & Ventes | Correction du modèle BulleGenerique\_TVA dans 
 le cas de l’utilisation d’une remise exceptionnelle | 20190 |
| 5.6.5 | Achats & Ventes | Correction de l’erreur « Echec de la conversion 
 de la valeur varchar’…’ en type de données bit. » en sélectionnant 
 un dépôt par les jumelles s’il a une raison sociale | 20214 |
| 5.6.5 | Budget | Correction de l’erreur « Conflit de types 
 d’opérandes… » à l’enregistrement d’un budget dupliqué | 20175 |
| 5.6.5 | Plan Comptable | Amélioration du message indiquant que la répartition 
 analytique dépasse 100% | 20216 |
| 5.6.5 | Plan Comptable | Contrôle de la somme des pourcentages de la 
 répartition analytique amélioré en fonction des arrondis | 20217 |
| 5.6.5 | Stocks | La zone de stockage d’un composant ne bloque 
 plus l’enregistrement d’une fiche d’assemblage | 20142 |
| 5.6.5 | Stocks | Correction du contrôle du stock du lot dans 
 le cas d’un composant de nomenclature | 20143 |
| 5.6.5 | Stocks | Correction de l’erreur « Il existe déjà 
 une ligne identique » et stock du lot bien actualisé lors 
 de la modification de la quantité dans un transfert de stock | 20145 |
| 5.6.5 | Stocks | « Emplacement » renommé en « Zone 
 de stockage » dans la sélection à partir du stock | 20193 |
| 5.6.5 | Stocks | La zone de stockage est bien reprise dans les 
 documents de stock | 20197 |
| 5.6.5 | Stocks | Correction du message « Pas assez de stock 
 actuel » à la suppression d’une ligne qu’on vient de saisir 
 dans une entrée en stock
  | 20202 |
| 5.6.5 | Stocks | Sélection de la gamme d’un composant de nomenclature 
 bien prise en compte | 20209 |
| 5.6.5 | Tiers | L’import d’adresses de tiers fonctionne correctement 
 en création et en modification | 20218 |
| 5.6.4 | Achats & Ventes | Correction de l’erreur « Syntaxe incorrecte 
 vers ‘MAX’ » à la suppression d’un document | 20125 |
| 5.6.4 | Achats & Ventes | Actualisation de l’article et du lot bien faite 
 lors du remplacement d’un article dans un document existant | 20116 |
| 5.6.4 | Stocks | Contrôle du stock des composants de la nomenclature 
 lors de l’import d’assemblage | 20106 |
| 5.6.3 | Achats & Ventes | Correction de l’erreur lors de la duplication 
 de document contenant une nomenclature | 20001 |
| 5.6.3 | Achats & Ventes | Numéro de lot pas obligatoire lors de l’import 
 de ligne pour des articles non gérés par lot ou des documents 
 ne mouvementant pas le stock | 20094 |
| 5.6.3 | Actions | Ajout du numéro interne de document dans l’action 
 créée lors de l’impression de document | 20013 |
| 5.6.3 | Contacts | Numéro de téléphone d’adresse conservé dans 
 les contacts lorsqu’on change d’onglet | 17142 |
| 5.6.3 | Contacts | Les adresses de contacts sans tiers sont bien 
 conservées | 19109 |
| 5.6.3 | Contacts | Correction de l’erreur lorsqu’on modifie un 
 contact sans date de création | 19965 |
| 5.6.3 | Contacts | Modifications des adresses conservées lorsqu’on 
 sélectionne une adresse bureau | 20051 |
| 5.6.3 | Contacts | Ajout de « Aucune » dans la liste 
 de sélection de l’adresse bureau dans les contacts | 20053 |
| 5.6.3 | Contacts | Pays, NPAI et code-barres récupérés lorsqu’on 
 sélectionne une adresse bureau | 20056 |
| 5.6.3 | Contacts | Saisie possible d’un titre dans les adresses 
 de contact | 20058 |
| 5.6.3 | Contacts | Complément de raison sociale et titre recopiés 
 lors de la sélection d’adresse dans le contact | 20069 |
| 5.6.3 | Contacts | Adresse de bureau du contact prise en compte 
 dans l’action | 20076 |
| 5.6.3 | Contacts | Ajout de la raison sociale et son complément 
 dans l’adresse du tiers dans l’action | 20090 |
| 5.6.3 | Contacts | Correction de l’erreur « FAT\_CODE non 
 trouvé » ou « SFT\_CODE » non trouvé lors de la 
 sélection d’un tiers dans un contact | 20091 |
| 5.6.3 | Stocks | Contrôle du stock à terme dans les documents 
 de sortie de stock renforcé | 19983 |
| 5.6.3 | Stocks | Correction de la violation d’accès dans les 
 documents lorsqu’on retire la colonne « N° de lot 1 » | 20027 |
| 5.6.3 | Stocks | Contrôle du stock réel dans les sorties de 
 stock renforcé | 20028 |
| 5.6.3 | Stocks | Contrôle du stock à terme dans les transferts 
 de stock et fiches d’assemblage renforcé | 20105 |
| 5.6.2 | Achats & Ventes | Correction de la violation d’accès lors de 
 l’import de ligne de document | 20088 |
| 5.6.0 | Aide | Intégration d’une nouvelle aide utilisateur | 19497 |
| 5.6.0 | Achats & Ventes | Neutralisation du double affichage de l’avertissement 
 de dépassement du stock mini de l’article | 17425 |
| 5.6.0 | Achats & Ventes | Impossible de saisir une ligne sans lot dans 
 une facture client même après avoir eu le message bloquant | 17513 |
| 5.6.0 | Achats & Ventes | Enchainement des fenêtres revu lorsqu’on ne 
 sélectionne pas de lot dans une facture | 17514 |
| 5.6.0 | Achats & Ventes | La fenêtre de sélection à partir du stock de 
 l’article n’est plus affichée après modification de la quantité | 17720 |
| 5.6.0 | Achats & Ventes | L’article est bien repris dans la fenêtre de 
 sélection à partir du stock de l’article lorsqu’on valide par  flèche 
 bas | 18307 |
| 5.6.0 | Achats & Ventes | Ajout d’une option permettant la création d’une 
 action à l’impression d’un document | 18310 |
| 5.6.0 | Achats & Ventes | Impression PDF du document attaché à l’action 
 lors d’une impression au format PDF | 18311 |
| 5.6.0 | Achats & Ventes | Possibilité de modifier les champs personnalisés 
 des lignes dans les documents qui ne sont plus modifiables | 18668 |
| 5.6.0 | Achats & Ventes | Document non importé partiellement si une ligne 
 est en erreur | 18675 |
| 5.6.0 | Achats & Ventes | Lignes en erreur détaillées lors de l’importation 
 de documents | 18784 |
| 5.6.0 | Achats & Ventes | Correction d’un contrôle sur le stock réél 
 négatif interdit lorsqu’on supprime un document d’achat | 18809 |
| 5.6.0 | Achats & Ventes | Correction de l’erreur « champ ‘PRD\_QTE’ 
 non trouvé » à l’enregistrement d’un document avec un forfait 
 dont l’un des composants est sérialisé | 18848 |
| 5.6.0 | Achats & Ventes | Les messages paramétrés dans la fiche tiers 
 s’affichent de nouveau lors du transfert de document | 18939 |
| 5.6.0 | Achats & Ventes | La fenêtre de sélection à partir du stock de 
 l’article affiche bien toute les informations lorsqu’on commence 
 par l’appeler à vide | 19000 |
| 5.6.0 | Achats & Ventes | Modification du lot dans le bon de livraison 
 bien répercutée dans le mouvement de stock | 19003 |
| 5.6.0 | Achats & Ventes | Prise en compte des nouvelles options pour 
 les lots dans le copier-coller de lignes entre documents | 19095 |
| 5.6.0 | Achats & Ventes | Modification du lot dans le transfert de stock 
 bien répercutée dans le mouvement de stock | 19188 |
| 5.6.0 | Achats & Ventes | Correction du message disant que plusieurs 
 lots sont affectés à la ligne alors qu’un seul est affecté lors 
 du changement de lot | 19235 |
| 5.6.0 | Achats & Ventes | Correction du modèle Chiffre d’affaires par 
 tiers et par article avec tous les sous-types de documents | 19259 |
| 5.6.0 | Achats & Ventes | Correction de l’erreur « Ce stock existe 
 déjà » lors de la sélection à partir du stock de l’article 
 pour un article de type pièce | 19330 |
| 5.6.0 | Achats & Ventes | Correction de l’affichage ‘Code article ZZZZZZZZZZZ’ 
 dans l’impression journal des ventes pour tous les articles | 19351 |
| 5.6.0 | Achats & Ventes | La fenêtre de sélection des lots ne s’ouvre 
 automatiquement que lorsque le lot n’est pas encore affecté | 19370 |
| 5.6.0 | Achats & Ventes | Correction de la gestion du prix de revient 
 au lot | 19373 |
| 5.6.0 | Achats & Ventes | Ajout d’un accès permettant de régler l’acompte 
 directement depuis le document | 19418 |
| 5.6.0 | Achats & Ventes | Affectation possible et obligatoire de la gamme 
 pour les composants de forfaits | 19503 |
| 5.6.0 | Achats & Ventes | Correction du message parlant de lot non sélectionné 
 dans la sélection de la gamme | 19504 |
| 5.6.0 | Achats & Ventes | Lignes sélectionnées en surbrillance dans la 
 sélection à partir du stock | 19523 |
| 5.6.0 | Achats & Ventes | Précision dans le message lorsque le transfert 
 du document ne peut se faire en raison du stock | 19538 |
| 5.6.0 | Achats & Ventes | Ajout d’un contrôle sur la date de fabrication 
 en création de lot par import | 19547 |
| 5.6.0 | Achats & Ventes | Ajout d’un contrôle sur la date de fabrication 
 en péremption de lot par import | 19548 |
| 5.6.0 | Achats & Ventes | Zone de stockage du lot bien reprise dans les 
 lignes de document | 19552 |
| 5.6.0 | Achats & Ventes | Possibilité d’importer la zone de stockage 
 en création de lot par import | 19553 |
| 5.6.0 | Achats & Ventes | La quantité du lot restant à livrer est cohérente 
 même après modification de la commande | 19559 |
| 5.6.0 | Achats & Ventes | Numéro(s) de pièce(s) créée(s) indiqué(s) dans 
 le rapport d’importation de document | 19588 |
| 5.6.0 | Achats & Ventes | Ajout des factures financières et avoirs financiers 
 dans l’impression de l’historique des ventes par représentants | 19598 |
| 5.6.0 | Achats & Ventes | Regroupement des erreurs sur les dates de péremptions 
 et / ou de fabrication du lot lors de l’import d’un fichier dans 
 le transfert d’un document | 19599 |
| 5.6.0 | Achats & Ventes | Correction de fautes dans les impressions journal 
 des ventes et journal des achats | 19600 |
| 5.6.0 | Achats & Ventes | Ajout du format .csv dans le filtre par défaut 
 de la fenêtre de sélection du fichier à importer | 19601 |
| 5.6.0 | Achats & Ventes | Dernier type d’import sélectionné conservé 
 dans l’import d’autres données | 19602 |
| 5.6.0 | Achats & Ventes | Etat « archivé » renommé en « archivé 
 (extrait) » dans la liste des documents | 19610 |
| 5.6.0 | Achats & Ventes | Filtre sur commercial du document et non du 
 tiers dans les impressions journal des ventes | 19614 |
| 5.6.0 | Achats & Ventes | Correction de l’affichage « 31/12/9999 » 
 lors de la sélection de la période toutes dans les impressions 
 journal des ventes et journal des achats | 19615 |
| 5.6.0 | Achats & Ventes | Affectation des numéros de lots des composants 
 de forfait | 19643 |
| 5.6.0 | Achats & Ventes | L’archivage et l’extraction des documents se 
 fait même s’il y a des champs personnalisés de type séparateur | 19650 |
| 5.6.0 | Achats & Ventes | Les documents archivés s’ouvrent bien depuis 
 la liste des documents archivés | 19651 |
| 5.6.0 | Achats & Ventes | Correction du contrôle du stock lors de la 
 duplication d’un document en avoir ou bon de retour | 19743 |
| 5.6.0 | Achats & Ventes | Ajout du lot et de la quantité dans les messages 
 sur le stock actuel et le stock à terme de l’article | 19798 |
| 5.6.0 | Achats & Ventes | Correction du stock commandé et du stock réservé 
 lors d’un transfert partiel en multi-lots | 19875 |
| 5.6.0 | Actions | Ajout d’un champ indiquant le traitement ayant 
 créé l’action | 19785 |
| 5.6.0 | Affaires | Coût horaire du salarié repris comme prix unitaire 
 dans la main d’œuvre réalisée | 19102 |
| 5.6.0 | Analytique | Correction de l’erreur « syntaxe incorrecte 
 vers ‘.‘ » dans l’extrait analytique lorsqu’il n’y avait 
 pas de champs personnalisés dans les écritures | 18903 |
| 5.6.0 | Articles | Correction de l’erreur « syntaxe incorrecte 
 vers le mot clé ‘LIKE’ » puis violation d’accès dans la recherche 
 d’article avec numéro de lot | 18947 |
| 5.6.0 | Articles | Plus de variation du prix de revient des composants 
 de nomenclatures après assemblage | 19086 |
| 5.6.0 | Articles | Délai de commercialisation repris par défaut 
 lors de la création d’un lot | 19514 |
| 5.6.0 | Banques | Evolution du type de coordonnées bancaires 
 « Canada » pour saisir banque, agence et compte | 18836 |
| 5.6.0 | Contact | Inversion des zones Nom et Prénom | 19509 |
| 5.6.0 | Création de société | Liste des codes APE présente lors de la création 
 d’une nouvelle base | 18874 |
| 5.6.0 | Création de société | Ajout des codes-barres EDI de TPF pour la contribution 
 sur les boissons sucrées et les boissons édulcorées | 19573 |
| 5.6.0 | Ecritures | Correction de l’erreur « E/S 32 » 
 lors de l’export d’écritures dont la première ligne est à zéro | 19192 |
| 5.6.0 | Ecritures | Correction de l’erreur « Nom de colonne 
 CPT\_NUMERO ambigu » à l’ouverture de la saisie des écritures | 19616 |
| 5.6.0 | EDI & Ecommerce | Changement du qualifiant de date dans le segment 
 DTM de 11 à 35 dans l’export des factures @GP | 18812 |
| 5.6.0 | EDI & Ecommerce | Ajout de la balise COM ;PMT dans l’export 
 des factures @GP | 18813 |
| 5.6.0 | EDI & Ecommerce | « Facturé à » repris dans l’adresse 
 de facturation plutôt que l’onglet Admin dans l’export des factures 
 @GP | 18814 |
| 5.6.0 | EDI & Ecommerce | Ajout du complément de raison sociale dans 
 l’export des factures @GP | 18918 |
| 5.6.0 | Encaissements & Décaissements | Correction de l’export d’échéanciers avec intitulé 
 des champs en en-tête de fichier | 18743 |
| 5.6.0 | Encaissements & Décaissements | Ajout de la référence du document dans les 
 règlements, paiements, remises en banque et émissions de paiement | 18849 |
| 5.6.0 | Encaissements & Décaissements | Colonne « Référence » du règlement 
 désormais triable | 18889 |
| 5.6.0 | Encaissements & Décaissements | Les échéances à la commande sont toujours visibles 
 dans la facture après transfert | 18979 |
| 5.6.0 | Encaissements & Décaissements | Correction de l’erreur « syntaxe incorrecte 
 vers ‘.‘ » à la création d’une nouvelle émission de 
 paiement | 19310 |
| 5.6.0 | Encaissements & Décaissements | Ajout d’une option dans les tables de références 
 pour paramétrer la remise en banque par défaut en fonction du 
 mode de règlement | 19417 |
| 5.6.0 | Ergonomie | Suppression des lignes horizontales dans les 
 grilles | 19633 |
| 5.6.0 | Ergonomie | Alignement des titres de colonnes avec le contenu | 19863 |
| 5.6.0 | Export Outlook | Les actions de type Rendez-vous sont bien créées 
 dans le calendrier Outlook | 17858 |
| 5.6.0 | Export Outlook | L’heure de fin des actions de type Rendez-vous 
 est bien synchronisée dans Outlook | 19090 |
| 5.6.0 | Ouverture de société | Correction de la violation d’accès arrivant 
 parfois lors de l’utilisation de l’option « Déconnecter » 
 à l’ouverture de la société | 18871 |
| 5.6.0 | Personnalisation des listes | Nom du champ posant problème ajouté dans le 
 message disant que le paramétrage des colonnes doit être réinitialisé | 19822 |
| 5.6.0 | Réapprovisionnement | Le réapprovisionnement se fait maintenant sur 
 l’article et plus sur le lot | 16075 |
| 5.6.0 | Réapprovisionnement | Commandes générées par le réapprovisionnement 
 avec lot transférable | 19021 |
| 5.6.0 | Stocks | Suppression du menu « Sélection explicite 
 des quantités » dans le menu contextuel de la fenêtre de 
 sélection de lot | 18902 |
| 5.6.0 | Stocks | Correction de l’affichage du nombre de numéros 
 de série dans différentes fenêtres | 18913 |
| 5.6.0 | Stocks | Suppression du menu « Stocks / Stock d’un 
 article et de ses équivalences » | 18915 |
| 5.6.0 | Stocks | Correction de l’erreur « Champ ART\_TYPE 
 non trouvé » dans les mouvements des numéros de série | 18916 |
| 5.6.0 | Stocks | Suppression de la fenêtre de sélection à partir 
 du stock dans la fenêtre « Stock des articles des lignes » | 18953 |
| 5.6.0 | Stocks | Suppression de la fenêtre de sélection à partir 
 du stock dans la liste des articles | 18956 |
| 5.6.0 | Stocks | Zone de stockage de la fiche article bien reprise 
 dans les documents de stock | 18983 |
| 5.6.0 | Stocks | Correction de la violation de contrainte Primary 
 Key « STK\_PDEP » dans l’objet dbo.ART\_STOCK lors d’une 
 sortie de stock | 19031 |
| 5.6.0 | Stocks | Prise en compte des décimales de la devise 
 dans l’assemblage de nomenclature | 19087 |
| 5.6.0 | Stocks | Les mouvements des documents archivés apparaissent 
 de nouveau dans les mouvements de stock | 19088 |
| 5.6.0 | Stocks | Correction de la violation de contrainte Primary 
 Key « STK\_PDEP » dans l’objet dbo.ART\_STOCK lors d’un 
 inventaire tournant | 19165 |
| 5.6.0 | Stocks | Correction de l’erreur « LIG\_NUMLOT non 
 trouvé » après la sélection d’un lot périmé | 19375 |
| 5.6.0 | Stocks | Ajout d’une fonction dans les imports permettant 
 d’importer une fiche d’assemblage de nomenclature | 19402 |
| 5.6.0 | Stocks | Lot des composants de nomenclature bien demandés 
 en désassemblage | 19561 |
| 5.6.0 | Stocks | Date de création du lot plus remplacée par 
 la date du dernier inventaire | 19576 |
| 5.6.0 | Stocks | Date de péremption du lot importable lors de 
 l’import des lignes d’inventaire | 19577 |
| 5.6.0 | Stocks | Lots des composants plus mélangés après suppression 
 d’une fiche d’assemblage | 19585 |
| 5.6.0 | Stocks | Tri possible dans la sélection à partir du 
 stock sur la gamme, le lot ou la date de fabrication | 19591 |
| 5.6.0 | Tables de reference | Option « Centralisé » dans les types 
 de règlements renommées en « Centraliser la comptabilisation » | 19429 |
| 5.6.0 | Tiers | La recherche dans les colonnes des listes est 
 maintenant insensible aux accents | 18547 |
| 5.6.0 | Tiers | Modification du champ Rue et  Complément 
 de rue de 40 à 60 caractères | 18736 |
| 5.6.0 | Transfert auto des commandes | Correction de OC\_F\_RS en DOC\_F\_RS dans la liste 
 des commandes | 19944 |


 


