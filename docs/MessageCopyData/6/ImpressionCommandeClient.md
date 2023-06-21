# Impression de commande client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une impression de commande client.


## Identifiant


4009


## Paramètres









| Nom | Type |   |   |
| NumeroInterne | string[10] |   | Obligatoire |
| Fichier | string[255] |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


 


## Exemple Delphi


const


  IdentifiantImpressionCommandeClient = 4009;


 


type


  TGMImpressionCommandeClient = packed record


    NumeroInterne: string[10];


    Fichier: string[255];


    Application: string[255];


  end;


 


procedure TGMEnvoiTachesMainForm.btnImprimerCommandeClick(ASender: TObject);


var


  DestinationForm: THandle;


  ImpressionCommandeClient: TGMImpressionCommandeClient;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'un numéro interne


    ControlerInformationManquante(edtNumeroInterneCommande, 'Veuillez indiquer le numéro interne de la commande à imprimer.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure ImpressionCommandeClient


    FillChar(ImpressionCommandeClient, SizeOf(ImpressionCommandeClient), #0);


 


    // Remplissage de la structure ImpressionCommandeClient


    ImpressionCommandeClient.NumeroInterne := edtNumeroInterneCommande.Text;


    ImpressionCommandeClient.Fichier := edtFichierCommande.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantImpressionCommandeClient;


    CopyDataStruct.cbData := SizeOf(ImpressionCommandeClient);


    CopyDataStruct.lpData := @ImpressionCommandeClient;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Handle, Longint(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


