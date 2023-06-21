# Ouverture de tiers par adresse email
## Description


Permet de demander l'ouverture dans Gestimum ERP d'un tiers à partir d'une adresse email de tiers donnée.


## Identifiant


1002


## Paramètres









| Nom | Type |   |   |
| Email | string[60] | Adresse email du tiers à ouvrir | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi


const


  IdentifiantOuvertureTiersParEmail = 1002;


 


type


  TGMOuvertureTiersParEmail = packed record


    Email: string[60];


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnOuvrirTiersParAdresseEmailClick(ASender: TObject);


var


  DestinationForm: THandle;


  OuvertureTiers: TGMOuvertureTiersParAdresseEmail;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'une adresse email


    ControlerInformationManquante(edtAdresseEmailTiers, 'Veuillez indiquer l''adresse email du tiers à ouvrir.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure OuvertureTiersParAdresseEmail


    FillChar(OuvertureTiers, SizeOf(OuvertureTiers), #0);


 


    // Remplissage de la structure OuvertureTiers


    OuvertureTiers.AdresseEmail := edtAdresseEmailTiers.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantOuvertureTiersParEmail;


    CopyDataStruct.cbData := SizeOf(OuvertureTiers);


    CopyDataStruct.lpData := @OuvertureTiers;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


