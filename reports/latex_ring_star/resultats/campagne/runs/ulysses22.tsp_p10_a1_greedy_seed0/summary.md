# Résultat greedy - ulysses22.tsp

- Instance : ulysses22.tsp
- Nombre de points : 22
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 62.858
- Coût marche : 19.499
- Coût total : 82.358

## Stations choisies

1, 5, 9, 11, 12, 15, 16, 18, 21, 22

## Cycle métro

1 -> 18 -> 22 -> 16 -> 21 -> 9 -> 11 -> 5 -> 15 -> 12 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8 | 2 |
| 5 | 5 | 1 |
| 9 | 9 | 1 |
| 11 | 11 | 1 |
| 12 | 7, 12, 13, 14 | 4 |
| 15 | 6, 15 | 2 |
| 16 | 16 | 1 |
| 18 | 4, 18 | 2 |
| 21 | 10, 19, 20, 21 | 4 |
| 22 | 2, 3, 17, 22 | 4 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 22 |
| 3 | 22 |
| 4 | 18 |
| 5 | 5 |
| 6 | 15 |
| 7 | 12 |
| 8 | 1 |
| 9 | 9 |
| 10 | 21 |
| 11 | 11 |
| 12 | 12 |
| 13 | 12 |
| 14 | 12 |
| 15 | 15 |
| 16 | 16 |
| 17 | 22 |
| 18 | 18 |
| 19 | 21 |
| 20 | 21 |
| 21 | 21 |
| 22 | 22 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.000272 s
- Graine : 0
- Détails : {}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
