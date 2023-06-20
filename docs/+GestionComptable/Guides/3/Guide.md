# Guide



Un guide est décrit par un code, un intitulé, un type (Ventes, Achats, 
 Trésorerie ou Opérations Diverses) et des lignes d’Écriture.


Vous pouvez également définir un journal et un libellé automatique par 
 défaut.


## Type du guide


Le type du guide doit correspondre au type 
 des journaux dans lesquels le guide sera utilisé.


 


Différents contrôles seront ainsi effectués par le logiciel. Par exemple, 
 l’appel des guides dans un journal affichera uniquement les guides de 
 même type que le journal. De plus, en définition du guide, les sens seront 
 respectés.


## Journal par défaut


Le journal par défaut sera automatiquement proposé en saisie guidée.


## Libellé automatique par défaut


Le libellé automatique du guide sera uniquement repris en saisie guidée. 
 Lorsque le guide est utilisé dans une écriture automatique, le logiciel 
 prend en compte le libellé automatique de la pièce appelante.


## Lignes du guide


La définition des lignes du guide doit être effectuée avec le plus grand 
 soin.


 


Avant de commencer à paramétrer ces lignes, il est indispensable de 
 déterminer :


* Par quel moyen 
 ce guide va être activé,
* Quelles sont les 
 informations connues et les informations à saisir.


 


Une ligne de guide est décrite par un compte, un libellé, un sens, un 
 montant ou une formule et une quantité.


 


Pour chaque ligne, vous devez déterminer les informations qui seront 
 saisies ou modifiables à l’appel du guide et celles qui seront fixes.


 


A partir de là, il vous suffit de rendre ou non accessible telle ou 
 telle information en cochant la case située à côté de celle-ci


### Compte


Il est possible d’indiquer :


* Un compte 
 comptable existant,
* Un compte 
 collectif,
* Un compte 
 de regroupement,
* Une racine 
 de compte (par exemple 607, tous les comptes commençant par 
 607 seront proposés lors de la saisie guidée)
* Ou de laisser la zone vide (uniquement pour la 
 saisie guidée).


 


Toutefois, les restrictions suivantes sont à apporter lorsque le guide 
 va être lié à une écriture automatique : sur la première ligne, il faut 
 renseigner le compte qui fera appel à cette écriture automatique et sur 
 les lignes suivantes, il faut éviter d’indiquer un compte de regroupement 
 sinon on perd une grande partie de la puissance des Écritures automatiques.


 


Si vous sélectionnez le champ GDL\_CPTSS, la saisie du compte sera possible 
 et vous pourrez passer alternativement d’un compte à saisir à un commencement 
 de compte sinon vous n’aurez pas accès à la zone compte.


### Libellé


Le libellé de l’écriture sera automatiquement repris sauf en cas d’appel 
 du guide à partir d’une écriture automatique. Dans ce cas, le logiciel 
 prend comme libellé de base celui de la première écriture.


 


Le signe "=" permet de prendre le libellé de la ligne précédente.


 


Si vous sélectionnez le champ GDL\_LIBSS, la saisie du libellé de l’écriture 
 sera possible sinon vous n’aurez pas accès à la zone Libellé.


### Sens


Saisissez C ou D ou double-cliquez pour passer d’un sens à un autre. 
 Ce choix n’est plus modifiable à l’appel du guide.


### Montant ou formule


Il est possible d’indiquer un montant fixe, une formule de calcul ou 
 de laisser la zone vide.


 


La colonne M (champ GDL\_FORMSS) permet de rendre ou non cette zone accessible 
 en saisie guidée, pour une saisie ou une modification éventuelle.


#### Comment définir une formule ?


Pour définir votre formule de calcul, voici les éléments à votre disposition 
 :


* Les opérateurs 
 de base : \*, /, 
 + , -


* Les parenthèses 
 : ( et ),


* Les constantes 
 numériques définies dans les tables que vous devez saisir précédées 
 du signe $ ($TVA),
* Le montant d’une 
 ligne d’écriture : #x où x 
 est le numéro de la ligne d’écriture dans le guide,
* Le solde de la 
 pièce en cours : #S.


### A retenir


Si le guide est utilisé avec les écritures automatiques, la première 
 ligne du guide ne sert que pour le paramétrage dans les journaux (seul 
 le compte est utile dans ce cas là) car la première ligne sera la ligne 
 d’appel dans la saisie standard.


### Quantité


Si la gestion des quantités est sélectionnée dans le paramétrage de 
 la société, vous avez la possibilité de saisir des quantités pour les 
 comptes autorisés.


 


Si vous sélectionnez le champ GDL\_QTESS, la saisie des quantités lors 
 de la saisie de l’écriture guidée sera possible sinon vous n’aurez pas 
 accès à la zone quantité.


 


[Voir aussi](javascript:RelatedTopic0.Click())


Voir aussi (espace réservé)
 

1. [Liste des rubriques](#)



