# ImporterEcritures

## Nom de la tâche


ImporterEcritures


## Description de la tâche


Importe un fichier d'écritures, comme l'assistant d'import d'écritures.


## Paramètres spécifiques de la tâche









| Nom | Description | Valeurs possibles | Présence |
| FormatFichier | Format de fichier | GestimumComptaVariable : Gestimum Gestion Comptable (longueurs variables)
GestimumComptaFixe : Gestimum Gestion Comptable (longueurs fixes)
GestimumComptaV15 : Gestimum Gestion Comptable version 1.5
GestimumGescomV15 : Gestimum Gestion Commerciale version 1.5
EBPV5V2000 : EBP versions 5 et 2000
EBPV3 : EBP version 3 | Obligatoire |
| FichierEcritures | Fichier d'écritures |   | Obligatoire |
| RenommerFichierEcritures | Nom à donner au fichier des écritures après l'import en cas de succès.
Il est possible d'indiquer un chemin devant le nom du fichier
pour qu'il soit déplacé avant d'être renommé.
Il est possible d'indiquer 2 noms de fichiers séparés par un point-virgule,
le premier utilisé en cas de succès, le second en cas d'échec. |   | Facultatif |
| FichierComptes | Fichier des comptes |   | Facultatif |
| RenommerFichierComptes | Nom à donner au fichier des comptes après l'import en cas de succès.
Il est possible d'indiquer un chemin devant le nom du fichier
pour qu'il soit déplacé avant d'être renommé.
Il est possible d'indiquer 2 noms de fichiers séparés par un point-virgule,
le premier utilisé en cas de succès, le second en cas d'échec. |   | Facultatif |
| Tester | Tester la validité des fichiers sans les importer réellement |   | Facultatif |
| Simulation | Créer les écritures en simulation |   | Facultatif |
| CreerSectionAnalytique | Créer les sections analytiques |   | Facultatif |
| PlanAnalytique | Plan pour créer les sections analytiques |   | Facultatif |


## Exemple


### Fichier .ini


[Tâche]


Nom=ImporterEcritures


Journal=JournalImporterEcritures.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO  


MotPasse=


Deconnecter=Non


Exclusif=Non


 


[Paramètres]


FormatFichier=GestimumComptaVariable


FichierEcritures=D:\Ecritures.txt


Tester=Non


CreerSectionAnalytique=Oui


PlanAnalytique=000


### Fichier .txt


1,28/02/2018,ACH,601101,,GESTIMUM,14,EUR,5000,D,,,0,,FAF20180228-789


>LIBRE,TEST3,100,4000,100,0


2,28/02/2018,ACH,445621,,GESTIMUM,14,EUR,1000,D,,,0,,FAF20180228-789


3,28/02/2018,ACH,401GESTIMUM,,GESTIMUM,14,EUR,6000,C,,,0,,FAF20180228-789


E30/09/2017,VIR45,0,3000


E30/10/2017,VIR45,0,2000


