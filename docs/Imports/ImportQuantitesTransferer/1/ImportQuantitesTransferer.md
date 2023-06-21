# Import de quantités à transférer



Le transfert de document avec import de fichier utilise cette structure de fichier


 


1. soit sur la liste des champs disponible pour l'import



```
    DOC_NUMERO
    LIG_NUMERO
    ART_CODE
    ART_GAMME
    LIG_QTE
    Si multi lot
    LLD_NUMLOT;LLD_QTE;LLD_DT_FAB;LLD_DT_PER
    Si mono lot
    LIG_NUMLOT;LIG_DT_PER;LIG_DT_FAB
    LIG_ZONE
    PRJ_CODE
    LIG_MEMO

```

1. soit en allant voir dans les préférences utilisateurs de la session Windows qui lancera le transfert en ligne de commande.


