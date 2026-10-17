# Résultat local_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2264.133
- Coût marche : 9621.308
- Coût total : 11885.440

## Stations choisies

1, 19, 20, 27, 48

## Cycle métro

1 -> 20 -> 27 -> 48 -> 19 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 18, 22, 31, 32, 35, 36, 44, 49 | 9 |
| 19 | 3, 8, 9, 10, 17, 19, 41, 45 | 8 |
| 20 | 2, 7, 16, 20, 21, 23, 29, 30, 42, 50 | 10 |
| 27 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |
| 48 | 4, 5, 6, 15, 24, 25, 33, 34, 37, 38, 39, 40, 43, 46, 48 | 15 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 20 |
| 3 | 19 |
| 4 | 48 |
| 5 | 48 |
| 6 | 48 |
| 7 | 20 |
| 8 | 19 |
| 9 | 19 |
| 10 | 19 |
| 11 | 27 |
| 12 | 27 |
| 13 | 27 |
| 14 | 27 |
| 15 | 48 |
| 16 | 20 |
| 17 | 19 |
| 18 | 1 |
| 19 | 19 |
| 20 | 20 |
| 21 | 20 |
| 22 | 1 |
| 23 | 20 |
| 24 | 48 |
| 25 | 48 |
| 26 | 27 |
| 27 | 27 |
| 28 | 27 |
| 29 | 20 |
| 30 | 20 |
| 31 | 1 |
| 32 | 1 |
| 33 | 48 |
| 34 | 48 |
| 35 | 1 |
| 36 | 1 |
| 37 | 48 |
| 38 | 48 |
| 39 | 48 |
| 40 | 48 |
| 41 | 19 |
| 42 | 20 |
| 43 | 48 |
| 44 | 1 |
| 45 | 19 |
| 46 | 48 |
| 47 | 27 |
| 48 | 48 |
| 49 | 1 |
| 50 | 20 |
| 51 | 27 |
| 52 | 27 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.006609 s
- Graine : 2
- Détails : {"accepted_moves": 10, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 14916.735925839565, "best_cost": 11885.440278885257}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
