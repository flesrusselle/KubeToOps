.PHONY: help check-prerequisites lint test cotd release-preview validate clean

help:
	@echo "KubeToOps - Convenient Developer Commands"
	@echo "-----------------------------------------"
	@echo "make check-prerequisites  Check host CLI dependencies"
	@echo "make lint                 Run linters (yamllint, shellcheck, pytest lint)"
	@echo "make test                 Run Python test suite"
	@echo "make cotd                 Generate Command of the Day locally"
	@echo "make release-preview      Generate Release Preview from git diff"
	@echo "make validate             Run master repository validation runner"

check-prerequisites:
	@bash scripts/check_prerequisites.sh

lint:
	@yamllint content/*.yaml .github/**/*.yml
	@shellcheck scripts/*.sh
	@pytest tests/

test:
	@if command -v pytest &>/dev/null; then pytest tests/; else python3 -m unittest discover -s tests; fi

cotd:
	@python3 scripts/generate_command_of_day.py

release-preview:
	@python3 scripts/generate_release_preview.py

validate:
	@bash scripts/validate_repository.sh

clean:
	@rm -rf .pytest_cache __pycache__ tests/__pycache__ scripts/__pycache__
