# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 16289.879
- Coût marche : 26566.986
- Coût total : 42856.865

## Stations choisies

1, 5, 6, 7, 10, 12, 13, 34, 38, 39

## Cycle métro

1 -> 38 -> 7 -> 6 -> 12 -> 13 -> 39 -> 10 -> 5 -> 34 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 9, 16, 22 | 5 |
| 5 | 2, 5, 29, 48 | 4 |
| 6 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 7 | 7, 18, 28, 36, 44 | 5 |
| 10 | 4, 10, 24, 26, 35, 42, 45 | 7 |
| 12 | 11, 12, 15, 20, 33, 40, 46 | 7 |
| 13 | 13, 14, 21, 23, 25, 47 | 6 |
| 34 | 3, 34, 41 | 3 |
| 38 | 31, 38 | 2 |
| 39 | 32, 39 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 5 |
| 3 | 34 |
| 4 | 10 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 1 |
| 10 | 10 |
| 11 | 12 |
| 12 | 12 |
| 13 | 13 |
| 14 | 13 |
| 15 | 12 |
| 16 | 1 |
| 17 | 6 |
| 18 | 7 |
| 19 | 6 |
| 20 | 12 |
| 21 | 13 |
| 22 | 1 |
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
| 33 | 12 |
| 34 | 34 |
| 35 | 10 |
| 36 | 7 |
| 37 | 6 |
| 38 | 38 |
| 39 | 39 |
| 40 | 12 |
| 41 | 34 |
| 42 | 10 |
| 43 | 6 |
| 44 | 7 |
| 45 | 10 |
| 46 | 12 |
| 47 | 13 |
| 48 | 5 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.119429 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 48833.89333184296, "best_cost": 42856.86505378866}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
