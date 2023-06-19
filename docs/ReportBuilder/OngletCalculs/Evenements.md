# Evénements
Des lignes de code peuvent être écrites en langage Pascal et exécutées lorsqu'un événement d'un objet du rapport se produira.


 


Par exemple, lors l'impression, l'événement "BeforePrint" de la bande "Header" est déclenché, permettant d'exécuter du code avant l'impression de la bande.


## Evénements de création et de destruction







| Nom | Description |
| OnCreate | L'événement OnCreate spécifie le gestionnaire d'événements à appeler lors de la première création du concepteur. Vous pouvez écrire du code dans le gestionnaire d'événements qui définit les valeurs initiales des propriétés et effectue tout traitement que vous souhaitez effectuer avant que l'utilisateur commence à interagir avec le concepteur.
Lorsqu'un formulaire est créé et que sa propriété Visible est True, les événements suivants se produisent dans l'ordre indiqué :* OnCreate
* OnShow
* OnActivate
* OnPaint
 |
| OnDestroy | L'événement OnDestroy se produit lorsque le concepteur est sur le point d'être détruit. Un formulaire est détruit par les méthodes Destroy, Free ou Release, ou lorsque le formulaire principal de l'application est fermé. |


## Événements du rapport







| Nom | Description |
| AfterAutoSearchDialogCreate | Cet événement se déclenche après la création de l'AutoSearchDialog, mais avant qu'il ne soit configuré pour refléter les AutoSearchFields. Les modifications apportées aux champs AutoSearchField à partir de cet événement seront reflétées dans la boîte de dialogue. |
| AfterPrint | Cet événement se déclenche une fois le processus d'impression terminé. Lorsque vous imprimez sur l'imprimante ou sur le fichier, AfterPrint se déclenche une fois le travail d'impression fermé ou après la fermeture du fichier. Lors de l'impression à l'écran, AfterPrint se déclenche après la fermeture du formulaire Aperçu avant impression. |
| BerforeAutoSearchDialogCreate | Cet événement se déclenche avant la création de l'AutoSearchDialog. Si ShowAutoSearchDialog est défini sur False dans cet événement, la boîte de dialogue n'est pas créée ou affichée. |
| BeforePrint  | Cet événement se déclenche avant que le processus d'impression ne commence. |
| OnAssignPreviewFormSettings | Cet événement se déclenche pour prendre en charge le paramètre de TppPreviewFormSettings et de TppTextSearchSettings avant que les valeurs ne soient affectées au formulaire d'aperçu. Fournit le timing approprié pour leur attribuer de nouvelles valeurs avant de les transférer dans le formulaire d'aperçu.

Utilisez OnPreviewFormCreate pour contrôler directement les propriétés de la boîte de dialogue, car l'événement OnPreviewFormCreate se déclenche après le transfert des paramètres.
 |
| OnAutoSearchDialogClose | Cet événement se déclenche après la fermeture de l'AutoSearchDialog. |
| OnCancel | Cet événement se déclenche quand l'utilisateur annule l'impression |
| OnCancelDialogCreate | Cet événement se déclenche après la création de la boîte de dialogue d'annulation. Vous pouvez accéder à la boîte de dialogue Annuler via la propriété CancelDialog. |
| OnCancelDialogClose | Cet événement se déclenche lorsque la boîte de dialogue Annuler est fermée. Cette boîte de dialogue est fermée lorsque l'utilisateur clique sur le bouton Annuler ou lorsque le processus d'impression est terminé. La boîte de dialogue Annuler s'affiche uniquement lors de l'impression sur l'imprimante ou dans un fichier. |
| OnEndColumn | Cet événement se déclenche après l'impression d'une colonne. Par exemple une colonne d'étiquette |
| OnEndFirstPass | Cet événement se déclenche une fois que le rapport a terminé le premier passage. Vous pouvez enregistrer tous les totaux généraux ou autres valeurs calculées à ce stade. |
| OnEndPage | Cet événement se déclenche une fois l'impression d'une page terminée. Si vous définissez DonePrinting sur True dans ce gestionnaire d'événements, aucune autre page ne s'imprimera. |
| OnEndSecondPass | Cet événement se déclenche une fois que le moteur de rapports a terminé le second passage. Si vous prenez le contrôle manuel du processus d'impression et avez des variables qui ne sont plus nécessaires lorsque le rapport est terminé, vous pouvez les effacer ici. |
| OnGetAutoSearchValues | Cet événement se déclenche chaque fois que le rapport est généré via un appel à la méthode Print et que AutoSearchFields existe. L'événement se déclenche quel que soit l'état de la propriété ShowAutoSearchDialog. Cet événement est généralement utilisé pour transférer des valeurs de critères de recherche aux composants d'accès aux données lorsque vous prenez le contrôle manuel sur les AutoSearchFields. Pour plus d'informations sur la manière et le moment de contrôler manuellement les champs AutoSearch, voir AutoSearchFields.

