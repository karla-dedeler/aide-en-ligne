# Version 9.5 build 1155 du 19/06/2023

### ÉVOLUTIONS PRINCIPALES


Cette version apporte les évolutions et corrections suivantes : 


#### ACHAT ET VENTE


##### CORRECTIONS : 


  

 `#28495` – Le montant de l’échéance se recalcule correctement lors de l’ajout d’un acompte.   

 `#26684` – Le regroupement par fournisseur des BR générait une erreur « Transférée en $piece ».   

 `#29471` – Gestion des échéances : un contrôle a été ajouté lors du regroupement des documents


#### IMPORTS


##### CORRECTIONS : 


  

 `#29470` – L’import de document avec multi-affaires : L’ordre des lignes importées est de nouveau respecté et le code affaire est correctement récupéré. 


 


##### EVOLUTIONS : 


  

 `#29452` – L’import des commentaires (PCF\_MEMO) dans l’import de tiers est de nouveau fonctionnel. 


#### ENCAISSEMENTS ET DECAISSEMENTS


##### CORRECTIONS : 


  

 `#29461` – La colonne « Sélectionnée (TMP\_SELECT » ne disparaît plus lors de l’ajout d’une autre colonne dans « Solder l’échéance avec ». 


 


##### EVOLUTIONS : 


  

 `#29348` – L’extension XML a été ajoutée dans les prélèvements/virements SEPA. Case à cocher présente dans la fiche BANQUE du dossier. 


 


#### STOCKS


##### CORRECTIONS : 


  

 `#28944` – Erreur "Expression de type non booléen spécifiée dans un contexte où une condition est attendue, près de 'and'" dans l'onglet "Stock" d'un dépôt.  

 `#28945` – Erreur "Expression de type non booléen spécifiée dans un contexte où une condition est attendue, près de ','" dans la consultation du stock d'un ensemble de dépôts.


#### LETTRAGE


##### EVOLUTIONS : 


  

 `#25724` – Il est maintenant possible d’afficher les champs ECR\_PIECE2 et ECR\_REFERE dans la fenêtre de lettrage manuel


#### IMMOBILISATIONS


 


##### CORRECTIONS : 


  

 `#28946` – Anomalie lors du calcul du montant de la +/- value dans le cas d’une cession qui intervenait après la date de fin d’amortissement.   

  


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)

