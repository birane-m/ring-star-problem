# Résultat tabu_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2085.319
- Coût marche : 9744.210
- Coût total : 11829.529

## Stations choisies

1, 5, 19, 20, 28

## Cycle métro

1 -> 20 -> 28 -> 5 -> 19 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 18, 22, 31, 32, 34, 35, 36, 44, 49 | 10 |
| 5 | 4, 5, 6, 15, 24, 25, 33, 37, 38, 39, 40, 43, 46, 48 | 14 |
| 19 | 3, 8, 9, 10, 17, 19, 41, 45 | 8 |
| 20 | 2, 7, 16, 20, 21, 23, 29, 30, 42, 50 | 10 |
| 28 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 20 |
| 3 | 19 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 20 |
| 8 | 19 |
| 9 | 19 |
| 10 | 19 |
| 11 | 28 |
| 12 | 28 |
| 13 | 28 |
| 14 | 28 |
| 15 | 5 |
| 16 | 20 |
| 17 | 19 |
| 18 | 1 |
| 19 | 19 |
| 20 | 20 |
| 21 | 20 |
| 22 | 1 |
| 23 | 20 |
| 24 | 5 |
| 25 | 5 |
| 26 | 28 |
| 27 | 28 |
| 28 | 28 |
| 29 | 20 |
| 30 | 20 |
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
| 41 | 19 |
| 42 | 20 |
| 43 | 5 |
| 44 | 1 |
| 45 | 19 |
| 46 | 5 |
| 47 | 28 |
| 48 | 5 |
| 49 | 1 |
| 50 | 20 |
| 51 | 28 |
| 52 | 28 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.074573 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 14916.735925839565, "best_cost": 11829.528919070392}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
