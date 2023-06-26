# Fichier Gestimum Gestion Commerciale 1.5 à largeur variable
## Type de fichier


Fichier texte à largeur variable.


 


Séparateur de champs : Virgule.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures uniquement.


## Exemple de fichier

````
"VTE",09/04/2015,"411C30","FAC15-00021","DUBOIS",09/04/2015,"",1394.64,0.00

"VTE",09/04/2015,"4457220","FAC15-00021","DUBOIS",,"",0.00,232.44

"VTE",09/04/2015,"707100","FAC15-00021","DUBOIS",,"",0.00,1162.20
````

## Structure des lignes d'écritures











| Ordre | Champ | Type | Longueur maximale |   |   | Exemple |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Code journal | Texte | 10 | Entre guillemets |   | "VTE" |
| 2 | Date d'écriture | Date | 10 | Format : JJ/MM/AAAA |   | 09/04/2015 |
| 3 | Numéro de compte | Texte | 25 | Entre guillemets |   | "411C30" |
| 4 | Numéro de pièce | Texte | 15 | Entre guillemets |   | "FAC15-00021" |
| 5 | Libellé de l'écriture | Texte | 60 | Entre guillemets |   | "DUBOIS" |
| 6 | Date d'échéance | Date | 10 | Format : JJ/MM/AAAA |   | 09/04/2015 |
| 7 | Type de TVA | Texte | 1 | Entre guillemets | Valeurs possibles : <br>E : Encaissements <br>D : Débits <br>F : Facturation <br>R : Décaissements <br>1 : Collectée non perçue <br>2 : Débits non perçus | "E" |
| 8 | Montant au débit | Montant |   | Séparateur décimal : Point |   | 1394.64 |
| 9 | Montant au crédit | Montant |   | Séparateur décimal : Point |   | 1394.64 |
| 10 | Code mode de règlement | Texte | 8 | Entre guillemets |   | "CB" |


