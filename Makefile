VENV := .venv
PY := $(if $(wildcard $(VENV)/bin/python3),$(VENV)/bin/python3,python3)

.PHONY: help setup test check build build-check publish-dry publish

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*## "} /^[a-zA-Z_-]+:.*## / {printf "  %-14s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: ## Create .venv and install Python tooling dependencies
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install -r tools/requirements.txt

test: ## Run all Python unit tests
	$(PY) -m unittest discover -s tools/tests -v

check: test build-check ## Run unit tests, drift guards, and all 15 library checks
	$(PY) tools/library_checks.py --report-dir check-report

build: ## Regenerate all derived artifacts from source
	$(PY) tools/build_tokens_css.py
	$(PY) tools/build_document_master.py
	$(PY) tools/build_readme.py

build-check: ## Verify all generated artifacts are drift-free
	$(PY) tools/build_tokens_css.py --check
	$(PY) tools/build_document_master.py --check
	$(PY) tools/build_readme.py --check

publish-dry: ## Preview Google Drive one-way mirror changes (no mutations)
	$(PY) tools/publish_drive.py --dry-run

publish: ## Publish main to Google Drive mirror and verify zero drift
	$(PY) tools/publish_drive.py --apply
	$(PY) tools/publish_drive.py --dry-run --fail-on-drift
