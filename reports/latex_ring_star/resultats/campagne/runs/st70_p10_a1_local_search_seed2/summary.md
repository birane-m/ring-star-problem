# Résultat local_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 319.939
- Coût marche : 759.450
- Coût total : 1079.389

## Stations choisies

1, 8, 34, 42, 45, 53, 57, 67, 68, 69

## Cycle métro

1 -> 69 -> 57 -> 42 -> 8 -> 68 -> 45 -> 34 -> 67 -> 53 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 16, 23, 36, 37, 47 | 6 |
| 8 | 3, 7, 8, 14, 19, 26, 28, 32, 49, 55 | 10 |
| 34 | 12, 17, 21, 33, 34, 60, 62 | 7 |
| 42 | 2, 4, 6, 18, 41, 42 | 6 |
| 45 | 25, 27, 39, 40, 45, 46, 61 | 7 |
| 53 | 5, 10, 50, 52, 53, 58 | 6 |
| 57 | 15, 24, 57, 63, 66 | 5 |
| 67 | 11, 48, 51, 54, 56, 64, 65, 67 | 8 |
| 68 | 9, 20, 30, 43, 44, 68 | 6 |
| 69 | 13, 22, 29, 31, 35, 38, 59, 69, 70 | 9 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 8 |
| 4 | 42 |
| 5 | 53 |
| 6 | 42 |
| 7 | 8 |
| 8 | 8 |
| 9 | 68 |
| 10 | 53 |
| 11 | 67 |
| 12 | 34 |
| 13 | 69 |
| 14 | 8 |
| 15 | 57 |
| 16 | 1 |
| 17 | 34 |
| 18 | 42 |
| 19 | 8 |
| 20 | 68 |
| 21 | 34 |
| 22 | 69 |
| 23 | 1 |
| 24 | 57 |
| 25 | 45 |
| 26 | 8 |
| 27 | 45 |
| 28 | 8 |
| 29 | 69 |
| 30 | 68 |
| 31 | 69 |
| 32 | 8 |
| 33 | 34 |
| 34 | 34 |
| 35 | 69 |
| 36 | 1 |
| 37 | 1 |
| 38 | 69 |
| 39 | 45 |
| 40 | 45 |
| 41 | 42 |
| 42 | 42 |
| 43 | 68 |
| 44 | 68 |
| 45 | 45 |
| 46 | 45 |
| 47 | 1 |
| 48 | 67 |
| 49 | 8 |
| 50 | 53 |
| 51 | 67 |
| 52 | 53 |
| 53 | 53 |
| 54 | 67 |
| 55 | 8 |
| 56 | 67 |
| 57 | 57 |
| 58 | 53 |
| 59 | 69 |
| 60 | 34 |
| 61 | 45 |
| 62 | 34 |
| 63 | 57 |
| 64 | 67 |
| 65 | 67 |
| 66 | 57 |
| 67 | 67 |
| 68 | 68 |
| 69 | 69 |
| 70 | 69 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.012592 s
- Graine : 2
- Détails : {"accepted_moves": 2, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 1105.8204001256327, "best_cost": 1079.3885281025769}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
