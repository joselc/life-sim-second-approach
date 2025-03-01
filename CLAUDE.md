# HexLife Development Guide

## Build/Test/Lint Commands
- Run all tests: `pytest tests/`
- Run specific test: `pytest tests/path/to/test_file.py::TestClass::test_function`
- Coverage: `pytest tests/ --cov=src/ --cov-report=xml`
- Format code: `black .`
- Sort imports: `isort .`
- Type check: `mypy src/`
- Lint: `flake8 src/ tests/`
- Install package in dev mode: `pip install -e .`

## Code Style Guidelines
- Follow PEP 8 and Black (88 char line limit)
- Use snake_case for functions/variables, PascalCase for classes
- Always use type hints for function parameters and return values
- Follow Clean Architecture principles with distinct layers (domain, application, interfaces, infrastructure)
- Keep domain entities pure and framework-independent
- Create separate models for different layers (DTOs, ViewModels)
- Use specific exception types and proper error handling
- Write clear docstrings in Google style
- Pygame code must stay in interfaces layer only, never in domain
- Test coverage target: 80%+