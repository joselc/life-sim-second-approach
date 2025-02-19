"""Configuration settings for the HexLife simulation."""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True)
class DisplayConfig:
    """Display-related configuration settings."""
    WINDOW_SIZE: Tuple[int, int] = (1024, 768)
    WINDOW_TITLE: str = "HexLife: Hexagonal Life Simulation"
    FPS: int = 60
    
@dataclass(frozen=True)
class Colors:
    """Color definitions used throughout the application."""
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BACKGROUND: Tuple[int, int, int] = (40, 44, 52)
    
@dataclass(frozen=True)
class SimulationConfig:
    """Simulation-related configuration settings."""
    INITIAL_GRID_SIZE: Tuple[int, int] = (50, 50)  # Width, Height
    TIME_STEP: float = 1.0  # seconds per simulation step
    
# Global configuration instances
display = DisplayConfig()
colors = Colors()
simulation = SimulationConfig() 