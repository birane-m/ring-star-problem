# Résultat local_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 119.265
- Coût marche : 584.179
- Coût total : 703.443

## Stations choisies

1, 4, 9, 15, 23

## Cycle métro

1 -> 23 -> 4 -> 15 -> 9 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 8, 11, 20, 22, 27, 28, 31, 32, 35, 36, 46, 51 | 15 |
| 4 | 4, 12, 13, 17, 18, 19, 25, 40, 41, 42, 47 | 11 |
| 9 | 5, 9, 10, 16, 21, 29, 30, 34, 38, 39, 49, 50 | 12 |
| 15 | 15, 33, 37, 44, 45 | 5 |
| 23 | 6, 7, 14, 23, 24, 26, 43, 48 | 8 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 4 |
| 5 | 9 |
| 6 | 23 |
| 7 | 23 |
| 8 | 1 |
| 9 | 9 |
| 10 | 9 |
| 11 | 1 |
| 12 | 4 |
| 13 | 4 |
| 14 | 23 |
| 15 | 15 |
| 16 | 9 |
| 17 | 4 |
| 18 | 4 |
| 19 | 4 |
| 20 | 1 |
| 21 | 9 |
| 22 | 1 |
| 23 | 23 |
| 24 | 23 |
| 25 | 4 |
| 26 | 23 |
| 27 | 1 |
| 28 | 1 |
| 29 | 9 |
| 30 | 9 |
| 31 | 1 |
| 32 | 1 |
| 33 | 15 |
| 34 | 9 |
| 35 | 1 |
| 36 | 1 |
| 37 | 15 |
| 38 | 9 |
| 39 | 9 |
| 40 | 4 |
| 41 | 4 |
| 42 | 4 |
| 43 | 23 |
| 44 | 15 |
| 45 | 15 |
| 46 | 1 |
| 47 | 4 |
| 48 | 23 |
| 49 | 9 |
| 50 | 9 |
| 51 | 1 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005085 s
- Graine : 1
- Détails : {"accepted_moves": 4, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 735.0003807891881, "best_cost": 703.4434495171793}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
