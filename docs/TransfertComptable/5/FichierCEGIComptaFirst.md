# Fichier CEGI Compta First à largeur fixe
## Type de fichier


Fichier texte à largeur fixe.


## Encodage du fichier


ANSI


## Lignes du fichier


Le fichier est constitué de lignes d'écritures. Chaque ligne d'écriture 
 peut être suivie d'une ou plusieurs lignes d'analytique, ou d'une ou plusieurs 
 lignes d'échéances, mais pas les deux.


 


Chaque ligne d'écriture commence par un numéro de compte. Chaque ligne 
 d'analytique commence par 83 espaces. Chaque ligne d'échéance commence 
 par 83 espaces.


## Exemple de fichier

````
C1C30       090415FAC15-00021 VTEDUBOIS     139464+D    O090415     FAC15-00021                                                                                      
4457220     090415FAC15-00021 VTEDUBOIS     23244+C     0+CAA1S3 

707100      090415FAC15-00021 VTEDUBOIS     116220+CO   0+CAA2S3       
````

## Structure des lignes d'écritures








| Position | Champ | Longueur | Format |
| --- | --- | --- | --- |
| 1 | Numéro de compte | 12 | Alpha |
| 13 | Date d'écriture | 6 | JJMMAA |
| 19 | Numéro de pièce | 12 | Numérique |
| 31 | Code journal | 3 | Alpha |
| 34 | Libellé de l'écriture | 25 | Alpha |
| 59 | Libellé complémentaire | 25 | Alpha |
| 84 | Montant en centimes | 11 | Numérique |
| 95 | Signe : + ou - | 1 | Alpha |
| 96 | Sens : D ou C | 1 | Alpha |


## Structure des ventilations analytiques








| Position | Champ | Longueur | Format |
| --- | --- | --- | --- |
| 1 |   | 83 |   |
| 84 | Montant | 11 | Numérique |
| 95 | Signe : + ou - | 1 | Alpha |
| 96 | Sens : D ou C | 1 | Alpha |
| 97 | A | 1 | Alpha |
| 98 | Code section analytique | 12 | Alpha |


## Structure des échéances








| Position | Champ | Longueur | Format |
| --- | --- | --- | --- |
| 1 |   | 83 |   |
| 84 | Montant | 11 | Numérique |
| 95 | Signe : + ou - | 1 | Alpha |
| 96 | Sens : D ou C | 1 | Alpha |
| 97 | Espaces  | 13 | Alpha |
| 110 | Catégorie de tiers | 1 | Alpha |
| 110 | E | 1 | Alpha |
| 112 | Date d'échéance | 6 | JJMMAA |
| 118 | Code journal de trésorerie | 2 | Alpha |
| 120 | Mode de règlement | 1 | Alpha |
| 121 | Numéro de facture | 29 | Alpha |


