# Résultat tabu_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 177.847
- Coût marche : 364.708
- Coût total : 542.555

## Stations choisies

1, 3, 8, 14, 15, 16, 19, 23, 47, 49

## Cycle métro

1 -> 3 -> 16 -> 49 -> 15 -> 19 -> 47 -> 14 -> 23 -> 8 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 27, 32 | 4 |
| 3 | 3, 20, 28, 35, 36 | 5 |
| 8 | 8, 26, 31, 48 | 4 |
| 14 | 6, 14, 25 | 3 |
| 15 | 15, 33, 37, 44, 45 | 5 |
| 16 | 2, 11, 16, 21, 29, 34, 50 | 7 |
| 19 | 13, 19, 40, 41, 42 | 5 |
| 23 | 7, 23, 24, 43 | 4 |
| 47 | 4, 12, 17, 18, 46, 47, 51 | 7 |
| 49 | 5, 9, 10, 30, 38, 39, 49 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 3 |
| 4 | 47 |
| 5 | 49 |
| 6 | 14 |
| 7 | 23 |
| 8 | 8 |
| 9 | 49 |
| 10 | 49 |
| 11 | 16 |
| 12 | 47 |
| 13 | 19 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |
| 17 | 47 |
| 18 | 47 |
| 19 | 19 |
| 20 | 3 |
| 21 | 16 |
| 22 | 1 |
| 23 | 23 |
| 24 | 23 |
| 25 | 14 |
| 26 | 8 |
| 27 | 1 |
| 28 | 3 |
| 29 | 16 |
| 30 | 49 |
| 31 | 8 |
| 32 | 1 |
| 33 | 15 |
| 34 | 16 |
| 35 | 3 |
| 36 | 3 |
| 37 | 15 |
| 38 | 49 |
| 39 | 49 |
| 40 | 19 |
| 41 | 19 |
| 42 | 19 |
| 43 | 23 |
| 44 | 15 |
| 45 | 15 |
| 46 | 47 |
| 47 | 47 |
| 48 | 8 |
| 49 | 49 |
| 50 | 16 |
| 51 | 47 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.123691 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 630.4676373541728, "best_cost": 542.5551826981241}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
