# Réparer une base de données

Lorsque la base de données est corrompue, la meilleure solution est 
 d’effectuer une restauration de la base de données depuis une sauvegarde 
 (backup), et non pas de tenter de réparer la base de données.


 


Toutefois, la commande DBCC CHECKDB 
 présente un certain nombre d’options qui peuvent être utilisées pour réparer 
 la base de données.


 


**ATTENTION**, certaines options peuvent générer des PERTES 
 DE DONNEES et ne doivent être utilisées qu’en dernier recours. 
 


## Options


### REPAIR\_FAST


L’option REPAIR\_FAST effectue les réparations mineures qui prennent 
 peu de temps et n’amènes pas de perte de données.


### REPAIR\_BUILD


L’option REPAIR\_BUILD procède à une vérification et à une réparation 
 globale qui nécessite plus de temps mais sans risque de perte de données. 
 L’option REPAIR\_BUILD nécessite que la base de données soit en mode mono-utilisateur.


### **REPAIR\_ALLOW\_DATA\_LOSS**


L’option **REPAIR\_ALLOW\_DATA\_LOSS** réalise toute les tâches de REPAIR\_BUILD 
 et ajoute les tâches supplémentaires pouvant conduite à une **PERTE DE DONNÉES** (Allocation 
 et suppression de lignes pour corriger des problèmes structuraux et des 
 erreurs de pages et suppression d’objets textes corrompus).


## **Recommandations**


Lorsque vous cherchez à résoudre des problèmes de base de données :


 


Commencez par REPAIR\_FAST ou REPAIR\_REBUILD


 


Si cela ne suffit pas, utilisez 
 l’option **REPAIR\_ALLOW\_DATA\_LOSS**, mais attention, ne perdez pas 
 de vue que l’option **REPAIR\_ALLOW\_DATA\_LOSS** peut conduire à une 
 **PERTE INACCEPTABLE DE DONNÉES IMPORTANTES**. Je vous recommande 
 fortement d’effectuer une sauvegarde de la base de données avant d’utiliser 
 l’option REPAIR\_ALLOW\_DATA\_LOSS


 


Pour assurer la récupération de la base de données dans son état d’origine, 
 nous vous suggérons de placer la commande DBCC dans une transaction pour 
 examiner les résultats et annuler la transaction si nécessaire.


## Pour en savoir plus


<https://msdn.microsoft.com/fr-fr/library/ms176064%28v=sql.120%29.aspx>


