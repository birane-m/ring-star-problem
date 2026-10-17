# Résultat tabu_search - rd100

- Instance : rd100
- Nombre de points : 100
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 1919.074
- Coût marche : 24464.167
- Coût total : 26383.241

## Stations choisies

1, 6, 34

## Cycle métro

1 -> 6 -> 34 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 12, 13, 14, 15, 18, 21, 49, 51, 60, 62, 63, 65, 67, 68, 69, 71, 75, 82, 83, 85, 86, 87, 90, 91, 97 | 27 |
| 6 | 2, 3, 4, 6, 9, 10, 16, 17, 19, 20, 23, 26, 27, 28, 31, 32, 33, 36, 37, 38, 45, 46, 47, 50, 53, 54, 56, 57, 58, 59, 64, 66, 70, 72, 73, 74, 76, 77, 78, 79, 84, 88, 89, 92, 93, 94, 95, 98, 99 | 49 |
| 34 | 5, 7, 11, 22, 24, 25, 29, 30, 34, 35, 39, 40, 41, 42, 43, 44, 48, 52, 55, 61, 80, 81, 96, 100 | 24 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 6 |
| 3 | 6 |
| 4 | 6 |
| 5 | 34 |
| 6 | 6 |
| 7 | 34 |
| 8 | 1 |
| 9 | 6 |
| 10 | 6 |
| 11 | 34 |
| 12 | 1 |
| 13 | 1 |
| 14 | 1 |
| 15 | 1 |
| 16 | 6 |
| 17 | 6 |
| 18 | 1 |
| 19 | 6 |
| 20 | 6 |
| 21 | 1 |
| 22 | 34 |
| 23 | 6 |
| 24 | 34 |
| 25 | 34 |
| 26 | 6 |
| 27 | 6 |
| 28 | 6 |
| 29 | 34 |
| 30 | 34 |
| 31 | 6 |
| 32 | 6 |
| 33 | 6 |
| 34 | 34 |
| 35 | 34 |
| 36 | 6 |
| 37 | 6 |
| 38 | 6 |
| 39 | 34 |
| 40 | 34 |
| 41 | 34 |
| 42 | 34 |
| 43 | 34 |
| 44 | 34 |
| 45 | 6 |
| 46 | 6 |
| 47 | 6 |
| 48 | 34 |
| 49 | 1 |
| 50 | 6 |
| 51 | 1 |
| 52 | 34 |
| 53 | 6 |
| 54 | 6 |
| 55 | 34 |
| 56 | 6 |
| 57 | 6 |
| 58 | 6 |
| 59 | 6 |
| 60 | 1 |
| 61 | 34 |
| 62 | 1 |
| 63 | 1 |
| 64 | 6 |
| 65 | 1 |
| 66 | 6 |
| 67 | 1 |
| 68 | 1 |
| 69 | 1 |
| 70 | 6 |
| 71 | 1 |
| 72 | 6 |
| 73 | 6 |
| 74 | 6 |
| 75 | 1 |
| 76 | 6 |
| 77 | 6 |
| 78 | 6 |
| 79 | 6 |
| 80 | 34 |
| 81 | 34 |
| 82 | 1 |
| 83 | 1 |
| 84 | 6 |
| 85 | 1 |
| 86 | 1 |
| 87 | 1 |
| 88 | 6 |
| 89 | 6 |
| 90 | 1 |
| 91 | 1 |
| 92 | 6 |
| 93 | 6 |
| 94 | 6 |
| 95 | 6 |
| 96 | 34 |
| 97 | 1 |
| 98 | 6 |
| 99 | 6 |
| 100 | 34 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.095821 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 30724.65250198571, "best_cost": 26383.241057706353}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
