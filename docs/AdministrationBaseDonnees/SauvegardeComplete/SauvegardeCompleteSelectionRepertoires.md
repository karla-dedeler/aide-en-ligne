# Sélection des répertoires

Dans cet écran, vous devez indiquer le nom du serveur et les répertoires 
 partagés sur celui-ci.


## SERVEUR SQL


Vous devez renseigner le nom du serveur sur lequel se trouve le dossier.


Par exemple : ServeurSQL


## RÉPERTOIRE TEMPORAIRE


Important :


Il n'est pas possible de faire une sauvegarde directe d'une base SQL 
 du serveur depuis un poste client.


Sur le serveur, un répertoire doit être créer sur un disque local (exemple 
 C:\Sauvegarde). Ce répertoire doit être accessible à partir du ou des 
 postes client qui lanceront la sauvegarde de Gestimum.


Vous devez paramétrer les droits nécessaires.


 


Ainsi, vous pourrez saisir le nom de ressource partagée sur le serveur 
 ainsi que le nom du répertoire correspondant (par exemple C:\Sauvegarde). 
 Ces informations seront conservées pour les prochaines sauvegardes.


## Ressources réseaux détectées


Vous devez saisir ici le nom du répertoire partagé sur le serveur. C’est 
 ce répertoire qui contiendra la sauvegarde.


Pour notre exemple, vous devrez saisir \\ServeurSQL\Sauvegarde.


Ce chemin sera utilisé pour copier la sauvegarde du serveur vers le 
 chemin définitif indiqué sur la fenêtre suivante.


## Nom du répertoire correspondant sur le serveur


Vous devez indiquer ici le chemin réel sur le serveur (Par exemple : 
 C:\Sauvegarde ) .


Quelque soit le poste qui lance la sauvegarde, ce chemin sera utilisé 
 pour effectuer la sauvegarde à partir du serveur dans le répertoire Sauvegarde 
 du lecteur C:\.


