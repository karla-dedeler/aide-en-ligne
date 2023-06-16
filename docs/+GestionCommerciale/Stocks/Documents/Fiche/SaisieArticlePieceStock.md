# Saisie d'article dans une pièce de stock



La saisie d’une référence article existant dans le fichier article appelle 
 automatiquement toutes les informations saisies dans la fiche de l’article 
 et concernant le document courant (libellé, unité de conditionnement, 
 prix, prix en devise,). Ces informations et leurs traitements varient 
 en fonction du [type 
 de l'article](../../../Articles/1/Article/OngletStock/ArticleOngletStock.md).


## Recherche de l’article


Un article peut être appelé par son code article, son libellé court, 
 sa référence constructeur ou encore par lecture ou saisie de son code 
 à barre (voir les Préférences) dans la colonne Article (ART\_CODE). La 
 [liste des articles](../../../Articles/1/ListeArticles.md) 
 s’ouvre par la liste déroulante dans la colonne Article.


 


Pour rechercher un article dans la liste, tapez le début du code ou 
 de la désignation et la liste déroulante se positionnera sur le 1er article 
 commençant par ces caractères.


### Article Gamme


L’affectation de la gamme est obligatoire pour un article gérant les 
 gammes. La liste déroulante vous permet de sélectionner les sous-gammes 
 existantes.


### Article de type Lot


L’affectation d'un numéro de lot est obligatoire 
 sur un document mouvementant une sortie. Pour tous les documents mouvementant 
 une entrée en stock, l’article dit être associé à un lot existant ou à 
 un lot qu’il faut créer.


### Article de type Série


Sur un document mouvementant une entrée en stock, 
 pour chaque série il est nécessaire de définir la fourchette des numéros 
 la composant (la quantité d’article représentant une série de numéro et 
 le premier numéro : le logiciel calcule automatiquement le dernier numéro).


 


Sur tous les documents mouvementant une sortie, 
 l’affectation du numéro de série dit être effectuée manuellement mais 
 reste modifiable par le menu contextuel.


### Nomenclature gérée en stock


Une nomenclature gérée en stock fonctionne comme un article de type 
 Pièce. Les mouvements s’appliquent uniquement sur la nomenclature.


### Nomenclature non gérée en stock


Une nomenclature non gérée en stock fonctionne comme un article de type 
 Pièce.


