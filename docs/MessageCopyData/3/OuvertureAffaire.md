# Ouverture d'affaire
## Description


Permet de demander l'ouverture dans Gestimum ERP d'une affaire à partir d'un code affaire donné.


## Identifiant


2000


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| Code | string[40] | Code de l'affaire à ouvrir | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

```
const
  IdentifiantOuvertureAffaire = 2000;
 
type
  TGMOuvertureAffaire = packed record
    Code: string[40];
    Application: string[255];
  end;
 
procedure TGMEnvoiTachesMainForm.btnOuvrirAffaireClick(ASender: TObject);
var
  DestinationForm: THandle;
  OuvertureAffaire: TGMOuvertureAffaire;
  CopyDataStruct: TCopyDataStruct;
begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie d'un numéro de téléphone
    ControlerInformationManquante(edtCodeAffaire, 'Veuillez indiquer le code de l''affaire à ouvrir.');
 
    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;
 
    // Initialisation de la structure OuvertureAffaire
    FillChar(OuvertureAffaire, SizeOf(OuvertureAffaire), #0);
 
    // Remplissage de la structure OuvertureAffaire
    OuvertureAffaire.Code := edtCodeAffaire.Text;
 
    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantOuvertureAffaire;
    CopyDataStruct.cbData := SizeOf(OuvertureAffaire);
    CopyDataStruct.lpData := @OuvertureAffaire;
 
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
```