Si ShowAutoSearchDialog a la valeur True et que la boîte de dialogue AutoSearch a été affichée, mais que l'utilisateur a cliqué sur «Annuler» pour quitter la boîte de dialogue, cet événement ne se déclenchera pas.
 |
| OnNoData | Cet événement se déclenche lorsqu'aucune donnée n'est trouvée par le pipeline de données connecté à un rapport. |
| OnOutlineNodeCreate | Cet événement se déclenche chaque fois qu'un nœud hiérarchique est créé au cours du processus de génération de rapport. Lorsqu'elle est activée, une structure arborescente hiérarchique est générée dynamiquement par le moteur de rapport et rendue par l'aperçu du rapport.

La propriété OutlineSettings est utilisée pour contrôler le comportement de la génération de plan de rapport. L'événement OnOutlineNodeCreate peut être utilisé pour personnaliser davantage le plan lors de sa génération.

Le paramètre aNode est le nœud en cours de création. Définissez la propriété aNode.Caption pour modifier la légende par défaut affectée au nœud.

La valeur par défaut du paramètre aAccept est True. Définissez aAccept sur False pour empêcher le nœud d'être inclus dans le rapport.
 |
| OnPageRequest | Cet événement se déclenche une fois que la méthode Print a été appelée et que tous les périphériques actuellement connectés ont été interrogés pour les pages du rapport qui sont nécessaires. Le résultat de ce processus d'interrogation est résumé par l'éditeur dans un objet PageRequest, qui est ensuite transmis au producteur. Le producteur tente ensuite de fournir les pages demandées, soit en exécutant le moteur de rapport (comme dans le cas des producteurs CustomReport), soit en recherchant le fichier d'archive (comme dans le cas des producteurs ArchiveReader). |
| OnPreviewFormCreate | Cet événement se déclenche une fois le formulaire Aperçu avant impression créé. Vous pouvez accéder au formulaire Aperçu avant impression via la propriété PreviewForm.
Vous pouvez définir les caractéristiques du formulaire Aperçu avant impression et du composant Visionneuse. Par exemple, le code suivant définit le formulaire Aperçu avant impression pour être agrandi et définit le zoom de la visionneuse sur la largeur de la page.
   ppReport1.PreviewForm.WindowState := wsMaximized;
   TppViewer (ppReport1.PreviewForm.Viewer) .ZoomSetting := zs100Percent;
Remarque: Assurez-vous de placer ppViewr dans la clause uses de votre unité afin que le type énuméré ZoomSetting soit reconnu par le compilateur. |
| OnPreviewFormClose | Cet événement se déclenche après la fermeture du formulaire Aperçu avant impression. Le formulaire Aperçu avant impression n'est créé que lorsque DeviceType a été défini sur dtScreen et que la méthode Print a été appelée. |
| OnPrintDialogCreate | Cet événement se déclenche une fois la boîte de dialogue Imprimer créée. Vous pouvez accéder à l'impression
Dialogue via la propriété PrintDialog. |
| OnPrintDialogClose | Cet événement se déclenche après la fermeture du dialogue d'impression. Vous pouvez accéder à la boîte de dialogue Imprimer via la propriété PrintDialog. |
| OnSaveText | L'événement OnSaveText se déclenche avant qu'un composant textuel soit écrit sur la ligne de texte par TextFileDevice. Toute modification apportée au paramètre Texte sera sauvegardée sur la ligne. Cet événement se déclenche uniquement lors de l'impression dans un fichier texte. |
| OnStartColumn | Cet événement se déclenche avant qu'une nouvelle colonne ne commence à imprimer sur le rapport. |
| OnStartFirstPass | Cet événement se déclenche avant que le moteur de rapport ne commence. Vous pouvez effectuer une initialisation au niveau du rapport dans cet événement. |
| OnStartPage | Cet événement se déclenche avant qu'une nouvelle page ne commence à imprimer sur le rapport. |
| OnStartSecondPass | Cet événement se déclenche avant que le moteur de rapport ne commence le second passage. Si vous prenez le contrôle manuel du processus d'impression, vous devez restaurer toutes les variables de rapport aux valeurs appropriées pour l'impression de la première page. |


## Événements des groupes standards







