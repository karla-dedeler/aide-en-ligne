# Gestion analytique



La gestion analytique offre des possibilités d’analyse supplémentaire 
 sur votre société. Cette gestion est à activer dans les préférences de 
 la société, onglet Comptabilité.


 


Un plan analytique est une organisation centrée sur un critère particulier 
 à analyser (ex: suivi des ventes par type de produits, suivi des charges 
 et des produits par services, ...). Chaque plan est composé de sections 
 analytiques de type Général, appartenant éventuellement à des sections 
 de type Regroupement suivant une codification hiérarchisée. Voir [Exemple](ExemplePlanAnalytique.md).


## Paramétrage des plans et des coûts


### Plan analytique


Pour chaque analyse, il est nécessaire de créer un plan analytique par 
 les tables de votre société.


 


Lors de la ventilation analytique de vos charges et de vos produits, 
 il sera possible d’effectuer autant de répartition analytique que de plans 
 créés.


 


Un plan est défini par un code, un libellé et un état Obligatoire ou 
 non. L’état Obligatoire a pour conséquence de rendre obligatoire la saisie 
 analytique sur ce plan pour les comptes définis en Saisie analytique Obligatoire.


### Coût analytique


Facultatif. Un coût analytique permet de réunir des sections de type 
 Général afin d’éditer une balance analytique avec rupture sur coût.


## Sections analytiques


Avant de créer vos sections, il est nécessaire de déterminer leur organisation 
 afin de les hiérarchiser.


 


Une section est définie par un code, un libellé, un type et, pour les 
 sections de type Général, un rattachement à un plan et éventuellement 
 à un coût analytique.


### Codification et type


Le type Regroupement permet de créer des sections de classification 
 sur lesquelles aucune affectation ne pourra être effectuée.


 


Une section analytique de type Général est toujours au niveau le plus 
 bas de l’organisation et correspond à un élément d’affectation de gestion.


 


C’est par la codification des sections que la hiérarchie des sections 
 s’effectue. Pour qu’une section appartienne à une section de type Regroupement, 
 son code doit commencer par le code de la section de regroupement (voir 
 [Exemple](ExemplePlanAnalytique.md)).


### Rattachement


Une section analytique Général doit obligatoirement être rattachée à 
 un plan et éventuellement à un coût analytique (à définir dans les tables).


 


Dans [l'exemple](ExemplePlanAnalytique.md), 
 les sections 941, 951, 9631 concernent le secteur Informatique de votre 
 société, vous pourriez donc les rattacher au coût analytique : Informatique, 
 tout comme les sections 942, 952, 9632 qui concerne les ventes d'Électroménager 
 que vous pourriez rattacher au coût Électroménager.


## Paramétrage de l’analytique


Une fois vos sections créées, il est nécessaire de choisir le :


### Paramétrage des comptes


Une fois vos sections sont créées, il est nécessaire d’activer la [Saisie 
 analytique](../../PlanComptable/2/CompteOngletGeneral.md) dans la fiche de chacun des comptes de charges et de produits 
 à suivre analytiquement (onglet Général), puis éventuellement de définir 
 une [répartition 
 analytique](../../PlanComptable/2/CompteOngletAnalytique.md) par plan (onglet Analytique).


## Paramétrage du transfert de l’analytique à partir de la gestion commerciale


Pour déterminer le paramétrage de l’[ici](../Trier/ParametrageAnalytiqueGestionCommerciale.md).


