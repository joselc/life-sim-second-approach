# HexLife: Hexagonal Life Simulation Engine

A life simulation engine built on a hexagonal grid, modeling ecological interactions between terrain, plants, climate, and eventually animals. The simulation emphasizes emergent behaviors through simple rule-based interactions between entities.

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

[License information to be added]

## Contributing

[Contribution guidelines to be added] 