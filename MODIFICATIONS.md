# Modifications de la version 0.2

## Algorithmes et contrôles

- Correction du voisinage 2-opt : les inversions atteignant le dernier sommet sont explorées.
- Évaluation des échanges 2-opt par différence de quatre arêtes, avec tolérance numérique.
- Réutilisation des distances dans une exécution.
- Validation des coordonnées finies, paramètres entiers et budgets.
- Échantillonnage de mouvements distincts sans boucle de rejet.
- Correction de la durée d'interdiction tabou : une tenure de un interdit effectivement le retour à l'itération suivante.
- Enregistrement des itérations réalisées, évaluations, motifs d'arrêt et trajectoires.
- Distinction des statuts CBC : optimum prouvé, solution entière sans preuve, absence de solution et indisponibilité du solveur.
- Conservation des journaux et bornes disponibles ; gestion des objectifs constants nuls.

## Architecture et sorties

- Centralisation des exécutions dans `execution.py` et des exports dans `artifacts.py`.
- Réduction de la CLI et conservation des principaux alias existants.
- Campagnes configurables et répétitions sur plusieurs graines.
- Identification des cas incluant `alpha` ; rejet des doublons de graines dans les imports comparatifs.
- Sorties complètes par exécution, index de navigation et empreintes des sources et données.
- Sauvegarde des cycles complets ; vérification des coûts avant relecture graphique.
- Régénération des figures sans résoudre de nouveau le problème.
- Les anciennes sources et sorties archivées ont été retirées ; les campagnes actuelles sont conservées.

## Figures

- Styles communs et distinction de la station imposée.
- Mise en page adaptée aux nuages de points allongés, sans déformer la géométrie.
- Coûts, paramètres, statut, durée et graine visibles.
- Comparaisons avant/après et courbes de convergence.
- Comparaisons par instance avec dispersion entre graines et matrices de gains.
- Distinction graphique des optima prouvés et solutions exactes sans preuve.
- Exports PNG, PDF et SVG.

## Livraison

- Installation du paquet et commande `ring-star`.
- Configurations de démonstration, d'expériences étendues et de budget de temps commun.
- Tests de régression et références par énumération sur de petits problèmes.
- Workflow GitHub Actions fourni pour Python 3.10 et 3.12 ; son exécution distante dépendra du dépôt.
- Ancien README remplacé par un point d’entrée vers le guide actuel ; le rapport reste à rédiger.

## Nettoyage

- Suppression des anciennes implémentations, des archives de sorties obsolètes, de l’image inutilisée et du lanceur de benchmarks remplacé par les campagnes configurées.
- Conservation de l’énoncé dans `docs/enonce_sae.pdf`.
- Suppression du second fichier requirements : les dépendances ont une source unique, `pyproject.toml`, utilisée aussi par `requirements.txt`.
- Archive sans dossier englobant, environnement virtuel, métadonnées Git ni caches.
- Commande `make cleanup` pour appliquer les suppressions dans un dépôt existant tout en conservant son historique Git.
