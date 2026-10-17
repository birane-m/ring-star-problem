# Résultat local_search - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 24.379
- Coût marche : 49.095
- Coût total : 73.474

## Stations choisies

1, 4, 6, 14, 20

## Cycle métro

1 -> 4 -> 14 -> 6 -> 20 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 16 | 3 |
| 4 | 2, 3, 4, 17, 18, 22 | 6 |
| 6 | 5, 6, 7, 9, 11 | 5 |
| 14 | 12, 13, 14, 15 | 4 |
| 20 | 10, 19, 20, 21 | 4 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 4 |
| 3 | 4 |
| 4 | 4 |
| 5 | 6 |
| 6 | 6 |
| 7 | 6 |
| 8 | 1 |
| 9 | 6 |
| 10 | 20 |
| 11 | 6 |
| 12 | 14 |
| 13 | 14 |
| 14 | 14 |
| 15 | 14 |
| 16 | 1 |
| 17 | 4 |
| 18 | 4 |
| 19 | 20 |
| 20 | 20 |
| 21 | 20 |
| 22 | 4 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.002751 s
- Graine : 0
- Détails : {"accepted_moves": 8, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 108.79469090767878, "best_cost": 73.47381814370546}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
