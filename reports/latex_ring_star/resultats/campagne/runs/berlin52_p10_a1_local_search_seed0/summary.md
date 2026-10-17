# Résultat local_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 3432.374
- Coût marche : 6425.724
- Coût total : 9858.098

## Stations choisies

1, 10, 18, 20, 24, 28, 35, 42, 43, 45

## Cycle métro

1 -> 20 -> 42 -> 18 -> 45 -> 10 -> 43 -> 28 -> 24 -> 35 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 32, 49 | 4 |
| 10 | 8, 9, 10 | 3 |
| 18 | 3, 17, 18, 21, 31 | 5 |
| 20 | 16, 20, 23, 29, 30, 50 | 6 |
| 24 | 4, 5, 6, 15, 24, 25, 37, 38, 40, 46, 48 | 11 |
| 28 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |
| 35 | 34, 35, 36, 39, 44 | 5 |
| 42 | 2, 7, 42 | 3 |
| 43 | 33, 43 | 2 |
| 45 | 19, 41, 45 | 3 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 18 |
| 4 | 24 |
| 5 | 24 |
| 6 | 24 |
| 7 | 42 |
| 8 | 10 |
| 9 | 10 |
| 10 | 10 |
| 11 | 28 |
| 12 | 28 |
| 13 | 28 |
| 14 | 28 |
| 15 | 24 |
| 16 | 20 |
| 17 | 18 |
| 18 | 18 |
| 19 | 45 |
| 20 | 20 |
| 21 | 18 |
| 22 | 1 |
| 23 | 20 |
| 24 | 24 |
| 25 | 24 |
| 26 | 28 |
| 27 | 28 |
| 28 | 28 |
| 29 | 20 |
| 30 | 20 |
| 31 | 18 |
| 32 | 1 |
| 33 | 43 |
| 34 | 35 |
| 35 | 35 |
| 36 | 35 |
| 37 | 24 |
| 38 | 24 |
| 39 | 35 |
| 40 | 24 |
| 41 | 45 |
| 42 | 42 |
| 43 | 43 |
| 44 | 35 |
| 45 | 45 |
| 46 | 24 |
| 47 | 28 |
| 48 | 24 |
| 49 | 1 |
| 50 | 20 |
| 51 | 28 |
| 52 | 28 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.010018 s
- Graine : 0
- Détails : {"accepted_moves": 16, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 12155.572132213485, "best_cost": 9858.097675874307}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
