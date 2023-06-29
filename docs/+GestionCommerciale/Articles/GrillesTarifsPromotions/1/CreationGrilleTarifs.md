# Création d'une grille de tarifs


## 


## Création d’une grille de tarifs


Une grille est décrite par son code (sur 10 caractères maximum), son 
 libellé et au moins une ligne de tarif.


 


Par le menu contextuel ou les raccourcis clavier, vous pouvez accéder 
 à la liste des tiers pour lesquels la grille de tarif est affectée.


### Saisie des lignes de tarifs


Vous pouvez créer autant de lignes de tarifs que de conditions particulières 
 applicables à un même tiers ou à une famille de tiers. Lorsque plusieurs 
 lignes de tarif concernent un même article, le logiciel respecte [certaines 
 priorités](../4/ConsultationTarifsArticles.md).


### Remise sur famille, sous-famille d’articles et sur article


Saisissez le code de la famille, de la sous-famille ou de l’article 
 puis saisissez la valeur de la remise.


 


Cas particulier: pour les articles gérant [les 
 gammes,](../../Gammes/2/Gamme/Gamme.md) vous n’êtes pas obligé de sélectionner les éléments de la 
 gamme. Si vous souhaitez appliquer un tarif particulier à une gamme précise, 
 vous devez sélectionner celle-ci à l’aide de la [vue standard](../../Gammes/2/Gamme/VuesStandardCartesienne.md) 
 ou [cartésienne](../../Gammes/2/Gamme/VuesStandardCartesienne.md).


 


Vous pouvez appliquer une remise unique ou des remises en cascade. Une 
 éventuelle majoration peut également être paramétrée avec le signe moins (-)devant 
 la valeur (-2% applique une majoration du prix de 2%).


 


Si la remise dépend de la quantité vendue, saisissez la quantité dans 
 la colonne Seuil.


### Prix pour "une famille" ou "une famille et sous famille" 
 ou "un article donné"


Saisissez la référence de la famille ou de la famille + sous-famille 
 ou de l’article, éventuellement [sa 
 gamme](../../Gammes/4/Articles.md) et son prix (par défaut en devise société).


 


Pour définir des prix en devise, indiquez le code de la devise dans 
 la colonne Devise.


 


Si le prix dépend de la quantité vendue ou achetée, saisissez dans la 
 colonne Seuil, la quantité à partir de laquelle le prix sera appliqué.


### Remises en cascade


Les remises en cascade peuvent s’appliquer à une famille, une sous-famille 
 d’articles ou à un article précis. Vous pouvez appliquer jusqu’à 6 remises 
 en cascade.


 


La remise en cascade peut s’appliquer sur :


* Une unique 
 ligne de tarif


Pour cette ligne de tarif, saisissez dans 
 la colonne Remise, chacune de vos remises séparées par le signe +. Par 
 exemple: 10+5+4


* Plusieurs 
 lignes de tarif


Lorsque les remises dépendent d’un seuil 
 de quantité, vous devez créer autant de lignes de tarifs que vous avez 
 de seuils de remises à distinguer


 


Saisissez alors dans chaque ligne de tarif le signe + suivi de la remise 
 (à l’exception de la première ligne).


### Gestion de la grille


Le menu contextuel et les boutons (Ajouter, Filtrer, Annuler le filtre, 
 Modifier) permettent de gérer plus simplement les grilles volumineuses.


 


Pour avoir plus de détail sur le fonctionnement de ces options cliquez 
 ici.


### Menu contextuel de la grille


Par le menu contextuel ou les raccourcis clavier, vous pouvez:


* Insérer 
 une ligne (Ins),
* Supprimer 
 une ligne (Ctrl + Suppr),
* Supprimer 
 toutes les lignes,
* Gérer 
 les créations et modifications de lignes,
* Accéder aux fonctions 
 générales d'une grille.


## Exemples


### Exemple 1


Deux remises sur article sont appliquées : 10% puis 5%. Les deux remises 
 s’appliqueront l’une après l’autre automatiquement selon la formule : 
 


Prix - Remise1 
 - Remise2


Avec


Remise 1 = Prix \* TauxRemise1/100


Remise 2 = (Prix - Remise1) 
 \* TauxRemise2/100


 


Pour un prix article de 10 Euros, vous obtenez un prix remisé de 8,55 
 : 


10 - 1 - 0,45


Avec


1 = 10 \* 10 / 100 


0,45 = (10 - 1) \* 5 / 100


### Exemple 2


Une première remise de 10% est 
 appliquée sur un article puis une remise supplémentaire de 5% 
 à partir de 50 articles vendus/achetés 
 s’applique


 


La première remise (10%) s’applique pour toute vente ou achat de l’article.


 


La deuxième remise intervient uniquement si la quantité d’articles vendus/achetés 
 est supérieure ou égale à 50. Dans ce cas, la remise s’applique sur le 
 prix remisé précédent (voir formule précédente).


### Exemple 3


Une remise de 10% sur une famille 
 d’article ou une remise de 15% 
 à partir de 50 articles vendus/achetés 
 sont appliquées. Chaque remise s’applique pour un certain nombre d’articles 
 vendus/achetés, il n’y a pas de remise en cascade.


### Exemple 4


Pour un même article, deux prix sont définis : l’un en euro (ou devise 
 société), l’autre en dollars.


 


En réalisation de document, le tarif sera appliqué suivant la devise 
 de celui-ci.


