# Modification de client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une modification de client.


## Identifiant


1004


## Paramètres









| Nom | Type |   |   |
| Code | string[20] |   | Facultatif |
| RaisonSociale | string[60] |   | Facultatif |
| Rue | string[40] |   | Facultatif |
| ComplementRue | string[40] |   | Facultatif |
| CodePostal | string[10] |   | Facultatif |
| NomVille | string[200] |   | Facultatif |
| Telephone1 | string[20] |   | Facultatif |
| Telephone2 | string[20] |   | Facultatif |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi


const


  IdentifiantModificationClient = 1004;


 


type


  TGMCreationModificationClient = packed record


    Code: string[20];


    RaisonSociale: string[60];


    Rue: string[40];


    ComplementRue: string[40];


    CodePostal: string[10];


    NomVille: string[200];


    Telephone1: string[20];


    Telephone2: string[20];


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnModifierClientClick(ASender: TObject);


var


  DestinationForm: THandle;


  ModificationClient: TGMCreationModificationClient;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie du code et de la raison sociale


    ControlerInformationManquante(edtCodeClientCreer, 'Veuillez indiquer le code du client à modifier.');


    ControlerInformationManquante(edtRaisonSocialeClientCreer, 'Veuillez indiquer la raison sociale du client à modifier.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure ModificationClient


    FillChar(ModificationClient, SizeOf(ModificationClient), #0);


 


    // Remplissage de la structure ModificationClient


    ModificationClient.Code := edtCodeClientModifier.Text;


    ModificationClient.RaisonSociale := edtRaisonSocialeClientModifier.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantModificationClient ;


    CopyDataStruct.cbData := SizeOf(ModificationClient);


    CopyDataStruct.lpData := @ModificationClient;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


