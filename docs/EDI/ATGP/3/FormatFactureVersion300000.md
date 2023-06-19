# Format de facture version 3.00.000
## Type de fichier


Fichier texte


 


Enregistrements à taille variable


 


Séparateur : point-virgule ;


## Description


En rouge données obligatoires à titre indicatif, peuvent varier suivant 
 demandes clients, et paramétrage du logiciel.


### Cinématique des enregistrements


ENT 
 (entête)


DTM 
 (informations dates)


REF (informations références, avoirs)


PAR (informations 
 partenaires)


PAD (optionnel: 
 détails partenaires)


COM (optionnel: commentaires)


TDT (optionnel: 
 transports)


TOD (optionnel: 
 condition de livraison)


LIG 
 (lignes)


MEA (optionnel 
 : détail mesures)


DOU (optionnel : détail douanes)


PAC (optionnel : détail emballage)


NAD (optionnel : détail partenaires)


LID (optionnel: détails de la ligne)


PID (optionnel: 
 détails du pied, dégressions globales et taxes parafiscales)


PIE (pied de facture)


TVA (détail des TVA)


TPF (détail taxes parafiscales)


END (fin de facture)


 


Entre crochets, longueur maximum autorisée de la donnée. Pour les valeurs 
 avec décimales, X.Y signifie X caractères dont 
 Y décimales (sans compter le caractère de séparation de décimale).


### Enregistrement ENT : Entête


1 Identifiant d'enregistrement 
 "ENT" [3]


2 Numéro de commande du distributeur 
 [35]


3 Date de commande JJ/MM/AAAA 
 [10]


4 Heure de commande HH:MN[5]


5 Date du message JJ/MM/AAAA [10]


6 Heure du message HH:MN[5]


7 Date du BL JJ/MM/AAAA [10]


8 Numéro de BL[35]


9 Date avis d'expédition JJ/MM/AAAA [10]


10 Numéro de l'avis d'expédition [35]


11 Date d'enlèvement JJ/MM/AAAA [10]


12 Heure d'enlèvement HH:MN [5]


13 Numéro de document [35]


14 Date/heure document JJ/MM/AAAA 
 HH:MN [16]


15 Date d'échéance JJ/MM/AAAA 
 [10]


16 Type de document (Facture/Avoir) 
 [7]


17 Code monnaie (EUR pour Euro) 
 [3]


18 Date d'échéance pour l'escompte JJ/MM/AAAA 
 [10]


19 Montant de l'escompte (si escompte, 
 le pourcentage de l'escompte est préconisé) [10.3]


20 Numéro de facture (obligatoire si avoir) 
 [35]


21 Date de facture JJ/MM/AAAA (obligatoire 
 si avoir) [10]


22 Pourcentage escompte (préférez le pourcentage 
 au montant) [6.3]


23 Nombre de jours escompte [3]


24 Pourcentage pénalité [6.3]


25 Nombre de jours pénalité [3]


26 Document de test (1/0) [1]


27 Code paiement [3]


28 Nature document (MAR pour marchandise et SRV 
 pour service) [3]


### Enregistrement DTM : Dates


1 Identifiant d'enregistrement 
 DTM [3]


2 Code date [3]


3 Date JJ/MM/AAAA [10]


### Enregistrement REF : Références (optionnel)


1 Identifiant d'enregistrement 
 REF [3]


2 Code référence [3]


3 Référence [35]


4 Date [10]


### Enregistrement PAR : Partenaires


1 Identifiant d'enregistrement 
 "PAR" [3]


2 Code EAN client (commandé 
 par) [13]


3 Libellé client [20]


4 Code EAN fournisseur (commandé 
 à) [13]


5 Libellé fournisseur [20]


6 Code EAN client livré [13]


7 Libellé client livré [20]


8 Code EAN client facturé [13]


9 Libellé client facturé [20]


10 Code EAN factor (obligatoire si factor) 
 [13]


11 Libellé alias factor (obligatoire si 
 factor) [35]


12 Code EAN régler à [13]


13 Libellé régler à [20]


14 Code EAN siège social vendeur (obligatoire 
 si différent du code EAN vendeur) [13]


15 Libellé siège social vendeur [20]


16 Code client normalisé @GP (obligatoire 
 si codification interne partenaire) [35]


 


Note : si votre client doit payer à votre commissionnaire/agent (= factor), 
 vous devez renseigner obligatoirement son code EAN s'il en a un, sinon 
 son libellé en minuscule sans aucun caractère spécial/espace.


### Enregistrement PAD : Détail partenaires (optionnel)


1 Identifiant d'enregistrement 
 "PAD" [3]


2 Code EAN [13]


3 Raison sociale [20]


4 Type de partenaire (IV = 
 facturé à, SU = facturé par, BY = commandé par, DP 
 = livré à) [3]


5 Adresse [35]


6 Adresse ligne 2 [35]


7 Adresse ligne 3 [35]


8 Code postal [9]


9 Ville [35]


10 Code pays [3]


11 Siret [35]


12 Numéro d'identification TVA [35]


13 RCS Ville [35]


14 RCS Numéro [35]


15 Capital social [35]


16 Forme juridique [35]


17 Référence fournisseur chez 
 la centrale [35]


18 Code interne partenaire chez le client 
 (obligatoire si codification interne partenaire) [35]


### Enregistrement COM : Commentaires (optionnel)


1 Identifiant d'enregistrement 
 "COM" [3]


2 Code commentaire [3]


3 Commentaire [350]


### Enregistrement TDT : Transport (optionnel)


1 Identifiant d'enregistrement 
 "TDT" [3]


2 Type de transport [3]


3 Numéro d'expédition [17]


4 Code mode transport [3]


5 Nom transporteur [35]


