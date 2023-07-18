# Création de pro forma client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création d'un pro forma client.


## Identifiant


4002


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| CodeClient | string[10] |   | Obligatoire |
| Lignes | array[0..99] of string[255] |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

```
const
  IdentifiantCreationProformaClient = 4002;

type
  TGMArrayOfLignes = array[0..99] of string[255];
 
  TGMCreationProformaClient = packed record
    CodeClient: string[20];
    Lignes: TGMArrayOfLignes;
    Application: string[255];
  end;
 
procedure TGMEnvoiTachesMainForm.btnCreerProformaClick(ASender: TObject);
var
  DestinationForm: THandle;
  CreationProformaClient: TGMCreationProformaClient;
  CopyDataStruct: TCopyDataStruct;
begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie d'un code client et de lignes
    ControlerInformationManquante(edtCodeClientProforma, 'Veuillez indiquer le code client de la proforma à créer.');
    ControlerInformationManquante(edtLignesProforma, 'Veuillez indiquer les lignes de la proforma à créer.');
 
    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;
 
    // Initialisation de la structure CreationProformaClient
    FillChar(CreationProformaClient, SizeOf(CreationProformaClient), #0);
 
    // Remplissage de la structure CreationProformaClient
    CreationProformaClient.CodeClient := edtCodeClientProforma.Text;
    CreationProformaClient.Lignes := SplitLignes(edtLignesProforma.Text);//18720

    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantCreationProformaClient;
    CopyDataStruct.cbData := SizeOf(CreationProformaClient);
    CopyDataStruct.lpData := @CreationProformaClient;
 
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Handle, Longint(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
```