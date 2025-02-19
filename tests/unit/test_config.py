"""Unit tests for configuration settings."""
import dataclasses
from typing import Tuple

import pytest

from src.config import Colors, DisplayConfig, SimulationConfig


def test_display_config_initialization() -> None:
    """Test that DisplayConfig is initialized with correct default values."""
    config = DisplayConfig()
    assert isinstance(config.WINDOW_SIZE, tuple)
    assert len(config.WINDOW_SIZE) == 2
    assert all(isinstance(dim, int) for dim in config.WINDOW_SIZE)
    assert config.WINDOW_TITLE == "HexLife: Hexagonal Life Simulation"
    assert isinstance(config.FPS, int)
    assert config.FPS > 0


def test_display_config_immutability() -> None:
    """Test that DisplayConfig instances are immutable."""
    config = DisplayConfig()
    with pytest.raises(dataclasses.FrozenInstanceError):
        config.WINDOW_SIZE = (800, 600)  # type: ignore
    with pytest.raises(dataclasses.FrozenInstanceError):
        config.WINDOW_TITLE = "New Title"  # type: ignore
    with pytest.raises(dataclasses.FrozenInstanceError):
        config.FPS = 30  # type: ignore


def test_colors_initialization() -> None:
    """Test that Colors is initialized with valid RGB values."""
    colors = Colors()
    
    def is_valid_rgb(color: Tuple[int, int, int]) -> bool:
        """Check if a color tuple contains valid RGB values."""
        return (
            len(color) == 3
            and all(isinstance(value, int) for value in color)
            and all(0 <= value <= 255 for value in color)
        )
    
    assert is_valid_rgb(colors.BLACK)
    assert is_valid_rgb(colors.WHITE)
    assert is_valid_rgb(colors.BACKGROUND)
    assert colors.BLACK == (0, 0, 0)
    assert colors.WHITE == (255, 255, 255)


def test_colors_immutability() -> None:
    """Test that Colors instances are immutable."""
    colors = Colors()
    with pytest.raises(dataclasses.FrozenInstanceError):
        colors.BLACK = (1, 1, 1)  # type: ignore
    with pytest.raises(dataclasses.FrozenInstanceError):
        colors.WHITE = (254, 254, 254)  # type: ignore
    with pytest.raises(dataclasses.FrozenInstanceError):
        colors.BACKGROUND = (100, 100, 100)  # type: ignore


def test_simulation_config_initialization() -> None:
    """Test that SimulationConfig is initialized with correct default values."""
    config = SimulationConfig()
    assert isinstance(config.INITIAL_GRID_SIZE, tuple)
    assert len(config.INITIAL_GRID_SIZE) == 2
    assert all(isinstance(dim, int) for dim in config.INITIAL_GRID_SIZE)
    assert all(dim > 0 for dim in config.INITIAL_GRID_SIZE)
    assert isinstance(config.TIME_STEP, float)
    assert config.TIME_STEP > 0


def test_simulation_config_immutability() -> None:
    """Test that SimulationConfig instances are immutable."""
    config = SimulationConfig()
    with pytest.raises(dataclasses.FrozenInstanceError):
        config.INITIAL_GRID_SIZE = (10, 10)  # type: ignore
    with pytest.raises(dataclasses.FrozenInstanceError):
        config.TIME_STEP = 0.5  # type: ignore 