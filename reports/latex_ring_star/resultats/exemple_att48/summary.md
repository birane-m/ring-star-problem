# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 16477.526
- Coût marche : 26266.228
- Coût total : 42743.754

## Stations choisies

1, 5, 10, 13, 18, 22, 30, 32, 33, 34

## Cycle métro

1 -> 22 -> 34 -> 5 -> 10 -> 32 -> 13 -> 33 -> 30 -> 18 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 9, 38, 40 | 5 |
| 5 | 2, 5, 29, 48 | 4 |
| 10 | 4, 10, 24, 26, 35, 42, 45 | 7 |
| 13 | 11, 13, 14, 21, 23, 25, 47 | 7 |
| 18 | 7, 18, 28, 31, 36, 44 | 6 |
| 22 | 3, 16, 22 | 3 |
| 30 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 32 | 32, 39 | 2 |
| 33 | 12, 15, 20, 33, 46 | 5 |
| 34 | 34, 41 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 5 |
| 3 | 22 |
| 4 | 10 |
| 5 | 5 |
| 6 | 30 |
| 7 | 18 |
| 8 | 1 |
| 9 | 1 |
| 10 | 10 |
| 11 | 13 |
| 12 | 33 |
| 13 | 13 |
| 14 | 13 |
| 15 | 33 |
| 16 | 22 |
| 17 | 30 |
| 18 | 18 |
| 19 | 30 |
| 20 | 33 |
| 21 | 13 |
| 22 | 22 |
| 23 | 13 |
| 24 | 10 |
| 25 | 13 |
| 26 | 10 |
| 27 | 30 |
| 28 | 18 |
| 29 | 5 |
| 30 | 30 |
| 31 | 18 |
| 32 | 32 |
| 33 | 33 |
| 34 | 34 |
| 35 | 10 |
| 36 | 18 |
| 37 | 30 |
| 38 | 1 |
| 39 | 32 |
| 40 | 1 |
| 41 | 34 |
| 42 | 10 |
| 43 | 30 |
| 44 | 18 |
| 45 | 10 |
| 46 | 33 |
| 47 | 13 |
| 48 | 5 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.122427 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 48833.89333184296, "best_cost": 42743.75402418659}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
