# Résultat local_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 187.782
- Coût marche : 366.826
- Coût total : 554.608

## Stations choisies

1, 7, 8, 14, 15, 16, 19, 20, 30, 47

## Cycle métro

1 -> 8 -> 7 -> 14 -> 47 -> 19 -> 15 -> 30 -> 16 -> 20 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 22, 27, 32 | 4 |
| 7 | 7, 23, 43 | 3 |
| 8 | 8, 26, 28, 31, 48 | 5 |
| 14 | 6, 14, 24, 25 | 4 |
| 15 | 5, 15, 33, 37, 44, 45 | 6 |
| 16 | 2, 9, 11, 16, 21, 29, 38, 50 | 8 |
| 19 | 13, 19, 40, 41, 42 | 5 |
| 20 | 3, 20, 35, 36 | 4 |
| 30 | 10, 30, 34, 39, 49 | 5 |
| 47 | 4, 12, 17, 18, 46, 47, 51 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 20 |
| 4 | 47 |
| 5 | 15 |
| 6 | 14 |
| 7 | 7 |
| 8 | 8 |
| 9 | 16 |
| 10 | 30 |
| 11 | 16 |
| 12 | 47 |
| 13 | 19 |
| 14 | 14 |
| 15 | 15 |
| 16 | 16 |
| 17 | 47 |
| 18 | 47 |
| 19 | 19 |
| 20 | 20 |
| 21 | 16 |
| 22 | 1 |
| 23 | 7 |
| 24 | 14 |
| 25 | 14 |
| 26 | 8 |
| 27 | 1 |
| 28 | 8 |
| 29 | 16 |
| 30 | 30 |
| 31 | 8 |
| 32 | 1 |
| 33 | 15 |
| 34 | 30 |
| 35 | 20 |
| 36 | 20 |
| 37 | 15 |
| 38 | 16 |
| 39 | 30 |
| 40 | 19 |
| 41 | 19 |
| 42 | 19 |
| 43 | 7 |
| 44 | 15 |
| 45 | 15 |
| 46 | 47 |
| 47 | 47 |
| 48 | 8 |
| 49 | 30 |
| 50 | 16 |
| 51 | 47 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.010109 s
- Graine : 0
- Détails : {"accepted_moves": 8, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 630.4676373541728, "best_cost": 554.6079279854779}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
