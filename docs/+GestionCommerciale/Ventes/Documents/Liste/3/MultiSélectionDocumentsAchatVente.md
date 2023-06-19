# Multi-sélection dans la liste des documents d'achat et vente


A partir de la liste des documents de vente et d’achat, la sélection multiple est possible.


## Fonctionnalités


Les fonctionnalités suivantes sont disponibles à partir du clic droit du menu contextuel :


* Regrouper par client
* Regrouper par payeur
* Transférer
* La suppression, duplication et impression seront traitées un peu plus tard


 


La fonctionnalité de multi sélection est à l’image de la multi sélection Windows. Pour sélectionner plusieurs documents consécutifs, cliquez sur le premier élément, appuyez sur la touche MAJ et maintenez-la enfoncée, puis cliquez sur le dernier élément.


 


Pour sélectionner plusieurs documents non consécutifs, appuyez sur la touche CTRL et maintenez-la enfoncée, puis cliquez sur chaque élément. Les éléments en surbrillance et avec l’icône de sélection actif seront considérés comme sélectionnés.


 


La touche F5 et l’option "Rafraîchir" du menu contextuel permettent la désélection des documents.


 


Les documents dans les états "En cours", "Imprimé" et "Transféré partiellement" peuvent être sélectionnés.


 


Les documents de type EDI à l’état Bon de préparation ou exportés seront traités dans une version ultérieure.


 


Les documents en contremarque peuvent être sélectionnés pour être regroupés ou transférés. Dans une sélection multiple la question  "Générer la contremarque" OUI/NON ne sera pas proposée.


 


Le regroupement consiste à créer un nouveau document et y recopier les lignes des documents sélectionnés. Ce module permet également de regrouper puis transférer les documents vers un document supérieur :


* Plusieurs Commandes en Commande ou Bon de livraison ou Facture
* Plusieurs Bons de livraisons en Facture


## Conditions de regroupement


Il existe des critères bloquants de regroupement, un message d’avertissement sera affiché lors de la sélection du document qui ne respecte pas les conditions suivantes empêchant leur sélection :


* Même sous-type de document,
* Même dépôt,
* Même nature comptable,
* Même devise,
* Facturation TTC cochée sur tous les documents ou décochée,
* Même commercial.


 


Les critères de regroupement non bloquants sont les suivants :


* L'affaire : si différente elle est ignoré en en-tête de document en revanche l'information est conservée à la ligne de document,
* Le mode de règlement : si différent il est ignoré mais le type de règlement est conservé pour les échéances,
* L'adresse de livraison : si différente elle est reprise du dernier document regroupé,
* Les champs personnalisés : si différents ils sont repris du dernier document regroupé,
* Le montant de remise exceptionnelle : si différent il est conservé et cumulé,
* Les pourcentages de remise accordée et exceptionnelle, d’escompte, frais, frais de port, frais supplémentaires et retenu de garantie : si différent ils sont ignorés.


## Transfert des documents


Le transfert des multiples documents sélectionnés génère un document transféré par document sélectionné.


Il est possible de transférer les documents suivants, comme dans le transfert classique :


* Pro forma vers Devis ou Accusé de réception ou bon de livraison ou Facture,
* Devis vers Pro forma ou Accusé de réception ou Bon de livraison ou Facture,
* Accusé de réception vers Bon de livraison ou Facture,
* Bon de livraison vers Facture,
* Bon de retour vers Facture ou Avoir,
* Facture vers Avoir.


