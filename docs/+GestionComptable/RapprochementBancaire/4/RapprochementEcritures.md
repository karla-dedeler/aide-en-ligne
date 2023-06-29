# Rapprochement des écritures



Une ligne d’écriture est composée d’une date 
 d’opération, d’un libellé, d’un numéro de pièce, d’une date de valeur, 
 d’un montant Débit ou Crédit, d’une date de relevé, d’un code relevé, 
 d’une date de saisie d’écriture, d’un code journal, d’un libellé automatique, 
 d’un numéro de ligne de l’écriture.


 


Les lignes peuvent être triées par date d’opération, montant, date de 
 saisie de l’écriture, code journal.


 


Vous pouvez afficher toutes les écritures, les écritures rapprochées 
 ou les écritures non rapprochées.


 


Pensez à paramétrer ces colonnes en appelant les propriétés du menu 
 contextuel.


 


Par ce menu, vous pouvez également :


* Sélectionner une 
 ligne
* Désélectionner 
 une ligne
* Sélectionner toutes 
 les lignes
* Désélectionner 
 toutes les lignes
* Rapprocher l’écriture au solde précédent 
 (cas du [premier 
 rapprochement bancaire](PremierRapprochementBancaire.md))
* Avoir les écritures du compte "[Dans le sens 
 de la banque](RapprochementBancaireSensBanque.md)"
* Accéder à [la 
 saisie standard](../../Ecritures/Saisie/Standard/SaisieStandard.md)
* Accéder à la consultation de l’écriture 
 d'origine des écritures d’A-Nouveaux en saisie standard
* [Imprimer 
 le rapprochement](../5/ImpressionRapprochementBancaire.md)


## Date d’opération


La date d’opération correspond par défaut à la date de saisie de l’écriture. 
 Si vous souhaitez faire correspondre votre rapprochement avec votre relevé, 
 vous pouvez indiquer [la 
 date d'opération du relevé](CreationRapprochementBancaire.md) qui sera prise en compte lors du pointage.


## Montant


Le sens du montant de l’écriture dépend du choix effectué dans le menu 
 contextuel "Dans le sens de la banque".


## Pointage des écritures à rapprocher


Le logiciel calcule automatiquement le solde des Écritures à rapprocher 
 par différence entre le solde du relevé reçu et le solde du relevé précédent.


Le rapprochement s’effectue ligne par ligne par un double-clic ou par 
 le menu contextuel.


 


Une ligne rapprochée apparaît dans une couleur différente paramétrée 
 dans les styles de la société et intègre éventuellement le code relevé, 
 la date d’opération et/ou la date de valeur.


 


A chaque pointage ou dépointage, le logiciel met à jour les soldes.


## Validation


Lorsque vous avez terminé de rapprocher les écritures, vous devez [ajourner ou 
 valider](ValidationRapprochementBancaire.md) votre rapprochement.


 