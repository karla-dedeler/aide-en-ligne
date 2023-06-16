# Types de documents de stock



## L’entrée/la sortie de stock


La ligne est composée d’une [référence 
 article](../../../Articles/1/Article/OngletAutre/ArticleOngletAutre.md), d’un libellé, et d’une quantité entrée/sortie dans son conditionnement. 
 Un nouveau prix peut éventuellement être saisi (pour le bon d’entrée uniquement) 
 et un libellé du mouvement.


 


Une entrée en stock peut ou non être valorisée. Lorsque vous enregistrez 
 une entrée de stock, le logiciel génère tous les mouvements correspondants 
 et met à jour la valeur de votre stock en prenant en compte soit le prix 
 de revient de votre article, soit le prix d’achat saisi, pour une entrée 
 en stock uniquement.


 


Le prix de revient dépend des mouvements précédemment enregistrés et 
 du [type 
 de stock](../../../Articles/1/Article/OngletStock/ArticleOngletStock.md) : PUMP, DPA, ….


## La perte


L’enregistrement d’une perte fonctionne comme une sortie de stock à 
 ceci près que le type de perte doit obligatoirement être sélectionné et 
 que le mouvement de perte augmente le stock Perte au lieu du stock Sorties.


## L’écart de stock


L’enregistrement d’un écart de stock ne mouvemente ni les entrées ni 
 les sorties. Vous indiquez un écart positif ou négatif et vous sélectionnez 
 le type d'altération de stock. Lors de la validation d'un inventaire tournant, 
 si le logiciel rencontre une différence entre le stock actuel et la quantité 
 inventoriée, une pièce d’écart de stock est automatiquement générée.


 


Une pièce d’écart d’un montant nul, correspond à un inventaire tournant 
 sans aucune différence de stock


## Le transfert de dépôt à dépôt


Le transfert de dépôt à dépôt permet de basculer des articles d’un dépôt 
 d’Origine vers un dépôt de Destination.


 


Cette opération équivaut donc à enregistrer en une seule opération: 
 un mouvement de sortie dans le dépôt d’Origine et un mouvement d’entrée 
 dans le dépôt Destination.


 


La ligne de transfert est obligatoirement composée d’un code et d’un 
 libellé article, de la quantité à transférer et du conditionnement. Vous 
 pouvez éventuellement saisir un libellé du mouvement.


 


Lorsque vous enregistrez le transfert, le logiciel génère tous les mouvements 
 correspondants dans chacun des dépôts et met à jour la valeur du stock 
 des deux dépôts.


 


La sortie est valorisée au prix de revient de l’article dans le dépôt 
 d’Origine et l’entrée est valorisée avec ce même prix


## La fiche d’assemblage


Consulter Fiche d'assemblage [Fiche 
 d'assemblage](../Fiche/Assemblage/FicheAssemblageNomenclatures.md).


## Inventaire


Consulter Fiche d'inventaire


