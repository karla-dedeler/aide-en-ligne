# Ouverture de document d'achat, vente ou stock par numéro interne
## Description


Permet de demander l'ouverture dans Gestimum ERP d'un document d'achat, vente ou stock à partir d'un numéro interne donné.


## Identifiant


4000


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| NumeroInterne | string[10] | Numéro interne du document d'achat, vente ou stock à ouvrir | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

````
const
  IdentifiantOuvertureDocument = 4000;

type
  TGMOuvertureDocument = packed record
    NumeroInterne: string[10];
    Application: string[255];
  end;                           

procedure TGMEnvoiTachesMainForm.btnOuvrirDocumentClick(ASender: TObject);

var
  DestinationForm: THandle;
  OuvertureDocument: TGMOuvertureDocument;
  CopyDataStruct: TCopyDataStruct;
begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie d'un numéro interne
    ControlerInformationManquante(edtNumeroInterneDocument, 'Veuillez indiquer le numéro interne du document à ouvrir.');
    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;
    // Initialisation de la structure OuvertureDocument
    FillChar(OuvertureDocument, SizeOf(OuvertureDocument), #0);
    // Remplissage de la structure OuvertureDocument
    OuvertureDocument.NumeroInterne := edtNumeroInterneDocument.Text;
    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantOuvertureDocument;
    CopyDataStruct.cbData := SizeOf(OuvertureDocument);
    CopyDataStruct.lpData := @OuvertureDocument;
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
````