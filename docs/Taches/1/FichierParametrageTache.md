# Fichier de paramétrage d'une tâche

Chaque tâche nécessite un fichier de paramétrage .ini composé des 3 sections suivantes :


## [Tâche]








| Paramètre | Description | Présence |
| --- | --- | --- |
| Nom | Identifiant de la tâche | Obligatoire |
| Journal | Fichier dans lequel seront enregistrés des événements au cours de l'exécution de la tâche. Si le chemin n'est pas précisé, alors il sera créé dans le même dossier que le fichier de paramètre de la tâche. | Facultatif |
| Statistiques | Fichier dans lequel pourront être enregistrées des statistiques à la fin de l'exécution de la tâche, dans un format INI, permettant d'être lues par un programme informatique | Facultatif |


## [Société]










| Paramètre | Description | Valeurs possibles | Présence | Valeur par défaut |
| --- | --- | --- | --- | --- |
| Fichier | Chemin et nom du fichier de connexion .Gestimum <br> Si le chemin n'est pas précisé, le fichier doit se trouver dans le dossier C:\ProgramData\Gestimum |   | Obligatoire |   |
| Utilisateur | Code utilisateur ERP |   | Obligatoire |   |
| MotPasse | Mot de passe de l'utilisateur ERP |   | Facultatif |   |
| Deconnecter | Déconnecter l'utilisateur déjà connecté avec ce nom | Oui <br>Non | Facultatif | Non |
| Exclusif | Interdire aux autres utilisateurs de se connecter | Oui <br>Non | Facultatif | Non |


## [Paramètres]


La liste des paramètres est propre à chaque tâche.


 


L'option en ligne de commande /descriptiontache permet d'afficher à l'écran la liste des paramètres d'une tâche.


