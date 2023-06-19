# Transfert des lignes en multi sélection dans un document


Cette fenêtre est accessible lorsque vous avez effectué une copie de 
 lignes à partir d’un document et que vous souhaitez les coller dans un 
 autre document qui correspond à un transfert de document.


 


Cette fenêtre est en 4 parties :


* Information sur 
 le nombre de lignes à traiter,
* Information sur 
 le document d’origine,
* Informations sur 
 le document destinataire,
* Options des lignes 
 que vous allez recopier.


## Information sur les lignes


En dessous du titre de la fenêtre, une ligne vous indique que vous réalisez 
 un transfert ou une copie de X lignes sur Y lignes. Si toutes les lignes 
 du document d’origine sont sélectionnées, cette ligne indiquera un transfert 
 ou une copie de(s) Y lignes.


 


X représente le nombre de lignes que vous souhaitez copier.


 


Y représente le nombre de lignes présentes dans le document d’origine.


 


C’est à vous de choisir si vous souhaitez réaliser un transfert (description 
 du traitement ci-dessous) ou une copie de lignes.


## Information sur le document d’origine


Les informations du document d’origine sont :


* Le type de document,
* Le numéro du document,
* Le libellé du tiers,
* Le pays du tiers.


 


Ces informations ne sont pas modifiables.


## Informations sur le document destinataire


Les informations du document destinataire sont : 


* Le type de document,
* L’état du document,
* Le libellé du tiers,
* Le pays du tiers.


 


Ces informations ne sont pas modifiables.


## Options des lignes que vous allez recopier


Les options de recopie de lignes sont :


* De créer des articles 
 inexistants (de manière interactive),
* La sélection manuelle 
 des quantités à transférer : Si cette option est sélectionnée, lors 
 de la validation de la fenêtre de copie de ligne, vous aurez une fenêtre 
 de sélection ou non des lignes et quantités à transférer.


* L’affectation manuelle 
 des gammes, N° de lot ou N° de série,
* La recopie des 
 gammes,
* La recopie des 
 lots,
* La recopie des 
 lignes de forfait,
* La recopie des 
 prix.


 


Les 4 dernières options 
 seront accessibles uniquement si parmi les lignes à copier, il y a des 
 articles de type [gammes](../../../../Articles/Gammes/2/Gamme/Gamme.md), [lots](../../../../Stocks/NumerosLots/2/Numéros_de_lots_de_A_à_Z.md), [forfait](../../../../Articles/1/Article/OngletGeneral/TypeArticle.md) 
 et que des pris sont renseignés.


 


Si le transfert est partiel, vous pouvez choisir 
 de :


* Gérer en reliquat 
 les quantités d’articles non livrés,
* Ne pas gérer en 
 reliquat les quantités d’articles non livrés,
* Ne pas faire le 
 transfert si les quantités en stock sont insuffisantes


Dans le dernier cas, l’accusé réception restera 
 en état "En-cours" et aucun Bon de livraison ne sera réalisé.


 


Lorsque vous avez sur votre document d’origine 
 un article gérant les gammes ou les numéros de lot et que vous n’avez 
 pas renseigné la gamme ou le numéro de lot sur celui-ci, vous devez sélectionner 
 l’affectation manuelle des gammes 
 ou n° lot ou n° de série. 
 


 


Suite à la validation de la fenêtre et suivant le document destinataire, 
 si vous copiez des articles gérants les gammes ou les lots, vous devez 
 sélectionner l’affectation manuelle des gammes ou n° lot vous aurez alors 
 une fenêtre d’[affectation des gammes 
 ou des lots](../4/AffectationGammeLot.md).


 


De même pour les articles en mode gestion "sérialisé", vous 
 aurez la fenêtre de [sélection 
 des numéros de série](../../../../Stocks/NumerosSeries/5/AffectationNumerosSeries.md).


## Effets du transfert de lignes


Après validation de la fenêtre, le transfert va créer :


* Les lignes à copier 
 en fin de document uniquement (pas d’insertion possible comme pour 
 la copie de lignes),
* Une ligne blanche 
 pour séparer les données déjà présentes dans le document destinataire 
 et les données qu’il va copier,
* Une ligne de commentaire 
 référençant le document d’origine.


 


A la fin de l’opération, le document d’origine passe en état transféré 
 (si reliquat) ou en état supprimé et est enregistré. Le document destinataire 
 est enregistré avec les lignes transférées.


