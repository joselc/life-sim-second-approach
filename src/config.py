"""Configuration settings for the HexLife simulation."""
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class DisplayConfig:
    """Display configuration settings."""

    WINDOW_SIZE: Tuple[int, int] = (1024, 768)
    WINDOW_TITLE: str = "HexLife: Hexagonal Life Simulation"
    FPS: int = 60

    # Grid display settings
    GRID_WIDTH: int = 5
    GRID_HEIGHT: int = 10
    HEX_SIZE: float = 30.0
    GRID_LINE_WIDTH: int = 1
    GRID_PADDING: int = 20

    # UI Layout Ratios
    COMMAND_COLUMN_RATIO: float = 0.2  # 1/5 of screen width
    SIMULATION_AREA_RATIO: float = 0.8  # 4/5 of screen width

    # Spacing/Padding
    COLUMN_PADDING: int = 10  # Internal padding for command column
    AREA_SEPARATOR: int = 2  # Width of separator line between areas

    # Text Configuration
    TITLE_TEXT: str = "HexLife"
    TITLE_FONT_SIZE: int = 24
    TITLE_PADDING: int = 20  # Padding from top of column


@dataclass(frozen=True)
class Colors:
    """Color definitions for the simulation."""

    BACKGROUND: Tuple[int, int, int] = (0, 0, 0)  # Black
    GRID_LINES: Tuple[int, int, int] = (100, 100, 100)  # Gray
    
    # UI Colors
    COMMAND_COLUMN_BACKGROUND: Tuple[int, int, int] = (40, 44, 52)  # Dark theme background
    COMMAND_COLUMN_TEXT: Tuple[int, int, int] = (255, 255, 255)  # White text
    AREA_SEPARATOR_COLOR: Tuple[int, int, int] = (70, 70, 70)  # Dark gray


@dataclass(frozen=True)
class SimulationConfig:
    """Simulation behavior configuration."""

    SIMULATION_SPEED: float = 1.0  # Base speed multiplier


# Create instances for importing
display = DisplayConfig()
colors = Colors()
simulation = SimulationConfig()
