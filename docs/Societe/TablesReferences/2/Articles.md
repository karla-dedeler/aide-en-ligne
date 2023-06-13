# Tables pour les articles



## Critères 1 à 5 sur les articles


Il est possible de définir 5 critères supplémentaires pour les fiches 
 'Article'. Pour chaque critère, il suffit de définir la liste des choix 
 qui apparaîtront ensuite dans la fiche des articles.


## Frais d'approche


Les frais d'approche définis ici pourront être appliqués sur le prix 
 de revient.


 


La colonne Complément permet de définir une formule de calcul utilisant 
 :


 


Le nom d'un champ (poids, prix,... ) Précédé du signe #.


 


Exemples :




|  |  |
| --- | --- |
| Variables | Champs correspondants |
| ART\_P\_ACH | Prix d’achat 
 général |
| ART\_P\_PRV | Prix de revient 
 de l’article |
| ART\_POIDSN | Poids Net de 
 l’article |
| ART\_POIDSB | Poids Brut de 
 l’article |
| ART\_POIDST | Tare de l’article |


 


Les opérateurs suivants :


+ pour une addition,


- pour une soustraction,


/ pour une division,


\* pour une multiplication.


 


Vous pouvez aussi utiliser des [constantes 
 numériques](TablesReferenceGenerales.md) (précédées du signe $).


 


Exemple de formule : pour obtenir 2% du prix de revient, il suffit d’inscrire:


##ART\_P\_PRV \* 0,02 Ou #ART\_P\_PRV \* $P2 (P2 est une [constante 
 numérique](TablesReferenceGenerales.md))


## Formule de prix rendu


À définir uniquement pour gérer le prix rendu (voir les [préférences 
 de gestion](../../PreferencesGestion/2-1/OngletArticles.md)), les formules de prix rendu définies ici seront applicables 
 sur le prix de vente de l'article. Les variables sont identiques à celles 
 des frais d’approche.


