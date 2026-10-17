# Résultat local_search - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 2304.799
- Coût marche : 9677.532
- Coût total : 11982.331

## Stations choisies

1, 5, 23, 28, 41

## Cycle métro

1 -> 23 -> 28 -> 5 -> 41 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 18, 22, 31, 32, 34, 35, 36, 44, 49 | 10 |
| 5 | 4, 5, 6, 15, 24, 25, 33, 37, 38, 39, 40, 43, 46, 48 | 14 |
| 23 | 2, 7, 16, 17, 20, 21, 23, 29, 30, 42, 50 | 11 |
| 28 | 11, 12, 13, 14, 26, 27, 28, 47, 51, 52 | 10 |
| 41 | 3, 8, 9, 10, 19, 41, 45 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 23 |
| 3 | 41 |
| 4 | 5 |
| 5 | 5 |
| 6 | 5 |
| 7 | 23 |
| 8 | 41 |
| 9 | 41 |
| 10 | 41 |
| 11 | 28 |
| 12 | 28 |
| 13 | 28 |
| 14 | 28 |
| 15 | 5 |
| 16 | 23 |
| 17 | 23 |
| 18 | 1 |
| 19 | 41 |
| 20 | 23 |
| 21 | 23 |
| 22 | 1 |
| 23 | 23 |
| 24 | 5 |
| 25 | 5 |
| 26 | 28 |
| 27 | 28 |
| 28 | 28 |
| 29 | 23 |
| 30 | 23 |
| 31 | 1 |
| 32 | 1 |
| 33 | 5 |
| 34 | 1 |
| 35 | 1 |
| 36 | 1 |
| 37 | 5 |
| 38 | 5 |
| 39 | 5 |
| 40 | 5 |
| 41 | 41 |
| 42 | 23 |
| 43 | 5 |
| 44 | 1 |
| 45 | 41 |
| 46 | 5 |
| 47 | 28 |
| 48 | 5 |
| 49 | 1 |
| 50 | 23 |
| 51 | 28 |
| 52 | 28 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005805 s
- Graine : 1
- Détails : {"accepted_moves": 7, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 14916.735925839565, "best_cost": 11982.330928066634}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
