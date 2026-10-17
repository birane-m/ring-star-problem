# Résultat local_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2325.666
- Coût marche : 9851.318
- Coût total : 12176.984

## Stations choisies

1, 5, 8, 20, 26

## Cycle métro

1 -> 8 -> 5 -> 26 -> 20 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 17, 18, 22, 31, 32, 34, 35, 36, 44, 49 | 12 |
| 5 | 4, 5, 6, 15, 24, 25, 33, 37, 38, 39, 40, 43, 46, 48 | 14 |
| 8 | 8, 9, 10, 19, 41, 45 | 6 |
| 20 | 2, 7, 16, 20, 21, 23, 29, 30, 42, 50 | 10 |
| 26 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 20 |
| 3 | 1 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 20 |
| 8 | 8 |
| 9 | 8 |
| 10 | 8 |
| 11 | 26 |
| 12 | 26 |
| 13 | 26 |
| 14 | 26 |
| 15 | 5 |
| 16 | 20 |
| 17 | 1 |
| 18 | 1 |
| 19 | 8 |
| 20 | 20 |
| 21 | 20 |
| 22 | 1 |
| 23 | 20 |
| 24 | 5 |
| 25 | 5 |
| 26 | 26 |
| 27 | 26 |
| 28 | 26 |
| 29 | 20 |
| 30 | 20 |
| 31 | 1 |
| 32 | 1 |
| 33 | 5 |
| 34 | 1 |
| 35 | 1 |
| 36 | 1 |
| 37 | 5 |
| 38 | 5 |
| 39 | 5 |
| 40 | 5 |
| 41 | 8 |
| 42 | 20 |
| 43 | 5 |
| 44 | 1 |
| 45 | 8 |
| 46 | 5 |
| 47 | 26 |
| 48 | 5 |
| 49 | 1 |
| 50 | 20 |
| 51 | 26 |
| 52 | 26 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005321 s
- Graine : 0
- Détails : {"accepted_moves": 7, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 14916.735925839565, "best_cost": 12176.984026278134}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
