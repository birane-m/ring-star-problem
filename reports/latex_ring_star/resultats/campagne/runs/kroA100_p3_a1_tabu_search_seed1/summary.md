# Résultat tabu_search - kroA100

- Instance : kroA100
- Nombre de points : 100
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 5481.605
- Coût marche : 69434.778
- Coût total : 74916.383

## Stations choisies

1, 79, 85

## Cycle métro

1 -> 79 -> 85 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 6, 8, 11, 15, 17, 23, 28, 31, 32, 42, 45, 47, 49, 56, 58, 60, 63, 67, 75, 77, 80, 89, 91, 92, 93, 98 | 27 |
| 79 | 4, 10, 16, 18, 19, 21, 22, 24, 26, 36, 38, 53, 59, 65, 66, 70, 72, 74, 79, 84, 88, 90, 94, 97, 99 | 25 |
| 85 | 2, 3, 5, 7, 9, 12, 13, 14, 20, 25, 27, 29, 30, 33, 34, 35, 37, 39, 40, 41, 43, 44, 46, 48, 50, 51, 52, 54, 55, 57, 61, 62, 64, 68, 69, 71, 73, 76, 78, 81, 82, 83, 85, 86, 87, 95, 96, 100 | 48 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 85 |
| 3 | 85 |
| 4 | 79 |
| 5 | 85 |
| 6 | 1 |
| 7 | 85 |
| 8 | 1 |
| 9 | 85 |
| 10 | 79 |
| 11 | 1 |
| 12 | 85 |
| 13 | 85 |
| 14 | 85 |
| 15 | 1 |
| 16 | 79 |
| 17 | 1 |
| 18 | 79 |
| 19 | 79 |
| 20 | 85 |
| 21 | 79 |
| 22 | 79 |
| 23 | 1 |
| 24 | 79 |
| 25 | 85 |
| 26 | 79 |
| 27 | 85 |
| 28 | 1 |
| 29 | 85 |
| 30 | 85 |
| 31 | 1 |
| 32 | 1 |
| 33 | 85 |
| 34 | 85 |
| 35 | 85 |
| 36 | 79 |
| 37 | 85 |
| 38 | 79 |
| 39 | 85 |
| 40 | 85 |
| 41 | 85 |
| 42 | 1 |
| 43 | 85 |
| 44 | 85 |
| 45 | 1 |
| 46 | 85 |
| 47 | 1 |
| 48 | 85 |
| 49 | 1 |
| 50 | 85 |
| 51 | 85 |
| 52 | 85 |
| 53 | 79 |
| 54 | 85 |
| 55 | 85 |
| 56 | 1 |
| 57 | 85 |
| 58 | 1 |
| 59 | 79 |
| 60 | 1 |
| 61 | 85 |
| 62 | 85 |
| 63 | 1 |
| 64 | 85 |
| 65 | 79 |
| 66 | 79 |
| 67 | 1 |
| 68 | 85 |
| 69 | 85 |
| 70 | 79 |
| 71 | 85 |
| 72 | 79 |
| 73 | 85 |
| 74 | 79 |
| 75 | 1 |
| 76 | 85 |
| 77 | 1 |
| 78 | 85 |
| 79 | 79 |
| 80 | 1 |
| 81 | 85 |
| 82 | 85 |
| 83 | 85 |
| 84 | 79 |
| 85 | 85 |
| 86 | 85 |
| 87 | 85 |
| 88 | 79 |
| 89 | 1 |
| 90 | 79 |
| 91 | 1 |
| 92 | 1 |
| 93 | 1 |
| 94 | 79 |
| 95 | 85 |
| 96 | 85 |
| 97 | 79 |
| 98 | 1 |
| 99 | 79 |
| 100 | 85 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.091318 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 77233.40480428514, "best_cost": 74916.38282947111}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
