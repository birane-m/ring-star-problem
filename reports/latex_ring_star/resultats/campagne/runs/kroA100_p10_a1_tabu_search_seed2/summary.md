# Résultat tabu_search - kroA100

- Instance : kroA100
- Nombre de points : 100
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 9759.386
- Coût marche : 31460.747
- Coût total : 41220.133

## Stations choisies

1, 3, 9, 13, 16, 21, 23, 56, 73, 78

## Cycle métro

1 -> 56 -> 16 -> 21 -> 23 -> 9 -> 3 -> 78 -> 13 -> 73 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 6, 28, 47, 49, 58, 63, 67, 92, 93 | 10 |
| 3 | 3, 14, 29, 41, 43, 46, 71, 100 | 8 |
| 9 | 7, 9, 12, 20, 27, 34, 35, 51, 55, 57, 61, 83, 86, 87 | 14 |
| 13 | 13, 33, 76, 82, 95 | 5 |
| 16 | 16, 18, 19, 22, 24, 53, 66, 70, 79, 88, 90, 94 | 12 |
| 21 | 10, 11, 15, 17, 21, 36, 38, 59, 72, 74, 84, 99 | 12 |
| 23 | 23, 32, 45, 60, 62, 77, 91, 98 | 8 |
| 56 | 4, 8, 26, 31, 42, 56, 65, 75, 80, 89, 97 | 11 |
| 73 | 2, 25, 40, 44, 50, 54, 64, 68, 69, 73, 81, 85 | 12 |
| 78 | 5, 30, 37, 39, 48, 52, 78, 96 | 8 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 73 |
| 3 | 3 |
| 4 | 56 |
| 5 | 78 |
| 6 | 1 |
| 7 | 9 |
| 8 | 56 |
| 9 | 9 |
| 10 | 21 |
| 11 | 21 |
| 12 | 9 |
| 13 | 13 |
| 14 | 3 |
| 15 | 21 |
| 16 | 16 |
| 17 | 21 |
| 18 | 16 |
| 19 | 16 |
| 20 | 9 |
| 21 | 21 |
| 22 | 16 |
| 23 | 23 |
| 24 | 16 |
| 25 | 73 |
| 26 | 56 |
| 27 | 9 |
| 28 | 1 |
| 29 | 3 |
| 30 | 78 |
| 31 | 56 |
| 32 | 23 |
| 33 | 13 |
| 34 | 9 |
| 35 | 9 |
| 36 | 21 |
| 37 | 78 |
| 38 | 21 |
| 39 | 78 |
| 40 | 73 |
| 41 | 3 |
| 42 | 56 |
| 43 | 3 |
| 44 | 73 |
| 45 | 23 |
| 46 | 3 |
| 47 | 1 |
| 48 | 78 |
| 49 | 1 |
| 50 | 73 |
| 51 | 9 |
| 52 | 78 |
| 53 | 16 |
| 54 | 73 |
| 55 | 9 |
| 56 | 56 |
| 57 | 9 |
| 58 | 1 |
| 59 | 21 |
| 60 | 23 |
| 61 | 9 |
| 62 | 23 |
| 63 | 1 |
| 64 | 73 |
| 65 | 56 |
| 66 | 16 |
| 67 | 1 |
| 68 | 73 |
| 69 | 73 |
| 70 | 16 |
| 71 | 3 |
| 72 | 21 |
| 73 | 73 |
| 74 | 21 |
| 75 | 56 |
| 76 | 13 |
| 77 | 23 |
| 78 | 78 |
| 79 | 16 |
| 80 | 56 |
| 81 | 73 |
| 82 | 13 |
| 83 | 9 |
| 84 | 21 |
| 85 | 73 |
| 86 | 9 |
| 87 | 9 |
| 88 | 16 |
| 89 | 56 |
| 90 | 16 |
| 91 | 23 |
| 92 | 1 |
| 93 | 1 |
| 94 | 16 |
| 95 | 13 |
| 96 | 78 |
| 97 | 56 |
| 98 | 23 |
| 99 | 21 |
| 100 | 3 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.192843 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 46042.25194591482, "best_cost": 41220.13346620655}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
