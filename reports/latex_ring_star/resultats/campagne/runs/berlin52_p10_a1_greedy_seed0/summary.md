# Résultat greedy - berlin52

- Instance : berlin52
- Nombre de points : 52
- Nombre de stations : 10
- Alpha : 1.0
- Station obligatoire : 1
- Type TSPLIB : EUC_2D

## Coûts

- Coût métro : 4831.477
- Coût marche : 7324.095
- Coût total : 12155.572

## Stations choisies

1, 4, 10, 11, 13, 28, 29, 33, 42, 47

## Cycle métro

1 -> 42 -> 29 -> 47 -> 13 -> 28 -> 11 -> 33 -> 10 -> 4 -> 1

## Affectations par station

| Station | Points rattachés | Nombre de points |
|---:|---|---:|
| 1 | 1, 3, 18, 20, 21, 22, 23, 31, 32, 34, 35, 36, 39, 44, 45, 49 | 16 |
| 4 | 4, 5, 6, 15, 24, 25, 37, 38, 40, 43, 46, 48 | 12 |
| 10 | 8, 9, 10, 19, 41 | 5 |
| 11 | 11, 51 | 2 |
| 13 | 13, 14, 52 | 3 |
| 28 | 12, 26, 27, 28 | 4 |
| 29 | 16, 29, 30, 50 | 4 |
| 33 | 33 | 1 |
| 42 | 2, 7, 17, 42 | 4 |
| 47 | 47 | 1 |

## Affectations détaillées par point

| Point | Station |
|---:|---:|
| 1 | 1 |
| 2 | 42 |
| 3 | 1 |
| 4 | 4 |
| 5 | 4 |
| 6 | 4 |
| 7 | 42 |
| 8 | 10 |
| 9 | 10 |
| 10 | 10 |
| 11 | 11 |
| 12 | 28 |
| 13 | 13 |
| 14 | 13 |
| 15 | 4 |
| 16 | 29 |
| 17 | 42 |
| 18 | 1 |
| 19 | 10 |
| 20 | 1 |
| 21 | 1 |
| 22 | 1 |
| 23 | 1 |
| 24 | 4 |
| 25 | 4 |
| 26 | 28 |
| 27 | 28 |
| 28 | 28 |
| 29 | 29 |
| 30 | 29 |
| 31 | 1 |
| 32 | 1 |
| 33 | 33 |
| 34 | 1 |
| 35 | 1 |
| 36 | 1 |
| 37 | 4 |
| 38 | 4 |
| 39 | 1 |
| 40 | 4 |
| 41 | 10 |
| 42 | 42 |
| 43 | 4 |
| 44 | 1 |
| 45 | 1 |
| 46 | 4 |
| 47 | 47 |
| 48 | 4 |
| 49 | 1 |
| 50 | 29 |
| 51 | 11 |
| 52 | 13 |

## Visualisation

figures/solution.png

## Exécution

- Statut : ok
- Optimalité prouvée : False
- Temps de calcul : 0.000924 s
- Graine : 0
- Détails : {}
- Borne inférieure : None
- Écart relatif solveur : None

[Configuration](configuration.json) · [Solution et métadonnées](solution.json) · [Historique](history.csv)
