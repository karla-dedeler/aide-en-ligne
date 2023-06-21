# Ouverture d'article
## Description


Permet de demander l'ouverture dans Gestimum ERP d'un article à partir d'un code article donné.


## Identifiant


3000


## Paramètres









| Nom | Type |   |   |
| Code | string[30] | Code de l'article à ouvrir | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi


const


  IdentifiantOuvertureArticle = 3000;


 


type


  TGMOuvertureArticle = packed record


    Code: string[30];


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnOuvrirArticleClick(ASender: TObject);


var


  DestinationForm: THandle;


  OuvertureArticle: TGMOuvertureArticle;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'un code


    ControlerInformationManquante(edtCodeArticle, 'Veuillez indiquer le code de l''article à ouvrir.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure OuvertureArticle


    FillChar(OuvertureArticle, SizeOf(OuvertureArticle), #0);


 


    // Remplissage de la structure OuvertureArticle


    OuvertureArticle.Code := edtCodeArticle.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantOuvertureArticle;


    CopyDataStruct.cbData := SizeOf(OuvertureArticle);


    CopyDataStruct.lpData := @OuvertureArticle;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


