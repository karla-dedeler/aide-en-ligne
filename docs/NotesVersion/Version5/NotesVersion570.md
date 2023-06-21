# Version 5.7.0 du 14/01/2016
 


#### ACHATS ET VENTES


`#14013` – Ajout dans la fiche article d’une 
 zone permettant la saisie d’un message et d’une option permettant d’afficher 
 ce message lors de la saisie de l’article dans les documents (achats, 
 ventes et stocks).


`#16084` – L’import de lignes de document 
 contrôle que les articles ne sont pas en sommeil.


`#16117` – Il est désormais possible de copier 
 le contenu de n’importe quelle cellule d’une grille en cliquant sur la 
 cellule puis par le menu contextuel « Copier la cellule » ou par le raccourci 
 clavier Ctrl+C.


`#16154` – L’import de document contrôle 
 que le tiers n’est pas en sommeil.


`#18897` – Le code article obligatoire est 
 contrôlé que le document soit créé par saisie, transfert, duplication, 
 ajout de lignes ou import.


`#19788` – Ajout du champ « Nomenclature 
 produit DEB » dans la personnalisation des listes dans les documents.


`#19851` – Le curseur clignotant est bien 
 visible dans l’ensemble des cellules lorsqu’on saisit.


`#19958` – Champ « Quantité à livrer » renommé 
 en « Quantité à réceptionner » dans le transfert partiel côté achats.


`#20206` – Le bouton « Nouveau » dans la 
 fenêtre de sélection à partir du stock n’est accessible que pour les articles 
 gérés par numéro de lot ou gamme.


`#20242` – L’acompte est bien repris lors 
 du transfert d’un document, le statut de l’échéance liée est bien conservé 
 et le net à payer et cohérent.


`#20246` – Le contrôle de la non sélection 
 d’une gamme dans les documents se fait au post de la ligne pour l’ensemble 
 des documents d’achats, ventes et stocks.


`#20258` – Correction du contrôle incohérent 
 « Numéro de lot obligatoire manquant » lors de l’import de ligne de documents 
 pour des articles non gérés par numéro de lot.


`#20246` – Les lignes d’un même article ne 
 sont pas cumulées dans le message d’avertissement sur le stock à terme.


`#20268` – Ajout du champ « Raison sociale 
 » dans la personnalisation de liste des documents.


`#20303` – Clarification de l’affichage du 
 code article dans le rapport d’importation.


#### ACTIONS


`#16562` – L’ordre par défaut de classement 
 des actions est inversé pour afficher la plus récente en haut de liste.


`#19953` – Le libellé des champs personnalisés 
 des actions est bien affiché dans la personnalisation de liste dans les 
 tiers.


#### ARTICLES


`#15465` – « Géré en contremarque » n’est 
 plus modifiable dans la fiche article lorsqu’on a uniquement le droit 
 de consulter.


`#18924` – Correction de la violation d’accès 
 lors de l’ouverture des mouvements de stock depuis une fiche article ouverte 
 à partir d’une fiche fournisseur.


`#19212` – Correction de l’indice de liste 
 hors limite lorsqu’on rend disponible un numéro de série réservé.


`#19950` – Ordre de tabulation de l’onglet 
 Autre de la fiche article modifié pour respecter l’ordre des champs.


`#20265` – Le champ image des fiches Articles, 
 Immos et Tiers a été scindé en deux, un champ Image et un champ Format 
 Image permettant ainsi de récupérer l’image en claire.


#### BANQUES


`#19836` – Modification du masque de saisie 
 du type de coordonnées bancaires Pologne.


#### CONTACTS


`#17167` – Les informations du contact (commercial, 
 famille, sous-famille, …) sont bien actualisées lors de la modification 
 de ces informations dans le tiers associé.


`#19085` – La famille et la sous-famille 
 sont bien affectées aux contacts créés depuis la fiche tiers. 


`#20194` – Ajout d’une zone commentaires 
 associée à l’adresse dans la fiche contact. 


#### DÉPÔTS


`#20282` – L’affichage du stock dans la fiche 
 dépôt respecte bien la taille de la fenêtre et ne reste pas en minimisé.


#### ENCAISSEMENTS ET DÉCAISSEMENTS


`#17196` – Les échéances faisant parties 
 d’un règlement multiple ne correspondant pas au montant total sont bien 
 considérées comme soldées si elles sont totalement réglées.


`#18900` – La colonne «État du règlement 
 » est maintenant triable dans les fenêtres des règlements. 


`#18920` – Ajout de la date de relance dans 
 les champs disponibles pour les modèles de relances RTF. 


`#19202` –  Code devise du compte au 
 lieu du code devise du règlement pour la position 235 dans les fichiers 
 au format virements internationaux.


