# Version 9.2 build 1061 du 11/12/2020

### ÉVOLUTIONS PRINCIPALES


Cette version intègre : 


 


* La mise en place du transfert en comptabilité de l'analytique de l'affaire à la ligne de document en achat et en vente
* La mise en place de l'import de la main d'œuvre dans le budgété et le réalisé des affaires via IHM et tâches en ligne de commande
* La mise en place de l'import des frais dans le budgété et le réalisé des affaires via IHM et tâches en ligne de commande


 


### Autres évolutions & correctifs (n° de ticket)





#### ACHAT ET VENTE


`#26520` - Correction de l'affichage des adresses de facturation et livraison dans les documents d'achat vente lorsque l'option "Afficher le code de la donnée sélectionnée dans les ..." des préférences utilisateur est activée.


`#26970` - Ajout d'une option dans les préférences de Gestion en achat et en vente permettant de masquer les articles interdits à l'achat et à la vente dans les documents d'achat et de vente.


`#26982` - Ajout dans les préférences de Gestion "Ventes, achats, stocks" d'une option de transfert avec origine du document de type menu déroulant proposant les choix : Aucun, Référence, N° Pièce / Date, N° Pièce / Date / Référence. Si l'option est activée avant migration, alors la valeur N° Pièce / Date / Référence sera mise en place, sinon l'option sera mise par défaut sur "Aucun".


`#27019` - La date de livraison dans les commandes est accessible sans activer l'option de modification des dates de livraison en achat et en vente.


`#27091` - Correction de l'erreur bloquante qui tenait compte uniquement des articles lottés lors du transfert de document avec import de fichier (via IHM ou tâche en ligne de commande) et ne traitait pas les autres types d'articles.


`#27116` - Le transfert de documents d'achat et de vente, avec sélection multiple, ne crée plus d'échéances supplémentaires.


#### STOCK


`#27048` - La duplication d'une facture contenant un article interdit à la vente ou à l'achat n'impacte plus le stock de l'article même si le document n'est pas créé.


#### TIERS


`#27029` - L'absence de saisie du commercial ou de la famille de tiers lors de la création d'un compte tiers depuis le plan comptable n'est plus bloquant même si l'option de champs obligatoires est activée dans les préférences de gestion | Tiers | Champs obligatoires.


`#27055` - L'import de compte tiers sans indiquer la rue de l'adresse de facturation alors qu'elle est obligatoire, ne crée plus un compte tiers sans fiche tiers.


#### TRANSFERT COMPTABLE


`#26649` - Correction du calcul d'arrondi effectué lors de la génération des écritures comptables de documents d'achat / vente ayant fait l'objet d'une création avec une saisie en TTC.


#### AFFAIRES


`#26766` - Mise en place du transfert en comptabilité de l'analytique de l'affaire à la ligne de document en achat et en vente.


`#26961` - Mise en place de l'import de la main d'œuvre dans le budgété et le réalisé des affaires.


`#26964` - Le coût horaire saisi dans l'onglet général de la fiche salarié est récupéré lors de la saisie du salarié dans l'onglet "Main d'œuvre" du budgété de l'affaire.


`#26969` - Mise en place de l'import des Frais dans le budgété et le réalisé des affaires.


`#27041` - Mise en place de filtres sur les catégories d'articles dans les frais et la main d'œuvre du budgété et réalisé de l'affaire, limitant aux catégories :


* "Main d'œuvre" et "Sous-traitance" les articles saisissables dans les lignes de main d'œuvre,
* "Autre" les articles saisissables dans les lignes de frais.


`#27064` - Mise en place d'un identifiant unique de ligne dans les frais et la main d'œuvre des affaires.


`#27067` - Ajout des champs : créée le, Créée par, Créé via, Modifiée le, Modifiée par et Modifiée via dans les lignes de frais et de main d'œuvre de l'affaire. 


#### G-CHANGE


`#26985` - Mise en place d'une tâche en ligne de commande d'import de la main d'œuvre du budgété et du réalisé de l'affaire.


`#26987` - Mise en place d'une tâche en ligne de commande d'import des frais du budgété et du réalisé de l'affaire.


#### BUDGET


`#27039` - La liste des périodes ne s'efface plus lorsque l'on change de plan analytique dans un budget.


#### IMPORTS


`#27027` - Correction de l'import de comptes, qui ne créait pas de compte tiers associé dans le cas où le champs PCF\_RS n'était pas présent dans le fichier d'import.


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


 


 


