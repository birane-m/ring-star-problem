# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 13414.556
- Coût marche : 43140.877
- Coût total : 56555.433

## Stations choisies

1, 7, 15, 25, 42

## Cycle métro

1 -> 7 -> 15 -> 25 -> 42 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 16, 22, 38, 41 | 8 |
| 7 | 6, 7, 17, 18, 19, 27, 28, 30, 31, 36, 37, 43, 44 | 13 |
| 15 | 11, 12, 15, 20, 33, 40, 46 | 7 |
| 25 | 13, 14, 21, 23, 25, 32, 34, 39, 47 | 9 |
| 42 | 2, 4, 5, 10, 24, 26, 29, 35, 42, 45, 48 | 11 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 1 |
| 4 | 42 |
| 5 | 42 |
| 6 | 7 |
| 7 | 7 |
| 8 | 1 |
| 9 | 1 |
| 10 | 42 |
| 11 | 15 |
| 12 | 15 |
| 13 | 25 |
| 14 | 25 |
| 15 | 15 |
| 16 | 1 |
| 17 | 7 |
| 18 | 7 |
| 19 | 7 |
| 20 | 15 |
| 21 | 25 |
| 22 | 1 |
| 23 | 25 |
| 24 | 42 |
| 25 | 25 |
| 26 | 42 |
| 27 | 7 |
| 28 | 7 |
| 29 | 42 |
| 30 | 7 |
| 31 | 7 |
| 32 | 25 |
| 33 | 15 |
| 34 | 25 |
| 35 | 42 |
| 36 | 7 |
| 37 | 7 |
| 38 | 1 |
| 39 | 25 |
| 40 | 15 |
| 41 | 1 |
| 42 | 42 |
| 43 | 7 |
| 44 | 7 |
| 45 | 42 |
| 46 | 15 |
| 47 | 25 |
| 48 | 42 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.004967 s
- Graine : 1
- Détails : {"accepted_moves": 9, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 63668.04323160226, "best_cost": 56555.43301333158}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
