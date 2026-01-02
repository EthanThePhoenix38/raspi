.PHONY: help install install-dev test lint format security clean build

help:  ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install package
	pip install -e .

install-dev:  ## Install development dependencies
	pip install -r requirements-dev.txt
	pip install -e .
	pre-commit install

test:  ## Run tests
	pytest tests/ -v --cov=src/raspi --cov-report=term-missing

test-cov:  ## Run tests with coverage report
	pytest tests/ -v --cov=src/raspi --cov-report=html --cov-report=term-missing

lint:  ## Run linting
	flake8 src/ tests/
	mypy src/

format:  ## Format code
	black src/ tests/

format-check:  ## Check code formatting
	black --check src/ tests/

security:  ## Run security checks
	bandit -r src/

pre-commit:  ## Run all pre-commit hooks
	pre-commit run --all-files

clean:  ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build package
	python -m build

dev:  ## Set up development environment
	make install-dev
	@echo "Development environment ready!"

check:  ## Run all checks (format, lint, security, tests)
	make format-check
	make lint
	make security
	make test
