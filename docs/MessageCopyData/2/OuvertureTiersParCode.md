# Ouverture de tiers par code
## Description


Permet de demander l'ouverture dans Gestimum ERP d'un tiers à partir d'un code tiers donné.


## Identifiant


1000


## Paramètres









| Nom | Type |   |   |
|---|---|---|---|
| Code | string[20] | Code du tiers à ouvrir | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message | Facultatif |


## Exemple Delphi

```
const
  IdentifiantOuvertureTiersParCode = 1000;
 
type
  TGMOuvertureTiersParCode = packed record
    Code: string[20];
    Application: string[255];
  end;

procedure TGMEnvoiTachesMainForm.btnOuvrirTiersParCodeClick(ASender: TObject);

var
  DestinationForm: THandle;
  OuvertureTiers: TGMOuvertureTiersParCode;
  CopyDataStruct: TCopyDataStruct;

begin
  ShowHourGlassCursor;
  try
    // Contrôle de la saisie d'un code
    ControlerInformationManquante(edtCodeTiers, 'Veuillez indiquer le code du tiers à ouvrir.');

    // Recherche du handle de la fenêtre de destination
    DestinationForm := RechercherDestinationForm;

    // Initialisation de la structure OuvertureTiers
    FillChar(OuvertureTiers, SizeOf(OuvertureTiers), #0);
 
    // Remplissage de la structure OuvertureTiers
    OuvertureTiers.Code := edtCodeTiers.Text;
 
    // Remplissage de la structure CopyDataStruct
    CopyDataStruct.dwData := IdentifiantOuvertureTiersParCode;
    CopyDataStruct.cbData := SizeOf(OuvertureTiers);
    CopyDataStruct.lpData := @OuvertureTiers;
 
    // Envoi du message WM\_COPYDATA
    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));
  finally
    HideHourGlassCursor;
  end;
end;
```

