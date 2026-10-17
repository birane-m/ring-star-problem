# Résultat tabu_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 293.185
- Coût marche : 708.722
- Coût total : 1001.908

## Stations choisies

1, 5, 26, 33, 40, 42, 56, 57, 68, 69

## Cycle métro

1 -> 69 -> 57 -> 26 -> 42 -> 68 -> 40 -> 33 -> 56 -> 5 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 16, 23, 36, 47 | 5 |
| 5 | 5, 10, 37, 50, 52, 53, 58 | 7 |
| 26 | 7, 8, 19, 26, 28, 49, 55 | 7 |
| 33 | 12, 21, 33, 34, 54, 60, 62 | 7 |
| 40 | 9, 25, 27, 39, 40, 45, 46, 61 | 8 |
| 42 | 2, 3, 4, 6, 18, 32, 41, 42 | 8 |
| 56 | 11, 48, 51, 56, 64, 65, 67 | 7 |
| 57 | 15, 24, 57, 63, 66 | 5 |
| 68 | 14, 17, 20, 30, 43, 44, 68 | 7 |
| 69 | 13, 22, 29, 31, 35, 38, 59, 69, 70 | 9 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 42 |
| 4 | 42 |
| 5 | 5 |
| 6 | 42 |
| 7 | 26 |
| 8 | 26 |
| 9 | 40 |
| 10 | 5 |
| 11 | 56 |
| 12 | 33 |
| 13 | 69 |
| 14 | 68 |
| 15 | 57 |
| 16 | 1 |
| 17 | 68 |
| 18 | 42 |
| 19 | 26 |
| 20 | 68 |
| 21 | 33 |
| 22 | 69 |
| 23 | 1 |
| 24 | 57 |
| 25 | 40 |
| 26 | 26 |
| 27 | 40 |
| 28 | 26 |
| 29 | 69 |
| 30 | 68 |
| 31 | 69 |
| 32 | 42 |
| 33 | 33 |
| 34 | 33 |
| 35 | 69 |
| 36 | 1 |
| 37 | 5 |
| 38 | 69 |
| 39 | 40 |
| 40 | 40 |
| 41 | 42 |
| 42 | 42 |
| 43 | 68 |
| 44 | 68 |
| 45 | 40 |
| 46 | 40 |
| 47 | 1 |
| 48 | 56 |
| 49 | 26 |
| 50 | 5 |
| 51 | 56 |
| 52 | 5 |
| 53 | 5 |
| 54 | 33 |
| 55 | 26 |
| 56 | 56 |
| 57 | 57 |
| 58 | 5 |
| 59 | 69 |
| 60 | 33 |
| 61 | 40 |
| 62 | 33 |
| 63 | 57 |
| 64 | 56 |
| 65 | 56 |
| 66 | 57 |
| 67 | 56 |
| 68 | 68 |
| 69 | 69 |
| 70 | 69 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.148761 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 1105.8204001256327, "best_cost": 1001.9075878489139}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
