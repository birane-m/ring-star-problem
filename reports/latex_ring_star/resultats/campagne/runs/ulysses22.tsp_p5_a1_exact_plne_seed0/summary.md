# Résultat exact_plne - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 22.616
- Coût marche : 48.955
- Coût total : 71.571

## Stations choisies

1, 6, 14, 20, 22

## Cycle métro

1 -> 20 -> 6 -> 14 -> 22 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8, 16 | 3 |
| 6 | 5, 6, 7, 9, 11 | 5 |
| 14 | 12, 13, 14, 15 | 4 |
| 20 | 10, 19, 20, 21 | 4 |
| 22 | 2, 3, 4, 17, 18, 22 | 6 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 22 |
| 3 | 22 |
| 4 | 22 |
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
| 17 | 22 |
| 18 | 22 |
| 19 | 20 |
| 20 | 20 |
| 21 | 20 |
| 22 | 22 |

## Visualisation

figures/solution.png

## Exécution

- Statut : feasible_time_limited
- Optimalité prouvée : False
- Temps de calcul : 5.017606 s
- Graine : 0
- Détails : {"solver": "CBC"}
- Borne inférieure : 66.378
- Écart relatif solveur : 0.0725536254118697

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
