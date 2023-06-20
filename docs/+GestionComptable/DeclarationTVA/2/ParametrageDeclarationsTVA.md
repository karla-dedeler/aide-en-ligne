# Paramétrage des déclarations de TVA



La déclaration de TVA diffère d’un pays à l’autre. C’est pourquoi, le 
 logiciel vous permet de programmer votre propre paramétrage des déclarations 
 de TVA.


 


Le paramétrage des déclarations de TVA permet de définir les regroupements 
 et les lignes de la déclaration de TVA.


 


Aucun calcul n’est effectué dans cette fenêtre.


## Modalités pour pouvoir effectuer le paramétrage


### Droit


Vous devez avoir sélectionné par le menu SOCIETE/Utilisateurs le droit 
 Paramétrer sur l’option Traitements/Déclaration de TVA pour pouvoir lancer 
 ce traitement.


## Réalisation du paramétrage


La fenêtre de paramétrage vous permet de saisir le détail du paramétrage 
 (onglet regroupements) puis de définir les lignes en fonction de celles 
 de la déclaration de TVA (onglet lignes).


### Paramétrage par défaut


Un paramétrage par défaut est disponible dans le répertoire Bases sous 
 la racine de Gestimum. Les fichiers contenant les informations sont :


* CA3 France.TVARegroupement,
* CA3 France.TVALignes.


 


Ceux-ci correspondent aux onglets Regroupements et lignes et peuvent 
 être importés.


 


Sur chaque onglet, le bouton "Importer" permet d’insérer le 
 paramétrage par défaut présent dans les fichiers "CA3 France.TVARegroupement" 
 et "CA3 France.TVALignes".


 


Le menu contextuel de chaque onglet permet également cet import.


### Onglet regroupement


Cet onglet permet de définir en détail les comptes de toutes les lignes.


 


Le bouton Importer et le menu contextuel permettent de réaliser l’import 
 du fichier par défaut des regroupements de TVA.


 


Par ce menu, il est également possible d’imprimer le paramétrage ainsi 
 que d’accéder aux informations générales des grilles.


 


La ligne peut être de type regroupement ou détail.


 


La ligne de regroupement comporte :


* Un code,
* Un libellé,


* Une coche dans 
 la colonne regroupement.


 


Chaque ligne détail comporte :


* Un code,
* Un libellé,
* Une nature : Ventes 
 (Débits), Ventes (Encaissement), Encaissements (Ventes), Immobilisations, 
 Biens et services, Achats (Décaissements),
* Un taux,
* Une racine de base 
 (compte de charge ou produit),
* Une racine de provision 
 (compte de TVA),
* Une opération (France, 
 UE, Export, DOM-TOM, Imposable, Non imposable …).


 


Sur chaque ligne le code, le libellé et la nature sont obligatoires.


 


Il est possible de modifier chaque ligne et même d’en insérer.


#### Insertion d’une ligne


En fin de grille, vous pouvez saisir le code, le libellé puis le paramétrage 
 souhaité. Lors de la validation de la ligne (flèche basse), celle-ci se 
 positionnera automatiquement dans la suite chronologique de la ligne.


 


Le menu contextuel permet également l'insertion et la suppression d'une 
 ligne.


 


Une fois ce paramétrage effectué, vous devez définir les regroupements 
 de vos différents codes afin de réaliser le paramétrage des lignes de 
 TVA.


### Onglet lignes


Cet onglet permet de définir les lignes de la déclaration de TVA avec 
 les formules qui regroupent les différentes lignes de l’onglet regroupement.


 


Le bouton Importer et le menu contextuel permettent de réaliser l’import 
 du fichier par défaut des regroupements de TVA.


 


Par ce menu, il est également possible d’imprimer le paramétrage ainsi 
 que d’accéder aux informations générales des grilles.


 


Chaque ligne comporte :


* Un code,
* Un libellé,
* Une section : TVA 
 brute due, TVA déductible, TVA nette,
* Une base : dans 
 cette colonne, vous devez saisir les codes des lignes de l’onglet 
 regroupement qui correspondent à la base de calcul de la taxe de cette 
 ligne,
* Une provision : 
 dans cette colonne, vous devez saisir les codes des lignes de l’onglet 
 regroupement qui correspondent au calcul de la taxe de cette ligne.


 


Sur chaque ligne le code, le libellé et la base sont obligatoires.


 


Il est possible de modifier chaque ligne et même d’en insérer.


#### Insertion d’une ligne


En fin de grille, vous devez saisir le code, le libellé puis le paramétrage 
 souhaité. Lors de la validation de la ligne (flèche basse), celle-ci se 
 positionnera automatiquement dans la suite chronologique de la ligne.


 


Une fois ce paramétrage effectué, vous pouvez ouvrir la liste des déclarations 
 de TVA et créer une nouvelle déclaration de TVA.


