# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 16539.121
- Coût marche : 28508.702
- Coût total : 45047.823

## Stations choisies

1, 6, 7, 10, 12, 14, 21, 42, 44, 48

## Cycle métro

1 -> 44 -> 7 -> 6 -> 12 -> 21 -> 10 -> 42 -> 48 -> 14 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 9, 16, 22 | 5 |
| 6 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 7 | 7, 18, 28, 36 | 4 |
| 10 | 4, 10, 24, 26, 35, 45 | 6 |
| 12 | 11, 12, 15, 20, 33, 40 | 6 |
| 14 | 3, 13, 14, 23, 25, 34, 41 | 7 |
| 21 | 21, 32, 47 | 3 |
| 42 | 2, 42 | 2 |
| 44 | 31, 38, 44, 46 | 4 |
| 48 | 5, 29, 39, 48 | 4 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 14 |
| 4 | 10 |
| 5 | 48 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 1 |
| 10 | 10 |
| 11 | 12 |
| 12 | 12 |
| 13 | 14 |
| 14 | 14 |
| 15 | 12 |
| 16 | 1 |
| 17 | 6 |
| 18 | 7 |
| 19 | 6 |
| 20 | 12 |
| 21 | 21 |
| 22 | 1 |
| 23 | 14 |
| 24 | 10 |
| 25 | 14 |
| 26 | 10 |
| 27 | 6 |
| 28 | 7 |
| 29 | 48 |
| 30 | 6 |
| 31 | 44 |
| 32 | 21 |
| 33 | 12 |
| 34 | 14 |
| 35 | 10 |
| 36 | 7 |
| 37 | 6 |
| 38 | 44 |
| 39 | 48 |
| 40 | 12 |
| 41 | 14 |
| 42 | 42 |
| 43 | 6 |
| 44 | 44 |
| 45 | 10 |
| 46 | 44 |
| 47 | 21 |
| 48 | 48 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.008517 s
- Graine : 1
- Détails : {"accepted_moves": 9, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 48833.89333184296, "best_cost": 45047.82260641131}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
