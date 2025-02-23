# HexLife: Hexagonal Life Simulation Engine

A life simulation engine built on a hexagonal grid, modeling ecological interactions between terrain, plants, climate, and eventually animals. The simulation emphasizes emergent behaviors through simple rule-based interactions between entities.

[![Tests](https://github.com/joselc/life-sim-second-approach/actions/workflows/test.yml/badge.svg)](https://github.com/joselc/life-sim-second-approach/actions/workflows/test.yml)
[![Lint](https://github.com/joselc/life-sim-second-approach/actions/workflows/lint.yml/badge.svg)](https://github.com/joselc/life-sim-second-approach/actions/workflows/lint.yml)
[![codecov](https://codecov.io/gh/joselc/life-sim-second-approach/branch/main/graph/badge.svg)](https://codecov.io/gh/joselc/life-sim-second-approach)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://github.com/joselc/life-sim-second-approach/blob/main/.github/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-blue)](http://mypy-lang.org/)
[![Linting: flake8](https://img.shields.io/badge/linting-flake8-yellowgreen)](https://flake8.pycqa.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)](https://www.pygame.org/)

## Features (Planned)

- Hexagonal grid-based world
- Multiple terrain types with unique properties
- Plant life simulation with growth and reproduction
- Climate system affecting environmental conditions
- Animal ecosystem (future)
- Clean architecture design
- Modular and extensible codebase

## Requirements

- Python 3.8 or higher
- Pygame 2.5.2
- Additional dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd hexlife
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Simulation

To start the simulation:

```bash
python src/main.py
```

## Development

### Project Structure

The project follows clean architecture principles:

```
hexlife/
├── src/
│   ├── domain/          # Core business logic
│   ├── application/     # Use cases and services
│   ├── infrastructure/  # External implementations
│   └── interfaces/      # UI and external adapters
└── tests/              # Test suites
```

### Development Guidelines

1. Follow clean architecture principles
2. Write tests for all new features
3. Use type hints
4. Follow PEP 8 style guide
5. Run linters before committing

### Running Tests

```bash
pytest tests/
```

### Code Quality

Before committing, run:

```bash
black .
isort .
mypy src/
flake8 src/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change. 