# Résultat tabu_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 81.809
- Coût marche : 745.757
- Coût total : 827.566

## Stations choisies

1, 9, 17

## Cycle métro

1 -> 9 -> 17 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 6, 7, 8, 11, 20, 22, 23, 24, 26, 27, 28, 31, 32, 35, 36, 43, 46, 48, 51 | 22 |
| 9 | 5, 9, 10, 16, 21, 29, 30, 34, 38, 39, 49, 50 | 12 |
| 17 | 4, 12, 13, 14, 15, 17, 18, 19, 25, 33, 37, 40, 41, 42, 44, 45, 47 | 17 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 17 |
| 5 | 9 |
| 6 | 1 |
| 7 | 1 |
| 8 | 1 |
| 9 | 9 |
| 10 | 9 |
| 11 | 1 |
| 12 | 17 |
| 13 | 17 |
| 14 | 17 |
| 15 | 17 |
| 16 | 9 |
| 17 | 17 |
| 18 | 17 |
| 19 | 17 |
| 20 | 1 |
| 21 | 9 |
| 22 | 1 |
| 23 | 1 |
| 24 | 1 |
| 25 | 17 |
| 26 | 1 |
| 27 | 1 |
| 28 | 1 |
| 29 | 9 |
| 30 | 9 |
| 31 | 1 |
| 32 | 1 |
| 33 | 17 |
| 34 | 9 |
| 35 | 1 |
| 36 | 1 |
| 37 | 17 |
| 38 | 9 |
| 39 | 9 |
| 40 | 17 |
| 41 | 17 |
| 42 | 17 |
| 43 | 1 |
| 44 | 17 |
| 45 | 17 |
| 46 | 1 |
| 47 | 17 |
| 48 | 1 |
| 49 | 9 |
| 50 | 9 |
| 51 | 1 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.049210 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 859.9917166154031, "best_cost": 827.5664027627151}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
