# Résultat local_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 304.676
- Coût marche : 746.774
- Coût total : 1051.450

## Stations choisies

1, 26, 31, 37, 42, 45, 52, 57, 67, 68

## Cycle métro

1 -> 31 -> 57 -> 26 -> 42 -> 68 -> 45 -> 67 -> 52 -> 37 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 16, 23, 36 | 4 |
| 26 | 7, 8, 19, 26, 28, 49, 55 | 7 |
| 31 | 13, 22, 29, 31, 35, 38, 59, 69, 70 | 9 |
| 37 | 37, 47, 50, 58 | 4 |
| 42 | 2, 3, 4, 6, 18, 32, 41, 42 | 8 |
| 45 | 25, 27, 39, 40, 45, 46, 61 | 7 |
| 52 | 5, 10, 12, 21, 34, 51, 52, 53, 60 | 9 |
| 57 | 15, 24, 57, 63, 66 | 5 |
| 67 | 11, 33, 48, 54, 56, 62, 64, 65, 67 | 9 |
| 68 | 9, 14, 17, 20, 30, 43, 44, 68 | 8 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 42 |
| 4 | 42 |
| 5 | 52 |
| 6 | 42 |
| 7 | 26 |
| 8 | 26 |
| 9 | 68 |
| 10 | 52 |
| 11 | 67 |
| 12 | 52 |
| 13 | 31 |
| 14 | 68 |
| 15 | 57 |
| 16 | 1 |
| 17 | 68 |
| 18 | 42 |
| 19 | 26 |
| 20 | 68 |
| 21 | 52 |
| 22 | 31 |
| 23 | 1 |
| 24 | 57 |
| 25 | 45 |
| 26 | 26 |
| 27 | 45 |
| 28 | 26 |
| 29 | 31 |
| 30 | 68 |
| 31 | 31 |
| 32 | 42 |
| 33 | 67 |
| 34 | 52 |
| 35 | 31 |
| 36 | 1 |
| 37 | 37 |
| 38 | 31 |
| 39 | 45 |
| 40 | 45 |
| 41 | 42 |
| 42 | 42 |
| 43 | 68 |
| 44 | 68 |
| 45 | 45 |
| 46 | 45 |
| 47 | 37 |
| 48 | 67 |
| 49 | 26 |
| 50 | 37 |
| 51 | 52 |
| 52 | 52 |
| 53 | 52 |
| 54 | 67 |
| 55 | 26 |
| 56 | 67 |
| 57 | 57 |
| 58 | 37 |
| 59 | 31 |
| 60 | 52 |
| 61 | 45 |
| 62 | 67 |
| 63 | 57 |
| 64 | 67 |
| 65 | 67 |
| 66 | 57 |
| 67 | 67 |
| 68 | 68 |
| 69 | 31 |
| 70 | 31 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.011521 s
- Graine : 0
- Détails : {"accepted_moves": 5, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 1105.8204001256327, "best_cost": 1051.449815229566}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
