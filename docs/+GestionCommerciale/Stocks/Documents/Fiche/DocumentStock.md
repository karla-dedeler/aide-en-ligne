# Document de stock



Tous les documents de stock ([entrée de 
 stock](FicheEntreeStock.md), [sortie de stock](FicheSortieStock.md), [Écart](FicheEcartStock.md), 
 [Perte](FicheSortiePertes.md), [Transfert 
 de stock](FicheTransfertStock.md), [Fiche 
 d'assemblage](Assemblage/FicheAssemblageNomenclatures.md)) ont un fonctionnement identique à quelques [différences 
 près](../Nouveau/TypesDocumentsStock.md) selon le type du document.


## Entête


L’entête d’un document de stock comporte nécessairement 
 une date de saisie, un dépôt de stock, un numéro de pièce. Pour chaque 
 pièce, il est possible d’indiquer une référence et de la rattacher à une 
 affaire.


 


Pour un transfert de stock, un dépôt d’Origine et un dépôt Destination 
 doivent obligatoirement être renseignés.


 


La quantité des [différents 
 stocks](../../../Articles/1/Article/OngletStock/ArticleOngletStock.md) pour un article s’affiche en entête de tous les documents de 
 stock. Ces stocks sont toujours affichés en unité de conditionnement de 
 vente.


## Saisie des articles


L'appel d'un article fonctionne comme dans tout document et les informations 
 à introduire dépendent de son type. Voir [Détail](SaisieArticlePieceStock.md).


 


Sur chaque ligne d’article, un menu contextuel donne accès aux opérations 
 suivantes :


* Ajout d’une ligne,
* Suppression de 
 la ligne courante,
* Consultation du 
 stock article et des équivalences,
* Saisie d’un numéro 
 de série,
* Modification des 
 propriétés de la grille.


 


En pied de tous les documents (sauf pour l’assemblage), vous disposez 
 de 2 boutons :


* Génération automatique 
 : suite à la sélection de différents critères vos lignes de mouvements 
 de stock sont générées automatiquement,
* Tout effacer : 
 les lignes de mouvement peuvent être effacées en totalité tant que 
 le document n’est pas en état supprimé,
* D’une zone commentaire 
 vous permet de saisir du texte, des informations complémentaires concernant 
 le document.


## Suivi des document et des mouvements d’entrée/sorties


Les entrée/sorties de stock créés peuvent être modifiés, complétés, 
 consultés et imprimés par la commande [Documents 
 de stock](../Liste/RechercheListeDocumentsStock.md) du menu STOCKS.


 


Tous les mouvements générés par les documents de stock mettent à jour 
 la fiche du dépôt et la [fiche 
 des articles](../../../Articles/1/Article/Article.md) entrés (onglet Stock) et sont accessibles [en 
 "Consultation des mouvements](../../Mouvements/1/MouvementsStock.md)"’.


