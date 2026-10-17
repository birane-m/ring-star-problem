# Résultat local_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 220.486
- Coût marche : 1135.224
- Coût total : 1355.710

## Stations choisies

1, 3, 40, 60, 63

## Cycle métro

1 -> 63 -> 3 -> 40 -> 60 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 13, 16, 23, 29, 36, 37, 47, 58, 70 | 10 |
| 3 | 2, 3, 4, 6, 7, 8, 14, 18, 19, 20, 26, 28, 30, 32, 41, 42, 43, 44, 49, 55, 68 | 21 |
| 40 | 9, 17, 25, 27, 39, 40, 45, 46, 61 | 9 |
| 60 | 5, 10, 11, 12, 21, 33, 34, 48, 50, 51, 52, 54, 56, 60, 62, 64, 65, 67 | 18 |
| 63 | 15, 22, 24, 31, 35, 38, 53, 57, 59, 63, 66, 69 | 12 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 3 |
| 4 | 3 |
| 5 | 60 |
| 6 | 3 |
| 7 | 3 |
| 8 | 3 |
| 9 | 40 |
| 10 | 60 |
| 11 | 60 |
| 12 | 60 |
| 13 | 1 |
| 14 | 3 |
| 15 | 63 |
| 16 | 1 |
| 17 | 40 |
| 18 | 3 |
| 19 | 3 |
| 20 | 3 |
| 21 | 60 |
| 22 | 63 |
| 23 | 1 |
| 24 | 63 |
| 25 | 40 |
| 26 | 3 |
| 27 | 40 |
| 28 | 3 |
| 29 | 1 |
| 30 | 3 |
| 31 | 63 |
| 32 | 3 |
| 33 | 60 |
| 34 | 60 |
| 35 | 63 |
| 36 | 1 |
| 37 | 1 |
| 38 | 63 |
| 39 | 40 |
| 40 | 40 |
| 41 | 3 |
| 42 | 3 |
| 43 | 3 |
| 44 | 3 |
| 45 | 40 |
| 46 | 40 |
| 47 | 1 |
| 48 | 60 |
| 49 | 3 |
| 50 | 60 |
| 51 | 60 |
| 52 | 60 |
| 53 | 63 |
| 54 | 60 |
| 55 | 3 |
| 56 | 60 |
| 57 | 63 |
| 58 | 1 |
| 59 | 63 |
| 60 | 60 |
| 61 | 40 |
| 62 | 60 |
| 63 | 63 |
| 64 | 60 |
| 65 | 60 |
| 66 | 63 |
| 67 | 60 |
| 68 | 3 |
| 69 | 63 |
| 70 | 1 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.007023 s
- Graine : 1
- Détails : {"accepted_moves": 5, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 1572.5306924123652, "best_cost": 1355.7097938033908}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
