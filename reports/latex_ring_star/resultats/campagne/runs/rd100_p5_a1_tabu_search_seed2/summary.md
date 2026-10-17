# Résultat tabu_search - rd100

- Instance : rd100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2394.093
- Coût marche : 17107.271
- Coût total : 19501.364

## Stations choisies

1, 16, 34, 56, 82

## Cycle métro

1 -> 82 -> 56 -> 16 -> 34 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 15, 18, 51, 60, 62, 65, 68, 69, 71, 83, 90, 91 | 14 |
| 16 | 2, 16, 23, 29, 31, 35, 36, 44, 45, 47, 52, 53, 57, 58, 66, 76, 84, 88, 89, 94, 98, 99, 100 | 23 |
| 34 | 5, 7, 11, 22, 24, 25, 30, 34, 39, 40, 41, 42, 43, 48, 55, 61, 80, 81, 96 | 19 |
| 56 | 6, 10, 17, 19, 27, 28, 33, 37, 38, 46, 50, 54, 56, 59, 70, 72, 73, 77, 79, 92, 93, 95 | 22 |
| 82 | 3, 4, 9, 12, 13, 14, 20, 21, 26, 32, 49, 63, 64, 67, 74, 75, 78, 82, 85, 86, 87, 97 | 22 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 82 |
| 4 | 82 |
| 5 | 34 |
| 6 | 56 |
| 7 | 34 |
| 8 | 1 |
| 9 | 82 |
| 10 | 56 |
| 11 | 34 |
| 12 | 82 |
| 13 | 82 |
| 14 | 82 |
| 15 | 1 |
| 16 | 16 |
| 17 | 56 |
| 18 | 1 |
| 19 | 56 |
| 20 | 82 |
| 21 | 82 |
| 22 | 34 |
| 23 | 16 |
| 24 | 34 |
| 25 | 34 |
| 26 | 82 |
| 27 | 56 |
| 28 | 56 |
| 29 | 16 |
| 30 | 34 |
| 31 | 16 |
| 32 | 82 |
| 33 | 56 |
| 34 | 34 |
| 35 | 16 |
| 36 | 16 |
| 37 | 56 |
| 38 | 56 |
| 39 | 34 |
| 40 | 34 |
| 41 | 34 |
| 42 | 34 |
| 43 | 34 |
| 44 | 16 |
| 45 | 16 |
| 46 | 56 |
| 47 | 16 |
| 48 | 34 |
| 49 | 82 |
| 50 | 56 |
| 51 | 1 |
| 52 | 16 |
| 53 | 16 |
| 54 | 56 |
| 55 | 34 |
| 56 | 56 |
| 57 | 16 |
| 58 | 16 |
| 59 | 56 |
| 60 | 1 |
| 61 | 34 |
| 62 | 1 |
| 63 | 82 |
| 64 | 82 |
| 65 | 1 |
| 66 | 16 |
| 67 | 82 |
| 68 | 1 |
| 69 | 1 |
| 70 | 56 |
| 71 | 1 |
| 72 | 56 |
| 73 | 56 |
| 74 | 82 |
| 75 | 82 |
| 76 | 16 |
| 77 | 56 |
| 78 | 82 |
| 79 | 56 |
| 80 | 34 |
| 81 | 34 |
| 82 | 82 |
| 83 | 1 |
| 84 | 16 |
| 85 | 82 |
| 86 | 82 |
| 87 | 82 |
| 88 | 16 |
| 89 | 16 |
| 90 | 1 |
| 91 | 1 |
| 92 | 56 |
| 93 | 56 |
| 94 | 16 |
| 95 | 56 |
| 96 | 34 |
| 97 | 82 |
| 98 | 16 |
| 99 | 16 |
| 100 | 16 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.120191 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 21243.250629357928, "best_cost": 19501.363506517166}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
