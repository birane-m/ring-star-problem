# Résultat tabu_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 180.259
- Coût marche : 373.494
- Coût total : 553.754

## Stations choisies

1, 7, 8, 9, 14, 15, 19, 20, 47, 50

## Cycle métro

1 -> 8 -> 7 -> 14 -> 47 -> 19 -> 15 -> 9 -> 50 -> 20 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 11, 22, 27, 32 | 5 |
| 7 | 7, 23, 43 | 3 |
| 8 | 8, 26, 28, 31, 48 | 5 |
| 9 | 5, 9, 10, 30, 38, 39, 49 | 7 |
| 14 | 6, 14, 24, 25 | 4 |
| 15 | 15, 33, 37, 44, 45 | 5 |
| 19 | 13, 19, 40, 41, 42 | 5 |
| 20 | 2, 3, 20, 29, 35, 36 | 6 |
| 47 | 4, 12, 17, 18, 46, 47, 51 | 7 |
| 50 | 16, 21, 34, 50 | 4 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 20 |
| 3 | 20 |
| 4 | 47 |
| 5 | 9 |
| 6 | 14 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 9 |
| 11 | 1 |
| 12 | 47 |
| 13 | 19 |
| 14 | 14 |
| 15 | 15 |
| 16 | 50 |
| 17 | 47 |
| 18 | 47 |
| 19 | 19 |
| 20 | 20 |
| 21 | 50 |
| 22 | 1 |
| 23 | 7 |
| 24 | 14 |
| 25 | 14 |
| 26 | 8 |
| 27 | 1 |
| 28 | 8 |
| 29 | 20 |
| 30 | 9 |
| 31 | 8 |
| 32 | 1 |
| 33 | 15 |
| 34 | 50 |
| 35 | 20 |
| 36 | 20 |
| 37 | 15 |
| 38 | 9 |
| 39 | 9 |
| 40 | 19 |
| 41 | 19 |
| 42 | 19 |
| 43 | 7 |
| 44 | 15 |
| 45 | 15 |
| 46 | 47 |
| 47 | 47 |
| 48 | 8 |
| 49 | 9 |
| 50 | 50 |
| 51 | 47 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.116828 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 630.4676373541728, "best_cost": 553.7535925355432}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
