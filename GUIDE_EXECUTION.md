# Utiliser la version révisée

Ce guide décrit les commandes et sorties de la version actuelle. La rédaction du rapport viendra ensuite.

## Installation et vérification

Depuis la racine du projet, sous Linux avec Python 3.10 ou plus :

```bash
make install
make test
```

`make install` crée `.venv` et installe le projet. La commande `ring-star` est disponible dans cet environnement. Sans Make :

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m unittest discover -s tests -v
```

Les dépendances sont définies uniquement dans `pyproject.toml`. Le fichier `requirements.txt` contient `-e .` : `pip install -r requirements.txt` installe donc ce même projet, sans recopier la liste des dépendances. Les versions utilisées pour chaque expérience sont conservées dans son fichier `environment.json`.

## Résoudre une instance

```bash
make greedy INSTANCE=data/instances/att48.tsp P=10 ALPHA=1
make local INSTANCE=data/instances/att48.tsp P=10 ITERATIONS=100 SEED=0
make tabu INSTANCE=data/instances/att48.tsp P=10 ITERATIONS=100 CANDIDATES=15 TENURE=10
make exact INSTANCE=data/instances/ulysses16.tsp P=5 TIME_LIMIT=30
```

`TIME_LIMIT=0` enlève volontairement la limite du solveur exact. Une limite positive ne signifie pas que le solveur s'est arrêté sur cette limite : son statut réel est enregistré.

La commande directe expose tous les paramètres :

```bash
.venv/bin/ring-star run tabu data/instances/att48.tsp 10 \
  --alpha 1 --seed 0 --iterations 100 \
  --tabu-tenure 10 --candidates-per-iteration 15
```

Pour un budget de temps d'amélioration :

```bash
.venv/bin/ring-star run local data/instances/att48.tsp 10 \
  --iterations 10000000 --search-time-limit 1
