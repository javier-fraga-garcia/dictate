RUFF_VERSION := 0.15.20

.PHONY: lint format fix up down create-topics run-producer test-shared test-shared-cov test-ingestion test-ingestion-cov test-lakehouse test-lakehouse-cov test-serving test-serving-cov

check:
	uvx ruff@$(RUFF_VERSION) check .

format:
	uvx ruff@$(RUFF_VERSION) format .

fix:
	uvx ruff@$(RUFF_VERSION) check . --fix