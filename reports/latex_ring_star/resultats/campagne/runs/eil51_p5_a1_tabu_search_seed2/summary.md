# Résultat tabu_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 134.457
- Coût marche : 565.639
- Coût total : 700.096

## Stations choisies

1, 3, 9, 17, 23

## Cycle métro

1 -> 3 -> 9 -> 17 -> 23 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 8, 11, 22, 27, 32, 46, 51 | 9 |
| 3 | 3, 20, 28, 31, 35, 36 | 6 |
| 9 | 5, 9, 10, 16, 21, 29, 30, 34, 38, 39, 49, 50 | 12 |
| 17 | 4, 12, 13, 15, 17, 18, 19, 33, 37, 40, 41, 42, 44, 45, 47 | 15 |
| 23 | 6, 7, 14, 23, 24, 25, 26, 43, 48 | 9 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 3 |
| 4 | 17 |
| 5 | 9 |
| 6 | 23 |
| 7 | 23 |
| 8 | 1 |
| 9 | 9 |
| 10 | 9 |
| 11 | 1 |
| 12 | 17 |
| 13 | 17 |
| 14 | 23 |
| 15 | 17 |
| 16 | 9 |
| 17 | 17 |
| 18 | 17 |
| 19 | 17 |
| 20 | 3 |
| 21 | 9 |
| 22 | 1 |
| 23 | 23 |
| 24 | 23 |
| 25 | 23 |
| 26 | 23 |
| 27 | 1 |
| 28 | 3 |
| 29 | 9 |
| 30 | 9 |
| 31 | 3 |
| 32 | 1 |
| 33 | 17 |
| 34 | 9 |
| 35 | 3 |
| 36 | 3 |
| 37 | 17 |
| 38 | 9 |
| 39 | 9 |
| 40 | 17 |
| 41 | 17 |
| 42 | 17 |
| 43 | 23 |
| 44 | 17 |
| 45 | 17 |
| 46 | 1 |
| 47 | 17 |
| 48 | 23 |
| 49 | 9 |
| 50 | 9 |
| 51 | 1 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.068379 s
- Graine : 2
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 735.0003807891881, "best_cost": 700.0963574804023}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
