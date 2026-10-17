# Résultat tabu_search - rd100

- Instance : rd100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2414.961
- Coût marche : 17190.245
- Coût total : 19605.207

## Stations choisies

1, 16, 32, 41, 56

## Cycle métro

1 -> 32 -> 56 -> 16 -> 41 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 15, 18, 51, 60, 62, 63, 64, 67, 68, 69, 71, 83, 86, 87, 90, 91, 97 | 19 |
| 16 | 2, 16, 23, 29, 31, 35, 36, 44, 45, 47, 52, 53, 57, 58, 66, 76, 84, 88, 89, 94, 98, 99, 100 | 23 |
| 32 | 3, 4, 9, 12, 13, 14, 20, 21, 26, 32, 33, 49, 74, 75, 78, 82, 85 | 17 |
| 41 | 5, 7, 11, 22, 24, 25, 30, 34, 39, 40, 41, 42, 43, 48, 55, 61, 65, 80, 81, 96 | 20 |
| 56 | 6, 10, 17, 19, 27, 28, 37, 38, 46, 50, 54, 56, 59, 70, 72, 73, 77, 79, 92, 93, 95 | 21 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 32 |
| 4 | 32 |
| 5 | 41 |
| 6 | 56 |
| 7 | 41 |
| 8 | 1 |
| 9 | 32 |
| 10 | 56 |
| 11 | 41 |
| 12 | 32 |
| 13 | 32 |
| 14 | 32 |
| 15 | 1 |
| 16 | 16 |
| 17 | 56 |
| 18 | 1 |
| 19 | 56 |
| 20 | 32 |
| 21 | 32 |
| 22 | 41 |
| 23 | 16 |
| 24 | 41 |
| 25 | 41 |
| 26 | 32 |
| 27 | 56 |
| 28 | 56 |
| 29 | 16 |
| 30 | 41 |
| 31 | 16 |
| 32 | 32 |
| 33 | 32 |
| 34 | 41 |
| 35 | 16 |
| 36 | 16 |
| 37 | 56 |
| 38 | 56 |
| 39 | 41 |
| 40 | 41 |
| 41 | 41 |
| 42 | 41 |
| 43 | 41 |
| 44 | 16 |
| 45 | 16 |
| 46 | 56 |
| 47 | 16 |
| 48 | 41 |
| 49 | 32 |
| 50 | 56 |
| 51 | 1 |
| 52 | 16 |
| 53 | 16 |
| 54 | 56 |
| 55 | 41 |
| 56 | 56 |
| 57 | 16 |
| 58 | 16 |
| 59 | 56 |
| 60 | 1 |
| 61 | 41 |
| 62 | 1 |
| 63 | 1 |
| 64 | 1 |
| 65 | 41 |
| 66 | 16 |
| 67 | 1 |
| 68 | 1 |
| 69 | 1 |
| 70 | 56 |
| 71 | 1 |
| 72 | 56 |
| 73 | 56 |
| 74 | 32 |
| 75 | 32 |
| 76 | 16 |
| 77 | 56 |
| 78 | 32 |
| 79 | 56 |
| 80 | 41 |
| 81 | 41 |
| 82 | 32 |
| 83 | 1 |
| 84 | 16 |
| 85 | 32 |
| 86 | 1 |
| 87 | 1 |
| 88 | 16 |
| 89 | 16 |
| 90 | 1 |
| 91 | 1 |
| 92 | 56 |
| 93 | 56 |
| 94 | 16 |
| 95 | 56 |
| 96 | 41 |
| 97 | 1 |
| 98 | 16 |
| 99 | 16 |
| 100 | 16 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.121420 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 21243.250629357928, "best_cost": 19605.206502161975}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
