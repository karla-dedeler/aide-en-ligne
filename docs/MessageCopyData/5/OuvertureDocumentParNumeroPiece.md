# Ouverture de document d'achat, vente ou stock par numéro de pièce
## Description


Permet de demander l'ouverture dans Gestimum ERP d'un document d'achat, vente ou stock à partir d'un numéro de pièce donné.


## Identifiant


4001


## Paramètres










| Nom | Type |   | Valeurs possibles |   |
| TypeDocument | string[1] | Type du document d'achat, vente ou stock à ouvrir | A : Achat
V : Vente
S : Stock | Obligatoire |
| SousTypeDocument | string[1] | Sous-type du document d'achat, vente ou stock à ouvrir | Achats :
D = Demande de prix
C = Commande
B = Livraison
R = Retour
F = Facture
A = Avoir
0 = Avoir financier
1 = Facture financière
 
Ventes :
P = Pro-Forma
D = Devis
C = Commande
B = Livraison
R = Retour
F = Facture
A = Avoir
0 = Avoir financier
1 = Facture financière
 
Stocks :
E = Entrée de stock
S = Sortie de stock
T = Transfert de stock
O = Assemblage de nomenclatures
M = Ecart de stock
X = Sortie pour perte | Obligatoire |
| NumeroPiece | string[15] | Numéro de pièce du document d'achat, vente ou stock à ouvrir |   | Obligatoire |
| Application | string[255] | Titre de l'application de destination du message |   | Facultatif |


## Exemple Delphi


const


  IdentifiantOuvertureDocumentParPiece = 4001;


 


type


  TGMOuvertureDocumentParPiece = packed record


    TypeDocument: string[1];


    SousTypeDocument: string[1];


    NumeroPiece: string[15];


    Application: string[255];


  end;                           


 


procedure TGMEnvoiTachesMainForm.btnOuvrirDocumentParPieceClick(ASender: TObject);


var


  DestinationForm: THandle;


  OuvertureDocument: TGMOuvertureDocumentParPiece;


  CopyDataStruct: TCopyDataStruct;


begin


  ShowHourGlassCursor;


  try


    // Contrôle de la saisie d'un type, d'un sous-type et d'un numéro de pièce


    ControlerInformationManquante(edtTypeDocument, 'Veuillez indiquer le type du document à ouvrir.');


    ControlerInformationManquante(edtSousTypeDocument, 'Veuillez indiquer le sous-type du document à ouvrir.');


    ControlerInformationManquante(edtNumeroPieceDocument, 'Veuillez indiquer le numéro de pièce du document à ouvrir.');


 


    // Recherche du handle de la fenêtre de destination


    DestinationForm := RechercherDestinationForm;


 


    // Initialisation de la structure OuvertureDocument


    FillChar(OuvertureDocument, SizeOf(OuvertureDocument), #0);


 


    // Remplissage de la structure OuvertureDocument


    OuvertureDocument.TypeDocument := edtTypeDocument.Text;


    OuvertureDocument.SousTypeDocument := edtSousTypeDocument.Text;


    OuvertureDocument.NumeroPiece := edtNumeroPieceDocument.Text;


 


    // Remplissage de la structure CopyDataStruct


    CopyDataStruct.dwData := IdentifiantOuvertureDocumentParPiece;


    CopyDataStruct.cbData := SizeOf(OuvertureDocument);


    CopyDataStruct.lpData := @OuvertureDocument;


 


    // Envoi du message WM\_COPYDATA


    SendMessage(DestinationForm, WM\_COPYDATA, Integer(Handle), Integer(@CopyDataStruct));


  finally


    HideHourGlassCursor;


  end;


end;


