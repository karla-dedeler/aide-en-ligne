# Tâches en ligne de commande
Cette application peut même être utilisée en ligne de commande, sans interface graphique.


## Options de ligne de commande


Voici les options de ligne de commande disponibles :


 







| Tâche |   |
|---|---|
| OuvrirTiers | [Ouverture de tiers par code](../2/OuvertureTiersParCode.md) |
| OuvrirTiersParTelephone | [Ouverture de tiers par numéro de téléphone](../2/OuvertureTiersParNumeroTelephone.md) |
| OuvrirTiersParEmail | [Ouverture de tiers par adresse email](../2/OuvertureTiersParAdresseEmail.md) |
| CreerClient | [Création de client](../2/CreationClient.md) |
| ModifierClient | [Modification de client](../2/ModificationClient.md) |
| OuvrirAffaire | [Ouverture d'affaire](../3/OuvertureAffaire.md) |
| CreerAffaire | [Création d'affaire](../3/CreationAffaire.md) |
| OuvrirArticle | [Ouverture d'article](../4/OuvertureArticle.md) |
| OuvrirDocument | [Ouverture de document d'achat, vente ou stock par numéro interne](../5/OuvertureDocumentParNumeroInterne.md) |
| OuvrirDocumentParPiece | [Ouverture de document d'achat, vente ou stock par numéro de pièce](../5/OuvertureDocumentParNumeroPiece.md) |
| CreerProformaClient | [Création de pro forma client](../6/CreationProformaClient.md) |
| CreerDevisClient | [Création de devis client](../6/CreationDevisClient.md) |
| CreerCommandeClient | [Création de commande client](../6/CreationCommandeClient.md) |
| CreerFactureClient | [Création de facture client](../6/CreationFactureClient.md) |
| CreerAvoirClient | [Création d'avoir client](../6/CreationAvoirClient.md) |
| ImprimerCommandeClient | [Impression de commande client](../6/ImpressionCommandeClient.md) |


 


Pour connaître la liste des tâches disponibles, vous pouvez lancer la commande suivante  :


GestimumEnvoiTaches.exe ListeTaches


 


Les syntaxes suivantes sont aussi acceptées :


GestimumEnvoiTaches.exe ?  

 GestimumEnvoiTaches.exe /?  

 GestimumEnvoiTaches.exe help  

 GestimumEnvoiTaches.exe /help


## Paramètres des options de ligne de commande


Chaque option peut prendre des paramètres.


 


Ces paramètres doivent suivre le nom de la tâche, séparés d'un espace.


## Exemples


### Ouverture de tiers par code


GestimumEnvoiTaches.exe OuvrirTiers C42


### Ouverture de tiers par numéro de téléphone


GestimumEnvoiTaches.exe OuvrirTiers 0134831637


### Ouverture de tiers par adresse email


GestimumEnvoiTaches.exe OuvrirTiersParEmail test@beka.fr


### Création de client


GestimumEnvoiTaches.exe CreerClient TEST "Client de test"


### Modification de client


GestimumEnvoiTaches.exe ModifierClient TEST "Client de test"


### Ouverture d'affaire


GestimumEnvoiTaches.exe OuvrirAffaire A42


### Création d'affaire


GestimumEnvoiTaches.exe CreerAffaire A42 "Affaire 42" C42


### Ouverture de document d'achat, vente ou stock par numéro interne


GestimumEnvoiTaches.exe OuvrirDocument 0000000798


### Ouverture de document d'achat, vente ou stock par numéro de pièce


GestimumEnvoiTaches.exe OuvrirDocumentParPiece CC20191015001


### Création de devis client


GestimumEnvoiTaches.exe CreerDevisClient BE0001 0792006;1;100 1542056;2;200 1543040;3;300


### Impression d'une commande client


GestimumEnvoiTaches.exe ImprimerCommandeClient 0000000798 C:\CommandeClient-0000000798.pdf


