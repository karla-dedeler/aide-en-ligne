# Création d'affaire
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une création d'affaire.


## Identifiant


2001


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| Code | string[10] |   | Facultatif |
| Nom | string[100] |   | Facultatif |
| CodeClient | string[20] |   | Facultatif |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

````
const
  IdentifiantCreationAffaire = 2001;

type
  TGMCreationAffaire = packed record
    Code: string[10];
    Nom: string[100];
    CodeClient: string[20];
    Application: string[255];
  end;

procedure TGMEnvoiTachesMainForm.btnCreerAffaireClick(ASender: TObject);

var
  DestinationForm: THandle;
  CreationAffaire: TGMCreationAffaire;
  CopyDataStruct: TCopyDataStruct;
begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie du code et du nom
    ControlerInformationManquante(edtCodeAffaireCreer, 'Veuillez indiquer le code de l''affaire à créer.');
    ControlerInformationManquante(edtNomAffaireCreer, 'Veuillez indiquer le nom de l''affaire à créer.');
    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;
    // Initialisation de la structure CreationAffaire
    FillChar(CreationClient, SizeOf(CreationAffaire), #0);
    // Remplissage de la structure CreationAffaire
    CreationAffaire.Code := edtCodeAffaireCreer.Text;
    CreationAffaire.Nom := edtNomAffaireCreer.Text;
    CreationAffaire.CodeClient := edtCodeClientAffaireCreer.Text;
    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantCreationAffaire;
    CopyDataStruct.cbData := SizeOf(CreationAffaire);
    CopyDataStruct.lpData := @CreationAffaire;
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
````