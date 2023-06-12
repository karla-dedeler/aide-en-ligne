



Version 7.0.0 build 766 du 28/11/2017



 


### LOI ANTI-FRAUDE TVA


#22555 – Mise en place 
 d’un journal d’historisation des modifications et suppressions de règlements.


#22556 – Mise en place 
 d’un export au format \*.csv, du journal d’historisation des modifications 
 et suppressions de règlements.


#22557 – Lors du lancement 
 de la clôture d’exercice, une sauvegarde automatique est lancée au début 
 de la procédure.


#22558 – Lancement 
 d'une sauvegarde automatique au début de la procédure de purge des écritures.


#22559 – Lancement 
 d'une sauvegarde automatique au début de la procédure de purge des documents.


#22735 – Ajout d’une 
 clé d’inaltérabilité dans les tables des documents, échéances, écritures 
 et règlements, certifiant qu’aucune insertion / modification / suppression 
 n’a été effectuée en dehors du logiciel.


### ACHAT ET VENTE


#16835 – L’enregistrement 
 du format d’import de documents s’effectue correctement.


#21247 – Les lignes 
 de nomenclature ou forfait ne passent pas à 0 si on clique sur "Annuler" 
 lorsque la composition s'affiche.


#21945 – Le prix de 
 revient remonte bien dans la ligne de document de vente lors de la sélection 
 du lot.


#22030 – Dans les 
 documents de type pro-forma, devis et bon de livraison, l'échéancier client/fournisseur 
 s'actualise bien lors de la modification des échéances du document.


#22034 – Le calcul 
 du prix de revient s'effectue correctement en cas de transfert partiel 
 avec frais d'approche d'achat.


#22051 – Correction 
 de la violation d'accès dans la fenêtre de recherche avancée des tiers, 
 depuis un document de vente.


#22301 – Le commentaire 
 d'adresse de tiers est bien repris dans les documents.


#22360 – Le transfert 
 d'un bon de retour en avoir ne génère plus un nouveau mouvement de stock.


#22567 – Intégration 
 d'un total des quantités par article dans le modèle d'impression "Historique 
 des achats par articles".


#22568 – On ne perd 
 plus la virgule lors d'un copier / coller de montant ou de quantité.


#22610 – Lors d'un 
 transfert partiel d'une commande d'achat en bon de réception, la mise 
 à zéro des quantités, dans la sélection manuelle des quantités à transférer, 
 ne bloque plus la génération du bon de réception.


#22625 – Lors du transfert 
 en bon de livraison d'une commande contenant une quantité négative, la 
 ligne négative est bien conservée.


#22681 – Le contrôle 
 de stock s'effectue bien sur l'ensemble des gammes, dans le cas d'un article 
 géré en lot et gamme.


### ARTICLES


#16211 
 – La TPF des articles composants remonte bien dans le pied de document 
 de vente.


#20066 
 – Les résultats dans le rapport d'import des articles n'est plus inversé.


### ASSEMBLAGE


#22496 
 – Le prix de revient du composant remonte dans l'assemblage de nomenclature.


### COMMERCIAUX ET BAREME


#21978 – Dans le calcul 
 de commissionnement des commerciaux, le pourcentage de marge dans la ligne 
 de total du barème se calcule correctement.


### CONDITIONNEMENT


#21978 – Le conditionnement 
 d'achat ne double plus les quantités lorsqu'il s'agit d'articles gérés 
 en lots.


### CONTACT


#21498 
 – La modification de valeurs directement dans la grille de l'onglet contact 
 des fiches tiers n'est plus possible, il faut passer par la mise à jour 
 des contacts.


### BANQUES


#14270 – Renommage 
 des étiquettes de type de coordonnées bancaires avec affichage du nombre 
 de caractères attendus dans chaque zone.


#16853 – Mise en place 
 d'une zone de saisie unique d'IBAN dans les coordonnées bancaires en sélectionnant 
 le type "Générique".