```

Le budget porte sur la phase d'amélioration, après la construction initiale. Il peut être dépassé du temps d'une évaluation en cours. Il ne garantit pas la même trajectoire d'une machine à l'autre. Un budget fixe d'itérations et une graine fixée permettent de reproduire la solution sur le même code ; les temps mesurés peuvent varier.

## Retrouver les sorties

Ouvrir `outputs/index.md` après une exécution. Chaque résolution crée un nouveau dossier dans `outputs/runs/` ; les résultats antérieurs ne sont pas écrasés.

| Fichier dans une résolution | Contenu |
|---|---|
| `summary.md` | Résumé, coûts, statut, liens et affectations |
| `configuration.json` | Problème, paramètres, origine des données et empreinte du fichier source |
| `environment.json` | Versions et empreinte des sources Python |
| `solution.json` | Solution complète, coordonnées, coûts, paramètres et statut |
| `history.csv` | Évolution des coûts, nombre d'évaluations et temps d'amélioration |
| `initial_solution.json` | Construction initiale, pour les méthodes d'amélioration |
| `solver.log` | Journal CBC lorsqu'une résolution exacte a été tentée |
| `figures/` | Solution, avant/après et convergence ; exports PNG, PDF et SVG |

Une exécution exacte sans solution conserve sa configuration et ses diagnostics, mais ne produit ni faux cycle ni figure de solution.

## Lancer une campagne

```bash
make benchmark
make benchmark CONFIG=configs/benchmark_demo.json
make benchmark-full
make benchmark-time
```

- `benchmark_demo.json` : huit instances, `p` dans `{3,5,10}`, trois graines, budget court ; exact limité à `n <= 22`, `p <= 5` et 5 secondes.
- `benchmark_full.json` : davantage de valeurs de `p`, trois poids `alpha`, cinq graines et budgets plus importants. Cette campagne est plus longue et n'est pas présentée comme entièrement exécutée dans la livraison.
- `benchmark_time_budget.json` : deux instances, cinq graines et un budget d'une seconde d'amélioration pour les deux méthodes aléatoires. Les budgets d'itérations élevés servent de garde-fou.

Les chemins d'instances d'un fichier de configuration sont relatifs à ce fichier. Les fautes de noms de paramètres sont rejetées. Les instances et toutes les valeurs de `p` sont vérifiées avant la première résolution.

Chaque campagne crée un dossier indépendant dans `outputs/benchmarks/` :

| Fichier ou dossier | Rôle |
|---|---|
| `index.md` | Point d'entrée, tableau des coûts, statuts et liens |
| `configuration.json`, `inputs.json`, `environment.json` | Configuration, entrées et environnement |
| `runs.csv` | Toutes les tentatives : graine, coûts, temps, paramètres, cycle et affectations |
| `summary.csv` | Moyenne, médiane, minimum, maximum, écart-type et taux de succès |
| `runs/` | Dossier complet de chaque calcul réalisé |
| `figures/by_instance/` | Comparaisons des coûts, temps et gains pour une même instance et un même alpha |
| `figures/gains_alpha_*.png` | Matrices de gains moyens par instance et nombre de stations |
| `completion.json` | Campagne terminée ou interrompue, avec compteurs |

Les méthodes déterministes sont exécutées une fois par cas ; les méthodes aléatoires une fois par graine. Les figures individuelles représentent la meilleure graine, clairement identifiée dans le tableau. Les graphiques comparatifs utilisent les moyennes et écarts-types, pas la seule meilleure exécution.

`mean_cost` concerne les solutions réalisables. `mean_seconds` inclut les tentatives sans solution, mais exclut les cas ignorés par configuration. Un écart-type n'est pas estimé lorsqu'une seule observation est disponible. La colonne des succès et celle des statuts doivent accompagner l'interprétation des moyennes.

Un écart à l'optimum n'est calculé que lorsqu'une preuve d'optimalité a été obtenue. Une borne inférieure et un écart solveur peuvent être absents si CBC ne fournit pas une borne exploitable ; aucune valeur n'est inventée. Les bornes lues dans le journal sont limitées par la précision d'affichage de CBC.

## Régénérer les figures sans recalculer les solutions

```bash
.venv/bin/ring-star plot-campaign outputs/benchmarks/IDENTIFIANT
make compare CAMPAIGN=outputs/benchmarks/IDENTIFIANT
```

Ces commandes relisent les solutions sauvegardées et vérifient leur faisabilité et leurs coûts. Elles n'appellent pas les méthodes d'optimisation. Les coordonnées enregistrées permettent de les utiliser après déplacement de la campagne, sans fichier `.tsp` à son emplacement d'origine.

Pour une solution seule :

```bash
.venv/bin/ring-star plot-saved CHEMIN/solution.json --output apercu.png
```

Les anciens CSV dépourvus de cycles ne sont pas utilisés pour inventer une nouvelle solution graphique. Il faut relancer ces expériences avec la nouvelle version.

## Conventions et limites

- Exactement `p` stations, avec `3 <= p <= n` ; le premier sommet est imposé.
- `0 <= alpha <= 10` ; objectif `alpha * longueur_cycle + somme_distances_affectation`.
- Distances euclidiennes non arrondies, conformément à la modélisation du projet ; les types TSPLIB `GEO` et `ATT` ne sont pas appliqués.
- Les valeurs sont exprimées dans les unités des coordonnées. Ne pas les interpréter comme des kilomètres ni comparer directement les coûts bruts d'instances différentes.
- Les fichiers d'entrée doivent avoir des identifiants TSPLIB exactement égaux à `1..n`. La numérotation Python interne commence à zéro et les exports à un.
- La recherche locale échantillonne des échanges : son arrêt ne certifie pas un optimum local sur tout le voisinage.
- Une comparaison à nombre d'itérations égal n'est pas une comparaison à effort égal. Le nombre de candidats évalués et les temps sont enregistrés ; une configuration dédiée propose un budget de temps commun.
- Les anciennes sources et sorties archivées ont été supprimées ; les campagnes actuelles restent dans `outputs/`.
- L’énoncé est conservé dans `docs/enonce_sae.pdf`. Le rapport sera rédigé ensuite.

## Fabriquer une archive

```bash
make package
```

Le ZIP conserve les sources, tests, configurations et sorties ; il exclut `.git`, les environnements virtuels, les caches et les fichiers Python compilés. Les configurations locales absentes de l'archive d'origine ne sont pas recréées.

## Mettre à jour un dépôt existant

Extraire les fichiers de cette archive directement à la racine du dépôt existant. Une extraction ne supprime pas les anciens fichiers déjà présents :

```bash
make cleanup
make install
make test
```

`make cleanup` supprime uniquement `_legacy/`, `archives/`, l’ancien fichier de versions figées, l’image inutilisée et l’ancien lanceur de benchmarks. Il conserve l’énoncé avant suppression si nécessaire. Il ne touche pas à `.git`, à l’environnement `.venv`, aux configurations locales ni aux résultats actuels. Un éventuel dossier `report/` n’est retiré que s’il est vide.
