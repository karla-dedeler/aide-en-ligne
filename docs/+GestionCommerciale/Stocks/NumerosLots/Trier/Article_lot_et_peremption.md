# Article lot et péremption



## Article gérant les lots et la péremption


Lorsque l‘article lot gère la péremption, vous avez la possibilité [d'afficher des colonnes supplémentaires](Peremption_Champs_disponibles_dans_tous_les_documents.md) pour suivre cette 
 gestion. Pour les documents pris en compte dans le stock, vous disposez 
 d’[autres colonnes](Peremption_Champs_disponibles_dans_les_documents_de_stock.md).


 


De plus des messages d'avertissements ou bloquants peuvent être paramétrés.


## Article périssable


Un article périssable est un article ayant le [mode 
 de gestion ’'lot''](../../../Articles/1/Article/OngletStock/ArticleOngletStock.md).


 


Si des lignes de stock existent pour cet article, vous pourrez transformer 
 l’article en périssable, uniquement si la [date de péremption](DatePeremption.md) 
 est renseignée sur toutes les lignes.


## Article périmé


Un article périmé est un article pour lequel la [date limite 
 de commercialisation](../../../Articles/1/Article/OngletStock/DelaiCommercialisation.md) est dépassée.


 


C‘est à dire que la date limite de commercialisation est inférieure 
 à la date de référence (date du document appelant, date système…).


 


Lors de l’appel d’un article dans un document, vous pouvez déterminer 
 dans les préférences de la gestion si vous souhaitez avoir un avertissement 
 ou un blocage pour vous informer que l’article est périmé.


 


De plus, il est possible de visualiser les lots périmés ou non par une 
 coche dans le champ "Périmé ?" STK\_PERIME (disponibles dans 
 les propriétés de la grille).


## Date de péremption


Une date de péremption est la date à laquelle un article ne peut plus 
 être vendu/consommé. A cette date, l’article est définitivement périmé.


 


Elle est affecté à un article/gamme gérant les lots dans un dépôt précis.


 


Cette date peut être renseignée lors de :


* La création de numéro de lot 
 en saisie d’un document,
* La création ou modification 
 de numéro de lot dans l'onglet stock de la fiche article.


## Date limite de commercialisation


La date limite de commercialisation est la date pour laquelle il est 
 préférable que l’article ne soit plus commercialisé.


 


Elle n’est pas saisissable, elle est calculée en fonction de la [date de péremption](DatePeremption.md) et du [délai de commercialisation](../../../Articles/1/Article/OngletStock/DelaiCommercialisation.md) 
 de la fiche article.


 


Le calcul de celle-ci est : Date de péremption - délai de commercialisation

