# Résultat local_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 3276.715
- Coût marche : 6719.427
- Coût total : 9996.142

## Stations choisies

1, 5, 19, 21, 28, 30, 36, 42, 43, 50

## Cycle métro

1 -> 36 -> 5 -> 28 -> 43 -> 19 -> 21 -> 42 -> 30 -> 50 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 18, 22, 31, 32, 49 | 6 |
| 5 | 4, 5, 6, 15, 24, 25, 38, 46, 48 | 9 |
| 19 | 3, 8, 9, 10, 19, 41, 45 | 7 |
| 21 | 17, 21 | 2 |
| 28 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |
| 30 | 30 | 1 |
| 36 | 34, 35, 36, 37, 39, 40, 44 | 7 |
| 42 | 2, 7, 42 | 3 |
| 43 | 33, 43 | 2 |
| 50 | 16, 20, 23, 29, 50 | 5 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 19 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 42 |
| 8 | 19 |
| 9 | 19 |
| 10 | 19 |
| 11 | 28 |
| 12 | 28 |
| 13 | 28 |
| 14 | 28 |
| 15 | 5 |
| 16 | 50 |
| 17 | 21 |
| 18 | 1 |
| 19 | 19 |
| 20 | 50 |
| 21 | 21 |
| 22 | 1 |
| 23 | 50 |
| 24 | 5 |
| 25 | 5 |
| 26 | 28 |
| 27 | 28 |
| 28 | 28 |
| 29 | 50 |
| 30 | 30 |
| 31 | 1 |
| 32 | 1 |
| 33 | 43 |
| 34 | 36 |
| 35 | 36 |
| 36 | 36 |
| 37 | 36 |
| 38 | 5 |
| 39 | 36 |
| 40 | 36 |
| 41 | 19 |
| 42 | 42 |
| 43 | 43 |
| 44 | 36 |
| 45 | 19 |
| 46 | 5 |
| 47 | 28 |
| 48 | 5 |
| 49 | 1 |
| 50 | 50 |
| 51 | 28 |
| 52 | 28 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.009904 s
- Graine : 2
- Détails : {"accepted_moves": 16, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 12155.572132213485, "best_cost": 9996.14157558931}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
