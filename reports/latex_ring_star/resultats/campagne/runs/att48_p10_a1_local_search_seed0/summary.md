# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 15302.394
- Coût marche : 30426.703
- Coût total : 45729.097

## Stations choisies

1, 3, 5, 7, 9, 14, 27, 42, 46, 47

## Cycle métro

1 -> 9 -> 46 -> 7 -> 27 -> 47 -> 42 -> 5 -> 14 -> 3 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8 | 2 |
| 3 | 3, 16, 22, 41 | 4 |
| 5 | 5, 29, 32, 39, 48 | 5 |
| 7 | 7, 18, 28, 36, 44 | 5 |
| 9 | 9, 38, 40 | 3 |
| 14 | 13, 14, 23, 25, 34 | 5 |
| 27 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 42 | 2, 4, 10, 24, 26, 35, 42, 45 | 8 |
| 46 | 12, 15, 31, 33, 46 | 5 |
| 47 | 11, 20, 21, 47 | 4 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 3 |
| 4 | 42 |
| 5 | 5 |
| 6 | 27 |
| 7 | 7 |
| 8 | 1 |
| 9 | 9 |
| 10 | 42 |
| 11 | 47 |
| 12 | 46 |
| 13 | 14 |
| 14 | 14 |
| 15 | 46 |
| 16 | 3 |
| 17 | 27 |
| 18 | 7 |
| 19 | 27 |
| 20 | 47 |
| 21 | 47 |
| 22 | 3 |
| 23 | 14 |
| 24 | 42 |
| 25 | 14 |
| 26 | 42 |
| 27 | 27 |
| 28 | 7 |
| 29 | 5 |
| 30 | 27 |
| 31 | 46 |
| 32 | 5 |
| 33 | 46 |
| 34 | 14 |
| 35 | 42 |
| 36 | 7 |
| 37 | 27 |
| 38 | 9 |
| 39 | 5 |
| 40 | 9 |
| 41 | 3 |
| 42 | 42 |
| 43 | 27 |
| 44 | 7 |
| 45 | 42 |
| 46 | 46 |
| 47 | 47 |
| 48 | 5 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.009181 s
- Graine : 0
- Détails : {"accepted_moves": 12, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 48833.89333184296, "best_cost": 45729.09742946026}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