### Enregistrement TOD : Conditions de livraison 
 (optionnel)


1 Identifiant d'enregistrement 
 "TOD" [3]


2 Type de condition [3]


3 Mode paiement [3]


4 Code INCOTERM 
 [3]


 


Note :


\* si Type de condition = 5 alors le mode de paiement est soit PP, soit CC


\* PU permet d'indiquer que le client est responsable du règlement des 
 frais d'enlèvement au point de chargement


### Enregistrement LIG : Ligne


1 Identifiant d'enregistrement 
 "LIG" [3]


2 Numéro de ligne (de 1 à n 
 remis à 0 pour chaque facture) [6]


3 Code EAN produit [14]


4 Code interne produit chez le fournisseur 
 [35]


5 Par combien (multiple de 
 commande) [10.3]


6 Quantité commandée [10.3]


7 Unité de quantité (PCE = pièce, KGM = kilogramme, 
 MTR = mètre, …) [3]


8 Quantité facturée [10.3]


9 Prix unitaire net [15.6]


10 Code monnaie (EUR = euro) 
 [3]


11 non utilisé


12 non utilisé


13 Taux de TVA (par exemple 
 19,6) [5.2]


14 Prix unitaire brut [15.6]


15 Poids net total ligne [9.3]


16 Libellé ligne de facture 
 (ou libellé du produit) [70]


17 Montant Net Ht de la ligne 
 [17.2]


18 Code interne produit chez le client 
 [35]


19 Prix net ristournable 
 (obligatoire si TPF) [15.6]


20 Montant net ristournable 
 (obligatoire si TPF) [17.2]


21 Référence ligne du composé (obligatoire 
 si c'est un composant) [35]


22 Type de sous-ligne (A = Ajouté, I = 
 Inclus) (obligatoire si c'est un composant) [5]


23 Identification de la description en 
 code (obligatoire si c'est un composé) [35]


24 Code EAN de l'article remplacé [35]


25 Unité du par combien (multiple de commande) 
 [3]


26 Numéro de ligne commande d'origine 
 [6]


27 Prix public TTC (secteur livre) [15.6]


28 Numéro commande d'origine [35]


29 Numéro BL d'origine [35]


30 Numéro ligne BL d'origine [6]


31 Prix brut remisé [15.6]


32 Montant brut remisé [17.2]


33 Date commande d'origine JJ/MM/AAAA 
 [10]


34 Date BL d'origine JJ/MM/AAAA [10]


### Enregistrement MEA : Mesures (optionnel)


1 Identifiant d'enregistrement 
 "MEA" [3]


2 Type de mesure [3]


3 Code [3]


4 Unité [3]


5 Valeur [9.3]


### Enregistrement DOU : Douane (optionnel)


1 Identifiant d'enregistrement 
 "DOU" [3]


2 Code pays origine [3]


3 Code régime [3]


4 Nomenclature [35]


### Enregistrement PAC : Emballage (optionnel)


1 Identifiant d'enregistrement 
 "PAC" [3]


2 Nombre de colis [8]


3 Code conditions du conditionnement (cf 
 table PAC.3) [3]


4 Type emballage (cf table PAC.4) [17]


5 Code paiement des frais de retour d'emballage 
 (cf table PAC.5) [3]


 


Note : obligatoire si document pour Carrefour pour des produits de marée 
 ou fruits et légumes


### Enregistrement NAD : Partenaire (optionnel)


1 Identifiant d'enregistrement 
 "NAD" [3]


2 Type de partenaire [3]


3 Code pays [3]


### Enregistrement LID : Détail ligne (dégression tarifaire, optionnel)


1 Identifiant d'enregistrement 
 "LID" [3]


2 Numéro de ligne [6]


3 Numéro de séquence de calcul 
 [1]


4 Code type de dégression tarifaire 
 (cf table LID.4) [5]


5 Libellé descriptif de la 
 dégression tarifaire [70]


6 Quantité ou montant unitaire 
 [12.6]


7 Unité de quantité (PCT pour une quantité en pourcentage, ou code monnaie) 
 [3]


8 Code taxe parafiscale (cf table LID.8) 
 [14]


9 Taux de TVA de la dégression 
 ou taxe parafiscale [5.2]


10 Montant de la dégression (obligatoire 
 si en pourcentage) [12.6]


11 Montant base de calcul [12.6]


### Enregistrement PID : détail de pied de facture


cf enregistrement LID pour le format (identique, 
 sauf Identifiant d'enregistrement: PID)


### Enregistrement PIE : pied de facture


1 Identifiant d'enregistrement 
 "PIE" [3]


2 Montant total hors taxes 
 [10.3]


3 Montant total TVA [10.3]


4 Montant total toutes taxes 
 comprises [10.3]


5 Montant total net ristournable (obligatoire 
 si TPF) [10.3]


6 Montant total TPF (obligatoire si TPF) 
 [10.3]


7 Montant total des taxes (obligatoire 
 si TPF) [10.3]


### Enregistrement TVA : détail TVA (obligatoire même en cas de TVA à 0%)


1 Identifiant d'enregistrement 
 "TVA" [3]


2 Taux de TVA [5.2]


3 Montant total soumis à TVA 
 [10.3]


4 Montant de la TVA [10.3]


5 Code TVA [35]


6 Libellé du code TVA [35]


7 Identification de compte [35]


### Enregistrement TPF : détail taxes parafiscales


1 Identifiant d'enregistrement 
 "TPF" [3]


2 Code taxe parafiscale [14]


3 Libellé taxe parafiscale 
 [70]


4 Montant final taxe parafiscale 
 [12.6]


5 Montant de base [16.2]


### Enregistrement END : fin de facture


1 Identifiant d'enregistrement 
 de fin de facture "END" [3]


