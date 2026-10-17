# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 13691.854
- Coût marche : 42997.804
- Coût total : 56689.658

## Stations choisies

1, 20, 25, 28, 42

## Cycle métro

1 -> 28 -> 20 -> 25 -> 42 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 16, 22, 38, 40, 41 | 9 |
| 20 | 11, 12, 15, 20, 33, 46, 47 | 7 |
| 25 | 13, 14, 21, 23, 25, 32, 34, 39 | 8 |
| 28 | 6, 7, 17, 18, 19, 27, 28, 30, 31, 36, 37, 43, 44 | 13 |
| 42 | 2, 4, 5, 10, 24, 26, 29, 35, 42, 45, 48 | 11 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 1 |
| 4 | 42 |
| 5 | 42 |
| 6 | 28 |
| 7 | 28 |
| 8 | 1 |
| 9 | 1 |
| 10 | 42 |
| 11 | 20 |
| 12 | 20 |
| 13 | 25 |
| 14 | 25 |
| 15 | 20 |
| 16 | 1 |
| 17 | 28 |
| 18 | 28 |
| 19 | 28 |
| 20 | 20 |
| 21 | 25 |
| 22 | 1 |
| 23 | 25 |
| 24 | 42 |
| 25 | 25 |
| 26 | 42 |
| 27 | 28 |
| 28 | 28 |
| 29 | 42 |
| 30 | 28 |
| 31 | 28 |
| 32 | 25 |
| 33 | 20 |
| 34 | 25 |
| 35 | 42 |
| 36 | 28 |
| 37 | 28 |
| 38 | 1 |
| 39 | 25 |
| 40 | 1 |
| 41 | 1 |
| 42 | 42 |
| 43 | 28 |
| 44 | 28 |
| 45 | 42 |
| 46 | 20 |
| 47 | 20 |
| 48 | 42 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005022 s
- Graine : 0
- Détails : {"accepted_moves": 7, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 63668.04323160226, "best_cost": 56689.65793053665}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
