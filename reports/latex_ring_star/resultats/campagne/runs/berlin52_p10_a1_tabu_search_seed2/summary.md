# Résultat tabu_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 3540.609
- Coût marche : 5916.322
- Coût total : 9456.930

## Stations choisies

1, 8, 12, 18, 20, 24, 27, 34, 42, 43

## Cycle métro

1 -> 20 -> 42 -> 18 -> 8 -> 43 -> 12 -> 27 -> 24 -> 34 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 32, 49 | 4 |
| 8 | 8, 9, 10, 19, 41, 45 | 6 |
| 12 | 11, 12, 51 | 3 |
| 18 | 3, 17, 18, 21, 31 | 5 |
| 20 | 16, 20, 23, 29, 30, 50 | 6 |
| 24 | 4, 5, 6, 15, 24, 25, 37, 38, 40, 46, 48 | 11 |
| 27 | 13, 14, 26, 27, 28, 47, 52 | 7 |
| 34 | 34, 35, 36, 39, 44 | 5 |
| 42 | 2, 7, 42 | 3 |
| 43 | 33, 43 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 18 |
| 4 | 24 |
| 5 | 24 |
| 6 | 24 |
| 7 | 42 |
| 8 | 8 |
| 9 | 8 |
| 10 | 8 |
| 11 | 12 |
| 12 | 12 |
| 13 | 27 |
| 14 | 27 |
| 15 | 24 |
| 16 | 20 |
| 17 | 18 |
| 18 | 18 |
| 19 | 8 |
| 20 | 20 |
| 21 | 18 |
| 22 | 1 |
| 23 | 20 |
| 24 | 24 |
| 25 | 24 |
| 26 | 27 |
| 27 | 27 |
| 28 | 27 |
| 29 | 20 |
| 30 | 20 |
| 31 | 18 |
| 32 | 1 |
| 33 | 43 |
| 34 | 34 |
| 35 | 34 |
| 36 | 34 |
| 37 | 24 |
| 38 | 24 |
| 39 | 34 |
| 40 | 24 |
| 41 | 8 |
| 42 | 42 |
| 43 | 43 |
| 44 | 34 |
| 45 | 8 |
| 46 | 24 |
| 47 | 27 |
| 48 | 24 |
| 49 | 1 |
| 50 | 20 |
| 51 | 12 |
| 52 | 27 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.137547 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 12155.572132213485, "best_cost": 9456.93045898402}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
