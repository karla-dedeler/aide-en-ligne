# Message Windows WM\_COPYDATA
Cette API s'appuie sur le message Windows WM\_COPYDATA qui permet d'envoyer de l'information à une application ouverte.


 


L'envoi de ce message se fait à l'aide d'un outil de développement logiciel.


 


Si on prend le cas de l'outil de développement Delphi, il faut utiliser la fonction SendMessage de l'API Windows pour envoyer ce message.


 


Cette fonction prend 2 autres paramètres, en plus du message WM\_COPYDATA :


 







| Paramètre |   |
| wParam | Handle de la fenêtre de l'application à laquelle le message doit être envoyé |
| lParam | Pointeur vers la structure de type COPYDATASTRUCT contenant les informations à envoyer |


 


La structure de type COPYDATASTRUCT contient 3 champs :


 







| Champ |   |
| dwData | Numéro qui identifie le type de demande qui est envoyée dans le message, par exemple 1001 pour une demande d'ouverture de fiche client par numéro de téléphone |
| cbData | Taille en octets de la structure passée dans le champ suivant (lpData) |
| lpData | Pointeur vers la structure propre au type de demande qui est envoyé |


