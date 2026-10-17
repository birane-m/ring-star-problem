# Résultat local_search - eil51

- Instance : eil51
- Nombre de points : 51
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 119.995
- Coût marche : 589.237
- Coût total : 709.232

## Stations choisies

1, 4, 15, 16, 23

## Cycle métro

1 -> 16 -> 15 -> 4 -> 23 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 8, 22, 27, 28, 31, 32, 46, 51 | 10 |
| 4 | 4, 12, 13, 17, 18, 19, 25, 40, 41, 42, 47 | 11 |
| 15 | 5, 10, 15, 33, 37, 39, 44, 45 | 8 |
| 16 | 2, 9, 11, 16, 20, 21, 29, 30, 34, 35, 36, 38, 49, 50 | 14 |
| 23 | 6, 7, 14, 23, 24, 26, 43, 48 | 8 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 16 |
| 3 | 1 |
| 4 | 4 |
| 5 | 15 |
| 6 | 23 |
| 7 | 23 |
| 8 | 1 |
| 9 | 16 |
| 10 | 15 |
| 11 | 16 |
| 12 | 4 |
| 13 | 4 |
| 14 | 23 |
| 15 | 15 |
| 16 | 16 |
| 17 | 4 |
| 18 | 4 |
| 19 | 4 |
| 20 | 16 |
| 21 | 16 |
| 22 | 1 |
| 23 | 23 |
| 24 | 23 |
| 25 | 4 |
| 26 | 23 |
| 27 | 1 |
| 28 | 1 |
| 29 | 16 |
| 30 | 16 |
| 31 | 1 |
| 32 | 1 |
| 33 | 15 |
| 34 | 16 |
| 35 | 16 |
| 36 | 16 |
| 37 | 15 |
| 38 | 16 |
| 39 | 15 |
| 40 | 4 |
| 41 | 4 |
| 42 | 4 |
| 43 | 23 |
| 44 | 15 |
| 45 | 15 |
| 46 | 1 |
| 47 | 4 |
| 48 | 23 |
| 49 | 16 |
| 50 | 16 |
| 51 | 1 |

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.005645 s
- Graine : 0
- Détails : {"accepted_moves": 3, "iterations": 100, "iteration_budget": 100, "evaluated_moves": 100, "stop_reason": "iteration_budget", "initial_cost": 735.0003807891881, "best_cost": 709.2315896028332}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
