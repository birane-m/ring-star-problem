# Résultat local_search - rd100

- Instance : rd100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2447.378
- Coût marche : 17482.848
- Coût total : 19930.226

## Stations choisies

1, 4, 5, 50, 84

## Cycle métro

1 -> 4 -> 50 -> 84 -> 5 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 15, 18, 51, 60, 62, 63, 67, 68, 69, 71, 83, 86, 87, 90, 97 | 17 |
| 4 | 3, 4, 9, 12, 13, 14, 20, 21, 26, 32, 33, 47, 49, 74, 75, 78, 82, 85, 99 | 19 |
| 5 | 5, 7, 11, 22, 24, 25, 30, 34, 36, 39, 40, 41, 42, 43, 48, 52, 55, 57, 61, 64, 65, 80, 81, 91, 96, 100 | 26 |
| 50 | 6, 10, 17, 19, 27, 28, 37, 38, 46, 50, 53, 54, 56, 59, 70, 72, 73, 77, 79, 92, 93, 95 | 22 |
| 84 | 2, 16, 23, 29, 31, 35, 44, 45, 58, 66, 76, 84, 88, 89, 94, 98 | 16 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 84 |
| 3 | 4 |
| 4 | 4 |
| 5 | 5 |
| 6 | 50 |
| 7 | 5 |
| 8 | 1 |
| 9 | 4 |
| 10 | 50 |
| 11 | 5 |
| 12 | 4 |
| 13 | 4 |
| 14 | 4 |
| 15 | 1 |
| 16 | 84 |
| 17 | 50 |
| 18 | 1 |
| 19 | 50 |
| 20 | 4 |
| 21 | 4 |
| 22 | 5 |
| 23 | 84 |
| 24 | 5 |
| 25 | 5 |
| 26 | 4 |
| 27 | 50 |
| 28 | 50 |
| 29 | 84 |
| 30 | 5 |
| 31 | 84 |
| 32 | 4 |
| 33 | 4 |
| 34 | 5 |
| 35 | 84 |
| 36 | 5 |
| 37 | 50 |
| 38 | 50 |
| 39 | 5 |
| 40 | 5 |
| 41 | 5 |
| 42 | 5 |
| 43 | 5 |
| 44 | 84 |
| 45 | 84 |
| 46 | 50 |
| 47 | 4 |
| 48 | 5 |
| 49 | 4 |
| 50 | 50 |
| 51 | 1 |
| 52 | 5 |
| 53 | 50 |
| 54 | 50 |
| 55 | 5 |
| 56 | 50 |
| 57 | 5 |
| 58 | 84 |
| 59 | 50 |
| 60 | 1 |
| 61 | 5 |
| 62 | 1 |
| 63 | 1 |
| 64 | 5 |
| 65 | 5 |
| 66 | 84 |
| 67 | 1 |
| 68 | 1 |
| 69 | 1 |
| 70 | 50 |
| 71 | 1 |
| 72 | 50 |
| 73 | 50 |
| 74 | 4 |
| 75 | 4 |
| 76 | 84 |
| 77 | 50 |
| 78 | 4 |
| 79 | 50 |
| 80 | 5 |
| 81 | 5 |
| 82 | 4 |
| 83 | 1 |
| 84 | 84 |
| 85 | 4 |
| 86 | 1 |
| 87 | 1 |
| 88 | 84 |
| 89 | 84 |
| 90 | 1 |
| 91 | 5 |
| 92 | 50 |
| 93 | 50 |
| 94 | 84 |
| 95 | 50 |
| 96 | 5 |
| 97 | 1 |
| 98 | 84 |
| 99 | 4 |
| 100 | 5 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.010244 s
- Graine : 0
- Détails : {"accepted_moves": 5, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 21243.250629357928, "best_cost": 19930.226125698176}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
