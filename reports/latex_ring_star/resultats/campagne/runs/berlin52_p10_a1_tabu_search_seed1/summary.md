# Résultat tabu_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 3445.381
- Coût marche : 6191.838
- Coût total : 9637.219

## Stations choisies

1, 3, 5, 12, 23, 27, 34, 41, 42, 43

## Cycle métro

1 -> 23 -> 42 -> 3 -> 41 -> 43 -> 12 -> 27 -> 5 -> 34 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 31, 32, 49 | 5 |
| 3 | 3, 17, 18 | 3 |
| 5 | 4, 5, 6, 15, 24, 25, 38, 40, 48 | 9 |
| 12 | 11, 12, 51 | 3 |
| 23 | 20, 21, 23, 29, 30, 50 | 6 |
| 27 | 13, 14, 26, 27, 28, 47, 52 | 7 |
| 34 | 16, 34, 35, 36, 37, 39, 44, 46 | 8 |
| 41 | 8, 9, 10, 19, 41, 45 | 6 |
| 42 | 2, 7, 42 | 3 |
| 43 | 33, 43 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 3 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 42 |
| 8 | 41 |
| 9 | 41 |
| 10 | 41 |
| 11 | 12 |
| 12 | 12 |
| 13 | 27 |
| 14 | 27 |
| 15 | 5 |
| 16 | 34 |
| 17 | 3 |
| 18 | 3 |
| 19 | 41 |
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
| 33 | 43 |
| 34 | 34 |
| 35 | 34 |
| 36 | 34 |
| 37 | 34 |
| 38 | 5 |
| 39 | 34 |
| 40 | 5 |
| 41 | 41 |
| 42 | 42 |
| 43 | 43 |
| 44 | 34 |
| 45 | 41 |
| 46 | 34 |
| 47 | 27 |
| 48 | 5 |
| 49 | 1 |
| 50 | 23 |
| 51 | 12 |
| 52 | 27 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.134605 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 12155.572132213485, "best_cost": 9637.219443200936}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
