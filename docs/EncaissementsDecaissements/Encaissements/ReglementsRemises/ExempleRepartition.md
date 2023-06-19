# Exemple de répartition

## Exemple 1


Soit une banque BQ définie avec une priorité 0 et un plafond à 200,00 
 € et la banque BQ1 définie avec une priorité 1 et un plafond de 300,00 
 €.


 


Rappel ! La priorité 0 est la 
 plus élevée, la 1 est juste en-dessous … et par conséquent la priorité 
 9 arrive en dernière position.


 


Pour chaque échéance, le logiciel recherche dans la banque définie avec 
 la priorité la plus élevée (BQ) si le plafond de remise lui permet de 
 recevoir le montant de l’échéance, si non, il consulte la banque ayant 
 une priorité plus basse …etc.


 


Échéance 1250,00 21/12/2018 BQ1


Échéance 250,00 22/12/2018 BQ


Échéance 3100,00 23/12/2018 BQ


Échéance 4100,00 23/12/2018


Échéance 5100,00 23/12/2018


 


Comme vous le remarquez, les deux dernières échéances ne peuvent être 
 affectées sans dépasser le plafond de remise.


## Exemple 2


Pour les mêmes échéances que l’exemple 1, augmentons le plafond de remise 
 de la banque BQ1 à 350,00 €. Vous obtenez alors cette répartition :


 


Échéance 1250,00 21/12/2018 BQ1


Échéance 250,00 22/12/2018 BQ


Échéance 3100,00 23/12/2018 BQ


Échéance 4100,00 23/12/2018 BQ1


Échéance 5100,00 23/12/2018


## Exemple 3


Inversons maintenant les priorités des journaux sans toucher aux plafonds 
 de l’exemple 1. La banque du journal BQ est définie avec une priorité 
 1 et un plafond à 200,00 € et la banque du journal BQ1 est définie avec 
 une priorité 0 et un plafond de 300,00 € :


 


Échéance 1250,00 21/12/2018 BQ1


Échéance 250,00 22/12/2018 BQ1


Échéance 3100,00 23/12/2018 BQ


Échéance 4100,00 23/12/2018 BQ


Échéance 5100,00 23/12/2018


