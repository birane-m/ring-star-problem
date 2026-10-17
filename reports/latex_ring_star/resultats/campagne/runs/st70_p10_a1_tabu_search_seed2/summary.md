# Résultat tabu_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 274.395
- Coût marche : 735.042
- Coût total : 1009.437

## Stations choisies

1, 8, 12, 31, 40, 42, 56, 58, 59, 68

## Cycle métro

1 -> 31 -> 59 -> 42 -> 8 -> 68 -> 40 -> 12 -> 56 -> 58 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 16, 23, 36 | 4 |
| 8 | 3, 7, 8, 14, 19, 26, 28, 32, 49, 55 | 10 |
| 12 | 12, 21, 33, 34, 52, 54, 60, 62 | 8 |
| 31 | 13, 29, 31, 35, 69, 70 | 6 |
| 40 | 9, 25, 27, 39, 40, 45, 46, 61 | 8 |
| 42 | 2, 4, 6, 18, 41, 42 | 6 |
| 56 | 11, 48, 51, 56, 64, 65, 67 | 7 |
| 58 | 5, 10, 37, 47, 50, 53, 58 | 7 |
| 59 | 15, 22, 24, 38, 57, 59, 63, 66 | 8 |
| 68 | 17, 20, 30, 43, 44, 68 | 6 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 8 |
| 4 | 42 |
| 5 | 58 |
| 6 | 42 |
| 7 | 8 |
| 8 | 8 |
| 9 | 40 |
| 10 | 58 |
| 11 | 56 |
| 12 | 12 |
| 13 | 31 |
| 14 | 8 |
| 15 | 59 |
| 16 | 1 |
| 17 | 68 |
| 18 | 42 |
| 19 | 8 |
| 20 | 68 |
| 21 | 12 |
| 22 | 59 |
| 23 | 1 |
| 24 | 59 |
| 25 | 40 |
| 26 | 8 |
| 27 | 40 |
| 28 | 8 |
| 29 | 31 |
| 30 | 68 |
| 31 | 31 |
| 32 | 8 |
| 33 | 12 |
| 34 | 12 |
| 35 | 31 |
| 36 | 1 |
| 37 | 58 |
| 38 | 59 |
| 39 | 40 |
| 40 | 40 |
| 41 | 42 |
| 42 | 42 |
| 43 | 68 |
| 44 | 68 |
| 45 | 40 |
| 46 | 40 |
| 47 | 58 |
| 48 | 56 |
| 49 | 8 |
| 50 | 58 |
| 51 | 56 |
| 52 | 12 |
| 53 | 58 |
| 54 | 12 |
| 55 | 8 |
| 56 | 56 |
| 57 | 59 |
| 58 | 58 |
| 59 | 59 |
| 60 | 12 |
| 61 | 40 |
| 62 | 12 |
| 63 | 59 |
| 64 | 56 |
| 65 | 56 |
| 66 | 59 |
| 67 | 56 |
| 68 | 68 |
| 69 | 31 |
| 70 | 31 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.151085 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 1105.8204001256327, "best_cost": 1009.4366573256352}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
