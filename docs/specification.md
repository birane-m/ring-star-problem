# Spécification du problème Ring-Star

## 1. Contexte

Le projet consiste à optimiser le tracé d'une ligne de transport public circulaire,
par exemple un métro, un tramway ou un bus en boucle.

On dispose d'un ensemble de points représentant des zones d'une agglomération :
quartiers, pôles d'activité, zones de population ou lieux pouvant accueillir une
station. La ligne circulaire ne passe pas par tous les points : elle doit desservir
seulement `p` stations choisies parmi les `n` points disponibles.

Les points non retenus comme stations sont rattachés à leur station la plus proche.
Ce rattachement représente le trajet d'accès des usagers, par exemple à pied.

Le problème combine donc deux décisions :

- choisir les stations à ouvrir ;
- construire un cycle reliant ces stations.

Ce problème est appelé problème de l'anneau-étoile, ou Ring-Star problem.

## 2. Données d'entrée

Une instance du problème contient :

- un ensemble de $n$ points :

$$
V = \{0, \dots, n - 1\}
$$

- les coordonnées planes de chaque point ;
- un entier $p$, nombre de stations à sélectionner ;
- un paramètre $\alpha$, poids du coût du cycle dans la fonction objectif.

Les coordonnées peuvent provenir d'instances TSPLIB compatibles, en particulier
des instances définies par un nuage de points.

Les distances utilisées sont euclidiennes :

$$
d(i,j) = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2}
$$

## 3. Conventions

L'énoncé impose que le premier sommet soit toujours une station.

Dans le code, les indices Python commencent à `0`, donc :

$$
\text{sommet } 1 \text{ de l'énoncé} = \text{sommet } 0 \text{ dans le programme}
$$

Par convention, on appellera ce sommet $r$ dans la spécification.

Le paramètre $p$ doit respecter :

$$
3 \leq p \leq n
$$

Le paramètre $\alpha$ doit respecter :

$$
0 \leq \alpha \leq 10
$$

## 4. Solution attendue

Une solution Ring-Star est composée de trois éléments.

### Stations

Un ensemble $S$ de $p$ points sélectionnés comme stations :

$$
S \subseteq V
$$

$$
|S| = p
$$

$$
r \in S
$$

### Affectations

Chaque point $i$ est affecté à une station $a(i)$.

Si $i$ est une station, alors :

$$
i \in S \Rightarrow a(i) = i
$$

Si $i$ n'est pas une station, alors $a(i)$ doit être une station :

$$
i \notin S \Rightarrow a(i) \in S
$$

Dans une solution normalisée, chaque point non-station est affecté à la station
la plus proche.

$$
\forall i \in V \setminus S,\quad a(i) \in \arg\min_{s \in S} d(i,s)
$$

### Cycle

Les $p$ stations doivent être reliées par un cycle simple.

Cela signifie que :

- chaque station apparaît exactement une fois dans l'ordre du cycle ;
- le cycle revient à son point de départ ;
- chaque station a degré `2` dans le cycle ;
- aucun point non-station n'appartient au cycle.

## 5. Fonction objectif

Le coût total d'une solution est :

$$
C_{\mathrm{total}} = \alpha \, C_{\mathrm{metro}} + C_{\mathrm{marche}}
$$

Avec :

$$
C_{\mathrm{metro}} = d(c_0,c_1) + d(c_1,c_2) + \dots + d(c_{p-2},c_{p-1}) + d(c_{p-1},c_0)
$$

où $(c_0, c_1, \dots, c_{p-1})$ désigne l'ordre des stations dans le cycle.

Autrement dit, on additionne les distances entre deux stations consécutives du
métro circulaire, puis on ajoute la dernière arête qui ramène à la première
station.

$$
C_{\mathrm{marche}} = \sum_{i \in V \setminus S} d(i, a(i))
$$

Objectif :

$$
\min C_{\mathrm{total}}
$$

Le paramètre $\alpha$ permet de pondérer l'importance de la longueur du métro
circulaire par rapport aux trajets d'accès.

## 6. Cas particuliers importants

Si $p = n$, tous les points sont des stations. Il n'y a donc plus de coût
d'affectation. Le problème devient un problème du voyageur de commerce, car il
faut trouver le meilleur cycle passant par tous les points.

Si $\alpha = 0$, le coût du cycle n'intervient plus. Il faut seulement choisir
$p$ stations minimisant les distances d'affectation. Le problème devient un
problème du p-médian.

Ces deux cas montrent que le problème Ring-Star généralise des problèmes connus
difficiles. On considère donc le problème Ring-Star comme NP-difficile.

## 7. Critères de validité d'une solution

Une solution est valide si toutes les conditions suivantes sont vérifiées :

- le nombre de stations est exactement `p` ;
- la station obligatoire est présente ;
- toutes les stations sont des points de l'instance ;
- chaque point possède exactement une affectation ;
- chaque affectation pointe vers une station ;
- une station est affectée à elle-même ;
- le cycle contient exactement les stations ;
- le cycle est simple ;
- le coût total est calculé avec la formule officielle.

Ces critères devront être vérifiés automatiquement par des tests.

## 8. Méthodes prévues

Le projet sera reconstruit autour de trois familles de méthodes.

### Heuristique constructive

Construire rapidement une première solution réalisable :

- choix initial de `p` stations ;
- affectation des points aux stations les plus proches ;
- construction d'un cycle sur les stations.

### Métaheuristique

Améliorer la solution initiale par recherche locale :

- échange entre une station et un point non-station ;
- recalcul des affectations ;
- amélioration du cycle ;
- conservation des meilleures solutions trouvées.

### Résolution exacte

Implémenter une formulation compacte en programmation linéaire en nombres
entiers pour obtenir des solutions optimales sur des instances de taille
raisonnable.

Cette méthode servira aussi de référence pour mesurer la qualité des heuristiques.

## 9. Sorties attendues

Le programme devra pouvoir produire :

- la liste des stations ;
- l'ordre du cycle ;
- l'affectation de chaque point ;
- le coût total ;
- le coût du cycle ;
- le coût d'affectation ;
- le temps d'exécution ;
- une visualisation graphique ;
- des résultats de benchmark exportables.
