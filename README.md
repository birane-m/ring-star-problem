# Ring-Star Problem

Ce dépôt contient une implémentation Python du problème **Ring-Star**, aussi
appelé problème de l'anneau-étoile.

L'idée générale est la suivante : on dispose d'un ensemble de points représentant
des lieux possibles dans une agglomération. On doit choisir `p` stations parmi
ces points, construire une ligne de transport circulaire passant par les stations
choisies, puis rattacher chaque point non choisi à une station.

Le projet permet de :

- charger des instances TSPLIB `.tsp` ;
- construire une solution avec une heuristique gloutonne ;
- améliorer cette solution avec des métaheuristiques ;
- résoudre exactement certaines petites instances par PLNE ;
- générer des résultats en JSON et Markdown ;
- produire des visualisations PNG ;
- comparer les méthodes avec des benchmarks.

Pour la description mathématique complète du problème, voir :

```text
docs/specification.md
```

## Problème Étudié

Une solution Ring-Star contient trois éléments :

- un ensemble de `p` stations ;
- un cycle métro reliant ces stations ;
- une affectation de chaque point à une station.

La fonction objectif combine :

- le coût du cycle métro ;
- le coût de marche des points non-stations vers leur station ;
- un paramètre `alpha` qui pondère le coût métro.

Le premier point de l'instance est toujours imposé comme station, conformément à
l'énoncé.

## Méthodes Implémentées

### Heuristique Gloutonne

La méthode gloutonne construit rapidement une solution réalisable :

- sélection de stations ;
- affectation des points à leur station la plus proche ;
- construction d'un cycle sur les stations ;
- amélioration du cycle par 2-opt.

### Métaheuristiques

Deux méthodes d'amélioration sont disponibles :

- recherche locale par échanges station / non-station ;
- recherche tabou, qui accepte parfois des déplacements moins bons pour sortir
  d'un optimum local.

### Résolution Exacte

La résolution exacte utilise un modèle PLNE avec PuLP/CBC. Elle permet de prouver
l'optimalité sur des instances de taille raisonnable. Sur des instances plus
grandes, elle peut devenir coûteuse en temps.

## Installation

Après clonage du dépôt :

```bash
make install
```

Cette commande crée l'environnement virtuel `.venv` et installe les dépendances
de `requirements.txt`.

Pour supprimer l'environnement virtuel :

```bash
make clean
```

## Utilisation Rapide

Lancer les tests :

```bash
make test
```

Résoudre une instance avec l'heuristique gloutonne :

```bash
make greedy INSTANCE=data/instances/att48.tsp P=10
```

Résoudre avec la recherche locale :

```bash
make local INSTANCE=data/instances/att48.tsp P=10 ITERATIONS=100
```

Résoudre avec la recherche tabou :

```bash
make tabu INSTANCE=data/instances/att48.tsp P=10 ITERATIONS=100 CANDIDATES=15
```

Résoudre exactement par PLNE :

```bash
make exact INSTANCE=data/instances/ulysses16.tsp P=5 TIME_LIMIT=0
```

`TIME_LIMIT=0` signifie qu'aucune limite de temps n'est imposée au solveur exact.

## Sorties Générées

Chaque commande de résolution génère automatiquement :

- un fichier JSON ;
- un résumé Markdown ;
- une visualisation PNG de la solution.

Exemple :

```bash
make tabu INSTANCE=data/instances/ulysses16.tsp P=5
```

peut générer :

```text
outputs/results/metaheuristics/ulysses16_tabu_p5.json
outputs/results/metaheuristics/ulysses16_tabu_p5.md
outputs/figures/metaheuristics/ulysses16_tabu_p5.png
```

## Benchmarks

Les benchmarks servent à comparer plusieurs méthodes sur les mêmes instances et
les mêmes valeurs de `p`.

Générer les résultats heuristiques et métaheuristiques :

```bash
make benchmark
```

Générer le CSV comparatif et les graphiques globaux :

```bash
make compare
```

Générer les PNG de toutes les solutions benchmarkées :

```bash
make plot-solutions
```

Tout générer pour le rapport :

```bash
make report
```

Les résultats sont écrits dans :

```text
outputs/results/
outputs/figures/
```

## Structure du Projet

```text
data/instances/          Instances TSPLIB utilisées
docs/specification.md    Spécification mathématique du problème
src/ring_star/           Code source principal
tests/                   Tests unitaires
scripts/                 Scripts de génération des benchmarks du rapport
outputs/                 Résultats générés localement
```

## Commandes Avancées

La commande générique suivante peut aussi être utilisée directement :

```bash
PYTHONPATH=src .venv/bin/python -m ring_star.cli run tabou data/instances/att48.tsp 10
```

Méthodes acceptées :

- `gloutonne`, `heuristique`, `greedy` ;
- `locale`, `local`, `local_search` ;
- `tabou`, `tabu`, `meta`, `metaheuristique` ;
- `exact`, `plne`.

## Vérification

Avant de modifier ou publier le projet :

```bash
make test
```

Les tests couvrent notamment :

- le chargement des instances TSPLIB ;
- la validation des solutions ;
- les heuristiques ;
- les métaheuristiques ;
- le modèle exact ;
- la génération des résultats et visualisations.
