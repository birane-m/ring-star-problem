# Résultat local_search - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 3
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 15.834
- Coût marche : 67.305
- Coût total : 83.138

## Stations choisies

1, 14, 19

## Cycle métro

1 -> 14 -> 19 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 8, 16, 17, 18, 22 | 9 |
| 14 | 5, 6, 12, 13, 14, 15 | 6 |
| 19 | 7, 9, 10, 11, 19, 20, 21 | 7 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 14 |
| 6 | 14 |
| 7 | 19 |
| 8 | 1 |
| 9 | 19 |
| 10 | 19 |
| 11 | 19 |
| 12 | 14 |
| 13 | 14 |
| 14 | 14 |
| 15 | 14 |
| 16 | 1 |
| 17 | 1 |
| 18 | 1 |
| 19 | 19 |
| 20 | 19 |
| 21 | 19 |
| 22 | 1 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.002168 s
- Graine : 1
- Détails : {"accepted_moves": 4, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 137.72086211084414, "best_cost": 83.13821247269269}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
