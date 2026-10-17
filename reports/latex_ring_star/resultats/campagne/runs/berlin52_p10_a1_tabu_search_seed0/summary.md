# Résultat tabu_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 3487.088
- Coût marche : 6201.619
- Coût total : 9688.708

## Stations choisies

1, 8, 12, 18, 20, 21, 24, 27, 35, 42

## Cycle métro

1 -> 8 -> 18 -> 21 -> 42 -> 20 -> 27 -> 12 -> 24 -> 35 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 32, 49 | 4 |
| 8 | 8, 9, 10, 19, 41, 45 | 6 |
| 12 | 11, 12, 33, 51 | 4 |
| 18 | 3, 18, 31 | 3 |
| 20 | 16, 20, 23, 29, 30, 50 | 6 |
| 21 | 17, 21 | 2 |
| 24 | 4, 5, 6, 15, 24, 25, 37, 38, 40, 43, 46, 48 | 12 |
| 27 | 13, 14, 26, 27, 28, 47, 52 | 7 |
| 35 | 34, 35, 36, 39, 44 | 5 |
| 42 | 2, 7, 42 | 3 |

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
| 17 | 21 |
| 18 | 18 |
| 19 | 8 |
| 20 | 20 |
| 21 | 21 |
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
| 33 | 12 |
| 34 | 35 |
| 35 | 35 |
| 36 | 35 |
| 37 | 24 |
| 38 | 24 |
| 39 | 35 |
| 40 | 24 |
| 41 | 8 |
| 42 | 42 |
| 43 | 24 |
| 44 | 35 |
| 45 | 8 |
| 46 | 24 |
| 47 | 27 |
| 48 | 24 |
| 49 | 1 |
| 50 | 20 |
| 51 | 12 |
| 52 | 27 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.135340 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 12155.572132213485, "best_cost": 9688.707649021764}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
