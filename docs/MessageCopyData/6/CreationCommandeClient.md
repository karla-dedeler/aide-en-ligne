# Création de commande client
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création de commande client.


## Identifiant


4004


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| CodeClient | string[10] |   | Obligatoire |
| Rue | string[40] |   | Facultatif |
| ComplementRue | string[40] |   | Facultatif |
| CodePostal | string[10] |   | Facultatif |
| Ville | string[200] |   | Facultatif |
| Lignes | array[0..99] of string[255] |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

```
const
  IdentifiantCreationCommandeClient = 4004;

type
  TGMArrayOfLignes = array[0..99] of string[255];
  TGMCreationCommandeClient = packed record
    CodeClient: string[20];
    Rue: string[40];
    ComplementRue: string[40];
    CodePostal: string[10];
    Ville: string[200];
    Lignes: TGMArrayOfLignes;
    Application: string[255];
  end;

procedure TGMEnvoiTachesMainForm.btnCreerCommandeClick(ASender: TObject);

var
  DestinationForm: THandle;
  CreationCommandeClient: TGMCreationCommandeClient;
  CopyDataStruct: TCopyDataStruct;
begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie d'un code client et de lignes
    ControlerInformationManquante(edtCodeClientCommande, 'Veuillez indiquer le code client de la commande à créer.');
    ControlerInformationManquante(edtLignesCommande, 'Veuillez indiquer les lignes de la commande à créer.');
    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;
    // Initialisation de la structure CreationCommandeClient
    FillChar(CreationCommandeClient, SizeOf(CreationCommandeClient), #0);
    // Remplissage de la structure CreationCommandeClient
    CreationCommandeClient.CodeClient := edtCodeClientCommande.Text;
    CreationCommandeClient.Lignes := SplitLignes(edtLignesCommande.Text);
    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantCreationCommandeClient;
    CopyDataStruct.cbData := SizeOf(CreationCommandeClient);
    CopyDataStruct.lpData := @CreationCommandeClient;
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Handle, Longint(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
```