| Nom | Description |
| AfterGenerate | L'événement AfterGenerate se déclenche après l'impression du groupe. Utilisez l'événement AfterGenerate lorsque vous souhaitez effectuer des actions après l'impression d'un groupe. AfterGenerate diffère de AfterPrint en ce que l'impression AfterPrint se déclenche chaque fois que le groupe a la possibilité d'imprimer. Parfois, le groupe a la possibilité d'imprimer, mais ce n'est pas le cas pour diverses raisons (généralement l'impression sur la page suivante à la place.) Dans ces cas, AfterPrint se déclenche, mais AfterGenerate ne le fait pas. |
| AfterPrint | Cet événement se déclenche après l'impression du groupe. |
| BeforeGenerate | L'événement BeforeGenerate se déclenche avant l'impression du groupe. Utilisez l'événement BeforeGenerate lorsque vous souhaitez effectuer des actions avant l'impression d'un groupe. BeforeGenerate diffère de BeforePrint en ce que BeforePrint se déclenche à chaque fois qu'un groupe a la possibilité d'imprimer. Parfois, le groupe a la possibilité d'imprimer, mais pour diverses raisons (généralement en imprimant sur la page suivante à la place.) Dans ces cas, BeforePrint se déclenche, mais pas BeforeGenerate. |
| BeforePrint | Cet événement se déclenche avant qu'un groupe commence à imprimer. |


## Événements des groupes personnalisés







| Nom | Description |
| AfterGroupBreak | Cet événement se déclenche chaque fois qu'un groupe est fini et que le groupe de bas de page a terminé l'impression. |
| BeforeGroupBreak | Cet événement se déclenche chaque fois qu'un groupe se finit avant que le groupe d'en-têtes de groupe ne commence à s'imprimer. |
| OnGetBreakValue | Cet événement se déclenche chaque fois qu'un groupe vérifie la valeur de rupture. Vous pouvez remplacer la valeur du groupe en définissant le paramètre aBreakValue |


## Événements des variables







| Nom | Description |
| OnCalc | Utilisez le gestionnaire d'événement OnCalc lorsque vous souhaitez effectuer des calculs. L'événement OnCalc se déclenche lorsque le calcul du composant doit être effectué. Par défaut, cet événement se produit une fois pour chaque traversée d'enregistrements terminée par le moteur de rapport. Vous pouvez contrôler exactement le moment où le composant est calculé et réinitialisé à l'aide des propriétés CalcType et ResetType respectivement.
La valeur actuelle de la variable est transmise dans le paramètre Value. Vous pouvez ensuite définir la valeur de la variable en définissant cette propriété ou en définissant directement l'une des propriétés 'As' de la variable. Si vous choisissez de définir le paramètre Value, assurez-vous que le type de données de votre affectation correspond au DataType de la variable. Par exemple, si le DataType est défini sur dtString, le code suivant déclenchera une exception:
Valeur := Valeur + 1;
Ce gestionnaire d'événements nécessite que Variable.DataType soit défini sur un type numérique. |
| OnDrawCommandClick | L'événement OnDrawCommandClick se déclenche lorsque la commande draw qui représente le composant dans le document de rapport est "cliquée" dans le composant TppViewer. Le paramètre aDrawCommand contient un objet TppDrawCommand. La pratique habituelle consiste à placer des données ou un handle d'objet d'information dans la propriété Tag de DrawCommand dans l'événement OnDrawCommandCreate afin que quelque chose d'intéressant puisse être fait en réponse au clic. |
| OnDrawCommandCreate | L'événement OnDrawCommandCreate se déclenche lorsque la commande draw qui représente le composant dans le document de rapport est créée. Le paramètre aDrawCommand contient l'objet TppDrawCommand. La pratique habituelle consiste à placer des données ou un handle d'objet d'information dans la propriété Tag de la DrawCommand, puis à faire quelque chose d'intéressant lorsque l'événement OnDrawCommandClick se déclenche. |
| OnGetText | L'événement OnGetText se déclenche chaque fois que la propriété Text du composant est référencée. Cela vous permet de remplacer la valeur de la propriété Text.
Remarque: Si vous devez regrouper un champ de texte personnalisé (TppVariable, TppLabel, ..), vous devez ajouter du code à ce gestionnaire d'événements pour contrôler la valeur du texte plutôt que d'utiliser l'événement OnPrint ou OnCalc. Ceci est nécessaire en raison du moment où chacun de ces événements se déclenche. |
| OnPrint | L'événement OnPrint se déclenche avant l'impression du composant. Utilisez l'événement OnPrint lorsque vous souhaitez contrôler dynamiquement l'apparence du composant de rapport. Par exemple, vous pouvez imprimer un composant de rapport de manière conditionnelle en définissant la propriété Visible du composant du rapport au moment de l'exécution en fonction de la valeur du champ de données. |
| OnReset | Utilisez le gestionnaire d'événements OnReset lorsque vous souhaitez contrôler la valeur initiale de la variable avant le début des calculs. L'événement OnReset se déclenche une fois que la valeur de la variable a été effacée. Vous pouvez définir la valeur initiale en modifiant le paramètre Value. Le code suivant initialiserait la variable à une valeur de 1:
Valeur := 1;
Ce gestionnaire d'événements nécessite que Variable.DataType soit défini sur un type numérique. Si le Variable.DataType n'était pas défini sur un type numérique, une exception serait déclenchée. |


