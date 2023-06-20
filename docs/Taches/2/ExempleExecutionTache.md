# Exemple d'exécution d'une tâche

## Exemple de fichier .ini


[Tâche] 


Nom=ImporterDocumentsVente


Journal=ImporterDocumentsVente.log


 


[Société] 


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres] 


FichierImporter=D:\ImporterDocumentsVente.txt


Champs=DOC\_STYPE;PCF\_CODE;DOC\_FPYEUR;DOC\_DATE;ART\_CODE;LIG\_QTE;LIG\_P\_PRV


SeparateurChamps=;


RenommerFichier=Oui


## Exemple de fichier texte


...


## Lancement de la tâche


Pour lancer une tâche, vous devez taper une commande, dans une invite 
 de commandes, ou dans un fichier .bat.


### Invite de commandes


Le commande sera composée :


* du chemin vers l'exécutable de Gestimum Gestion Commerciale 
 ou l'exécutable de Gestimum Gestion Comptable
* de l'option /tache:
* du chemin vers le fichier .ini 
 de paramétrage de la tâche


 


Par exemple, pour la tâche d'import de document de vente, il faut taper 
 ceci dans l'invite de commandes : 


"C:\Program Files\Gestimum\GestimumGestion.exe" 
 /tache:"C:\Program Files\Gestimum\Taches\ImportDocumentsVente.ini"


### Fichier .bat


Cette commande peut aussi être placée dans un fichier ImportDocumentsVente.bat.


