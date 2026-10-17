# Résultat local_search - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 32.465
- Coût marche : 30.677
- Coût total : 63.143

## Stations choisies

1, 2, 3, 4, 6, 7, 12, 13, 15, 16

## Cycle métro

1 -> 16 -> 13 -> 12 -> 7 -> 6 -> 15 -> 4 -> 2 -> 3 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8 | 2 |
| 2 | 2 | 1 |
| 3 | 3 | 1 |
| 4 | 4 | 1 |
| 6 | 6, 9, 11 | 3 |
| 7 | 7, 10 | 2 |
| 12 | 12 | 1 |
| 13 | 13, 14 | 2 |
| 15 | 5, 15 | 2 |
| 16 | 16 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 15 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 6 |
| 10 | 7 |
| 11 | 6 |
| 12 | 12 |
| 13 | 13 |
| 14 | 13 |
| 15 | 15 |
| 16 | 16 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.004541 s
- Graine : 2
- Détails : {"accepted_moves": 9, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 76.43541565372277, "best_cost": 63.142788514252274}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
