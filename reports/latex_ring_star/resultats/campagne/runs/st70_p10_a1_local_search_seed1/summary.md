# Résultat local_search - st70

- Instance : st70
- Nombre de points : 70
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 318.604
- Coût marche : 773.114
- Coût total : 1091.718

## Stations choisies

1, 12, 26, 32, 43, 45, 53, 57, 67, 69

## Cycle métro

1 -> 69 -> 57 -> 26 -> 32 -> 43 -> 45 -> 67 -> 12 -> 53 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 16, 23, 36, 37, 47 | 6 |
| 12 | 12, 21, 33, 34, 52, 60 | 6 |
| 26 | 8, 19, 26, 28, 49, 55 | 6 |
| 32 | 2, 3, 4, 7, 14, 18, 20, 30, 32, 42 | 10 |
| 43 | 6, 9, 17, 41, 43, 44, 68 | 7 |
| 45 | 25, 27, 39, 40, 45, 46, 61 | 7 |
| 53 | 5, 10, 50, 53, 58 | 5 |
| 57 | 15, 24, 57, 63, 66 | 5 |
| 67 | 11, 48, 51, 54, 56, 62, 64, 65, 67 | 9 |
| 69 | 13, 22, 29, 31, 35, 38, 59, 69, 70 | 9 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 32 |
| 3 | 32 |
| 4 | 32 |
| 5 | 53 |
| 6 | 43 |
| 7 | 32 |
| 8 | 26 |
| 9 | 43 |
| 10 | 53 |
| 11 | 67 |
| 12 | 12 |
| 13 | 69 |
| 14 | 32 |
| 15 | 57 |
| 16 | 1 |
| 17 | 43 |
| 18 | 32 |
| 19 | 26 |
| 20 | 32 |
| 21 | 12 |
| 22 | 69 |
| 23 | 1 |
| 24 | 57 |
| 25 | 45 |
| 26 | 26 |
| 27 | 45 |
| 28 | 26 |
| 29 | 69 |
| 30 | 32 |
| 31 | 69 |
| 32 | 32 |
| 33 | 12 |
| 34 | 12 |
| 35 | 69 |
| 36 | 1 |
| 37 | 1 |
| 38 | 69 |
| 39 | 45 |
| 40 | 45 |
| 41 | 43 |
| 42 | 32 |
| 43 | 43 |
| 44 | 43 |
| 45 | 45 |
| 46 | 45 |
| 47 | 1 |
| 48 | 67 |
| 49 | 26 |
| 50 | 53 |
| 51 | 67 |
| 52 | 12 |
| 53 | 53 |
| 54 | 67 |
| 55 | 26 |
| 56 | 67 |
| 57 | 57 |
| 58 | 53 |
| 59 | 69 |
| 60 | 12 |
| 61 | 45 |
| 62 | 67 |
| 63 | 57 |
| 64 | 67 |
| 65 | 67 |
| 66 | 57 |
| 67 | 67 |
| 68 | 43 |
| 69 | 69 |
| 70 | 69 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.012562 s
- Graine : 1
- Détails : {"accepted_moves": 4, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 1105.8204001256327, "best_cost": 1091.7181155119472}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
