# Résultat tabu_search - att48

- Instance : att48
- Nombre de points : 48
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : ATT

## Coûts

- Coût métro : 14188.458
- Coût marche : 41220.179
- Coût total : 55408.636

## Stations choisies

1, 13, 30, 42, 46

## Cycle métro

1 -> 46 -> 30 -> 13 -> 42 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 9, 16, 22, 40, 41 | 8 |
| 13 | 11, 13, 14, 21, 23, 25, 32, 34, 39, 47 | 10 |
| 30 | 6, 7, 17, 19, 27, 28, 30, 36, 37, 43 | 10 |
| 42 | 2, 4, 5, 10, 24, 26, 29, 35, 42, 45, 48 | 11 |
| 46 | 12, 15, 18, 20, 31, 33, 38, 44, 46 | 9 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 1 |
| 4 | 42 |
| 5 | 42 |
| 6 | 30 |
| 7 | 30 |
| 8 | 1 |
| 9 | 1 |
| 10 | 42 |
| 11 | 13 |
| 12 | 46 |
| 13 | 13 |
| 14 | 13 |
| 15 | 46 |
| 16 | 1 |
| 17 | 30 |
| 18 | 46 |
| 19 | 30 |
| 20 | 46 |
| 21 | 13 |
| 22 | 1 |
| 23 | 13 |
| 24 | 42 |
| 25 | 13 |
| 26 | 42 |
| 27 | 30 |
| 28 | 30 |
| 29 | 42 |
| 30 | 30 |
| 31 | 46 |
| 32 | 13 |
| 33 | 46 |
| 34 | 13 |
| 35 | 42 |
| 36 | 30 |
| 37 | 30 |
| 38 | 46 |
| 39 | 13 |
| 40 | 1 |
| 41 | 1 |
| 42 | 42 |
| 43 | 30 |
| 44 | 46 |
| 45 | 42 |
| 46 | 46 |
| 47 | 13 |
| 48 | 42 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.062852 s
- Graine : 1
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 63668.04323160226, "best_cost": 55408.63622165777}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
