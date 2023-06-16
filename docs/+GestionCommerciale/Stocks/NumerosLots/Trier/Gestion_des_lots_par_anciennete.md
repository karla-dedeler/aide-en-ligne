# Gestion des lots par ancienneté



Lors de l'affectation manuelle du lot (Exemple : Lors du transfert d'une commande client), il sélectionne désormais par défaut la première ligne qui vérifie les conditions suivantes :


* Si périssable et pas de sélection explicite : Premier avec une date limite de consommation minimale et stock suffisant,
* Si non trouvé et périssable : Premier avec une date limite de consommation minimale et stock non nul,
* Si non trouvé et pas de sélection explicite : Premier avec stock suffisant,
* Si non trouvé : Premier avec stock non nul,
* Si non trouvé : Premier avec lot renseigné.


 


Par conséquent, l'ordre dans lequel se trouve la grille est important (N° de lot, Dont création du lot, Stock disponible, Date de péremption, etc. ; Croissant ou décroissant).


 


En fonction du contexte, l'ordre par défaut est différent (Exemple : sélection pour affectation du N° de lot --> Ordre par "Date de création du lot").


