# Sources du rapport Ring-Star

Ces sources reprennent la présentation du rapport BAAC : couverture sobre,
couleurs anthracite et terre cuite, deux parties, résumé, glossaire, références
et annexes. Le contenu est adapté au modèle Ring-Star réellement implémenté.

## Installation dans le projet

Extraire cette archive dans `reports/latex_ring_star/`, depuis la racine du
projet. L'archive est plate : `main.tex` est directement à sa racine.
Placer le PDF livré dans `reports/RingStar_rapport.pdf`.
L'archive ne contient ni dépôt Git ni environnement Python.

## Compilation

Depuis ce dossier, avec Python 3 et une distribution TeX Live :

```bash
python3 scripts/generer_tableaux.py
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Sans latexmk : compiler `main.tex` trois fois avec `pdflatex`.
Sous Ubuntu, les paquets habituels sont `latexmk`, `texlive-latex-extra`,
`texlive-lang-french` et `texlive-fonts-recommended`.
Le script de tableaux utilise uniquement la bibliothèque standard Python.
Les tableaux sont déjà fournis ; aucune résolution n'est requise pour compiler.
La disposition des courbes de comparaison et de convergence est adaptée à une
page A4. Le script optionnel `scripts/generer_figures_rapport.py` les recrée depuis
les résultats enregistrés, avec l'environnement Python du projet (Matplotlib).
Il ne relance aucune optimisation. Les autres figures fournies sont conservées.

## Fichiers

- `main.tex`, `preambule.tex`, `page_de_garde.tex` : structure et présentation.
- `chapitres/` : résumé, introduction, modèle, méthodes et analyse.
- `annexes/`, `glossaire.tex`, `references.tex` : repères complémentaires.
- `figures/` : couverture fournie et figures vectorielles enregistrées du projet.
- `tableaux/` : tableaux générés depuis les données archivées.
- `resultats/` : résultats de campagne et exemple individuel, configurations,
  coordonnées TSPLIB, validation et provenance.
- `scripts/generer_tableaux.py` : vérification indépendante des coûts et tableaux.
- `correctifs/export_cas_ignores.patch` : correctif ciblé, à intégrer séparément.

## Données et portée

La campagne présentée est `20261017T184415046891Z_demo_multi_graines_7cc051` :
huit instances, p = 3, 5, 10, alpha = 1 ; graines 0, 1, 2 pour les recherches.
Elle comporte 172 solutions, 3 optima prouvés et 20 cas exacts ignorés,
pour 192 enregistrements attendus. Les variantes complète et à budget de temps
ne sont pas présentées comme exécutées.
Les coûts sont euclidiens non arrondis dans les unités des coordonnées,
même pour les sources GEO ou ATT.

L'export `resultats/campagne/runs.csv` original contient 191 lignes : le dernier
cas ignoré, rd100/p10/PLNE, n'avait pas été écrit. La synthèse est complète.
La copie `resultats/runs_reconcilies.csv` ajoute cette ligne en la marquant
ignorée, sans inventer de résultat de résolution. Les données originales sont
conservées. Le script documente cette réconciliation dans le fichier de
provenance et recalcule les coûts des 172 solutions de campagne.

## Correctif à appliquer depuis la racine du dépôt

```bash
git apply --check reports/latex_ring_star/correctifs/export_cas_ignores.patch
git apply reports/latex_ring_star/correctifs/export_cas_ignores.patch
make test
```

Le patch ajoute l'écriture finale du CSV et renforce le test existant qui
contrôle les cas ignorés. Aucun solveur ni coût n'est modifié. La suite reste
composée de 101 tests, tous passés dans l'environnement de revue ; journal
dans `resultats/tests_revue.log`. Le patch n'a pas été appliqué au dépôt distant.

Le commit publié documenté est `8761003`. Les calculs archivés portent leur
empreinte de sources propre ; cette empreinte ne doit pas être confondue avec
le hash Git ni avec une affirmation de relance après chaque modification.

La couverture est créditée dans `IMAGE_SOURCE.txt` et dans les références.
