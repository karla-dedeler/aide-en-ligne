# Saisie au kilomètre


La saisie au kilomètre (menu Écritures) permet d’enregistrer des écritures 
 les unes à la suite des autres dans différents journaux (ou par la [Saisie Guidée](../Guidee/SaisieGuideeEcritures.md)) 
 et différentes périodes. La fenêtre de saisie au kilomètre est composée 
 d’un entête, d’une grille de saisie et d’un pied.


 


L’entête permet de préciser l’exercice ou la période de saisie et d’appeler 
 un guide de saisie :


* La grille de saisie vous permet 
 de saisir les écritures et tant que vous êtes sur la saisie au kilomètre 
 de modifier et supprimer une ligne écriture. Les boutons donnant accès 
 à la saisie [des 
 échéances](../Standard/Echeancier.md) et de [l'analytique](../Standard/RepartitionAnalytique.md) 
 sont disponibles afin de compléter votre la saisie.
* Le pied de la saisie 
 affiche les informations de totalisation et les raccourcis.


 


Afin de constater en temps réel les écritures de conversion, vous pouvez 
 afficher la fenêtre d'informations.


 


A la fermeture de la fenêtre de la saisie au kilomètre, un contrôle 
 vérifie l’équilibre des écritures passées dans une devise de saisie autre 
 que celle du dossier (en particulier, pour une devise avec un taux de 
 change très faible ou très élevé). Par le menu contextuel, vous pouvez 
 accéder à la pièce déséquilibrée suivante.


 


Ensuite, les écritures sont automatiquement reportées dans les journaux 
 correspondants.


## Entête de la grille


L’entête de la grille de saisie vous donne accès à :


* La sélection d’exercice 
 sur lequel vous souhaitez saisir des écritures,
* La sélection de 
 la période précise (mois) pour laquelle vous souhaitez saisir des 
 écriture,
* l’appel d’ un [guide de saisie](../Guidee/SaisieGuideeEcritures.md).


## Grille de saisie


La grille de saisie permet d’enregistrer les lignes d’écriture pour 
 différents journaux à différentes dates. Tant que vous êtes dans la fenêtre 
 de saisie, vous pouvez modifier et supprimer une ligne écriture.


 


Pour repérer facilement les pièces, le logiciel utilise une couleur 
 pour les lignes paires, une couleur pour les lignes impaires, une couleur 
 pour les écritures de simulation et une couleur pour les écritures réelles 
 (à définir dans les préférences de votre dossier)


 


Le triangle situé sur le bord gauche de la ligne signale la ligne d’écriture 
 courante.


 


Si certaines colonnes de votre grille sont inutiles ou au contraire 
 si vous souhaitez ajouter certaines colonnes, utilisez les propriétés 
 de la grille (menu contextuel).


## Saisie d’une ligne


Vous devez obligatoirement renseigner :


* Le 
 journal : Lorsque le journal gère la contrepartie automatique 
 (exemple: journal de trésorerie), la ligne de contrepartie se génère 
 automatiquement comme pour la [saisie 
 standard](../Standard/SaisieStandard.md).
* La date de l’écriture 
 : Lorsque la date du jour fait partie de la période de saisie sélectionnée, 
 vous aurez celle-ci par défaut,
* Le compte,
* La devise : Vous 
 aurez par défaut la devise du journal,
* Le montant de l’opération.


 


Suite à la validation de la pièce, la ligne suivante vous propose automatiquement 
 le journal, la date, la devise et éventuellement le compte de contrepartie. 
 


 


Ainsi, vous pouvez continuer de saisir sur le même journal pour la même 
 période ou changer la sélection de celui-ci.


## Menu contextuel


Le menu contextuel (clic droit) donne accès à toutes les fonctions de 
 base et à toutes les opérations possibles à partir du journal.


 


Option de base :


* [Ajout de pièce](../Standard/popup/PopupAjoutPiece.md),
* [Suppression de pièce](../Standard/popup/PopupSuppressionPiece.md),
* [Pièce en mode simulation](../Standard/popup/PopupSimulation.md),
* [Guides](../Guidee/SaisieGuideeEcritures.md),
* [Pièce déséquilibrée suivante](../Standard/popup/PopupPieceDesequilibreeSuivante.md),
* [Insérer une écriture](../Standard/popup/PopupInsertionEcriture.md),
* [Ajout d'écriture en fin de 
 pièce](../Standard/popup/PopupAjoutPiece.md),
* [Suppression d'écriture](../Standard/popup/PopupSuppressionPiece.md).


## Option spécifique à la saisie au kilomètre


Effacer les écriture déjà validées : cette option 
 permet de transférer les écritures dans les différents journaux correspondants 
 afin de vider l’écran de saisie


## Option de saisie complémentaire et de consultation


* [Échéancier](../Standard/Echeancier.md),
* [Analytique](../Standard/RepartitionAnalytique.md),
* [Lettrage 
 manuel](../../../Lettrage/2/LettrageManuel.md),
* [Extrait 
 de compte simplifié](../Standard/popup/PopupExtraitSimplifie.md),
* [Extrait 
 de compte par échéances](../../ExtraitCompte/ExtraitCompteParEcheances.md),
* [Extrait 
 analytique](../../ExtraitCompte/ExtraitAnalytique.md),
* Propriétés


 


Les flèches (en bas à gauche de la fenêtre de saisie) vous permettent 
 de déplacer les lignes dans une écriture.


 


Vous disposez également des boutons :


* [Échéancier](../Standard/Echeancier.md),
* [Analytique](../Standard/RepartitionAnalytique.md),
* [Lettrage](../../../Lettrage/2/LettrageManuel.md),
* [Solder](../Standard/popup/PopupSolder.md).


## Pied de la saisie


Les appels de compte définis dans le journal s’affichent ici. Double-cliquez 
 sur le raccourci à utiliser ou tapez en colonne Compte: \* suivi du numéro.


 


Les totaux Débit et Crédit ainsi que les soldes peuvent être :


* Ceux de toutes 
 les écritures du journal (les écritures présentes dans la saisie au 
 kilomètre et celles déjà existantes dans le journal pour la période 
 de l’écriture sélectionnée),
* Ceux de la pièce 
 sélectionnée


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('a1');
 FilePopupInit('a2');
 FilePopupInit('a3');
 FilePopupInit('a4');
 FilePopupInit('a5');
 FilePopupInit('a6');
 FilePopupInit('a7');
 FilePopupInit('a8');
//]]>
