# Résultat tabu_search - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 29.686
- Coût marche : 35.635
- Coût total : 65.321

## Stations choisies

1, 6, 7, 13, 15, 17, 18, 19, 20, 22

## Cycle métro

1 -> 22 -> 17 -> 18 -> 15 -> 6 -> 7 -> 19 -> 20 -> 13 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 16 | 3 |
| 6 | 6, 11 | 2 |
| 7 | 7 | 1 |
| 13 | 12, 13, 14 | 3 |
| 15 | 5, 15 | 2 |
| 17 | 2, 3, 17 | 3 |
| 18 | 4, 18 | 2 |
| 19 | 9, 10, 19 | 3 |
| 20 | 20, 21 | 2 |
| 22 | 22 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 17 |
| 3 | 17 |
| 4 | 18 |
| 5 | 15 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 19 |
| 10 | 19 |
| 11 | 6 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 15 |
| 16 | 1 |
| 17 | 17 |
| 18 | 18 |
| 19 | 19 |
| 20 | 20 |
| 21 | 20 |
| 22 | 22 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.104904 s
- Graine : 2
- Détails : {"performed_moves": 98, "tabu_tenure": 10, "candidates_per_iteration": 15, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 1500, "stop_reason": "iteration_budget", "initial_cost": 82.35756523562077, "best_cost": 65.32138320949014}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
