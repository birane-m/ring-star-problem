# Campagne demo_multi_graines

- Créée le : 2026-10-17T18:46:02.517816+00:00
- Cas : 24 ; résultats : 192

[Configuration](configuration.json) · [Résultats détaillés](runs.csv) · [Synthèse](summary.csv)

Les méthodes aléatoires sont répétées sur les graines configurées. Les méthodes déterministes ne sont exécutées qu'une fois.

Les graphiques comparent les moyennes et écarts-types observés. Les solutions illustrées sont les meilleures graines, signalées comme telles.

Les temps excluent les lectures et exports et incluent les tentatives sans solution. Les coûts moyens concernent les exécutions réussies, dont le nombre est indiqué. Le budget de recherche porte sur la phase d'amélioration et peut être dépassé du temps d'une évaluation en cours.

Les coûts portent sur les distances euclidiennes non arrondies. Ne pas comparer les coûts bruts entre instances dont les unités diffèrent.

## Résultats par cas

| Instance | p | α | Méthode | Statuts | Succès | Coût moyen | Écart-type | Temps moyen (s) | Solution représentative |
|---|---:|---:|---|---|---:|---:|---:|---:|---|
| ulysses16 | 3 | 1 | PLNE / CBC | {"optimal": 1} | 1/1 | 68.2731 | n.d. | 0.0893 | [Meilleure graine 0](runs/ulysses16.tsp_p3_a1_exact_plne_seed0/summary.md) |
| ulysses16 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 113.3067 | n.d. | 0.0003 | [Meilleure graine 0](runs/ulysses16.tsp_p3_a1_greedy_seed0/summary.md) |
| ulysses16 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 68.2731 | 0.0000 | 0.0019 | [Meilleure graine 0](runs/ulysses16.tsp_p3_a1_local_search_seed0/summary.md) |
| ulysses16 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 68.2731 | 0.0000 | 0.0210 | [Meilleure graine 0](runs/ulysses16.tsp_p3_a1_tabu_search_seed0/summary.md) |
| ulysses16 | 5 | 1 | PLNE / CBC | {"optimal": 1} | 1/1 | 65.3775 | n.d. | 1.7722 | [Meilleure graine 0](runs/ulysses16.tsp_p5_a1_exact_plne_seed0/summary.md) |
| ulysses16 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 89.1917 | n.d. | 0.0002 | [Meilleure graine 0](runs/ulysses16.tsp_p5_a1_greedy_seed0/summary.md) |
| ulysses16 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 65.5512 | 0.1505 | 0.0025 | [Meilleure graine 0](runs/ulysses16.tsp_p5_a1_local_search_seed0/summary.md) |
| ulysses16 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 65.3775 | 0.0000 | 0.0423 | [Meilleure graine 0](runs/ulysses16.tsp_p5_a1_tabu_search_seed0/summary.md) |
| ulysses16 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| ulysses16 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 76.4354 | n.d. | 0.0002 | [Meilleure graine 0](runs/ulysses16.tsp_p10_a1_greedy_seed0/summary.md) |
| ulysses16 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 63.5826 | 0.3945 | 0.0046 | [Meilleure graine 2](runs/ulysses16.tsp_p10_a1_local_search_seed2/summary.md) |
| ulysses16 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 63.2887 | 0.0181 | 0.0684 | [Meilleure graine 0](runs/ulysses16.tsp_p10_a1_tabu_search_seed0/summary.md) |
| ulysses22 | 3 | 1 | PLNE / CBC | {"optimal": 1} | 1/1 | 83.1382 | n.d. | 0.4890 | [Meilleure graine 0](runs/ulysses22.tsp_p3_a1_exact_plne_seed0/summary.md) |
| ulysses22 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 137.7209 | n.d. | 0.0002 | [Meilleure graine 0](runs/ulysses22.tsp_p3_a1_greedy_seed0/summary.md) |
| ulysses22 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 83.1382 | 0.0000 | 0.0021 | [Meilleure graine 0](runs/ulysses22.tsp_p3_a1_local_search_seed0/summary.md) |
| ulysses22 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 83.1382 | 0.0000 | 0.0244 | [Meilleure graine 0](runs/ulysses22.tsp_p3_a1_tabu_search_seed0/summary.md) |
| ulysses22 | 5 | 1 | PLNE / CBC | {"feasible_time_limited": 1} | 1/1 | 71.5707 | n.d. | 5.0176 | [Meilleure graine 0](runs/ulysses22.tsp_p5_a1_exact_plne_seed0/summary.md) |
| ulysses22 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 108.7947 | n.d. | 0.0002 | [Meilleure graine 0](runs/ulysses22.tsp_p5_a1_greedy_seed0/summary.md) |
| ulysses22 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 72.5447 | 0.8254 | 0.0029 | [Meilleure graine 1](runs/ulysses22.tsp_p5_a1_local_search_seed1/summary.md) |
| ulysses22 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 71.5707 | 0.0000 | 0.0342 | [Meilleure graine 0](runs/ulysses22.tsp_p5_a1_tabu_search_seed0/summary.md) |
| ulysses22 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| ulysses22 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 82.3576 | n.d. | 0.0003 | [Meilleure graine 0](runs/ulysses22.tsp_p10_a1_greedy_seed0/summary.md) |
| ulysses22 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 65.8251 | 0.2530 | 0.0067 | [Meilleure graine 0](runs/ulysses22.tsp_p10_a1_local_search_seed0/summary.md) |
| ulysses22 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 65.3160 | 0.0672 | 0.1018 | [Meilleure graine 0](runs/ulysses22.tsp_p10_a1_tabu_search_seed0/summary.md) |
| att48 | 3 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| att48 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 78299.7651 | n.d. | 0.0005 | [Meilleure graine 0](runs/att48_p3_a1_greedy_seed0/summary.md) |
| att48 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 72273.6419 | 1076.6511 | 0.0044 | [Meilleure graine 1](runs/att48_p3_a1_local_search_seed1/summary.md) |
| att48 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 70903.1287 | 0.0000 | 0.0462 | [Meilleure graine 0](runs/att48_p3_a1_tabu_search_seed0/summary.md) |
| att48 | 5 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| att48 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 63668.0432 | n.d. | 0.0006 | [Meilleure graine 0](runs/att48_p5_a1_greedy_seed0/summary.md) |
| att48 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 56467.9905 | 275.9815 | 0.0050 | [Meilleure graine 2](runs/att48_p5_a1_local_search_seed2/summary.md) |
| att48 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 55615.9204 | 202.5054 | 0.0622 | [Meilleure graine 1](runs/att48_p5_a1_tabu_search_seed1/summary.md) |
| att48 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| att48 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 48833.8933 | n.d. | 0.0007 | [Meilleure graine 0](runs/att48_p10_a1_greedy_seed0/summary.md) |
| att48 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 45563.0942 | 455.5493 | 0.0087 | [Meilleure graine 1](runs/att48_p10_a1_local_search_seed1/summary.md) |
| att48 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 42790.2073 | 59.2005 | 0.1206 | [Meilleure graine 0](runs/att48_p10_a1_tabu_search_seed0/summary.md) |
| eil51 | 3 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| eil51 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 859.9917 | n.d. | 0.0006 | [Meilleure graine 0](runs/eil51_p3_a1_greedy_seed0/summary.md) |
| eil51 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 828.2642 | 0.6043 | 0.0041 | [Meilleure graine 0](runs/eil51_p3_a1_local_search_seed0/summary.md) |
| eil51 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 827.5664 | 0.0000 | 0.0500 | [Meilleure graine 0](runs/eil51_p3_a1_tabu_search_seed0/summary.md) |
| eil51 | 5 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| eil51 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 735.0004 | n.d. | 0.0007 | [Meilleure graine 0](runs/eil51_p5_a1_greedy_seed0/summary.md) |
| eil51 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 708.5625 | 4.8195 | 0.0053 | [Meilleure graine 1](runs/eil51_p5_a1_local_search_seed1/summary.md) |
| eil51 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 698.1699 | 2.6445 | 0.0670 | [Meilleure graine 0](runs/eil51_p5_a1_tabu_search_seed0/summary.md) |
| eil51 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| eil51 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 630.4676 | n.d. | 0.0011 | [Meilleure graine 0](runs/eil51_p10_a1_greedy_seed0/summary.md) |
| eil51 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 563.9896 | 8.9331 | 0.0094 | [Meilleure graine 0](runs/eil51_p10_a1_local_search_seed0/summary.md) |
| eil51 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 550.9850 | 7.4423 | 0.1194 | [Meilleure graine 1](runs/eil51_p10_a1_tabu_search_seed1/summary.md) |
| berlin52 | 3 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| berlin52 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 16352.3195 | n.d. | 0.0006 | [Meilleure graine 0](runs/berlin52_p3_a1_greedy_seed0/summary.md) |
| berlin52 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 14095.0217 | 19.2491 | 0.0042 | [Meilleure graine 0](runs/berlin52_p3_a1_local_search_seed0/summary.md) |
| berlin52 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 14090.9625 | 12.2182 | 0.0506 | [Meilleure graine 0](runs/berlin52_p3_a1_tabu_search_seed0/summary.md) |
| berlin52 | 5 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| berlin52 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 14916.7359 | n.d. | 0.0007 | [Meilleure graine 0](runs/berlin52_p5_a1_greedy_seed0/summary.md) |
| berlin52 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 12014.9184 | 148.4786 | 0.0059 | [Meilleure graine 2](runs/berlin52_p5_a1_local_search_seed2/summary.md) |
| berlin52 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 11813.4900 | 22.6270 | 0.0744 | [Meilleure graine 2](runs/berlin52_p5_a1_tabu_search_seed2/summary.md) |
| berlin52 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| berlin52 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 12155.5721 | n.d. | 0.0009 | [Meilleure graine 0](runs/berlin52_p10_a1_greedy_seed0/summary.md) |
| berlin52 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 9869.3444 | 121.5646 | 0.0102 | [Meilleure graine 1](runs/berlin52_p10_a1_local_search_seed1/summary.md) |
| berlin52 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 9594.2859 | 121.7072 | 0.1358 | [Meilleure graine 2](runs/berlin52_p10_a1_tabu_search_seed2/summary.md) |
| st70 | 3 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| st70 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 1897.3665 | n.d. | 0.0009 | [Meilleure graine 0](runs/st70_p3_a1_greedy_seed0/summary.md) |
| st70 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 1762.4928 | 11.5533 | 0.0059 | [Meilleure graine 0](runs/st70_p3_a1_local_search_seed0/summary.md) |
| st70 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 1753.2359 | 0.0000 | 0.0689 | [Meilleure graine 0](runs/st70_p3_a1_tabu_search_seed0/summary.md) |
| st70 | 5 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| st70 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 1572.5307 | n.d. | 0.0010 | [Meilleure graine 0](runs/st70_p5_a1_greedy_seed0/summary.md) |
| st70 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 1388.7219 | 34.0107 | 0.0073 | [Meilleure graine 1](runs/st70_p5_a1_local_search_seed1/summary.md) |
| st70 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 1360.1715 | 6.8607 | 0.0898 | [Meilleure graine 2](runs/st70_p5_a1_tabu_search_seed2/summary.md) |
| st70 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| st70 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 1105.8204 | n.d. | 0.0013 | [Meilleure graine 0](runs/st70_p10_a1_greedy_seed0/summary.md) |
| st70 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 1074.1855 | 20.6322 | 0.0122 | [Meilleure graine 0](runs/st70_p10_a1_local_search_seed0/summary.md) |
| st70 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 1006.8953 | 4.3198 | 0.1508 | [Meilleure graine 0](runs/st70_p10_a1_tabu_search_seed0/summary.md) |
| kroA100 | 3 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| kroA100 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 77233.4048 | n.d. | 0.0021 | [Meilleure graine 0](runs/kroA100_p3_a1_greedy_seed0/summary.md) |
| kroA100 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 76618.8397 | 645.1910 | 0.0084 | [Meilleure graine 2](runs/kroA100_p3_a1_local_search_seed2/summary.md) |
| kroA100 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 75202.8156 | 496.1162 | 0.0923 | [Meilleure graine 0](runs/kroA100_p3_a1_tabu_search_seed0/summary.md) |
| kroA100 | 5 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| kroA100 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 68427.5687 | n.d. | 0.0019 | [Meilleure graine 0](runs/kroA100_p5_a1_greedy_seed0/summary.md) |
| kroA100 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 60284.1178 | 1653.9726 | 0.0103 | [Meilleure graine 0](runs/kroA100_p5_a1_local_search_seed0/summary.md) |
| kroA100 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 58433.1841 | 59.5721 | 0.1184 | [Meilleure graine 0](runs/kroA100_p5_a1_tabu_search_seed0/summary.md) |
| kroA100 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| kroA100 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 46042.2519 | n.d. | 0.0022 | [Meilleure graine 0](runs/kroA100_p10_a1_greedy_seed0/summary.md) |
| kroA100 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 43469.8013 | 862.2719 | 0.0151 | [Meilleure graine 1](runs/kroA100_p10_a1_local_search_seed1/summary.md) |
| kroA100 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 41457.1301 | 256.1678 | 0.1910 | [Meilleure graine 2](runs/kroA100_p10_a1_tabu_search_seed2/summary.md) |
| rd100 | 3 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| rd100 | 3 | 1 | Construction par grille | {"ok": 1} | 1/1 | 30724.6525 | n.d. | 0.0017 | [Meilleure graine 0](runs/rd100_p3_a1_greedy_seed0/summary.md) |
| rd100 | 3 | 1 | Recherche locale | {"ok": 3} | 3/3 | 26625.7357 | 394.0881 | 0.0084 | [Meilleure graine 1](runs/rd100_p3_a1_local_search_seed1/summary.md) |
| rd100 | 3 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 26393.3315 | 17.4772 | 0.0948 | [Meilleure graine 1](runs/rd100_p3_a1_tabu_search_seed1/summary.md) |
| rd100 | 5 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| rd100 | 5 | 1 | Construction par grille | {"ok": 1} | 1/1 | 21243.2506 | n.d. | 0.0019 | [Meilleure graine 0](runs/rd100_p5_a1_greedy_seed0/summary.md) |
| rd100 | 5 | 1 | Recherche locale | {"ok": 3} | 3/3 | 20528.9308 | 567.2787 | 0.0105 | [Meilleure graine 0](runs/rd100_p5_a1_local_search_seed0/summary.md) |
| rd100 | 5 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 19541.4821 | 55.8012 | 0.1209 | [Meilleure graine 2](runs/rd100_p5_a1_tabu_search_seed2/summary.md) |
| rd100 | 10 | 1 | PLNE / CBC | {"skipped": 1} | 0/1 | n.d. | n.d. | n.d. | {"skipped": 1} |
| rd100 | 10 | 1 | Construction par grille | {"ok": 1} | 1/1 | 16692.4194 | n.d. | 0.0022 | [Meilleure graine 0](runs/rd100_p10_a1_greedy_seed0/summary.md) |
| rd100 | 10 | 1 | Recherche locale | {"ok": 3} | 3/3 | 14072.2597 | 254.5044 | 0.0154 | [Meilleure graine 2](runs/rd100_p10_a1_local_search_seed2/summary.md) |
| rd100 | 10 | 1 | Recherche tabou | {"ok": 3} | 3/3 | 13604.2925 | 163.3950 | 0.1926 | [Meilleure graine 0](runs/rd100_p10_a1_tabu_search_seed0/summary.md) |

## Figures

- [figures/by_instance/att48_alpha_1.png](figures/by_instance/att48_alpha_1.png)
- [figures/by_instance/berlin52_alpha_1.png](figures/by_instance/berlin52_alpha_1.png)
- [figures/by_instance/eil51_alpha_1.png](figures/by_instance/eil51_alpha_1.png)
- [figures/by_instance/kroA100_alpha_1.png](figures/by_instance/kroA100_alpha_1.png)
- [figures/by_instance/rd100_alpha_1.png](figures/by_instance/rd100_alpha_1.png)
- [figures/by_instance/st70_alpha_1.png](figures/by_instance/st70_alpha_1.png)
- [figures/by_instance/ulysses16_alpha_1.png](figures/by_instance/ulysses16_alpha_1.png)
- [figures/by_instance/ulysses22_alpha_1.png](figures/by_instance/ulysses22_alpha_1.png)
- [figures/gains_alpha_1.png](figures/gains_alpha_1.png)
