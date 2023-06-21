# Ouverture de tiers par numéro de téléphone
## Description


Permet de demander l'ouverture dans Gestimum ERP d'un tiers à partir d'un numéro de téléphone de tiers donné.


## Identifiant


1001


## Paramètres









| Nom | Type |   |   |
| Telephone | string[20] | Numéro de téléphone du tiers à ouvrir | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi


const


  IdentifiantOuvertureTiersParTelephone = 1001;


 


type


  TGMOuvertureTiersParTelephone = packed record


    Telephone: string[20];


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnOuvrirTiersParTelephoneClick(ASender: TObject);


var


  DestinationForm: THandle;


  OuvertureTiers: TGMOuvertureTiersParTelephone;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'un numéro de téléphone


    ControlerInformationManquante(edtTelephoneTiers, 'Veuillez indiquer le numéro de téléphone du tiers à ouvrir.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure OuvertureTiers


    FillChar(OuvertureTiers, SizeOf(OuvertureTiers), #0);


 


    // Remplissage de la structure OuvertureTiers


    OuvertureTiers.Telephone := edtTelephoneTiers.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantOuvertureTiersParTelephone;


    CopyDataStruct.cbData := SizeOf(OuvertureTiers);


    CopyDataStruct.lpData := @OuvertureTiers;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


