# Résultat tabu_search - kroA100

- Instance : kroA100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 7311.263
- Coût marche : 51131.153
- Coût total : 58442.416

## Stations choisies

1, 20, 73, 78, 79

## Cycle métro

1 -> 79 -> 20 -> 78 -> 73 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 6, 8, 11, 15, 17, 28, 31, 32, 42, 45, 47, 49, 56, 58, 63, 67, 75, 80, 89, 91, 92, 93, 98 | 24 |
| 20 | 7, 9, 12, 20, 23, 27, 34, 35, 43, 46, 51, 55, 57, 60, 62, 77, 83, 86, 87 | 19 |
| 73 | 2, 25, 40, 44, 50, 54, 61, 64, 68, 69, 73, 81, 82, 85 | 14 |
| 78 | 3, 5, 13, 14, 29, 30, 33, 37, 39, 41, 48, 52, 71, 76, 78, 95, 96, 100 | 18 |
| 79 | 4, 10, 16, 18, 19, 21, 22, 24, 26, 36, 38, 53, 59, 65, 66, 70, 72, 74, 79, 84, 88, 90, 94, 97, 99 | 25 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 73 |
| 3 | 78 |
| 4 | 79 |
| 5 | 78 |
| 6 | 1 |
| 7 | 20 |
| 8 | 1 |
| 9 | 20 |
| 10 | 79 |
| 11 | 1 |
| 12 | 20 |
| 13 | 78 |
| 14 | 78 |
| 15 | 1 |
| 16 | 79 |
| 17 | 1 |
| 18 | 79 |
| 19 | 79 |
| 20 | 20 |
| 21 | 79 |
| 22 | 79 |
| 23 | 20 |
| 24 | 79 |
| 25 | 73 |
| 26 | 79 |
| 27 | 20 |
| 28 | 1 |
| 29 | 78 |
| 30 | 78 |
| 31 | 1 |
| 32 | 1 |
| 33 | 78 |
| 34 | 20 |
| 35 | 20 |
| 36 | 79 |
| 37 | 78 |
| 38 | 79 |
| 39 | 78 |
| 40 | 73 |
| 41 | 78 |
| 42 | 1 |
| 43 | 20 |
| 44 | 73 |
| 45 | 1 |
| 46 | 20 |
| 47 | 1 |
| 48 | 78 |
| 49 | 1 |
| 50 | 73 |
| 51 | 20 |
| 52 | 78 |
| 53 | 79 |
| 54 | 73 |
| 55 | 20 |
| 56 | 1 |
| 57 | 20 |
| 58 | 1 |
| 59 | 79 |
| 60 | 20 |
| 61 | 73 |
| 62 | 20 |
| 63 | 1 |
| 64 | 73 |
| 65 | 79 |
| 66 | 79 |
| 67 | 1 |
| 68 | 73 |
| 69 | 73 |
| 70 | 79 |
| 71 | 78 |
| 72 | 79 |
| 73 | 73 |
| 74 | 79 |
| 75 | 1 |
| 76 | 78 |
| 77 | 20 |
| 78 | 78 |
| 79 | 79 |
| 80 | 1 |
| 81 | 73 |
| 82 | 73 |
| 83 | 20 |
| 84 | 79 |
| 85 | 73 |
| 86 | 20 |
| 87 | 20 |
| 88 | 79 |
| 89 | 1 |
| 90 | 79 |
| 91 | 1 |
| 92 | 1 |
| 93 | 1 |
| 94 | 79 |
| 95 | 78 |
| 96 | 78 |
| 97 | 79 |
| 98 | 1 |
| 99 | 79 |
| 100 | 78 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.119624 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 68427.56868588035, "best_cost": 58442.416343534256}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
