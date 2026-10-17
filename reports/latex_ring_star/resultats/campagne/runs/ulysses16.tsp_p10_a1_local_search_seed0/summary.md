# Résultat local_search - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 38.893
- Coût marche : 24.807
- Coût total : 63.700

## Stations choisies

1, 2, 4, 6, 7, 8, 9, 10, 13, 16

## Cycle métro

1 -> 16 -> 10 -> 9 -> 6 -> 7 -> 13 -> 8 -> 4 -> 2 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1 | 1 |
| 2 | 2, 3 | 2 |
| 4 | 4 | 1 |
| 6 | 5, 6 | 2 |
| 7 | 7 | 1 |
| 8 | 8 | 1 |
| 9 | 9, 11 | 2 |
| 10 | 10 | 1 |
| 13 | 12, 13, 14, 15 | 4 |
| 16 | 16 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 2 |
| 4 | 4 |
| 5 | 6 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |
| 11 | 9 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 13 |
| 16 | 16 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.004583 s
- Graine : 0
- Détails : {"accepted_moves": 12, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 76.43541565372277, "best_cost": 63.69970950001921}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
