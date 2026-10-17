# Résultat local_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 124.919
- Coût marche : 588.093
- Coût total : 713.013

## Stations choisies

1, 4, 15, 23, 50

## Cycle métro

1 -> 23 -> 4 -> 15 -> 50 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 8, 11, 20, 22, 27, 28, 31, 32, 36, 46, 51 | 14 |
| 4 | 4, 12, 13, 17, 18, 19, 25, 40, 41, 42, 47 | 11 |
| 15 | 5, 10, 15, 33, 37, 44, 45 | 7 |
| 23 | 6, 7, 14, 23, 24, 26, 43, 48 | 8 |
| 50 | 9, 16, 21, 29, 30, 34, 35, 38, 39, 49, 50 | 11 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 4 |
| 5 | 15 |
| 6 | 23 |
| 7 | 23 |
| 8 | 1 |
| 9 | 50 |
| 10 | 15 |
| 11 | 1 |
| 12 | 4 |
| 13 | 4 |
| 14 | 23 |
| 15 | 15 |
| 16 | 50 |
| 17 | 4 |
| 18 | 4 |
| 19 | 4 |
| 20 | 1 |
| 21 | 50 |
| 22 | 1 |
| 23 | 23 |
| 24 | 23 |
| 25 | 4 |
| 26 | 23 |
| 27 | 1 |
| 28 | 1 |
| 29 | 50 |
| 30 | 50 |
| 31 | 1 |
| 32 | 1 |
| 33 | 15 |
| 34 | 50 |
| 35 | 50 |
| 36 | 1 |
| 37 | 15 |
| 38 | 50 |
| 39 | 50 |
| 40 | 4 |
| 41 | 4 |
| 42 | 4 |
| 43 | 23 |
| 44 | 15 |
| 45 | 15 |
| 46 | 1 |
| 47 | 4 |
| 48 | 23 |
| 49 | 50 |
| 50 | 50 |
| 51 | 1 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005137 s
- Graine : 2
- Détails : {"accepted_moves": 2, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 735.0003807891881, "best_cost": 713.0125416115617}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
