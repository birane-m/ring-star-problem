# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 14491.334
- Coût marche : 41321.948
- Coût total : 55813.282

## Stations choisies

1, 6, 12, 25, 42

## Cycle métro

1 -> 42 -> 25 -> 12 -> 6 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 16, 22, 38, 41 | 8 |
| 6 | 6, 7, 17, 18, 19, 27, 28, 30, 36, 37, 43, 44 | 12 |
| 12 | 11, 12, 15, 20, 31, 33, 40, 46, 47 | 9 |
| 25 | 13, 14, 21, 23, 25, 32, 34, 39 | 8 |
| 42 | 2, 4, 5, 10, 24, 26, 29, 35, 42, 45, 48 | 11 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 1 |
| 4 | 42 |
| 5 | 42 |
| 6 | 6 |
| 7 | 6 |
| 8 | 1 |
| 9 | 1 |
| 10 | 42 |
| 11 | 12 |
| 12 | 12 |
| 13 | 25 |
| 14 | 25 |
| 15 | 12 |
| 16 | 1 |
| 17 | 6 |
| 18 | 6 |
| 19 | 6 |
| 20 | 12 |
| 21 | 25 |
| 22 | 1 |
| 23 | 25 |
| 24 | 42 |
| 25 | 25 |
| 26 | 42 |
| 27 | 6 |
| 28 | 6 |
| 29 | 42 |
| 30 | 6 |
| 31 | 12 |
| 32 | 25 |
| 33 | 12 |
| 34 | 25 |
| 35 | 42 |
| 36 | 6 |
| 37 | 6 |
| 38 | 1 |
| 39 | 25 |
| 40 | 12 |
| 41 | 1 |
| 42 | 42 |
| 43 | 6 |
| 44 | 6 |
| 45 | 42 |
| 46 | 12 |
| 47 | 12 |
| 48 | 42 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.061578 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 63668.04323160226, "best_cost": 55813.282224084614}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
