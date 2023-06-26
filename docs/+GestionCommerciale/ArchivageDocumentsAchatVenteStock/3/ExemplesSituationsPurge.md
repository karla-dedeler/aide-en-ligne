# Exemples de situations de purge








| Cas     | État du dossier                                        | Résultat de la purge                                                                              |
|---------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| 1er cas | Dossier ne gérant pas de stock                         | Purge des documents archivés jusqu’à la date de demande de purge - 1 jour                         |
| 2ème cas | Dossier avec gestion de stock                          | Pas d’inventaire, faire un inventaire complet sur le Dépôt xxx                                    |
| 3ème cas | Dossier avec gestion de stock                          | Des documents avant l’inventaire, un inventaire complet                                           |
|          |                                                       | Demande purge date inventaire + 1 jour, purge des documents archivés et des mouvements jusqu’à la  |
|          |                                                       | date d’inventaire (document d’inventaire exclu)                                                    |
| 4ème cas | Dossier avec gestion de stock                          | Un inventaire complet, des documents après l’inventaire complet (archivés/en état Archivés ou En  |
|          |                                                       | cours)                                                                                           |
|          |                                                       | Demande purge date inventaire + 1 jour, message : Rien à purger, pas de document avant l’inventaire |
| 5ème cas | Dossier avec gestion de stock                          | Un inventaire complet, des documents après l’inventaire complet (archivés/en état Archivés ou En  |
|          |                                                       | cours), un inventaire tournant                                                                    |
|          |                                                       | Des documents après l’inventaire tournant (archivés/en état Archivés ou En cours)                  |
|          |                                                       | Demande purge date inventaire + 1 jour, message : Rien à purger, pas de document avant l’inventaire |
| 6ème cas | Dossier avec gestion de stock                          | Un inventaire complet (1), des documents après l’inventaire complet (archivés/en état Archivés ou |
|          |                                                       | En cours), un inventaire complet (2)                                                              |
|          |                                                       | Demande purge date inventaire (2) + 1 jour, purge des documents archivés, en état archivés, et des |
|          |                                                       | mouvements jusqu’à la date d’inventaire (2) (document d’inventaire (2) exclu)                      |
| 7ème cas | Dossier avec gestion de stock                          | Un inventaire complet (1), des documents après l’inventaire complet (archivés/en état Archivés ou |
|          |                                                       | En cours), un inventaire tournant                                                                 |
|          |                                                       | Des documents après l’inventaire tournant (archivés/en état Archivés ou En cours)                  |
|          |                                                       | Un inventaire complet (2)                                                                         |
|          |                                                       | Demande purge 15 jours avant inventaire (2), message : Rien à purger, pas de document avant       |
|          |                                                       | l’inventaire complet (1)                                                                          |
|          |                                                       | Demande purge date inventaire (2) + 1 jour, purge des documents archivés et en état archivés et des |
|          |                                                       | mouvements jusqu’à la date d’inventaire (2) (document d’inventaire (2) exclu)                      |
| 8ème cas | Dossier avec gestion de stock                          | Un inventaire complet (1) dépôt 1, un inventaire complet (1) dépôt 2, des documents après         |
|          |                                                       | l’inventaire (archivés/en état Archivés ou En cours), un inventaire tournant                        |
|          |                                                       | Des documents après l’inventaire (archivés/en état Archivés ou En cours)                           |
|          |                                                       | Un inventaire complet (2) dépôt 1                                                                  |
|          |                                                       | Demande purge date inventaire (2) + 1 jour, purge des documents archivés et en état Archivés et    |
|          |                                                       | des mouvements du dépôt 1 jusqu’à la date d’inventaire (document d’inventaire (2) exclu)          |


[Voir aussi](javascript:RelatedTopic0.Click())



Voir aussi (espace réservé)


1. [Liste des rubriques](#)



