# Exécution de plusieurs tâches
Lorsque vous avez plusieurs tâches à lancer, vous pouvez les lancer 
 soit en parallèle, soit en série.


 


Attention, exécuter 2 tâches en parallèle requiert que 1) chaque tâche 
 utilise un code utilisateur spécifique, et que 2) le code de débridage 
 autorise à ces 2 utilisateurs de se connecter simultanément.


 


Pour exécuter plusieurs tâches en parallèle, il faut écrire "call" 
 au début de chaque ligne de commande.


 


Par exemple, pour paralleléliser un import de documents d'achat et un 
 import de documents de vente :


call "C:\Program Files\Gestimum\Taches\ImportDocumentsAchat.bat"


call "C:\Program Files\Gestimum\Taches\ImportDocumentsVente.bat"


 


Le fichier ImportDocumentsAchat.bat 
 doit contenir la commande suivante :


"C:\Program Files\Gestimum\GestimumGestion.exe" 
 /tache:"C:\Program Files\Gestimum\Taches\ImportDocumentsAchats.ini"


 


Le fichier ImportDocumentsVente.bat 
 doit contenir la commande suivante :


"C:\Program Files\Gestimum\GestimumGestion.exe" 
 /tache:"C:\Program Files\Gestimum\Taches\ImportDocumentsVentes.ini"


