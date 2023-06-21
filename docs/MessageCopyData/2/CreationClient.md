# Création de client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création de client.


## Identifiant


1003


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


  IdentifiantCreationClient = 1003;


 


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


 


procedure TGMEnvoiTachesMainForm.btnCreerClientClick(ASender: TObject);


var


  DestinationForm: THandle;


  CreationClient: TGMCreationModificationClient;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie du code et de la raison sociale


    ControlerInformationManquante(edtCodeClientCreer, 'Veuillez indiquer le code du client à créer.');


    ControlerInformationManquante(edtRaisonSocialeClientCreer, 'Veuillez indiquer la raison sociale du client à créer.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure CreationClient


    FillChar(CreationClient, SizeOf(CreationClient), #0);


 


    // Remplissage de la structure CreationClient


    CreationClient.Code := edtCodeClientCreer.Text;


    CreationClient.RaisonSociale := edtRaisonSocialeClientCreer.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantCreationClient;


    CopyDataStruct.cbData := SizeOf(CreationClient);


    CopyDataStruct.lpData := @CreationClient;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


