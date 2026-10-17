# Résultat greedy - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 68.083
- Coût marche : 8.352
- Coût total : 76.435

## Stations choisies

1, 3, 4, 5, 9, 10, 11, 12, 15, 16

## Cycle métro

1 -> 4 -> 3 -> 16 -> 12 -> 10 -> 9 -> 11 -> 5 -> 15 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 8 | 2 |
| 3 | 2, 3 | 2 |
| 4 | 4 | 1 |
| 5 | 5 | 1 |
| 9 | 9 | 1 |
| 10 | 10 | 1 |
| 11 | 11 | 1 |
| 12 | 7, 12, 13, 14 | 4 |
| 15 | 6, 15 | 2 |
| 16 | 16 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 3 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 15 |
| 7 | 12 |
| 8 | 1 |
| 9 | 9 |
| 10 | 10 |
| 11 | 11 |
| 12 | 12 |
| 13 | 12 |
| 14 | 12 |
| 15 | 15 |
| 16 | 16 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.000223 s
- Graine : 0
- Détails : {}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
