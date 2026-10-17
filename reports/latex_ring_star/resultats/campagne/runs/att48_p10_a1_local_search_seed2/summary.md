# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 16020.451
- Coût marche : 29891.911
- Coût total : 45912.363

## Stations choisies

1, 7, 13, 22, 29, 30, 32, 41, 42, 46

## Cycle métro

1 -> 22 -> 41 -> 29 -> 42 -> 32 -> 13 -> 30 -> 7 -> 46 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 9, 40 | 4 |
| 7 | 7, 18, 28, 36, 44 | 5 |
| 13 | 11, 13, 14, 21, 23, 25, 47 | 7 |
| 22 | 3, 16, 22 | 3 |
| 29 | 2, 5, 29 | 3 |
| 30 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 32 | 32, 39 | 2 |
| 41 | 34, 41 | 2 |
| 42 | 4, 10, 24, 26, 35, 42, 45, 48 | 8 |
| 46 | 12, 15, 20, 31, 33, 38, 46 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 29 |
| 3 | 22 |
| 4 | 42 |
| 5 | 29 |
| 6 | 30 |
| 7 | 7 |
| 8 | 1 |
| 9 | 1 |
| 10 | 42 |
| 11 | 13 |
| 12 | 46 |
| 13 | 13 |
| 14 | 13 |
| 15 | 46 |
| 16 | 22 |
| 17 | 30 |
| 18 | 7 |
| 19 | 30 |
| 20 | 46 |
| 21 | 13 |
| 22 | 22 |
| 23 | 13 |
| 24 | 42 |
| 25 | 13 |
| 26 | 42 |
| 27 | 30 |
| 28 | 7 |
| 29 | 29 |
| 30 | 30 |
| 31 | 46 |
| 32 | 32 |
| 33 | 46 |
| 34 | 41 |
| 35 | 42 |
| 36 | 7 |
| 37 | 30 |
| 38 | 46 |
| 39 | 32 |
| 40 | 1 |
| 41 | 41 |
| 42 | 42 |
| 43 | 30 |
| 44 | 7 |
| 45 | 42 |
| 46 | 46 |
| 47 | 13 |
| 48 | 42 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.008334 s
- Graine : 2
- Détails : {"accepted_moves": 6, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 48833.89333184296, "best_cost": 45912.36253902775}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
