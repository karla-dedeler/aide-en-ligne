# PopupFusionPièces

La fusion est possible 
 si le tri de la saisie standard est par [ordre](PopupTri.md).


Les lignes d'écritures 
 de deux pièces distinctes sont réunies en une seule pièce si :


* Elles 
 ont la même date,
* Elles 
 ont la même devise,
* Elles 
 ont le même numéro de pièce (pour les journaux d’achats et de ventes),
* Elles 
 n’ont pas d’écriture rapprochée,
* Elles 
 n’ont pas d’écriture issue de règlement.


 


Pour cela, vous devez 
 sélectionner une ligne quelconque de la première pièce et lancer la commande.


Si la sélection est correcte, 
 vous obtiendrez une seule pièce.


//<![CDATA[
 if( typeof( FilePopupInit ) != 'function' ) FilePopupInit = new Function();
 FilePopupInit('A1');
//]]>
