# Résultat tabu_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 174.162
- Coût marche : 382.484
- Coût total : 556.646

## Stations choisies

1, 3, 4, 15, 16, 19, 23, 25, 27, 49

## Cycle métro

1 -> 27 -> 23 -> 25 -> 4 -> 19 -> 15 -> 49 -> 16 -> 3 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 22, 32 | 4 |
| 3 | 3, 20, 28, 31, 35, 36 | 6 |
| 4 | 4, 12, 17, 18, 47 | 5 |
| 15 | 15, 33, 37, 44, 45 | 5 |
| 16 | 2, 11, 16, 21, 29, 34, 50 | 7 |
| 19 | 19, 40, 41, 42 | 4 |
| 23 | 7, 23, 24, 26, 43 | 5 |
| 25 | 13, 14, 25 | 3 |
| 27 | 6, 27, 46, 48, 51 | 5 |
| 49 | 5, 9, 10, 30, 38, 39, 49 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 3 |
| 4 | 4 |
| 5 | 49 |
| 6 | 27 |
| 7 | 23 |
| 8 | 1 |
| 9 | 49 |
| 10 | 49 |
| 11 | 16 |
| 12 | 4 |
| 13 | 25 |
| 14 | 25 |
| 15 | 15 |
| 16 | 16 |
| 17 | 4 |
| 18 | 4 |
| 19 | 19 |
| 20 | 3 |
| 21 | 16 |
| 22 | 1 |
| 23 | 23 |
| 24 | 23 |
| 25 | 25 |
| 26 | 23 |
| 27 | 27 |
| 28 | 3 |
| 29 | 16 |
| 30 | 49 |
| 31 | 3 |
| 32 | 1 |
| 33 | 15 |
| 34 | 16 |
| 35 | 3 |
| 36 | 3 |
| 37 | 15 |
| 38 | 49 |
| 39 | 49 |
| 40 | 19 |
| 41 | 19 |
| 42 | 19 |
| 43 | 23 |
| 44 | 15 |
| 45 | 15 |
| 46 | 27 |
| 47 | 4 |
| 48 | 27 |
| 49 | 49 |
| 50 | 16 |
| 51 | 27 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.117645 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 630.4676373541728, "best_cost": 556.6460813744685}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
