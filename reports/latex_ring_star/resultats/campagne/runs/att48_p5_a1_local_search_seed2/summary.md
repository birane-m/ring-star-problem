# Résultat local_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 14876.569
- Coût marche : 41282.312
- Coût total : 56158.881

## Stations choisies

1, 13, 18, 27, 42

## Cycle métro

1 -> 18 -> 27 -> 13 -> 42 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 15, 16, 22, 38, 40, 41 | 10 |
| 13 | 11, 12, 13, 14, 20, 21, 23, 25, 32, 34, 39, 47 | 12 |
| 18 | 7, 18, 28, 31, 33, 36, 44, 46 | 8 |
| 27 | 6, 17, 19, 27, 30, 37, 43 | 7 |
| 42 | 2, 4, 5, 10, 24, 26, 29, 35, 42, 45, 48 | 11 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 1 |
| 4 | 42 |
| 5 | 42 |
| 6 | 27 |
| 7 | 18 |
| 8 | 1 |
| 9 | 1 |
| 10 | 42 |
| 11 | 13 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 1 |
| 16 | 1 |
| 17 | 27 |
| 18 | 18 |
| 19 | 27 |
| 20 | 13 |
| 21 | 13 |
| 22 | 1 |
| 23 | 13 |
| 24 | 42 |
| 25 | 13 |
| 26 | 42 |
| 27 | 27 |
| 28 | 18 |
| 29 | 42 |
| 30 | 27 |
| 31 | 18 |
| 32 | 13 |
| 33 | 18 |
| 34 | 13 |
| 35 | 42 |
| 36 | 18 |
| 37 | 27 |
| 38 | 1 |
| 39 | 13 |
| 40 | 1 |
| 41 | 1 |
| 42 | 42 |
| 43 | 27 |
| 44 | 18 |
| 45 | 42 |
| 46 | 18 |
| 47 | 13 |
| 48 | 42 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005138 s
- Graine : 2
- Détails : {"accepted_moves": 6, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 63668.04323160226, "best_cost": 56158.88061370139}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
