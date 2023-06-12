




Version 6.0.0 build 750 du 20/04/2017



 


### ACHATS ET VENTES


#15817 – Ajout d’un portefeuille des commandes fournisseurs.


#16098 – Intégration d’un nouveau modèle de relevé de factures pour 
 tous les types de règlements.


#16866 – Intégration d’un nouveau modèle pour les livraisons prévues 
 sur les 30 prochains jours.


#18492 – Lors du transfert d’une facture en avoir, le mouvement de stock 
 de l’avoir se fait bien à la date de l’avoir.


#20304 – Option pour avoir une ligne à 0 bien prise en compte si on 
 n’a pas assez de stock lors du transfert de la commande en bon de livraison.


#20305 – Contrôle du stock amélioré lors de la suppression d’une ligne 
 dans une commande fournisseur.


#20983 – Ajout d’une totalisation des colonnes Total HT, Total TVA, 
 Total TTC, Total Brut, Total Net et Total TPF en pied des listes des documents 
 d’achats et de ventes.


#21099 – La fenêtre de composition des nomenclatures et forfaits ne 
 s’ouvre plus lorsqu’on déplace une ligne dans un document.


#21249 – Possibilité de transférer les lignes textes et totaux lors 
 du transfert de la commande en bon de livraison avec fichier des quantités, 
 depuis l’application ou via la tâche en lignes de commande.


#21258 – Montant total du document bien recalculé après duplication 
 lorsqu’on a dans les lignes une nomenclature ou un forfait avec une remise 
 à 100%.


#21480 – Correction de l’’option « Contrôler la référence article dans 
 les devis ». 


#21539 – On ne demande plus la sélection du N° de série lors de l’utilisation 
 dans un document d’une nomenclature gérée en stock si l’un des composants 
 est géré par N° de série.


#21681 – Contrôle du stock amélioré lorsqu’on a dans un document un 
 article et une nomenclature ou forfait qui utilise cet article comme composant.


### ARTICLES


#20608 – La classification EDI pour la TPF 2 est bien conservée et ne 
 remplace plus la TPF 1.


### CONTACTS


#21532 – Correction de la recherche sur la famille ou la sous-famille 
 de contact après changement dans le tiers.


#21615 – Possibilité de géolocaliser  avec Google Maps plusieurs 
 adresses de contacts.


### CREATION DE SOCIETE


#17923 – Les filtres au commercial ne sont plus activés par défaut pour 
 les groupes ADMIN et DEFAUT dans une nouvelle société.


#21282 – Ajout de « APPL Affaire Personnelle Profession Libéral » dans 
 les statuts juridiques par défaut.


### ENCAISSEMENTS & DECAISSEMENTS


#21434 – Les modifications sur les échéances multiples faites via l’outil 
 de modification dans les relances sont bien conservées lors de la clôture.


### ERGONOMIE


#20745 – « Informations sur la base de données » déplacé dans le menu 
 OUTILS.


#21773 – Ajout d’un style « Gestimum Bleu » dans les barres d’outils.


#21863 – Optimisation des jointures lors de l’ouverture des listes et 
 onglets utilisant des champs complémentaires.


### NATURES COMPTABLES


#21568 – Zone de saisie de l’intitulé limitée à 40 caractères pour respecter 
 la taille du champ.


### PAYS & VILLES


#19739 – Ouverture de la liste des villes pour sélection lors de la 
 saisie d’un code postal correspondant à plusieurs villes.


### PREFERENCES


#21300 – Option « Ouvrir les fenêtres maximisées » activée par défaut 
 dans les Préférences utilisateur.


#21376 – Suppression de l’onglet « Exports d’achats, ventes et stocks 
 » dans les Préférences utilisateur de la comptabilité.


### STOCKS


#14265 – Le prix de revient est bien mis à 0 lorsqu’on fait une entrée 
 non valorisée alors qu’on n’avait plus de stock. 


#18381 – Amélioration de la valorisation du stock dans le dépôt de destination 
 lors d’un transfert de stock.


#20707 – Possibilité de créer des champs perso dans les documents de 
 stocks.


#20708 – Possibilité de créer des champs perso dans les lignes de documents 
 de stocks.


#21360 – Création d’un onglet « Commentaires » dans les documents de 
 stocks.


#21538 – Correction de l’erreur « Champ ART\_SERIE non trouvé » en affectant 
 les N° de série à un composant d’assemblage via le bouton « Stock »


### TIERS


