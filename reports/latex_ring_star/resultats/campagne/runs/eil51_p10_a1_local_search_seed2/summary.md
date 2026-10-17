# Résultat local_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 174.556
- Coût marche : 390.411
- Coût total : 564.967

## Stations choisies

1, 9, 14, 15, 20, 29, 30, 41, 47, 48

## Cycle métro

1 -> 20 -> 29 -> 9 -> 30 -> 15 -> 41 -> 47 -> 14 -> 48 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 11, 22, 27, 28, 31, 32 | 7 |
| 9 | 5, 9, 16, 38, 49, 50 | 6 |
| 14 | 14, 24, 25 | 3 |
| 15 | 15, 33, 37, 44, 45 | 5 |
| 20 | 3, 20, 35, 36 | 4 |
| 29 | 2, 21, 29 | 3 |
| 30 | 10, 30, 34, 39 | 4 |
| 41 | 13, 19, 40, 41, 42 | 5 |
| 47 | 4, 12, 17, 18, 46, 47, 51 | 7 |
| 48 | 6, 7, 8, 23, 26, 43, 48 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 29 |
| 3 | 20 |
| 4 | 47 |
| 5 | 9 |
| 6 | 48 |
| 7 | 48 |
| 8 | 48 |
| 9 | 9 |
| 10 | 30 |
| 11 | 1 |
| 12 | 47 |
| 13 | 41 |
| 14 | 14 |
| 15 | 15 |
| 16 | 9 |
| 17 | 47 |
| 18 | 47 |
| 19 | 41 |
| 20 | 20 |
| 21 | 29 |
| 22 | 1 |
| 23 | 48 |
| 24 | 14 |
| 25 | 14 |
| 26 | 48 |
| 27 | 1 |
| 28 | 1 |
| 29 | 29 |
| 30 | 30 |
| 31 | 1 |
| 32 | 1 |
| 33 | 15 |
| 34 | 30 |
| 35 | 20 |
| 36 | 20 |
| 37 | 15 |
| 38 | 9 |
| 39 | 30 |
| 40 | 41 |
| 41 | 41 |
| 42 | 41 |
| 43 | 48 |
| 44 | 15 |
| 45 | 15 |
| 46 | 47 |
| 47 | 47 |
| 48 | 48 |
| 49 | 9 |
| 50 | 9 |
| 51 | 47 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.009382 s
- Graine : 2
- Détails : {"accepted_moves": 11, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 630.4676373541728, "best_cost": 564.9670123921741}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
