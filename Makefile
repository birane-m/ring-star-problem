VENV ?= .venv
PYTHON_BOOTSTRAP ?= python3
PYTHON ?= $(VENV)/bin/python
PYTHONPATH ?= src
CLI := PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m ring_star.cli
INSTALL_STAMP := $(VENV)/.installed

INSTANCE ?= data/instances/att48.tsp
P ?= 10
METHOD ?= tabou
ITERATIONS ?= 100
CANDIDATES ?= 15
TIME_LIMIT ?= 0

.PHONY: help install test plot-instance run greedy local tabu exact run-greedy run-local run-tabu run-exact benchmark benchmark-greedy benchmark-meta compare plot-solutions report clean

help:
	@echo "Commandes disponibles :"
	@echo "  make install                         Creer .venv et installer les dependances"
	@echo "  make test                            Lancer les tests"
	@echo "  make plot-instance INSTANCE=...      Dessiner le nuage de points"
	@echo "  make run METHOD=tabou INSTANCE=... P=10"
	@echo "  make greedy INSTANCE=... P=10"
	@echo "  make local INSTANCE=... P=10 ITERATIONS=100"
	@echo "  make tabu INSTANCE=... P=10 ITERATIONS=100 CANDIDATES=15"
	@echo "  make exact INSTANCE=... P=5 TIME_LIMIT=0"
	@echo "  make benchmark                       Generer les CSV heuristique + meta"
	@echo "  make compare                         Generer CSV comparatif + graphes"
	@echo "  make plot-solutions                  Generer les PNG de solutions"
	@echo "  make report                          benchmark + compare + plot-solutions"
	@echo "  make clean                           Supprimer .venv"

$(PYTHON):
	$(PYTHON_BOOTSTRAP) -m venv $(VENV)

$(INSTALL_STAMP): requirements.txt | $(PYTHON)
	$(PYTHON) -m pip install -r requirements.txt
	touch $(INSTALL_STAMP)

install: $(INSTALL_STAMP)

test: $(INSTALL_STAMP)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m unittest discover -s tests

plot-instance: $(INSTALL_STAMP)
	$(CLI) plot-instance $(INSTANCE)

run: $(INSTALL_STAMP)
	$(CLI) run $(METHOD) $(INSTANCE) $(P)

greedy: run-greedy

local: run-local

tabu: run-tabu

exact: run-exact

run-greedy: $(INSTALL_STAMP)
	$(CLI) run gloutonne $(INSTANCE) $(P)

run-local: $(INSTALL_STAMP)
	$(CLI) run locale $(INSTANCE) $(P) --iterations $(ITERATIONS)

run-tabu: $(INSTALL_STAMP)
	$(CLI) run tabou $(INSTANCE) $(P) --iterations $(ITERATIONS) --candidates-per-iteration $(CANDIDATES)

run-exact: $(INSTALL_STAMP)
	$(CLI) run exact $(INSTANCE) $(P) --time-limit $(TIME_LIMIT)

benchmark: benchmark-greedy benchmark-meta

benchmark-greedy: $(INSTALL_STAMP)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_report_benchmarks.py greedy

benchmark-meta: $(INSTALL_STAMP)
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) scripts/run_report_benchmarks.py meta --local-iterations $(ITERATIONS) --tabu-iterations $(ITERATIONS) --candidates-per-iteration $(CANDIDATES)

compare: $(INSTALL_STAMP)
	$(CLI) compare-benchmarks

plot-solutions: $(INSTALL_STAMP)
	$(CLI) plot-benchmark-solutions

report: benchmark compare plot-solutions

clean:
	rm -rf $(VENV)