### BUDGET


#18936 – Le montant 
 du budget est bien réparti par période pour les lignes secondaires du 
 budget.


### DEBRIDAGE


#22214 – Suppression 
 de la case à cocher « Web service et tâches en ligne de commande uniquement 
 » dans la gestion des utilisateurs.


#22592 – Les états 
 financiers sont désormais accessibles en version INITIALE de l'ERP.


#22807 – Les SIG ne 
 sont plus disponibles en version INITIALE.


#22591 – L'analytique 
 n'est plus disponible en version INITIALE.


### ENCAISSEMENTS ET DECAISSEMENTS


#21928 – Affichage 
 du montant total de la sélection multiple d'échéances, dans les 4 listes 
 d'échéances en affichant les champs ECH\_D\_ARECEV, ECH\_E\_ARECEV, ECH\_D\_ADEP, 
 ECH\_E\_ADEP.


#22058 – Correction 
 du message d’erreur s’il y a un avoir parmi les échéances sélectionnées, 
 lors de la remise en banque via l’option « Règlements et remise des échéances 
 ».


#22760 – Correction 
 du message "Ancêtre de 'lblPeriode' non trouvé" à l'impression 
 du portefeuille des effets.


### GAMMES


#22237 – Mise en place 
 d’un contrôle de valeur de gamme lors de l’import de lignes dans un document.


#22463 – Il est désormais 
 possible d’importer plusieurs codes de valeurs de gammes lors de l’import 
 de lignes dans un document, en utilisant le « \ » comme séparateur de 
 valeurs.


### GEOLOCALISATION


#22450 – Augmentation 
 de la taille des champs latitude et longitude de la table des tiers.


#22563 – Correction 
 de l’erreur de script à la géolocalisation d’un tiers.


### LISTES ET PERSONNALISATIONS


#21370 – Le nom des 
 champs est affiché dans les filtres de personnalisation des listes au 
 lieu des codes de champs.


#21671 – Il n'est 
 plus nécessaire de saisir 2 fois les conditions des filtres si on utilise 
 les critères comme variable.


### PAYS ET VILLE


#22369 – Correction du code postal de la 
 ville de Nice (06000).


### STOCK


#20500 – Correction de 
 la violation d’accès à l’ouverture de la liste des lots dans toutes les 
 grilles, lorsque la mise en mémoire des données est activée dans les préférences 
 de la société.


#20694 - Ajout d'une barre 
 avec le total de différentes colonnes en bas des fenêtres de mouvements 
 de stock (Nombre de pièces, Inventaire, Ecart, Entrée, Sortie).


#21022 - Ajout d'une barre 
 avec le total de différentes colonnes en bas des fenêtres de stock (Inventaire, 
 Entrée, Sortie, Valeur de stock).


#22417 – Amélioration des 
 performances d’affichage des mouvements de stocks.


#22505 - A la saisie d'une 
 commande client, d'une nomenclature gérée en stock avec des composants 
 gérés en stock, le stock à terme du composant est alimenté.


#22859 - Correction de 
 la valorisation du stock lors de transfert de stock.


### TIERS


#22426 - Les champs "Créé le" et "Créé par" s'alimentent 
 à la création des tiers.


#22572 - Dans la recherche avancée des tiers, on tient bien compte du 
 filtre "en sommeil".


#22582 – La période sélectionnée dans les actions des tiers est mémorisée.


#22891 - Correction de l’erreur "champ 'JRN\_CODE' non trouvé" 
 lors d’une ré-imputation de tiers.


#22927 – En cas d’absence de connexion internet, l’enregistrement des 
 adresses s’effectue.


#23012 – Actualisation du lien vers le site Manageo.fr depuis la fiche 
 tiers.


#23022 – La recherche de tiers sur Manageo.fr 
 s’effectue également à partir du SIREN.


