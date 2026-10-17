# Résultat local_search - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 35.688
- Coût marche : 30.101
- Coût total : 65.789

## Stations choisies

1, 4, 6, 9, 13, 15, 17, 19, 21, 22

## Cycle métro

1 -> 22 -> 17 -> 4 -> 15 -> 6 -> 9 -> 19 -> 21 -> 13 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 16 | 3 |
| 4 | 4, 18 | 2 |
| 6 | 6, 7 | 2 |
| 9 | 9, 11 | 2 |
| 13 | 12, 13, 14 | 3 |
| 15 | 5, 15 | 2 |
| 17 | 2, 3, 17 | 3 |
| 19 | 10, 19 | 2 |
| 21 | 20, 21 | 2 |
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
| 9 | 9 |
| 10 | 19 |
| 11 | 9 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 15 |
| 16 | 1 |
| 17 | 17 |
| 18 | 4 |
| 19 | 19 |
| 20 | 21 |
| 21 | 21 |
| 22 | 22 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.006774 s
- Graine : 2
- Détails : {"accepted_moves": 14, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 82.35756523562077, "best_cost": 65.78923975194607}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