#### ERGONOMIE


`#20228` – Ajout d’une option dans les Préférences 
 utilisateur permettant d’afficher les lignes horizontales dans les listes.


#### PERSONNALISATION DES LISTES


`#18899` – La variable « Est nulle » dans 
 les filtres sur des champs de type dates permet bien de filtrer les données 
 sans date. 


`#20314` – Correction de l’erreur Echec de 
 l’assert lorsqu’on utilise « >> » dans la personnalisation de liste 
 avec un champ personnalisé de type séparateur.


#### RÉAPPROVISIONNEMENTS


`#18456` – Le stock de l’article n’est plus 
 doublé dans le calcul du besoin lorsque l’article est également composant 
 de nomenclature. 


#### REGROUPEMENT AUTOMATIQUE


`#20180` – Correction du blocage BL indiqué 
 comme verrouillé par un autre utilisateur lorsqu’on regroupe des BL antérieurs 
 avec des BL postérieurs à l’inventaire.


#### STOCKS


`#16414` – Ajout dans le menu contextuel 
 de la saisie de l’inventaire de l’accès au détail des ventes et des achats 
 par article. 


`#18396` – Le filtre sur la gamme est bien 
 conservé dans le stock des numéros de série lorsqu’on verrouille pour 
 mettre à jour. 


`#19057` – Le dépôt sélectionné est bien 
 conservé lorsqu’on passe du stock des numéros de séries aux mouvements 
 de stock des numéros de séries.


`#19098` – Plus de violation d’accès après 
 avoir retiré la colonne « N° de lot 1 » dans les composants de la fiche 
 d’assemblage.


`#19941` – La réservation des numéros de 
 série sur les devis se fait bien dans le stock.


`#19956` – Ajout des champs Type d’article, 
 Type de gamme et Lot ou série dans la personnalisation de liste de l’inventaire.


`#20198` – Il n’est plus possible de sélectionner 
 un autre dépôt que celui du document dans la sélection à partir du stock.


`#20252` – Le stock des composants non gérés 
 en stock n’est plus décrémenté lors de l’import d’assemblage. 


#### TACHES EN LIGNE DE COMMANDE


`#20266` – Possibilité de déclencher par 
 tâche en ligne de commande l’import des tiers, contacts et articles.


 #20280 – Les valeurs du paramètre 
 permettant d’indiquer si la première ligne contient le nom des champs 
 est désormais Oui ou Non au lieu de 0 ou 1. 


#### TARIFS ET PROMOTIONS


`#19288` – Ajout d’une option dans les promotions 
 permettant de cumuler la remise de la promotion et/ou d’imposer le prix 
 de la promotion avec la grille de tarifs ou le tarif article.


`#20267` – Option « Exception » dans les 
 promotions renommée  en « Imposée ».


#### TRANSFERT COMPTABLE


`#17009` – Ajout du pays dans la personnalisation 
 de liste des documents de ventes et d’achats dans la sélection du transfert 
 comptable.


#### UTILISATEURS ET SALARIES


`#17802` – Possibilité d’accéder à la liste 
 des utilisateurs lorsqu’on ne fait pas partie du groupe Admin, mais pas 
 à la liste des groupes.


#### EDI


`#20295` – Suppression de la fenêtre indiquant 
 le code article et affichée devant la fenêtre d’import EDI. 


#### ÉCRITURES


`#17243` – Ajout du libellé du mode de règlement 
 dans la personnalisation de la liste de la saisie des écritures.


`#18763` – La saisie au kilomètre ne verrouille 
 plus les périodes utilisées lorsque la saisie est terminée.


`#19154` – Le type d’échéance « Sur quoi 
 » est correctement renseigné en cas d’échéances multiples affectées depuis 
 l’écriture.


#### ÉTATS FINANCIERS


`#20144` – Plus de code erreur et PDF bien 
 généré à l’impression PDF du compte de résultat.


#### JOURNAUX


`#15373` – Augmentation de la taille du code 
 journal pour le passer à 10 caractères. 


`#16028` – Dans l’impression des journaux 
 le tri « Standard » a été renommé en tri par « Ordre de saisie » au côté 
 du tri par « Date » ou « Pièce ». 


#### PLAN COMPTABLE


`#19543` – Augmentation de la taille du code 
 tiers pour le passer à 20 caractères et du compte pour le passer à 25 
 caractères. 


`#20165` – Plus d’erreur « Nom de colonne 
 MVN\_CODE ambigu » lors de l’ajout du code du modèle analytique dans la 
 personnalisation de la liste du plan comptable.


 


 


![](../assets/images/Version5/Images/Modules_de_l_ERP.png)


