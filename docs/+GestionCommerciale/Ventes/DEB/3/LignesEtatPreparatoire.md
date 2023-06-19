# Lignes de l'état préparatoire
Lors du lancement du calcul permettant la remontée des lignes, 3 options 
 sont à votre disposition :


 


* Afficher la totalité des lignes 
 sans les regrouper par article : Si cette option est décochée, 
 les montants seront regroupés par code article.
* Exclure les articles dont le code 
 nomenclature produit n'est pas renseigné : Si cette option 
 est décochée, les articles dont le code intracommunautaire n'est pas 
 renseigné dans la fiche article seront exclus.
* Calculer à partir des bons de livraison 
 et de retour, au lieu des factures et avoirs


 


Vous avez également la possibilité, depuis le menu contextuel accessible 
 via un clic droit dans la grille, d'ajouter des lignes de déclaration 
 manuelles, de supprimer une ligne ou d'ouvrir le document à l'origine 
 ou l'article concerné.


 


Ces lignes sont regroupées en fonction du [niveau 
 d’obligation](SeuilsDeclaration.md) :


#### Niveau 3 et 4 (simplifié)


Les lignes sont regroupées par nomenclature produit et numéro de TVA 
 intracommunautaire acquéreur.


##### Composition de la ligne


Le bouton Calculer génère automatiquement une ligne par article sur 
 la période de référence avec les informations suivantes :


* [Nomenclature du produit](../2/ParametrageArticles.md),
* [Pays](../2/ParametrageTiers.md) de destination ou 
 de provenance (code pays de l’adresse de livraison du client ou code 
 pays de l’adresse de facturation du fournisseur),
* Valeur fiscale qui correspond au montant Brut HT,
* [N° de TVA intracommunautaire](../2/ParametrageTiers.md) 
 de l'acquéreur (uniquement pour les expéditions).


 


Vous devez saisir [le Régime](CodesRegimes.md) (code sur 
 2 chiffres) qui fixe la nature de l'opération.


#### Niveau 1 et 2 (détaillé)


Les lignes sont regroupées par nomenclature produit, numéro de TVA intracommunautaire 
 acquéreur, condition de livraison et mode de transport.


##### Composition de la ligne


Le bouton Calculer génère automatiquement une ligne par article sur 
 la période de référence avec les informations suivantes :


* [Nomenclature du produit](../2/ParametrageArticles.md),
* [Pays](../2/ParametragePays.md) de destination ou de 
 provenance (code pays de l’adresse de livraison du client ou code 
 pays de l’adresse de facturation du fournisseur),
* Valeur fiscale qui correspond au montant Brut HT,
* Valeur statistique qui est égale à la valeur fiscale augmentée 
 des frais accessoires,
* [Masse nette](../2/ParametrageArticles.md) exprimée 
 en kilos sans décimale (Pour obtenir le calcul de celle-ci [cliquez 
 ici](CalculMasseNette.md)),
* Nature de la transaction qui décrit la nature de l'opération réalisée 
 (11: vente ferme, 41 : expédition de biens destinés à faire l’objet 
 d’un travail à façon...),
* [Conditions de livraison](../2/CodesConditionsLivraison.md),
* [Modes de transport](../2/CodesModesTransporst.md),
* [Pays](CodesPays.md) d'origine, uniquement pour les 
 introductions,
* [N° de TVA intracommunautaire](../2/ParametrageTiers.md) 
 de l'acquéreur (uniquement pour les expéditions).


 


Vous devez saisir :


* [Le Régime](CodesRegimes.md) (code sur 2 chiffres) 
 qui fixe la nature de l'opération,
* Le Département qui correspond au département français d'origine 
 ou de destination du flux,
* Les Unités supplémentaires, pour certains articles qui ne se mesurent 
 pas en kilos (litres, carats...). Elle 
 ne comporte pas de décimale. Les unités comprises entre 0 et 1 sont 
 codifiées 1.


 