### UTILISATEURS


#21784 – Mise en place d'un outil de création 
 des utilisateurs par import.


### G-CHANGE


#21904 – Mise en place de l’import des 
 champs personnalisés dans l’import de tiers en tâche en ligne de commande.


#22424 – Lors de l'import d'écritures en 
 tâche en ligne de commande, l'analytique se renseigné.


#22436 – Ajout des paramètres "CreerSectionAnalytique" 
 et "PlanAnalytique" dans la tâche en ligne de commande de création 
 d'écritures.


#22565 – Mise en place d’un message de 
 retour plus explicite, lorsque l’IBAN importé n’est pas conforme.


#22588 – Mise en place d'un nouveau paramètre 
 dans l'import d'écritures en ligne de commande pour générer un rapport 
 JSON : "Statistiques".


#22569 - Lors d'import en tâche en ligne 
 de commande ou via le Web service, il n'y a plus d'ouverture de boite 
 de dialogue de l'ERP.


#22663 – Implémentation d’un paramètre 
 « statistiques » dans toutes les tâches en ligne de commande d’import.


#22674 - La création d'une affaire associée 
 à un tiers inexistant n'est plus possible via import, Tâche en ligne de 
 commande et Web service.


#22676 - La création d’un mode de règlement 
 associé à un type de règlement inexistant n’est pas possible via import, 
 Tâche en ligne de commande et Web service.


#22683 - La création d’un mode de règlement 
 sans type de règlement n’est pas possible via import, Tâche en ligne de 
 commande et Web service.


#22684 – Mise en place de messages de retour 
 plus explicites dans l’import des banques de tiers.


### ECRITURES & IMPORT


#21310 – Le code du mode de règlement inexistant 
 est bien indiqué dans le message de retour, lors de l’import d’écriture.


#21659 – Lors de l’import d’écritures, 
 les écritures déséquilibrées sont rejetées.


#22553 – L'ensemble des lignes d'une pièce 
 comptable sont rejetées en cas d'anomalie détectée dans le fichier de 
 création.


#22888 – Distinction de la notion d’écriture 
 et ligne d’écriture dans le rapport statistique d’import d’écritures.


### ERGONOMIE


#22593 – L'accès aux SIG s'effectue via 
 le menu Décisionnel.


### PLAN COMPTABLE


#22551 – Lors de la création de comptes 
 par import, les options "centralisé", "échéance" et 
 "lettrable" sont prises en compte.


#22564 - Il est possible de supprimer des 
 coordonnées bancaires de tiers via la comptabilité.


### SOLDES INTERMÉDIAIRES DE GESTION


#19105 – La personnalisation des comptes 
 dans le modèle "Détaillé" des SIG est conservée après validation.


#21509 – L'impression des SIG s'effectue 
 en paysage par défaut.


#21510 – Activation de l'option "Imprimer 
 sur une seule page" dans l'impression des SIG.


#22411 – Désactivation de l'ouverture d'un 
 extrait de compte vide en N-1 dans les SIG détaillés.


#22616 – Ajout d'un titre contenant le 
 nom de la société, la date est l'heure, dans les modèles d'impression 
 des SIG.


#22620 – Désactivation de l'ouverture de 
 l'extrait de compte par un double clic dans les cellules du SIG ne contenant 
 pas de paramétrages de comptes.


### IMMOBILISATIONS


#17222 – Mise en place d'un outil de création 
 des immobilisations par import.


#20907 – Mise en place d’un outil de comptabilisation 
 en masse d’une sélection d’immobilisations. (Acquisitions / Dotations 
 / Cessions / Sorties)


#22348 – Mise en place d’une option de 
 comptabilisation des dotations aux amortissements, mensuelle, trimestrielle, 
 semestrielle ou annuelle.


#22821 – Les immobilisations en sommeil, 
 ne sont plus prises en compte dans la comptabilisation en masse.


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


