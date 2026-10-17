# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 10732.275
- Coût marche : 60170.854
- Coût total : 70903.129

## Stations choisies

1, 36, 48

## Cycle métro

1 -> 36 -> 48 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 11, 15, 16, 22, 23, 38, 40, 41 | 12 |
| 36 | 6, 7, 12, 17, 18, 19, 20, 27, 28, 30, 31, 33, 36, 37, 43, 44, 46, 47 | 18 |
| 48 | 2, 4, 5, 10, 13, 14, 21, 24, 25, 26, 29, 32, 34, 35, 39, 42, 45, 48 | 18 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 48 |
| 3 | 1 |
| 4 | 48 |
| 5 | 48 |
| 6 | 36 |
| 7 | 36 |
| 8 | 1 |
| 9 | 1 |
| 10 | 48 |
| 11 | 1 |
| 12 | 36 |
| 13 | 48 |
| 14 | 48 |
| 15 | 1 |
| 16 | 1 |
| 17 | 36 |
| 18 | 36 |
| 19 | 36 |
| 20 | 36 |
| 21 | 48 |
| 22 | 1 |
| 23 | 1 |
| 24 | 48 |
| 25 | 48 |
| 26 | 48 |
| 27 | 36 |
| 28 | 36 |
| 29 | 48 |
| 30 | 36 |
| 31 | 36 |
| 32 | 48 |
| 33 | 36 |
| 34 | 48 |
| 35 | 48 |
| 36 | 36 |
| 37 | 36 |
| 38 | 1 |
| 39 | 48 |
| 40 | 1 |
| 41 | 1 |
| 42 | 48 |
| 43 | 36 |
| 44 | 36 |
| 45 | 48 |
| 46 | 36 |
| 47 | 36 |
| 48 | 48 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.046239 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 78299.76512022842, "best_cost": 70903.12865213412}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
