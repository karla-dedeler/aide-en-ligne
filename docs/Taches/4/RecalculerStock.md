# RecalculerStock

## Nom de la tâche


RecalculerStock


## Description de la tâche


Recalcule le stock.


## Paramètres spécifiques de la tâche











| Nom | Description | Valeurs possibles | Présence | Valeur par défaut | Exemple |
| Depots | Dépôts dans lesquels le stock est à recalculer, séparés par des ";"
ou alors \* si le stock est à recalculer dans l'ensemble des dépôts |   | Obligatoire |   | DEP1;DEP2;DEP5 |
| Article1 | Premier article de l'intervalle d'articles dont il faut recalculer le stock |   | Facultatif |   |   |
| Article2 | Dernier article de l'intervalle d'articles dont il faut recalculer le stock |   | Facultatif |   |   |
| Articles | Articles dont le stock est à recalculer, séparés par des ";" |   | Facultatif |   | A2;X12;C1 |
| Famille1 | Première famille d'articles dont il faut recalculer le stock |   | Facultatif |   |   |
| Famille2 | Dernière famille d'articles dont il faut recalculer le stock |   | Facultatif |   |   |
| SousFamille1 | Première sous-famille d'articles dont il faut recalculer le stock |   | Facultatif |   |   |
| SousFamille2 | Dernière sous-famille d'articles dont il faut recalculer le stock |   | Facultatif |   |   |
| TypeArticles | Type des articles dont il faut recalculer le stock |   | Facultatif |   |   |
| Categorie | Catégorie des articles dont il faut recalculer le stock |   | Facultatif |   |   |
| ModeGestion | Mode de gestion des articles dont il faut recalculer le stock |   | Facultatif |   |   |
| GroupeEquivalences | Groupe d'équivalence des articles dont il faut recalculer le stock |   | Facultatif |   |   |
| MouvementsStock | Mettre à jour les mouvements de stock | Oui
Non | Facultatif | Non |   |
| NumerosSeriesReserves | Supprimer la réservation des numéros de séries | Oui
Non | Facultatif | Non |   |
| EpurerArticles | Épurer les articles | Oui
Non | Facultatif | Non |   |
| EpurerGammes | Épurer les gammes | Oui
Non | Facultatif | Non |   |
| EpurerNumerosLots | Épurer les numéros de lots | Oui
Non | Facultatif | Non |   |
| EpurerNumerosSeries | Épurer les numéros de séries | Oui
Non | Facultatif | Non |   |


## Exemple


[Tâche]


Nom=RecalculerStock


Journal=RecalculerStock.log


 


[Société]


Fichier=C:\ProgramData\Gestimum\DEMO.Gestimum


Utilisateur=DEMO


 


[Paramètres]


Dépots=001;002;SAV


Article1=ELS


Article2=EPE


MouvementsStock=Oui


