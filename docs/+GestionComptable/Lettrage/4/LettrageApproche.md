# Lettrage approché


Le lettrage approché est proposé lorsque l’équilibre des écritures sélectionnées 
 en [lettrage manuel](../2/LettrageManuel.md) 
 n’est pas respecté.


 


Le lettrage rapproché constate le montant de l’écart de lettrage et 
 propose l’écriture de régularisation.


## Constat du lettrage


Le lettrage approché détecte automatiquement le code lettrage de la 
 fiche tiers à affecter à la future écriture de régularisation de lettrage.


 


Il a également déterminé l’écart de lettrage (différence entre le montant 
 de l’achat ou la vente et le règlement) ainsi que son sens (solde Débiteur 
 ou Créditeur).


## Écriture de régularisation


Pour la réalisation de l’écriture de régularisation, 
 outre le montant de l’écart de lettrage, vous devez choisir un code journal, 
 une date d’écriture, un type d’écart, un compte et un libellé d’écriture.


### Code journal OD


C’est le journal dans lequel l’écriture de régularisation sera passée.


 


Le logiciel reprend par défaut le code du journal d’OD présent dans 
 les paramètres de la société.


 


Vous pouvez toutefois changer ce journal par un autre de type OD présent 
 dans la liste des journaux.


### Date d’écriture


La date d’écriture par défaut est la date système, vous pouvez éventuellement 
 modifier cette date afin qu’elle corresponde aux Écriture que vous souhaitez 
 lettrer.


### Type d’écart


La sélection du type d’écart détermine les comptes de perte et de gain 
 dans lesquels l’écriture sera passée. 


Celui paramétré par défaut est l’écart de règlement. 


Vous pouvez toutefois le changer par le type de change ou de conversion.


 


Remarque :


Lorsque l’écart est supérieur à celui paramétré dans les préférences 
 de la société, le type n’est pas renseigné par défaut.


En fait c’est à vous de le renseigner et à la validation vous aurez 
 un message d’avertissement vous informant que vous avez dépassé l’écart 
 de tant et il vous permet de valider ou non quand même celui-ci.


### Comptes de perte et de gain


Les comptes de perte et de gain sont renseignés par défaut suivant le 
 type d’écart sélectionné. 


Ces comptes sont définis dans l’onglet comptabilité du paramétrage de 
 la société.


### Libellé écriture


Il correspond au libellé qui sera présent sur l’écriture de régularisation 
 générée


Une fois ces paramètres définis, vous pouvez cliquer sur le bouton Lettrer.


Le logiciel va lettrer les Écritures sélectionnées ainsi que l’écriture 
 de régularisation qu’il a générée.


