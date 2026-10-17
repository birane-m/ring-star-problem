VENV ?= .venv
PYTHON_BOOTSTRAP ?= python3
PYTHON ?= $(VENV)/bin/python
CLI := PYTHONPATH=src $(PYTHON) -m ring_star.cli
STAMP := $(VENV)/.installed
INSTANCE ?= data/instances/att48.tsp
P ?= 10
ALPHA ?= 1
SEED ?= 0
METHOD ?= tabou
ITERATIONS ?= 100
CANDIDATES ?= 15
TENURE ?= 20
TIME_LIMIT ?= 30
CONFIG ?= configs/benchmark_demo.json
OUTPUT_ROOT ?= outputs
CAMPAIGN ?=

.PHONY: help install test run greedy local tabu exact benchmark benchmark-full benchmark-time report compare plot-solutions plot-instance clean cleanup package
help:
	@echo "make install | test | run | greedy | local | tabu | exact | cleanup"
	@echo "make benchmark CONFIG=configs/benchmark_demo.json"
	@echo "make benchmark-full : campagne complète, plus longue"
	@echo "make benchmark-time : même budget d'amélioration pour locale et tabou"
	@echo "Les sorties sont indexées dans outputs/index.md"
$(VENV)/bin/python:
	$(PYTHON_BOOTSTRAP) -m venv $(VENV)
$(STAMP): pyproject.toml requirements.txt | $(VENV)/bin/python
	$(PYTHON) -m pip install -e .
	touch $(STAMP)
install: $(STAMP)
test: $(STAMP)
	MPLBACKEND=Agg PYTHONPATH=src $(PYTHON) -m unittest discover -s tests -v
run: $(STAMP)
	$(CLI) run $(METHOD) $(INSTANCE) $(P) --alpha $(ALPHA) --seed $(SEED) --iterations $(ITERATIONS) --tabu-tenure $(TENURE) --candidates-per-iteration $(CANDIDATES) --time-limit $(TIME_LIMIT) --output-root $(OUTPUT_ROOT)
greedy:
	$(MAKE) run METHOD=greedy
local:
	$(MAKE) run METHOD=local
tabu:
	$(MAKE) run METHOD=tabu
exact:
	$(MAKE) run METHOD=exact
plot-instance: $(STAMP)
	$(CLI) plot-instance $(INSTANCE)
benchmark: $(STAMP)
	$(CLI) benchmark --config $(CONFIG) --output-root $(OUTPUT_ROOT)
benchmark-full:
	$(MAKE) benchmark CONFIG=configs/benchmark_full.json
benchmark-time:
	$(MAKE) benchmark CONFIG=configs/benchmark_time_budget.json
# Generate the complete fresh campaign, including configured exact runs.
report: benchmark
compare plot-solutions: $(STAMP)
	@test -n "$(CAMPAIGN)" || (echo "Préciser CAMPAIGN=outputs/benchmarks/<identifiant>"; exit 2)
	$(CLI) plot-campaign $(CAMPAIGN)
clean:
	rm -rf $(VENV)
package:
	$(PYTHON_BOOTSTRAP) scripts/package_project.py

cleanup:
	$(PYTHON_BOOTSTRAP) scripts/cleanup_legacy.py
