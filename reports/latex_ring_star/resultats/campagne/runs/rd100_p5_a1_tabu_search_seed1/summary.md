# Résultat tabu_search - rd100

- Instance : rd100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2413.194
- Coût marche : 17104.683
- Coût total : 19517.876

## Stations choisies

1, 4, 16, 34, 46

## Cycle métro

1 -> 4 -> 46 -> 16 -> 34 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 15, 18, 51, 60, 62, 63, 65, 67, 68, 69, 71, 83, 86, 87, 90, 91, 97 | 19 |
| 4 | 3, 4, 9, 12, 13, 14, 20, 21, 26, 32, 33, 49, 64, 74, 75, 78, 82, 85 | 18 |
| 16 | 2, 16, 23, 29, 31, 35, 36, 44, 45, 47, 52, 53, 57, 58, 66, 76, 84, 88, 89, 94, 98, 99, 100 | 23 |
| 34 | 5, 7, 11, 22, 24, 25, 30, 34, 39, 40, 41, 42, 43, 48, 55, 61, 80, 81, 96 | 19 |
| 46 | 6, 10, 17, 19, 27, 28, 37, 38, 46, 50, 54, 56, 59, 70, 72, 73, 77, 79, 92, 93, 95 | 21 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 4 |
| 4 | 4 |
| 5 | 34 |
| 6 | 46 |
| 7 | 34 |
| 8 | 1 |
| 9 | 4 |
| 10 | 46 |
| 11 | 34 |
| 12 | 4 |
| 13 | 4 |
| 14 | 4 |
| 15 | 1 |
| 16 | 16 |
| 17 | 46 |
| 18 | 1 |
| 19 | 46 |
| 20 | 4 |
| 21 | 4 |
| 22 | 34 |
| 23 | 16 |
| 24 | 34 |
| 25 | 34 |
| 26 | 4 |
| 27 | 46 |
| 28 | 46 |
| 29 | 16 |
| 30 | 34 |
| 31 | 16 |
| 32 | 4 |
| 33 | 4 |
| 34 | 34 |
| 35 | 16 |
| 36 | 16 |
| 37 | 46 |
| 38 | 46 |
| 39 | 34 |
| 40 | 34 |
| 41 | 34 |
| 42 | 34 |
| 43 | 34 |
| 44 | 16 |
| 45 | 16 |
| 46 | 46 |
| 47 | 16 |
| 48 | 34 |
| 49 | 4 |
| 50 | 46 |
| 51 | 1 |
| 52 | 16 |
| 53 | 16 |
| 54 | 46 |
| 55 | 34 |
| 56 | 46 |
| 57 | 16 |
| 58 | 16 |
| 59 | 46 |
| 60 | 1 |
| 61 | 34 |
| 62 | 1 |
| 63 | 1 |
| 64 | 4 |
| 65 | 1 |
| 66 | 16 |
| 67 | 1 |
| 68 | 1 |
| 69 | 1 |
| 70 | 46 |
| 71 | 1 |
| 72 | 46 |
| 73 | 46 |
| 74 | 4 |
| 75 | 4 |
| 76 | 16 |
| 77 | 46 |
| 78 | 4 |
| 79 | 46 |
| 80 | 34 |
| 81 | 34 |
| 82 | 4 |
| 83 | 1 |
| 84 | 16 |
| 85 | 4 |
| 86 | 1 |
| 87 | 1 |
| 88 | 16 |
| 89 | 16 |
| 90 | 1 |
| 91 | 1 |
| 92 | 46 |
| 93 | 46 |
| 94 | 16 |
| 95 | 46 |
| 96 | 34 |
| 97 | 1 |
| 98 | 16 |
| 99 | 16 |
| 100 | 16 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.121184 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 21243.250629357928, "best_cost": 19517.876243680956}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
