# Saisie d'un inventaire



Avant de créer une pièce d’inventaire, il est nécessaire [d'ouvrir 
 (préparer)](PreparationInventaire.md) votre inventaire.


 


La création de pièces d’inventaire passe par la commande Nouveau document 
 d’inventaire du menu STOCKS.


 


Vous pouvez également créer une nouvelle pièce à partir de la Documents 
 de stock du menu STOCKS. Un bordereau de saisie peut être dans un premier 
 temps imprimé puis complété.


## Entête


Une saisie d’inventaire est obligatoirement associée à un dépôt et donc 
 à l’inventaire courant.


 


La génération des lignes d’articles à inventorier peut être manuelle 
 ou [automatique](GenerationAutomatiqueLignesInventaire.md) 
 (Bouton Génération Auto).


## Lignes d’inventaire


Les lignes d’inventaire peuvent être saisies manuellement ou être générées 
 automatiquement pour une sélection d’articles.


 


Une ligne d’inventaire est obligatoirement composée d’un code et d’un 
 libellé article, d’un conditionnement et de la quantité inventoriée en 
 stock.


 


Le même article pourra être introduit uniquement 
 s’il a un conditionnement ou une gamme ou un numéro de lot différent.


 


Le prix des articles inventoriés est affiché en fonction du [calcul du prix de revient](../../../Articles/1/Article/SelectionPrixRevientDocuments.md) (sur article ou sur stock).


 


Le menu contextuel vous permet :


* d'insérer une ligne
* de supprimer une 
 ligne
* d'imprimer le bordereau 
 de saisie
* de paramétrer les 
 préférences notamment d’ajouter des colonnes


### Référence article


Pour appeler un article, vous avez la possibilité de saisir le code 
 article, le code à barre, le libellé court, la désignation ou encore la 
 référence constructeur de [l'article](../../../Articles/1/Article/Article.md). 
 Pour rechercher un article dans la liste, tapez le début du code ou de 
 la désignation et la liste déroulante se positionnera sur le 1er article 
 commençant par ces caractères.


### Cas particulier :


Pour un article gérant les numéros de lot, la 
 sélection d’un numéro de lot est obligatoire par la liste déroulante (u 
 F4). La création d’un numéro de lot est possible par la combinaison de 
 touche F4 + F2. De plus, vus avez la possibilité de saisir la date de 
 péremption du lot. Cette date devient obligatoire lorsque l’article est 
 périssable.


 


La saisie de la zone de stockage est également prise en compte.


 


Pour un article gérant les [gammes](../../../Articles/Gammes/2/Gamme/Gamme.md), 
 la sélection d’une gamme est obligatoire par la [vue standard](../../../Articles/Gammes/2/Gamme/VuesStandardCartesienne.md) 
 ou [cartésienne](../../../Articles/Gammes/2/Gamme/VuesStandardCartesienne.md).


### Quantité


Vous disposez de 3 champs de quantités :


* la quantité en 
 stock correspond à la quantité en stock à la date de l’inventaire
* la quantité inventoriée 
 peut être saisie à tout moment avant validation de l’inventaire
* l'écart en quantité 
 entre la quantité saisie et la quantité en stock à la date de l'inventaire


 


Pour éditer un bordereau de saisie, laissez 
 à zéro les quantités inventoriées que vus compléterez ensuite.


### Conditionnement


Le logiciel propose soit l’unité de conditionnement de stock soit l’unité 
 de conditionnement de vente en fonction des choix définis dans les préférences 
 de la gestion mais vous avez la possibilité de modifier l’unité de conditionnement 
 par défaut dans la liste déroulante.


 


Tant que l’inventaire n’est pas validé, le logiciel traite les quantités 
 dans les différents conditionnements.


 


A la validation de l’inventaire, le logiciel convertit les quantités 
 inventoriées en nombre d’unités de conditionnement de vente.


## Pied de document


Une zone commentaire vous permet de saisir du texte, des informations 
 complémentaires concernant le document.


## Bordereau de saisie d’inventaire


Un bordereau de saisie des lignes d’inventaire (sans quantité) peut 
 être imprimé afin d’être complété par les différentes personnes responsables 
 de l’inventaire.


 


Il suffit de saisir ou de [générer 
 automatiquement](GenerationAutomatiqueLignesInventaire.md) les lignes des articles à inventorier puis de cliquer 
 sur le bouton Imprimer.


 


Dès que vus enregistrez votre saisie d’inventaire, 
 le logiciel génère la pièce d’inventaire correspondante et lui attribue 
 automatiquement un numéro de pièce.


 


Pour revenir sur ces lignes d’inventaire, il suffit de réouvrir la pièce 
 d’inventaire par la commande "[Documents 
 de stock](../../Documents/Liste/RechercheListeDocumentsStock.md)" du menu STOCKS.


## Modification et gestion des pièces d’inventaire


