"""Configuration settings for the HexLife simulation."""
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class DisplayConfig:
    """Display configuration settings."""
    WINDOW_SIZE: Tuple[int, int] = (1024, 768)
    WINDOW_TITLE: str = "HexLife Simulation"
    FPS: int = 60
    
    # Grid display settings
    GRID_WIDTH: int = 5
    GRID_HEIGHT: int = 10
    HEX_SIZE: float = 30.0
    GRID_LINE_WIDTH: int = 1
    GRID_PADDING: int = 20


@dataclass(frozen=True)
class Colors:
    """Color definitions for the simulation."""
    BACKGROUND: Tuple[int, int, int] = (0, 0, 0)  # Black
    GRID_LINES: Tuple[int, int, int] = (100, 100, 100)  # Gray


@dataclass(frozen=True)
class SimulationConfig:
    """Simulation behavior configuration."""
    SIMULATION_SPEED: float = 1.0  # Base speed multiplier


# Create instances for importing
display = DisplayConfig()
colors = Colors()
simulation = SimulationConfig()
