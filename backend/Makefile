.PHONY: install
install:
	poetry install --sync --no-interaction --no-root
	poetry run pre-commit install --config ../.pre-commit-config.yaml

.PHONY: run
run:
	poetry run potato --db ../storage/recipes.db
