# Import de tarifs et références fournisseurs


Cet import se réalise depuis l’import d’article et concerne la table 
 avec l’identifiant "004: Table ART\_FOURN" (Tarifs Fournisseurs 
 liés aux articles).


Pour chaque import, il est obligatoire d’avoir au minimum la table 001 
 avec le code article et la désignation (même pour une mise à jour).


Cet import concerne l'onglet fournisseur de la fiche article.


 


Les champs obligatoires sont :


* Code fournisseur 
 (PCF\_CODE)
* Priorité (ART\_PFOURN) 
 : il représente la priorité des fournisseurs principaux ("0"…"9"). 
 Si ce champ n’est pas renseigné, dans le fichier importé, il prendra 
 le numéro de la ligne par défaut.


