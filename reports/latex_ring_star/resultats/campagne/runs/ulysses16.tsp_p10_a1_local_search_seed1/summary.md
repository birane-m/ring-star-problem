# Résultat local_search - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 27.839
- Coût marche : 36.066
- Coût total : 63.905

## Stations choisies

1, 6, 7, 8, 9, 10, 12, 13, 14, 16

## Cycle métro

1 -> 8 -> 14 -> 7 -> 6 -> 9 -> 10 -> 12 -> 13 -> 16 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3 | 3 |
| 6 | 5, 6 | 2 |
| 7 | 7 | 1 |
| 8 | 4, 8 | 2 |
| 9 | 9, 11 | 2 |
| 10 | 10 | 1 |
| 12 | 12 | 1 |
| 13 | 13 | 1 |
| 14 | 14, 15 | 2 |
| 16 | 16 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 8 |
| 5 | 6 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |
| 11 | 9 |
| 12 | 12 |
| 13 | 13 |
| 14 | 14 |
| 15 | 14 |
| 16 | 16 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.004649 s
- Graine : 1
- Détails : {"accepted_moves": 6, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 76.43541565372277, "best_cost": 63.90518435789723}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
