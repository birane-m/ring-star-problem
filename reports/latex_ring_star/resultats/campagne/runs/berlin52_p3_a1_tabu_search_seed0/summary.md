# Résultat tabu_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 1673.863
- Coût marche : 12410.045
- Coût total : 14083.908

## Stations choisies

1, 5, 27

## Cycle métro

1 -> 5 -> 27 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 7, 8, 16, 17, 18, 19, 20, 21, 22, 23, 29, 30, 31, 32, 34, 35, 36, 41, 42, 44, 45, 49, 50 | 26 |
| 5 | 4, 5, 6, 9, 10, 15, 24, 25, 33, 37, 38, 39, 40, 43, 46, 48 | 16 |
| 27 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 1 |
| 8 | 1 |
| 9 | 5 |
| 10 | 5 |
| 11 | 27 |
| 12 | 27 |
| 13 | 27 |
| 14 | 27 |
| 15 | 5 |
| 16 | 1 |
| 17 | 1 |
| 18 | 1 |
| 19 | 1 |
| 20 | 1 |
| 21 | 1 |
| 22 | 1 |
| 23 | 1 |
| 24 | 5 |
| 25 | 5 |
| 26 | 27 |
| 27 | 27 |
| 28 | 27 |
| 29 | 1 |
| 30 | 1 |
| 31 | 1 |
| 32 | 1 |
| 33 | 5 |
| 34 | 1 |
| 35 | 1 |
| 36 | 1 |
| 37 | 5 |
| 38 | 5 |
| 39 | 5 |
| 40 | 5 |
| 41 | 1 |
| 42 | 1 |
| 43 | 5 |
| 44 | 1 |
| 45 | 1 |
| 46 | 5 |
| 47 | 27 |
| 48 | 5 |
| 49 | 1 |
| 50 | 1 |
| 51 | 27 |
| 52 | 27 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.051480 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 16352.31950652313, "best_cost": 14083.90825964823}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
