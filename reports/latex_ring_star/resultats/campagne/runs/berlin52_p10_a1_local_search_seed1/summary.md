# Résultat local_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 3757.415
- Coût marche : 5996.379
- Coût total : 9753.794

## Stations choisies

1, 5, 12, 13, 18, 20, 27, 36, 41, 42

## Cycle métro

1 -> 36 -> 5 -> 12 -> 27 -> 13 -> 20 -> 42 -> 18 -> 41 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 32, 49 | 4 |
| 5 | 4, 5, 6, 15, 24, 25, 38, 43, 46, 48 | 10 |
| 12 | 11, 12, 33, 51 | 4 |
| 13 | 13, 14, 52 | 3 |
| 18 | 3, 17, 18, 21, 31 | 5 |
| 20 | 16, 20, 23, 29, 30, 50 | 6 |
| 27 | 26, 27, 28, 47 | 4 |
| 36 | 34, 35, 36, 37, 39, 40, 44 | 7 |
| 41 | 8, 9, 10, 19, 41, 45 | 6 |
| 42 | 2, 7, 42 | 3 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 18 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 42 |
| 8 | 41 |
| 9 | 41 |
| 10 | 41 |
| 11 | 12 |
| 12 | 12 |
| 13 | 13 |
| 14 | 13 |
| 15 | 5 |
| 16 | 20 |
| 17 | 18 |
| 18 | 18 |
| 19 | 41 |
| 20 | 20 |
| 21 | 18 |
| 22 | 1 |
| 23 | 20 |
| 24 | 5 |
| 25 | 5 |
| 26 | 27 |
| 27 | 27 |
| 28 | 27 |
| 29 | 20 |
| 30 | 20 |
| 31 | 18 |
| 32 | 1 |
| 33 | 12 |
| 34 | 36 |
| 35 | 36 |
| 36 | 36 |
| 37 | 36 |
| 38 | 5 |
| 39 | 36 |
| 40 | 36 |
| 41 | 41 |
| 42 | 42 |
| 43 | 5 |
| 44 | 36 |
| 45 | 41 |
| 46 | 5 |
| 47 | 27 |
| 48 | 5 |
| 49 | 1 |
| 50 | 20 |
| 51 | 12 |
| 52 | 13 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.010738 s
- Graine : 1
- Détails : {"accepted_moves": 11, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 12155.572132213485, "best_cost": 9753.793976145174}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
