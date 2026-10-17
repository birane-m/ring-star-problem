# Résultat exact_plne - ulysses16.tsp

- Instance : ulysses16.tsp
- Nombre de points : 16
- Nombre de stations : 5
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : GEO

## Coûts

- Coût métro : 18.248
- Coût marche : 47.130
- Coût total : 65.378

## Stations choisies

1, 6, 7, 13, 15

## Cycle métro

1 -> 13 -> 7 -> 6 -> 15 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 2, 3, 4, 8, 16 | 6 |
| 6 | 6, 9, 11 | 3 |
| 7 | 7, 10 | 2 |
| 13 | 12, 13, 14 | 3 |
| 15 | 5, 15 | 2 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 15 |
| 6 | 6 |
| 7 | 7 |
| 8 | 1 |
| 9 | 6 |
| 10 | 7 |
| 11 | 6 |
| 12 | 13 |
| 13 | 13 |
| 14 | 13 |
| 15 | 15 |
| 16 | 1 |

## Visualisation

figures/solution.png

## Exécution

- Statut : optimal
- Optimalité prouvée : True
- Temps de calcul : 1.772192 s
- Graine : 0
- Détails : {"solver": "CBC"}
- Borne inférieure : 65.37754906166406
- Écart relatif solveur : 0.0

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
