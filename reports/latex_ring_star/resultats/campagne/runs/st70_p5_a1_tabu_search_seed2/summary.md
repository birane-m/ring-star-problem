# Résultat tabu_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 202.956
- Coût marche : 1152.841
- Coût total : 1355.797

## Stations choisies

1, 9, 32, 60, 63

## Cycle métro

1 -> 63 -> 32 -> 9 -> 60 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 13, 16, 23, 29, 36, 37, 47, 58, 70 | 10 |
| 9 | 9, 17, 25, 27, 39, 40, 43, 44, 45, 46, 61, 68 | 12 |
| 32 | 2, 3, 4, 6, 7, 8, 14, 18, 19, 20, 26, 28, 30, 32, 41, 42, 49, 55 | 18 |
| 60 | 5, 10, 11, 12, 21, 33, 34, 48, 50, 51, 52, 54, 56, 60, 62, 64, 65, 67 | 18 |
| 63 | 15, 22, 24, 31, 35, 38, 53, 57, 59, 63, 66, 69 | 12 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 32 |
| 3 | 32 |
| 4 | 32 |
| 5 | 60 |
| 6 | 32 |
| 7 | 32 |
| 8 | 32 |
| 9 | 9 |
| 10 | 60 |
| 11 | 60 |
| 12 | 60 |
| 13 | 1 |
| 14 | 32 |
| 15 | 63 |
| 16 | 1 |
| 17 | 9 |
| 18 | 32 |
| 19 | 32 |
| 20 | 32 |
| 21 | 60 |
| 22 | 63 |
| 23 | 1 |
| 24 | 63 |
| 25 | 9 |
| 26 | 32 |
| 27 | 9 |
| 28 | 32 |
| 29 | 1 |
| 30 | 32 |
| 31 | 63 |
| 32 | 32 |
| 33 | 60 |
| 34 | 60 |
| 35 | 63 |
| 36 | 1 |
| 37 | 1 |
| 38 | 63 |
| 39 | 9 |
| 40 | 9 |
| 41 | 32 |
| 42 | 32 |
| 43 | 9 |
| 44 | 9 |
| 45 | 9 |
| 46 | 9 |
| 47 | 1 |
| 48 | 60 |
| 49 | 32 |
| 50 | 60 |
| 51 | 60 |
| 52 | 60 |
| 53 | 63 |
| 54 | 60 |
| 55 | 32 |
| 56 | 60 |
| 57 | 63 |
| 58 | 1 |
| 59 | 63 |
| 60 | 60 |
| 61 | 9 |
| 62 | 60 |
| 63 | 63 |
| 64 | 60 |
| 65 | 60 |
| 66 | 63 |
| 67 | 60 |
| 68 | 9 |
| 69 | 63 |
| 70 | 1 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.090365 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 1572.5306924123652, "best_cost": 1355.7967868800956}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
