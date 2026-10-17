# Résultat tabu_search - kroA100

- Instance : kroA100
- Nombre de points : 100
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 7064.802
- Coût marche : 51422.799
- Coût total : 58487.601

## Stations choisies

1, 15, 39, 53, 57

## Cycle métro

1 -> 53 -> 15 -> 57 -> 39 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 6, 8, 28, 31, 42, 47, 49, 56, 58, 63, 67, 80, 89, 92, 93 | 16 |
| 15 | 11, 15, 17, 21, 23, 32, 36, 45, 59, 72, 74, 91, 98 | 13 |
| 39 | 2, 3, 5, 13, 14, 29, 30, 33, 37, 39, 40, 41, 44, 48, 50, 52, 54, 64, 68, 71, 73, 76, 78, 82, 85, 95, 96, 100 | 28 |
| 53 | 4, 10, 16, 18, 19, 22, 24, 26, 38, 53, 65, 66, 70, 75, 79, 84, 88, 90, 94, 97, 99 | 21 |
| 57 | 7, 9, 12, 20, 25, 27, 34, 35, 43, 46, 51, 55, 57, 60, 61, 62, 69, 77, 81, 83, 86, 87 | 22 |

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
| 10 | 53 |
| 11 | 15 |
| 12 | 57 |
| 13 | 39 |
| 14 | 39 |
| 15 | 15 |
| 16 | 53 |
| 17 | 15 |
| 18 | 53 |
| 19 | 53 |
| 20 | 57 |
| 21 | 15 |
| 22 | 53 |
| 23 | 15 |
| 24 | 53 |
| 25 | 57 |
| 26 | 53 |
| 27 | 57 |
| 28 | 1 |
| 29 | 39 |
| 30 | 39 |
| 31 | 1 |
| 32 | 15 |
| 33 | 39 |
| 34 | 57 |
| 35 | 57 |
| 36 | 15 |
| 37 | 39 |
| 38 | 53 |
| 39 | 39 |
| 40 | 39 |
| 41 | 39 |
| 42 | 1 |
| 43 | 57 |
| 44 | 39 |
| 45 | 15 |
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
| 59 | 15 |
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
| 72 | 15 |
| 73 | 39 |
| 74 | 15 |
| 75 | 53 |
| 76 | 39 |
| 77 | 57 |
| 78 | 39 |
| 79 | 53 |
| 80 | 1 |
| 81 | 57 |
| 82 | 39 |
| 83 | 57 |
| 84 | 53 |
| 85 | 39 |
| 86 | 57 |
| 87 | 57 |
| 88 | 53 |
| 89 | 1 |
| 90 | 53 |
| 91 | 15 |
| 92 | 1 |
| 93 | 1 |
| 94 | 53 |
| 95 | 39 |
| 96 | 39 |
| 97 | 53 |
| 98 | 15 |
| 99 | 53 |
| 100 | 39 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.118388 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 68427.56868588035, "best_cost": 58487.601062018024}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