#14232 – Ajout du choix de la codification des comptes tiers dans les 
 Préférences de la comptabilité.


#15450 – Possibilité d’afficher jusqu’à 10 adresses de livraison dans 
 la personnalisation de la liste.


#21573 – Possibilité de géolocaliser  avec Google Maps plusieurs 
 adresses de facturation de tiers.


#21661 – Le pays se met bien à jour lors de la sélection d’une ville.


#21733 – Ajout d’une option dans l’outil pour mettre à jour les tiers 
 afin de géocoder les adresses.


#21734 – La date est toujours renseignée avec l’heure, quel que soit 
 la méthode de création du tiers.


#21759 – Le lien vers le site Manageo est de nouveau opérationnel.


### TRANSFERT COMPTABLE


#21870 – La date d’échéance est bien reprise lors du transfert comptable 
 au format QuadraCompta.


### AFFAIRES


#18875 – Intégration de nouveaux modèles ReportBuilder pour les affaires.


#21691 – Onglet « Personnalisé » déplacé en dernier dans la fiche.


### EDI & E-COMMERCE


#21636 – L’option « NAD RE (réglé à) » tient bien compte du paramétrage 
 de l’export des factures EDICOT.


### TACHES EN LIGNES DE COMMANDE


#21251 – Accents retirés dans les noms des paramètres des tâches en 
 lignes de commande.


#21452 – Ajout de nouvelles tâches en lignes de commande pour les imports 
 existants, accessible avec le module G-Change.


#21482 – Correction du fichier log des tâches en lignes de commande 
 lors de l’utilisation du paramètre « PremiereLigneContientNomsChamps ».


#21546 – Tâche « TransfertDocumentsAchVte » renommée en « TransfererDocumentsAchVte 
 ».


#21658 – Ajout d’un paramètre « Simulation » dans la tâche d’import 
 d’écritures.


#21780 – Ajout d’un paramètre « Tester » dans la tâche d’import d’écritures.


#21781 – Ajout d’un paramètre « Tester » dans la tâche d’import de comptes.


#21793 – Ajout de paramètres « CalculerNumeroCompte » et « CalculerCodeTiers 
 » dans la tâche d’import de comptes. 


### BALANCE


#19397 – Amélioration des jointures et des comparaisons de dates dans 
 les modèles de balances âgées.


### ECRITURES


#17285 – Le numéro de pièce est bien repris dans l’échéance après modification 
 d’une écriture.


#17299 – Les modèles d’échéanciers tiennent bien compte des règlements 
 lettrés.


#18348 – La devise de l’échéance est bien actualisée après modification 
 de l’écriture.


#21267 – L’échéance n’est plus dupliquée lorsqu’on déplace une écriture 
 d’un journal vers un autre.


#21364 – Ajout de champs « Numéro de pièce complémentaire » et « Référence 
 » dans les écritures.


#21385 – L’échéance est bien supprimée lorsqu’on remplace un compte 
 gérant les échéances par un compte ne les gérant pas dans les écritures.


#21514 – L’échéance est bien actualisée lorsqu’on change le sens de 
 l’écriture.


#21554 – Le code du mode de règlement est bien repris dans l’écriture 
 s’il est modifié dans la fenêtre de l’échéancier.


#21579 – Correction de la violation d’accès lorsqu’on cherche à importer 
 un fichier d’écritures vide.


#21603 – Affichage des écritures bien actualisé lors de la saisie d’une 
 date personnalisée dans la saisie standard.


### JOURNAUX


#20696 – Ajout d’une option permettant de continuer la codification 
 du numéro de pièce lors de l’import des écritures s’il n’est pas renseigné.


### PLAN COMPTABLE


#21558 – Les lignes ne sont plus doublées dans le rapport d’import des 
 comptes.


#21585 – Correction du rapport d’import des comptes lorsqu’on renseigne 
 les champs en première ligne.


#21693 – La date est toujours renseignée avec l’heure, quel que soit 
 la méthode de création du compte.


### IMMOBILISATIONS


#21487 – Le plan d’amortissement n’est pas modifié si la comptabilisation 
 de la sortie de l’immobilisation échoue en raison d’erreurs. 


#21564 – Possibilité de sélectionner une autre catégorie que « Corporelle 
 » pour les immobilisations de type « Bien ».


### RAPPROCHEMENT BANCAIRE


#21129 – Ajout d’un format de date avec heure pour l’import des relevés 
 bancaire au format OFX.


 


 


 


![](../assets/images/Version6/Images/Modules_de_l_ERP.png)


