# Résultat local_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 180.357
- Coût marche : 392.037
- Coût total : 572.394

## Stations choisies

1, 8, 14, 15, 19, 20, 29, 30, 46, 50

## Cycle métro

1 -> 8 -> 20 -> 29 -> 50 -> 30 -> 15 -> 19 -> 14 -> 46 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 27, 32 | 4 |
| 8 | 7, 8, 26, 28, 31, 48 | 6 |
| 14 | 6, 14, 18, 23, 24, 25, 43 | 7 |
| 15 | 15, 17, 33, 37, 44, 45 | 6 |
| 19 | 4, 13, 19, 40, 41, 42 | 6 |
| 20 | 3, 20, 35, 36 | 4 |
| 29 | 2, 21, 29 | 3 |
| 30 | 10, 30, 39, 49 | 4 |
| 46 | 5, 11, 12, 46, 47, 51 | 6 |
| 50 | 9, 16, 34, 38, 50 | 5 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 29 |
| 3 | 20 |
| 4 | 19 |
| 5 | 46 |
| 6 | 14 |
| 7 | 8 |
| 8 | 8 |
| 9 | 50 |
| 10 | 30 |
| 11 | 46 |
| 12 | 46 |
| 13 | 19 |
| 14 | 14 |
| 15 | 15 |
| 16 | 50 |
| 17 | 15 |
| 18 | 14 |
| 19 | 19 |
| 20 | 20 |
| 21 | 29 |
| 22 | 1 |
| 23 | 14 |
| 24 | 14 |
| 25 | 14 |
| 26 | 8 |
| 27 | 1 |
| 28 | 8 |
| 29 | 29 |
| 30 | 30 |
| 31 | 8 |
| 32 | 1 |
| 33 | 15 |
| 34 | 50 |
| 35 | 20 |
| 36 | 20 |
| 37 | 15 |
| 38 | 50 |
| 39 | 30 |
| 40 | 19 |
| 41 | 19 |
| 42 | 19 |
| 43 | 14 |
| 44 | 15 |
| 45 | 15 |
| 46 | 46 |
| 47 | 46 |
| 48 | 8 |
| 49 | 30 |
| 50 | 50 |
| 51 | 46 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.008607 s
- Graine : 1
- Détails : {"accepted_moves": 12, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 630.4676373541728, "best_cost": 572.3937545592128}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
