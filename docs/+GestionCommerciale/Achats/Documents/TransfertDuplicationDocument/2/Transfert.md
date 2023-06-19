# Transfert d'un document d'achat ou vente


Le transfert d’un document a pour effet de transformer un type de document 
 en un autre type de document, dans la chaîne du processus de vente ou 
 d’achat.


 


Le tiers et les informations contenues dans le document source sont 
 entièrement reprises.


 


Dans tous les cas, le transfert permet :


* De saisir directement le numéro de pièce souhaité (si vus souhaitez 
 une numérotation automatique, vus ne devez rien saisir),
* De préciser la date de réalisation du document,
* De sélectionner le dépôt (pour tous les documents avant le BL 
 ou Factures).


 


Il est possible de récupérer :


* De créer des articles inexistants (de manière interactive) sous 
 certaines conditions,
* Le numéro et le type de la pièce d’origine (sélection de l’option 
 dans les préférences de la gestion) en ligne de commentaire. Lorsqu’un 
 libellé/types de document est présent dans la fiche du Pays de l’adresse 
 de facturation du document d’origine, la ligne de commentaire générée 
 prend en compte ce libellé,
* Les gammes, numéro de lot ou numéro de série,
* Les lignes de texte,
* Les lignes de totalisation (Sous-total et Total).


 


Pour les 2 dernières options, les différentes possibilités de recopie 
 sont disponibles uniquement si les données sont présentes dans le document 
 d’origine (sinon elles sont grisées).


 


Si vous n’avez pas de stock pour un des articles de la pièce que vous 
 transférez, cet article n’apparaîtra pas dans le document de destination


Le document source est automatiquement passé en état "Transféré" 
 (sauf cas particulier). C’est-à-dire qu’il disparaît de la liste des documents 
 à l'état "En cours" mais peut être consulté par une [recherche sur l'état 
 "Transféré"](../../Liste/1/ListeDocumentsAchat.md).


 


A la fin du traitement, les possibles anomalies rencontrées sont affichées 
 dans la fenêtre de validation du transfert [un 
 rapport de traitement](RapportFinTraitement.md).


 


Pour avoir un exemple de rapport cliquez ici .


 


Le transfert s’effectue par le menu contextuel + "Transfert" 
 à partir de :


* La "Liste des documents",
* L’entête de la pièce d’origine.


## Transfert d’un devis


Un devis peut être transférer dans un type de document supérieur (Accusé 
 réception, Bon de livraison, Facture) mais il peut également être transférer 
 en Pro-forma.


Si le devis contient un article non référencé dans la base, une option 
 supplémentaire vous permet de [créer 
 l'article](../5/CréationArticleDuplicationTransfert.md).


## Transfert d’un devis en AR ou document supérieur


Si dans les préférences de la gestion, onglet Ventes, l’option "Contrôle 
 de la référence article" est cochée et que l’option "Devis avec 
 contrôle de la référence article" n’est pas coché, lors du transfert 
 d’un devis, ayant un article non référencé, en AR ou document supérieur, 
 la fenêtre de création de la fiche article est proposée.


## Transfert d’un accusé de réception


Sur un accusé de réception, le transfert permet de passer d’un état 
 de commande à un état de livraison (livraison globale ou partielle) ainsi 
 que d’afficher ou non une quantité à 0 si le stock est absent


### Livraison partielle d’une commande client


Dans le cas d’une livraison partielle, vous pouvez choisir de :


* Gérer en reliquat les quantités d’articles non livrés,
* Ne pas gérer en reliquat les quantités d’articles non livrés,
* Ne pas faire le transfert si les quantités en stock sont insuffisantes.


 


Dans le dernier cas, l’Accusé réception restera en état ‘En-cours’ et 
 aucun Bon de livraison ne sera réalisé.


Ensuite, vous avez la possibilité de choisir la [sélection 
 ou non des lignes et quantités](../3/SelectionLignesQuantitesDuplicationTransfert.md) à transférer.


### Livraison à partir d’un autre dépôt


Le transfert en "Bon de livraison" ou en "Facture" 
 permet de choisir un dépôt différent du dépôt du document source. En combinaison 
 avec la livraison partielle, vous pouvez donc livrer des articles pris 
 dans des dépôts différents.


Création d’une ligne avec une quantité à 0 si stock absent : Cette option 
 vous permet d’afficher les reliquats sur les bons de livraison sans avoir 
 à affecter manuellement la quantité à livrer à 0.


## Transfert d’une commande fournisseur


Sur une commande fournisseur, le transfert permet d’enregistrer une 
 réception d’articles (globale ou partielle).


### Réception partielle d’une commande fournisseur


Dans le cas d’une réception partielle, vous pouvez choisir de :


* Gérer en reliquat les quantités d’articles non livrés,
* Ne pas gérer en reliquat les quantités d’articles non livrés.


 


Ensuite, vous avez la possibilité de choisir la [sélection 
 ou non des lignes et quantités](../3/SelectionLignesQuantitesDuplicationTransfert.md) à transférer.


### Réception à partir d’un autre dépôt


Le transfert en bon de réception ou en facture permet de choisir un 
 dépôt différent du dépôt du document source. En combinaison avec la réception 
 partielle, vous pouvez donc stocker des articles reçus dans des dépôts 
 différents.


