# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 13679.201
- Coût marche : 41946.642
- Coût total : 55625.843

## Stations choisies

1, 12, 13, 28, 42

## Cycle métro

1 -> 42 -> 13 -> 12 -> 28 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 16, 22, 38, 41 | 8 |
| 12 | 11, 12, 15, 20, 33, 40, 46 | 7 |
| 13 | 13, 14, 21, 23, 25, 32, 34, 39, 47 | 9 |
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
| 11 | 12 |
| 12 | 12 |
| 13 | 13 |
| 14 | 13 |
| 15 | 12 |
| 16 | 1 |
| 17 | 28 |
| 18 | 28 |
| 19 | 28 |
| 20 | 12 |
| 21 | 13 |
| 22 | 1 |
| 23 | 13 |
| 24 | 42 |
| 25 | 13 |
| 26 | 42 |
| 27 | 28 |
| 28 | 28 |
| 29 | 42 |
| 30 | 28 |
| 31 | 28 |
| 32 | 13 |
| 33 | 12 |
| 34 | 13 |
| 35 | 42 |
| 36 | 28 |
| 37 | 28 |
| 38 | 1 |
| 39 | 13 |
| 40 | 12 |
| 41 | 1 |
| 42 | 42 |
| 43 | 28 |
| 44 | 28 |
| 45 | 42 |
| 46 | 12 |
| 47 | 13 |
| 48 | 42 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.062101 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 63668.04323160226, "best_cost": 55625.84275154893}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
