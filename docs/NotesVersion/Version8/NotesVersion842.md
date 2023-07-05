# Version 8.4.2 build 860 du 27/11/2019

 




 


#### CHAMPS PERSONNALISÉS


`#25913` - Les nouvelles adresses de tiers s'enregistrent lors de l'utilisation 
 de champs personnalisés dans les adresses de tiers.


#### EDI CHORUS


`#25924` - Mise en place d'un nœud 
 XML "AdditionalItemProperty" dans le fichier d'export au format 
 CHORUS, avec la valeur "Regroupement", permettant de remonter 
 les ligne de sous-total.


`#25926` - Ajout d'une zone "N° 
 d'engagement" permettant de saisir le N° d'engagement Chorus dans 
 les documents de vente.


`#25927` - Ajout d'une zone "N° 
 de bon de commande" permettant de saisir le n° de bon de commande 
 Chorus dans les documents de vente.


`#25928` - Mise en place d'un nœud 
 XML "ContractDocumentReference" dans le fichier d'export au 
 format CHORUS avec le N° d'engagement et le type "Engagement".


`#25929` - Mise en place d'un nœud 
 XML "ContractDocumentReference" dans le fichier d'export au 
 format CHORUS avec le N° de bon de commande et le type "Bon de commande".


`#25930` - Mise en place d'un contrôle 
 sur la présence du code pays dans l'adresse de livraison des documents 
 de vente lors de l'export au format CHORUS.


`#25931` - Mise en place d'un contrôle 
 sur le n° d'engagement et le n° de bon de commande dans la fenêtre d'export 
 des factures et avoirs clients au format Chorus, permettant de s'assurer 
 que seule l'une des 2 occurrences est remplie.


`#25932` - Le nœud XML "Billingreference" du fichier au format 
 Chorus apparaît uniquement pour les avoirs afin d'y renseigner le n° de 
 la facture d'origine quand cette information est connue. 


`#25937` - Mise en place dans le 
 fichier d'export au format CHORUS d'un nœud "InvoiceLine" avec 
 un sous-nœud "AdditionalItemProperty" ayant la valeur "Regroupement", 
 permettant de remonter les lignes de sous-total ou total.


 


 


![](../assets/images/Version7/Images/Modules_de_l_ERP.png)


 


