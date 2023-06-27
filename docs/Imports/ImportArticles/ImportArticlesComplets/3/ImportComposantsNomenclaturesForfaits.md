# Import de composants de nomenclatures ou forfaits


Cet import se réalise depuis l’import d’article et concerne la table 
 002 : Table ART\_PROD (Composants des articles de type Forfait ou Nomenclature).


 


Pour chaque import, il est obligatoire d’avoir au minimum la table 001 
 avec le code article et la désignation (même pour une mise à jour).


 


Important !


 


L’importation des nomenclatures ou des forfaits est possible uniquement 
 dans le cadre d’une mise à jour. Toutes les fiches des articles contenant 
 et composants doivent donc être créés avant importation.


 


Pour importer une nomenclature ou un forfait, 
 il faut importer autant d’enregistrements qu’il y a de lignes de composant.


 


L’enregistrement doit contenir obligatoirement 
 : le type de l’article contenant (TYPE\_LIGNE, c’est à dire Forfait ou 
 Nomenclature), le code de l’article contenant (ART\_CODE), le numéro d’ordre 
 du composant dans la grille (PROD\_LIGNE, de 001 à 999), le code de l’article 
 composant (PROD\_CODE).


 


Pour les lignes de nomenclatures, le prix est obligatoirement celui 
 de l’article composant, il est impossible d’indiquer un autre tarif.


 


Pour des lignes de forfait, le prix d’un composant peut être modifié 
 par l’import (PROD\_PRIX).


