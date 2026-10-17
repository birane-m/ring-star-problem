# Résultat tabu_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 276.653
- Coût marche : 732.689
- Coût total : 1009.342

## Stations choisies

1, 2, 28, 31, 34, 40, 50, 57, 65, 68

## Cycle métro

1 -> 31 -> 57 -> 2 -> 28 -> 68 -> 40 -> 34 -> 65 -> 50 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 16, 23, 36, 47 | 5 |
| 2 | 2, 4, 6, 7, 18, 19, 32, 42 | 8 |
| 28 | 3, 8, 14, 20, 26, 28, 49, 55 | 8 |
| 31 | 13, 22, 29, 31, 35, 38, 59, 69, 70 | 9 |
| 34 | 12, 17, 21, 33, 34, 54, 60, 62 | 8 |
| 40 | 9, 25, 27, 39, 40, 45, 46, 61 | 8 |
| 50 | 5, 10, 37, 50, 52, 53, 58 | 7 |
| 57 | 15, 24, 57, 63, 66 | 5 |
| 65 | 11, 48, 51, 56, 64, 65, 67 | 7 |
| 68 | 30, 41, 43, 44, 68 | 5 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 28 |
| 4 | 2 |
| 5 | 50 |
| 6 | 2 |
| 7 | 2 |
| 8 | 28 |
| 9 | 40 |
| 10 | 50 |
| 11 | 65 |
| 12 | 34 |
| 13 | 31 |
| 14 | 28 |
| 15 | 57 |
| 16 | 1 |
| 17 | 34 |
| 18 | 2 |
| 19 | 2 |
| 20 | 28 |
| 21 | 34 |
| 22 | 31 |
| 23 | 1 |
| 24 | 57 |
| 25 | 40 |
| 26 | 28 |
| 27 | 40 |
| 28 | 28 |
| 29 | 31 |
| 30 | 68 |
| 31 | 31 |
| 32 | 2 |
| 33 | 34 |
| 34 | 34 |
| 35 | 31 |
| 36 | 1 |
| 37 | 50 |
| 38 | 31 |
| 39 | 40 |
| 40 | 40 |
| 41 | 68 |
| 42 | 2 |
| 43 | 68 |
| 44 | 68 |
| 45 | 40 |
| 46 | 40 |
| 47 | 1 |
| 48 | 65 |
| 49 | 28 |
| 50 | 50 |
| 51 | 65 |
| 52 | 50 |
| 53 | 50 |
| 54 | 34 |
| 55 | 28 |
| 56 | 65 |
| 57 | 57 |
| 58 | 50 |
| 59 | 31 |
| 60 | 34 |
| 61 | 40 |
| 62 | 34 |
| 63 | 57 |
| 64 | 65 |
| 65 | 65 |
| 66 | 57 |
| 67 | 65 |
| 68 | 68 |
| 69 | 31 |
| 70 | 31 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.152493 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 1105.8204001256327, "best_cost": 1009.3417715191679}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
