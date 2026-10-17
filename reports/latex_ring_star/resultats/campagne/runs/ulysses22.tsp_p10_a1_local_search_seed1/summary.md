# Résultat local_search - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 31.506
- Coût marche : 34.588
- Coût total : 66.094

## Stations choisies

1, 4, 6, 10, 13, 15, 16, 17, 20, 22

## Cycle métro

1 -> 22 -> 17 -> 4 -> 15 -> 6 -> 10 -> 20 -> 13 -> 16 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8 | 2 |
| 4 | 4, 18 | 2 |
| 6 | 6, 7, 11 | 3 |
| 10 | 9, 10 | 2 |
| 13 | 12, 13, 14 | 3 |
| 15 | 5, 15 | 2 |
| 16 | 16 | 1 |
| 17 | 2, 3, 17 | 3 |
| 20 | 19, 20, 21 | 3 |
| 22 | 22 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 17 |
| 3 | 17 |
| 4 | 4 |
| 5 | 15 |
| 6 | 6 |
| 7 | 6 |
| 8 | 1 |
| 9 | 10 |
| 10 | 10 |
| 11 | 6 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 15 |
| 16 | 16 |
| 17 | 17 |
| 18 | 4 |
| 19 | 20 |
| 20 | 20 |
| 21 | 20 |
| 22 | 22 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.006745 s
- Graine : 1
- Détails : {"accepted_moves": 7, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 82.35756523562077, "best_cost": 66.09415158730476}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
