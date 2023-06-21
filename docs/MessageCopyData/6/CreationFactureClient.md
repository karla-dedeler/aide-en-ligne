# Création de facture client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création de facture client.


## Identifiant


4007


## Paramètres









| Nom | Type |   |   |
| CodeClient | string[10] |   | Obligatoire |
| Lignes | array[0..99] of string[255] |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi


const


  IdentifiantCreationFactureClient = 4007;


 


type


  TGMArrayOfLignes = array[0..99] of string[255];


 


  TGMCreationFactureClient = packed record


    CodeClient: string[20];


    Lignes: TGMArrayOfLignes;


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnCreerFactureClick(ASender: TObject);


var


  DestinationForm: THandle;


  CreationFactureClient: TGMCreationFactureClient;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'un code client et de lignes


    ControlerInformationManquante(edtCodeClientFacture, 'Veuillez indiquer le code client de la facture à créer.');


    ControlerInformationManquante(edtLignesFacture, 'Veuillez indiquer les lignes de la facture à créer.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure CreationFactureClient


    FillChar(CreationFactureClient, SizeOf(CreationFactureClient), #0);


 


    // Remplissage de la structure CreationFactureClient


    CreationFactureClient.CodeClient := edtCodeClientFacture.Text;


    CreationFactureClient.Lignes := SplitLignes(edtLignesFacture.Text); //18720


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantCreationFactureClient;


    CopyDataStruct.cbData := SizeOf(CreationFactureClient);


    CopyDataStruct.lpData := @CreationFactureClient;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Handle, Longint(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


