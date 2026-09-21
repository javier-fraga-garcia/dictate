RUFF_VERSION := 0.15.20

.PHONY: lint format fix run

check:
	uvx ruff@$(RUFF_VERSION) check .

format:
	uvx ruff@$(RUFF_VERSION) format .

fix:
	uvx ruff@$(RUFF_VERSION) check . --fix

run: 
	uv run src/main.py

signal:
	kill -10 $$(pgrep -f "main.py" | head -n 1)