La commande "Documents de stock" du menu STOCKS vous permet 
 de modifier une pièce d’inventaire, de compléter les quantités d’une pièce 
 avant validation de l’inventaire, de consulter et d’imprimer le détail 
 d’une pièce d’inventaire.


## Génération automatique des lignes d'inventaire


Le choix des articles peut s’effectuer sur l’ensemble du stock ou uniquement 
 sur les articles référencés dans le dépôt.


 


La sélection des articles s’effectue pour :


* un article Unique
* un ensemble d'articles 
 (Avancée)
* tous 
 les articles


 


Le bouton [Définir](../../Trier/ZoneSelectionUnPlusieursArticles.md) 
 permet de choisir l’ordre de tri de vos lignes d’inventaire : code article, 
 famille, sous-famille, type, catégorie ou zone de stockage.


 


Afin de limiter le traitement de la génération automatique, vous pouvez 
 déterminer un nombre maximum de lignes à générer.


 


Vous pouvez également demander la génération des lignes pour les articles 
 ayant une quantité en stock non nulle.


 


Une quantité par défaut peut être demandée: la Quantité en Stock, une 
 quantité nulle (pour les bordereau de saisie), une quantité commune à 
 tous les articles.


 


Pour l'inventaire complet, la quantité en stock est la suivante :


* si la date d'inventaire 
 est > ou = à la date du jour et si on fait une génération automatique 
 du stock alors la quantité qui apparaîtra dans notre fiche de saisie 
 sera = au stock actuel
* si la date d'inventaire 
 est < à la date du jour et si on fait une génération automatique 
 du stock alors la quantité qui apparaîtra dans notre fiche de saisie 
 sera = au stock au dernier jour de cette date d'inventaire


 


Le prix unitaire de l’article peut-être affecté automatiquement à l’article 
 inventorié.


 


Ce prix est celui de référence (PUMP ou DPA ou PMA ou …) du dernier 
 mouvement antérieur à l'inventaire (si celui ci est non nul) sinon il 
 est celui de la fiche article.


 


Vous pouvez saisir un libellé qui sera affecté à chaque mouvement (ligne 
 d’inventaire) lors du traitement de la génération automatique des lignes. 
 Par défaut aucun libellé n’est affecté aux lignes d’inventaire.


 


Une fois votre paramétrage réalisé, vous pouvez lancer le traitement 
 de la génération automatique à l'aide du bouton "Générer".


 


A la fin du traitement, un message vous indique le nombre de lignes 
 générées. Suite à la fermeture de cette fenêtre (bouton Fermer), vous 
 accéder à la visualisation de votre bordereau d'inventaire.


## Différence entre inventaire complet et inventaire tournant


Pour un inventaire Complet, 
 la validation génère un mouvement d’inventaire de type Comptabilisés, 
 consultable à partir de la commande "Mouvements de stock" du 
 menu STOCKS et met à jour le stock Inventaire. Le logiciel met également 
 à jour les lignes de mouvements dans la fiche des articles et du dépôt.


 


Pour un inventaire Tournant, 
 le logiciel génère une pièce d’écart de stock dans laquelle il enregistre 
 tous les écarts constatés entre le stock Actuel et le stock inventorié.


## Calcul des quantités en stock


Les quantités saisies dans vos pièces d’inventaire sont automatiquement 
 traitées et converties en quantité d’unité de conditionnement de vente 
 si celles-ci sont saisies dans une unité de conditionnement différente.


 


Si des mouvements de stock (ventes, achats, livraison, réception,…) 
 ont été enregistrés entre la date d’inventaire et la date de validation, 
 le logiciel les prend en compte afin que votre stock reste cohérent.


## Exemple


A la date d’ouverture de l’inventaire au 31/12/2007, voici les quantités 
 inventoriées : 10 Articles ART1 et 15 articles ART2


Au 01/01/2008, les ventes suivantes sont réalisées : 1 Article ART1 
 et 2 articles ART2


Au 02/01/2008, les achats suivants sont enregistrés : 2 articles ART1 
 et 1 article ART2


Les quantités en stock après validation de l’inventaire au 03/01/2008 
 seront les suivantes : 11 Articles ART1 (10–1+2) et 14 articles ART2 (15-2+1)


## Comment votre stock est-il valorisé ?


Le logiciel prend automatiquement le dernier prix à la date de l’inventaire, 
 soit le PMP, le DPA, le PMA, ou encore le prix moyen, suivant le type 
 de stock.


 


Lors d’un premier inventaire, si aucune entrée n’a encore été valorisée, 
 le logiciel prend alors le prix de revient indiqué dans la fiche article.


## Écarts de stock/inventaire


L’impression Écarts de stock/Inventaire permet d’obtenir pour chacun 
 des articles la quantité et la valeur du stock avant et après validation 
 de l’inventaire ainsi que l’écart.


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
 FilePopupInit('a2');
 FilePopupInit('a3');
//]]>
