# Jointures
La construction 
 de ce type de requête n’est pas acceptée par cet outil :


 


INNER JOIN DOCUMENTS D ON


  D.DOC\_NUMERO = L.DOC\_NUMERO AND


  DOC\_TYPE = 'V' AND


  DOC\_STYPE in ('A', 'F', '0', '1')


 


Il faut reporter la condition dans la clause WHERE pour obtenir le même 
 résultat :


 


INNER JOIN DOCUMENTS D ON


  D.DOC\_NUMERO = L.DOC\_NUMERO


WHERE


  DOC\_TYPE = 'V' AND DOC\_STYPE IN ('A', 'F', 
 '0', '1')


