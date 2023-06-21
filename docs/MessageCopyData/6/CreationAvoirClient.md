# Création d'avoir client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création d'avoir client.


## Identifiant


4008


## Paramètres









| Nom | Type |   |   |
| CodeClient | string[10] |   | Obligatoire |
| Lignes | array[0..99] of string[255] |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi


const


  IdentifiantCreationAvoirClient = 4008;


 


type


  TGMArrayOfLignes = array[0..99] of string[255];


 


  TGMCreationAvoirClient = packed record


    CodeClient: string[20];


    Lignes: TGMArrayOfLignes;


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnCreerAvoirClick(ASender: TObject);


var


  DestinationForm: THandle;


  CreationAvoirClient: TGMCreationAvoirClient;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'un code client et de lignes


    ControlerInformationManquante(edtCodeClientAvoir, 'Veuillez indiquer le code client de l''avoir à créer.');


    ControlerInformationManquante(edtLignesAvoir, 'Veuillez indiquer les lignes de l''avoir à créer.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure CreationAvoirClient


    FillChar(CreationAvoirClient, SizeOf(CreationAvoirClient), #0);


 


    // Remplissage de la structure CreationAvoirClient


    CreationAvoirClient.CodeClient := edtCodeClientAvoir.Text;


    CreationAvoirClient.Lignes := SplitLignes(edtLignesAvoir.Text);


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantCreationAvoirClient;


    CopyDataStruct.cbData := SizeOf(CreationAvoirClient);


    CopyDataStruct.lpData := @CreationAvoirClient;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Handle, Longint(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


