# Résultat tabu_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2317.033
- Coût marche : 9506.299
- Coût total : 11823.332

## Stations choisies

1, 5, 19, 23, 27

## Cycle métro

1 -> 23 -> 27 -> 5 -> 19 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 18, 22, 31, 32, 34, 35, 36, 44, 49 | 10 |
| 5 | 4, 5, 6, 15, 24, 25, 33, 37, 38, 39, 40, 43, 46, 48 | 14 |
| 19 | 3, 8, 9, 10, 19, 41, 45 | 7 |
| 23 | 2, 7, 16, 17, 20, 21, 23, 29, 30, 42, 50 | 11 |
| 27 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 23 |
| 3 | 19 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 23 |
| 8 | 19 |
| 9 | 19 |
| 10 | 19 |
| 11 | 27 |
| 12 | 27 |
| 13 | 27 |
| 14 | 27 |
| 15 | 5 |
| 16 | 23 |
| 17 | 23 |
| 18 | 1 |
| 19 | 19 |
| 20 | 23 |
| 21 | 23 |
| 22 | 1 |
| 23 | 23 |
| 24 | 5 |
| 25 | 5 |
| 26 | 27 |
| 27 | 27 |
| 28 | 27 |
| 29 | 23 |
| 30 | 23 |
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
| 42 | 23 |
| 43 | 5 |
| 44 | 1 |
| 45 | 19 |
| 46 | 5 |
| 47 | 27 |
| 48 | 5 |
| 49 | 1 |
| 50 | 23 |
| 51 | 27 |
| 52 | 27 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.073291 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 14916.735925839565, "best_cost": 11823.332382007175}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
