# Résultat local_search - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 16.867
- Coût marche : 48.776
- Coût total : 65.644

## Stations choisies

1, 6, 7, 13, 14

## Cycle métro

1 -> 13 -> 7 -> 6 -> 14 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 8, 16 | 6 |
| 6 | 5, 6, 9, 11 | 4 |
| 7 | 7, 10 | 2 |
| 13 | 12, 13 | 2 |
| 14 | 14, 15 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 6 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 6 |
| 10 | 7 |
| 11 | 6 |
| 12 | 13 |
| 13 | 13 |
| 14 | 14 |
| 15 | 14 |
| 16 | 1 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.002601 s
- Graine : 2
- Détails : {"accepted_moves": 10, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 89.19171939152906, "best_cost": 65.64365345512392}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
