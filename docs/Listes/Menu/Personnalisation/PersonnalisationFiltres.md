# Personnalisation des filtres


Pour paramétrer des filtres dans une liste, vous devez sélectionner le menu Propriétés dans le menu contextuel de la liste.


 


Un filtre permet de générer des sous-listes complémentaires à la liste/grille d'origine. Ces sous-listes font apparaître uniquement les données répondant aux critères définis dans le filtre.


 


Un filtre est défini par un nom, un type (Général, Utilisateur ou Groupe) et une ou plusieurs conditions associée(s), applicable(s) sur la liste des données.


## Comment créer un filtre ?


Pour créer un filtre :


1. Saisir le nom du filtre
2. Choisir son type
3. Définir la première condition : variable, relation puis valeur


* + Si le filtre à créer comprend une unique condition, il suffit de cliquer sur le bouton Ajouter pour enregistrer la condition dans la zone vierge puis cliquer sur le bouton Enregistrer le filtre
	+ Si le filtre à créer est multi-conditions, il faut choisir, après avoir défini la première condition, l'opérateur logique ET ou OU qui liera la première condition à la suivante. Pour cela, il faut cliquer sur ET ou OU pour respectivement activer/désactiver l'opérateur logique. La condition peut maintenant être sauvegardée avec le bouton Ajouter et la condition suivante peut être créée. Lorsque toutes les conditions sont créées, le filtre peut être enregistré


4. Enregistrer le filtre par le bouton enregistre, puis fermer la fenêtre par le bouton ok.


 


Si vous créez un filtre sans cliquer sur le bouton Enregistrer, la fermeture par la croix pose la question de l’enregistrement ce qui évite de perdre le filtre saisi.


## Liste des filtres


Cette zone fait apparaître les différents filtres au fur et à mesure de leur création. Pour travailler sur un filtre, il suffit de le sélectionner pour que les zones situées sur la droite décrivent les conditions associées au filtre.


## Duplication d'un filtre


Il suffit de sélectionner un filtre existant et de cliquer sur le bouton Dupliquer. Le logiciel propose comme Nom de filtre «Copie de xxx», il suffit alors de modifier ou non le nom puis de cliquer sur le bouton Enregistrer.


## Nom du filtre


En création d'un filtre, il suffit de saisir le nom du filtre. Celui-ci sera repris comme nom d'onglet pour afficher la sous-liste.


## Type du filtre


Le type du filtre permet de rendre accessible les sous-listes en fonction des utilisateurs ou des groupes. Le type Général affiche la sous-liste quelque soit l'utilisateur, le type Utilisateur propose la sous-liste et donc le filtre uniquement pour l'utilisateur courant, le type Groupe propose la sous-liste à tous les utilisateurs appartenant au même groupe que l'utilisateur courant.


## Liste des conditions


Cette zone affiche le contenu de ou des conditions paramétrées pour le filtre courant. Pour modifier le contenu d'une condition, il suffit de la sélectionner pour voir apparaître son détail. Après modification, il suffit de cliquer sur le bouton Enregistrer.


### Définition d’une condition


* Zone Variable : la variable est à saisir ou à sélectionner dans la liste déroulante
* Zone Relation : la relation à appliquer est à choisir dans la liste déroulante. Son contenu dépend du type de la variable sélectionnée: Date, Numérique, Logique, Chaîne. La Relation Contient est disponible uniquement si vous utilisez un moteur SQL,
* Zone Valeur : saisir la formule, le montant, la date, l'information nécessaire à la condition. La formule peut être composée des quatre opérateurs de base : +, -, \* et / ainsi que des parenthèses. Lien entre plusieurs conditions lorsque la condition est reliée à une condition suivante, choisissez l’opérateur nécessaire. L'opérateur ET rend la condition EXCLUSIVE (les données doivent répondre à toutes les conditions), l'opérateur OU rend la condition INCLUSIVE (les données doivent répondre à l'une des conditions).


## Exemple de filtre sur la liste des documents


Pour obtenir un filtre affichant les documents de type Facture et les documents de type Avoir, celui-ci doit contenir deux conditions : l'une qui filtre les documents de type Facture, l'autre qui filtre les documents de type Avoir. Le lien entre les deux conditions est OU et non ET car sinon aucun document ne s'afficherait puisqu'un document ne peut être à la fois de type Avoir et de type Facture.


Obtenir les factures et les avoirs signifie filtrer les documents qui sont soit de type Avoir, soit de type Facture.


