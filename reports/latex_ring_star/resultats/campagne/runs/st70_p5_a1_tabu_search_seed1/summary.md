# Résultat tabu_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 217.422
- Coût marche : 1150.657
- Coût total : 1368.079

## Stations choisies

1, 22, 32, 60, 61

## Cycle métro

1 -> 22 -> 32 -> 61 -> 60 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 13, 16, 23, 29, 36, 37, 47, 58, 70 | 10 |
| 22 | 15, 22, 24, 31, 35, 38, 53, 57, 59, 63, 66, 69 | 12 |
| 32 | 2, 3, 4, 6, 7, 8, 14, 18, 19, 20, 26, 28, 30, 32, 41, 42, 44, 49, 55, 68 | 20 |
| 60 | 5, 10, 11, 12, 21, 33, 34, 48, 50, 51, 52, 54, 56, 60, 64, 65, 67 | 17 |
| 61 | 9, 17, 25, 27, 39, 40, 43, 45, 46, 61, 62 | 11 |

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
| 9 | 61 |
| 10 | 60 |
| 11 | 60 |
| 12 | 60 |
| 13 | 1 |
| 14 | 32 |
| 15 | 22 |
| 16 | 1 |
| 17 | 61 |
| 18 | 32 |
| 19 | 32 |
| 20 | 32 |
| 21 | 60 |
| 22 | 22 |
| 23 | 1 |
| 24 | 22 |
| 25 | 61 |
| 26 | 32 |
| 27 | 61 |
| 28 | 32 |
| 29 | 1 |
| 30 | 32 |
| 31 | 22 |
| 32 | 32 |
| 33 | 60 |
| 34 | 60 |
| 35 | 22 |
| 36 | 1 |
| 37 | 1 |
| 38 | 22 |
| 39 | 61 |
| 40 | 61 |
| 41 | 32 |
| 42 | 32 |
| 43 | 61 |
| 44 | 32 |
| 45 | 61 |
| 46 | 61 |
| 47 | 1 |
| 48 | 60 |
| 49 | 32 |
| 50 | 60 |
| 51 | 60 |
| 52 | 60 |
| 53 | 22 |
| 54 | 60 |
| 55 | 32 |
| 56 | 60 |
| 57 | 22 |
| 58 | 1 |
| 59 | 22 |
| 60 | 60 |
| 61 | 61 |
| 62 | 61 |
| 63 | 22 |
| 64 | 60 |
| 65 | 60 |
| 66 | 22 |
| 67 | 60 |
| 68 | 32 |
| 69 | 22 |
| 70 | 1 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.090104 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 1572.5306924123652, "best_cost": 1368.078588269259}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
