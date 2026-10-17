# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 10720.322
- Coût marche : 60792.657
- Coût total : 71512.979

## Stations choisies

1, 5, 36

## Cycle métro

1 -> 36 -> 5 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 11, 15, 16, 22, 23, 38, 40, 41 | 12 |
| 5 | 2, 4, 5, 10, 13, 14, 21, 24, 25, 26, 29, 32, 34, 35, 39, 42, 45, 48 | 18 |
| 36 | 6, 7, 12, 17, 18, 19, 20, 27, 28, 30, 31, 33, 36, 37, 43, 44, 46, 47 | 18 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 5 |
| 3 | 1 |
| 4 | 5 |
| 5 | 5 |
| 6 | 36 |
| 7 | 36 |
| 8 | 1 |
| 9 | 1 |
| 10 | 5 |
| 11 | 1 |
| 12 | 36 |
| 13 | 5 |
| 14 | 5 |
| 15 | 1 |
| 16 | 1 |
| 17 | 36 |
| 18 | 36 |
| 19 | 36 |
| 20 | 36 |
| 21 | 5 |
| 22 | 1 |
| 23 | 1 |
| 24 | 5 |
| 25 | 5 |
| 26 | 5 |
| 27 | 36 |
| 28 | 36 |
| 29 | 5 |
| 30 | 36 |
| 31 | 36 |
| 32 | 5 |
| 33 | 36 |
| 34 | 5 |
| 35 | 5 |
| 36 | 36 |
| 37 | 36 |
| 38 | 1 |
| 39 | 5 |
| 40 | 1 |
| 41 | 1 |
| 42 | 5 |
| 43 | 36 |
| 44 | 36 |
| 45 | 5 |
| 46 | 36 |
| 47 | 36 |
| 48 | 5 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.004032 s
- Graine : 1
- Détails : {"accepted_moves": 3, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 78299.76512022842, "best_cost": 71512.97859727692}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
