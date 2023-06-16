# Articles


La gestion d’une gamme pour un article s’effectue par l’affectation 
 d’un code gamme définie dans [les fiches 
 Gammes](../2/Gamme/Gamme.md) et la mise en place des différents tarifs de la gamme.


## Affectation de la gamme


Lors de la création de la fiche article, vous pouvez sélectionner dans 
 la liste déroulante une gamme. Celles-ci sont créées par le menu ARTICLES/[Gammes](../2/Gamme/Gamme.md).


 


Elle doit être choisit avant que vous demandiez l’enregistrement de 
 la fiche article car elle fait partie de la clé du code article. Une fois 
 la fiche article enregistrée, le champ est grisé et l’article est considéré 
 comme gérant [les gammes](../1/Etapes.md).


 


Conséquences de l’affectation :


* Un article gérant 
 les gammes ne peut être de type Nomenclature ou forfait. Mais un article 
 gérant les gammes peut être un composant d’une nomenclature ou d’un 
 forfait,
* Un article gérant 
 les gammes ne peut avoir de tarif multidevises,
* Un article gérant 
 les gammes peut avoir le mode de gestion lot ou série.


## Prix de l’article associé à une gamme


Les articles gérant les gammes peuvent avoir des prix multiples en fonction 
 des éléments de la gamme sélectionnés et non en fonction des devises (article 
 ne gérant pas les gamme).


### Référentiel


Les articles gérant les gammes ont un tarif référentiel. 
 C’est le prix de base de l’article.


 


Lorsque les éléments de la gamme n’ont pas de tarif spécifique c’est 
 le tarif référentiel qui sera pris en compte.


### Prix spécifique


Il est possible de définir un prix de vente pour chacun 
 des éléments de la gamme.


 


Pour définir un prix, il faut sélectionner la sous-gamme dans la liste 
 déroulante : seules les sous-gammes pour lesquelles le code a été affecté 
 à la gamme seront proposées.


 


Les prix de la sous-gamme (Prix d'achat, 
 Coefficient, Prix 
 de vente) sont accessibles et permettent de saisir manuellement 
 les valeurs.


 


Si lors de la création de l’article, vous sélectionnez les éléments 
 de la gamme avant d’avoir renseigner les prix d’achat et de vente du tarif 
 référentiel, vous aurez un message d’avertissement.


 


Par la [mise 
 à jour de tarif](../../1/MiseJourMasse/MiseJourArticlesMasse.md), il est possible de modifier les tarifs référentiel 
 et des sous-gammes des articles gérant les gammes.


## Article gérant les gammes composant d’un article de type nomenclature 
 ou forfait


Les articles gérant les gammes peuvent être [les 
 composants](../../1/Article/OngletComposants/NomenclaturesForfaits.md) d’une nomenclature ou d’un forfait. Les éléments de la 
 gamme devront être précisés lors de la création de la [fiche 
 d'assemblage](../../../Stocks/Documents/Fiche/Assemblage/FicheAssemblageNomenclatures.md).


## Article gérant les gammes ayant un tarif fournisseur


Dans [l'onglet 
 fournisseurs](../../1/Article/OngletFournisseurs/ArticleOngletFournisseurs.md) de la fiche article gérant les gammes, vous pouvez renseigner 
 l’élément de la gamme pour lequel vous souhaitez affecter une quantité 
 mini, un délai, un prix …


 


[Voir aussi](javascript:RelatedTopic0.Click())


Voir aussi (espace réservé)
 

1. [Liste des rubriques](#)



