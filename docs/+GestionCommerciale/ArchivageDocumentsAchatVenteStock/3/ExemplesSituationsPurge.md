# Exemples de situations de purge








| Cas | État du dossier | Résultat de la purge |
| 1er cas | Dossier ne gérant pas de stock Pas de demande d'inventaire | Purge des documents archivés jusqu’à la date de demande de purge -1 jour |
| 2ème cas | Dossier avec gestion de stock Pas d’inventaire | Message : faire un inventaire complet sur le Dépôt xxx. |
| 3ème cas | Dossier avec gestion de stock
Des documents avant l’inventaire
Un inventaire complet
Demande purge date inventaire + 1 jour | Purge des documents archivés et des mouvements jusqu’à la date d’inventaire (document d’inventaire exclu). |
| 4ème cas | Dossier avec gestion de stock
Un inventaire complet
Des documents après l’inventaire complet (archivés/ en état Archivés ou En cours)
Demande purge date inventaire + 1 jour | Message : Rien à purger
En effet, car il n’y a pas de document avant l’inventaire complet |
| 5ème cas | Dossier avec gestion de stock
Un inventaire complet
Des documents après l’inventaire complet (archivés/ en état Archivés ou En cours)
Un inventaire tournant
Des documents après l’inventaire tournant (archivés/ en état Archivés ou En cours)
Demande purge date inventaire + 1 jour | Message : Rien à purger
En effet, car il n’y a pas de document avant l’inventaire complet |
| 6ème cas | Dossier avec gestion de stock
Un inventaire complet (1)
Des documents après l’inventaire complet (archivés/ en état Archivés ou En cours)
Un inventaire complet (2)
Demande purge date inventaire (2) + 1 jour | Purge des documents archivés, en état archivés, et des mouvements jusqu’à la date d’inventaire (2) (document d’inventaire (2) exclu) |
| 7ème cas | Dossier avec gestion de stock
Un inventaire complet (1)
Des documents après l’inventaire complet (archivés/ en état Archivés ou En cours)
Un inventaire tournant
Des documents après l’inventaire tournant (archivés/ en état Archivés ou En cours)
Un inventaire complet (2)
Demande purge 15 jours avant inventaire (2) | Message : Rien à purger
En effet, car il n’y a pas de document avant l’inventaire complet (1)
Demande purge date inventaire (2) + 1 jour :
Purge des documents archivés et en état archivés et des mouvements jusqu’à la date d’inventaire (2) (document d’inventaire (2) exclu) |
| 8ème cas | Dossier avec gestion de stock
Un inventaire complet (1) dépôt 1
Un inventaire complet (1) dépôt 2
Des documents après l’inventaire (archivés/ en état Archivés ou En cours)
Un inventaire tournant
Des documents après l’inventaire (archivés/ en état Archivés ou En cours)
Un inventaire complet (2) dépôt 1
Demande purge date inventaire (2) + 1 jour | Purge des documents archivés et en état Archivés et des mouvements du dépôt1 jusqu’à la date d’inventaire (document d’inventaire (2) exclu) |


[Voir aussi](javascript:RelatedTopic0.Click())



Voir aussi (espace réservé)


1. [Liste des rubriques](#)



