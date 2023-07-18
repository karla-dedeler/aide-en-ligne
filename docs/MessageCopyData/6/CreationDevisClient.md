# Création de devis client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création de devis client.


## Identifiant


4003


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| CodeClient | string[10] |   | Obligatoire |
| Lignes | array[0..99] of string[255] |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

```
const
  IdentifiantCreationDevisClient = 4003;
 
type
  TGMArrayOfLignes = array[0..99] of string[255];
 
  TGMCreationDevisClient = packed record
    CodeClient: string[20];
    Lignes: TGMArrayOfLignes;
    Application: string[255];
  end;
 
procedure TGMEnvoiTachesMainForm.btnCreerDevisClick(ASender: TObject);
var
  DestinationForm: THandle;
  CreationDevisClient: TGMCreationDevisClient;
  CopyDataStruct: TCopyDataStruct;
begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie d'un code client et de lignes
    ControlerInformationManquante(edtCodeClientDevis, 'Veuillez indiquer le code client du devis à créer.');
    ControlerInformationManquante(edtLignesDevis, 'Veuillez indiquer les lignes du devis à créer.');
 
    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;

    // Initialisation de la structure CreationDevisClient
    FillChar(CreationDevisClient, SizeOf(CreationDevisClient), #0);
 
    // Remplissage de la structure CreationDevisClient
    CreationDevisClient.CodeClient := edtCodeClientDevis.Text;
    CreationDevisClient.Lignes := SplitLignes(edtLignesDevis.Text);//18720
 
    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantCreationDevisClient;
    CopyDataStruct.cbData := SizeOf(CreationDevisClient);
    CopyDataStruct.lpData := @CreationDevisClient;
 
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Handle, Longint(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
```