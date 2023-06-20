# Lancement depuis un langage de programmation
Si vous êtes développeur, vous pouvez appeler les tâches en ligne de 
 commande depuis vos programmes.


## Exemple en C#


var process = new Process();


process.StartInfo.FileName = "cmd.exe";


process.StartInfo.WorkingDirectory = @"C:\Program 
 Files\Gestimum\GestimumGestion.exe";


process.StartInfo.Arguments = "/tache:"C:\Program 
 Files\Gestimum\Taches\ImportDocumentsAchats.ini"";


process.Start();


