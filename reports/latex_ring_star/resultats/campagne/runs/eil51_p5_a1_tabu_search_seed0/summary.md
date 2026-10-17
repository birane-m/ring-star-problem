# Résultat tabu_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 114.803
- Coût marche : 580.352
- Coût total : 695.155

## Stations choisies

1, 6, 9, 17, 20

## Cycle métro

1 -> 6 -> 17 -> 9 -> 20 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 11, 22, 26, 27, 28, 31, 32 | 9 |
| 6 | 6, 7, 14, 23, 24, 25, 43, 46, 48, 51 | 10 |
| 9 | 5, 9, 10, 16, 21, 30, 34, 38, 39, 49, 50 | 11 |
| 17 | 4, 12, 13, 15, 17, 18, 19, 33, 37, 40, 41, 42, 44, 45, 47 | 15 |
| 20 | 2, 3, 20, 29, 35, 36 | 6 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 20 |
| 3 | 20 |
| 4 | 17 |
| 5 | 9 |
| 6 | 6 |
| 7 | 6 |
| 8 | 1 |
| 9 | 9 |
| 10 | 9 |
| 11 | 1 |
| 12 | 17 |
| 13 | 17 |
| 14 | 6 |
| 15 | 17 |
| 16 | 9 |
| 17 | 17 |
| 18 | 17 |
| 19 | 17 |
| 20 | 20 |
| 21 | 9 |
| 22 | 1 |
| 23 | 6 |
| 24 | 6 |
| 25 | 6 |
| 26 | 1 |
| 27 | 1 |
| 28 | 1 |
| 29 | 20 |
| 30 | 9 |
| 31 | 1 |
| 32 | 1 |
| 33 | 17 |
| 34 | 9 |
| 35 | 20 |
| 36 | 20 |
| 37 | 17 |
| 38 | 9 |
| 39 | 9 |
| 40 | 17 |
| 41 | 17 |
| 42 | 17 |
| 43 | 6 |
| 44 | 17 |
| 45 | 17 |
| 46 | 6 |
| 47 | 17 |
| 48 | 6 |
| 49 | 9 |
| 50 | 9 |
| 51 | 6 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.064716 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 735.0003807891881, "best_cost": 695.1548629222576}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
