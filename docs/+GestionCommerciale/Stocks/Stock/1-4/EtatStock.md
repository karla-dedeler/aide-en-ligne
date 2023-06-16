# Etat du stock



L’état du stock d’un article permet pour un ou plusieurs dépôts de :


* Consulter le détail 
 des quantités pour un article donné,
* Consulter éventuellement 
 ses équivalences,
* Sélectionner une 
 ligne,
* Créer une ligne 
 de stock.


 


Les deux dernières options ne sont disponibles qu’en création de documents 
 et de fiches d’assemblage uniquement.


 


Cet état est disponible depuis le menu STOCKS/Stock et le menu contextuel 
 :


* De la liste des 
 articles,
* De la grille de 
 saisie d'une pièce de ventes ou d'achats ou de stocks,
* De la grille de 
 la consultation de l'état de stock d'une commande (appeler depuis 
 la liste des documents de ventes ou d’achats)
* De la grille des 
 composants d’une fiche d'assemblage,
* De la grille de 
 recherche articles (CTRL+R sur la liste des articles).


## Entête : définition de la consultation


### Article à consulter


L’article de référence renseigné par défaut est celui sur lequel vous 
 étiez positionné lors de la demande de l’état de stock. Il reste modifiable 
 par la liste déroulante.


 


Suivant le [paramétrage 
 de la fiche article](../../../Articles/1/Article/OngletInfos/ArticleOngletInfos.md), le logiciel vous propose automatiquement les 
 articles équivalents, le groupe d’équivalence ou l’article de remplacement. 
 Par la sélection ou non du champ, vous avez la possibilité d’afficher 
 ou non ces lignes d’articles équivalents dans la grille de consultation.


### Stock


Ce champ permet d’obtenir le stock en cours avec ou non prise en compte 
 des articles dont la quantité en stock est égale à zéro.


### Décomposition de la grille


Il est possible de [décomposer](../1-3/OptionsDecompositionStock.md) 
 (bouton Décomposer) la grille.


### Choix du dépôt


L’état de stock peut être demandé sur un dépôt (Unique), sur plusieurs 
 dépôt à sélectionner (Ensemble) ou sur la totalité des dépôts (Tous).


### Gamme / N° de Lot


Ces deux champs sont accessibles uniquement lorsque l’article de référence 
 gère [les gammes](../../../Articles/Gammes/2/Gamme/Gamme.md) 
 et/ou les [numéros 
 de lot](../../NumerosLots/2/Numéros_de_lots_de_A_à_Z.md).


 


Plusieurs possibilités sont à votre disposition pour la [sélection des gammes](../../../Articles/Gammes/5/SelectionValeursComposantesGammes.md) et/ou [la sélection des 
 numéros de lot](../../NumerosLots/Trier/Selection_d_un_numero_de_lot_dans_un_document.md).


## Grille de consultation


L’état du stock affiche les quantités par dépôt pour l’article de référence 
 et ses équivalences si vous avez souhaité les avoir.


 


La colonne des Priorités affiche le code priorité des équivalences (G : groupe d’équivalence, R : article de remplacement, Chiffre : article équivalent avec 
 priorité).


 


Lorsque l’article ou l’un de ses équivalents gère les gammes et/ou les 
 lots, les colonnes du même nom sont renseignées.


 


Lorsque vous gérez les articles [périssables](../../NumerosLots/Trier/ArticlePerissable.md), vous 
 disposez dans les propriétés de la grille de plusieurs champs spécifiques.


 


Ces champs et beaucoup d’autres peuvent être afficher ou non par l’appel 
 des propriétés du menu contextuel.


 


Ce même menu vous permet :


* De sélectionner 
 une ligne,
* D’afficher les 
 lots périmés (si l’article est périssable),
* D'épurer les gammes 
 et/ou les numéros de lot,
* D’activer la recherche 
 automatique,
* D’accéder aux fonctions 
 générales des grilles.


## Pied : création d’une ligne de stock


Cette partie apparaît uniquement lors de l’appel de l’état du stock 
 à partir du menu contextuel :


* De la grille de 
 saisie d’une pièce de ventes ou d’achats ou de stocks,
* De la grille des 
 composants d’une fiche d'assemblage.


 


La création d’une ligne de stock supplémentaire s’effectue par la sélection 
 du bouton Nouveau puis de différents paramètres :


* Un article 
 : celui de référence ou un équivalent ou de remplacement,
* Un dépôt,
* Un emplacement 
 : l’emplacement indiqué ici est uniquement à titre indicatif. Il sera 
 reporté dans la ligne de stock de l’onglet stock de la fiche article.


 


Si l’article gère les gammes, vous aurez également 
 la possibilité de sélectionner une gamme inexistante à l’aide de la vue 
 standard ou cartésienne,


 


Si l’article gère les numéros de lot, vous aurez 
 également la possibilité de créer une ligne avec un numéro de lot inexistant, 
 ainsi que de renseigner la date de péremption.


 


Le menu contextuel de la fenêtre vous permet de rafraîchir l’état du 
 stock.


 


Après avoir saisi vos informations, si vous cliquez sur :


* Le bouton Enregistrer, vous resterez sur la 
 fenêtre et une nouvelle ligne apparaîtra dans la grille de consultation,
* Le bouton Valider, la fenêtre se fermera automatiquement 
 et vous retournerez sur la fenêtre de saisie du document.


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
 FilePopupInit('a2');
 FilePopupInit('a3');
//]]>
