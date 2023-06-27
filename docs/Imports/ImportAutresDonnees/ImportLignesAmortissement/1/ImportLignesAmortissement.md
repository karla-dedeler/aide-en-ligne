# Import de lignes d'amortissement
Cet import permet de créer les lignes d'amortissement d'immobilisations.


 


Il est accessible par le menu OUTILS | Importer | Autres données.


 


Il permet aussi de modifier les lignes d'amortissement des immobilisations. Il faut pour cela renseigner dans le fichier texte à importer le code immobilisation (IMO\_CODE) et le numéro de ligne d'amortissement (LIG\_NUMERO).


 


Les champs suivants ne peuvent pas être vides :


* date de début
* date de fin
* montant de la dotation
* taux d'amortissement


 


La VNC de la dernière ligne est contrôlée et doit être égale à zéro. Dans le cas contraire, l'import ne se fait pas.


 


Les champs suivants seront automatiquement renseignés s'ils ne sont pas remplis :


* base d'amortissement
* cumul des dotations
* VNC
* Soldée


 


La case à cocher "Reprise" dans l'onglet Entrée de l'immobilisation se coche automatiquement si une des lignes est soldée et si elle n'était pas cochée.


