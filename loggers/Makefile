#
# Makefile
#
SHELL=/bin/bash
.DEFAULT_GOAL=help

# Help help! I'm being repressed!
.PHONY: help
help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# # Common targets
# .PHONY: clean
# clean: ## Cleans the workspace
# 	@rm -rf .coverage .pytest_cache coverage.xml junit.xml

# .PHONY: install
# install: ## Installs all dependencies, and creates a lock file if one doesn't exist
# 	@poetry run python -m pip install --upgrade pip
# 	@poetry install

# .PHONY: lock
# lock: ## Update the poetry lock file
# 	@poetry lock --no-update

## TESTING
# @poetry run in front if that's what you're using

.PHONY: test-custom
test-custom: ## Run tests that are marked "integration"
	pytest -m "custom"

.PHONY: test-integration
test-integration: ## Run tests that are marked "integration"
	pytest -m "integration"

.PHONY: test-all
test-all: ## Run all the tests
	pytest

.PHONY: test
test: ## Run tests that are not marked "integration"
	make test-all
