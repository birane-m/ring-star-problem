# Résultat tabu_search - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 14.639
- Coût marche : 53.634
- Coût total : 68.273

## Stations choisies

1, 7, 13

## Cycle métro

1 -> 13 -> 7 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 8, 16 | 6 |
| 7 | 5, 6, 7, 9, 10, 11 | 6 |
| 13 | 12, 13, 14, 15 | 4 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 7 |
| 6 | 7 |
| 7 | 7 |
| 8 | 1 |
| 9 | 7 |
| 10 | 7 |
| 11 | 7 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 13 |
| 16 | 1 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.020987 s
- Graine : 0
- Détails : {"performed_moves": 100, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 113.30673824011149, "best_cost": 68.2731464941567}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
