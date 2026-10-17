# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 16193.851
- Coût marche : 26576.152
- Coût total : 42770.003

## Stations choisies

1, 3, 5, 6, 7, 10, 13, 33, 38, 39

## Cycle métro

1 -> 38 -> 7 -> 6 -> 33 -> 13 -> 39 -> 10 -> 5 -> 3 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 9, 40 | 4 |
| 3 | 3, 16, 22, 34, 41 | 5 |
| 5 | 2, 5, 29, 48 | 4 |
| 6 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 7 | 7, 18, 28, 36, 44 | 5 |
| 10 | 4, 10, 24, 26, 35, 42, 45 | 7 |
| 13 | 11, 13, 14, 21, 23, 25, 47 | 7 |
| 33 | 12, 15, 20, 33, 46 | 5 |
| 38 | 31, 38 | 2 |
| 39 | 32, 39 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 5 |
| 3 | 3 |
| 4 | 10 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 1 |
| 10 | 10 |
| 11 | 13 |
| 12 | 33 |
| 13 | 13 |
| 14 | 13 |
| 15 | 33 |
| 16 | 3 |
| 17 | 6 |
| 18 | 7 |
| 19 | 6 |
| 20 | 33 |
| 21 | 13 |
| 22 | 3 |
| 23 | 13 |
| 24 | 10 |
| 25 | 13 |
| 26 | 10 |
| 27 | 6 |
| 28 | 7 |
| 29 | 5 |
| 30 | 6 |
| 31 | 38 |
| 32 | 39 |
| 33 | 33 |
| 34 | 3 |
| 35 | 10 |
| 36 | 7 |
| 37 | 6 |
| 38 | 38 |
| 39 | 39 |
| 40 | 1 |
| 41 | 3 |
| 42 | 10 |
| 43 | 6 |
| 44 | 7 |
| 45 | 10 |
| 46 | 33 |
| 47 | 13 |
| 48 | 5 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.121435 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 48833.89333184296, "best_cost": 42770.00268273156}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
