# Résultat tabu_search - kroA100

- Instance : kroA100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 7003.014
- Coût marche : 51366.521
- Coût total : 58369.535

## Stations choisies

1, 39, 53, 57, 74

## Cycle métro

1 -> 53 -> 74 -> 57 -> 39 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 6, 8, 28, 31, 42, 47, 49, 56, 58, 63, 67, 80, 89, 92, 93, 98 | 17 |
| 39 | 2, 3, 5, 13, 14, 29, 30, 33, 37, 39, 40, 41, 44, 48, 50, 52, 54, 64, 68, 71, 73, 76, 78, 82, 85, 95, 96, 100 | 28 |
| 53 | 4, 16, 18, 19, 22, 24, 26, 53, 65, 66, 70, 75, 79, 88, 90, 94, 97 | 17 |
| 57 | 7, 9, 12, 20, 23, 25, 27, 34, 35, 43, 46, 51, 55, 57, 60, 61, 62, 69, 77, 81, 83, 86, 87 | 23 |
| 74 | 10, 11, 15, 17, 21, 32, 36, 38, 45, 59, 72, 74, 84, 91, 99 | 15 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 39 |
| 3 | 39 |
| 4 | 53 |
| 5 | 39 |
| 6 | 1 |
| 7 | 57 |
| 8 | 1 |
| 9 | 57 |
| 10 | 74 |
| 11 | 74 |
| 12 | 57 |
| 13 | 39 |
| 14 | 39 |
| 15 | 74 |
| 16 | 53 |
| 17 | 74 |
| 18 | 53 |
| 19 | 53 |
| 20 | 57 |
| 21 | 74 |
| 22 | 53 |
| 23 | 57 |
| 24 | 53 |
| 25 | 57 |
| 26 | 53 |
| 27 | 57 |
| 28 | 1 |
| 29 | 39 |
| 30 | 39 |
| 31 | 1 |
| 32 | 74 |
| 33 | 39 |
| 34 | 57 |
| 35 | 57 |
| 36 | 74 |
| 37 | 39 |
| 38 | 74 |
| 39 | 39 |
| 40 | 39 |
| 41 | 39 |
| 42 | 1 |
| 43 | 57 |
| 44 | 39 |
| 45 | 74 |
| 46 | 57 |
| 47 | 1 |
| 48 | 39 |
| 49 | 1 |
| 50 | 39 |
| 51 | 57 |
| 52 | 39 |
| 53 | 53 |
| 54 | 39 |
| 55 | 57 |
| 56 | 1 |
| 57 | 57 |
| 58 | 1 |
| 59 | 74 |
| 60 | 57 |
| 61 | 57 |
| 62 | 57 |
| 63 | 1 |
| 64 | 39 |
| 65 | 53 |
| 66 | 53 |
| 67 | 1 |
| 68 | 39 |
| 69 | 57 |
| 70 | 53 |
| 71 | 39 |
| 72 | 74 |
| 73 | 39 |
| 74 | 74 |
| 75 | 53 |
| 76 | 39 |
| 77 | 57 |
| 78 | 39 |
| 79 | 53 |
| 80 | 1 |
| 81 | 57 |
| 82 | 39 |
| 83 | 57 |
| 84 | 74 |
| 85 | 39 |
| 86 | 57 |
| 87 | 57 |
| 88 | 53 |
| 89 | 1 |
| 90 | 53 |
| 91 | 74 |
| 92 | 1 |
| 93 | 1 |
| 94 | 53 |
| 95 | 39 |
| 96 | 39 |
| 97 | 53 |
| 98 | 1 |
| 99 | 74 |
| 100 | 39 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.117202 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 68427.56868588035, "best_cost": 58369.534762261625}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
