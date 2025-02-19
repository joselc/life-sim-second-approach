"""Shared test fixtures for the HexLife test suite."""
import dataclasses
from typing import Generator

import pytest

from src.config import Colors, DisplayConfig, SimulationConfig


@pytest.fixture
def display_config() -> DisplayConfig:
    """Provide a fresh DisplayConfig instance for each test."""
    return DisplayConfig()


@pytest.fixture
def colors() -> Colors:
    """Provide a fresh Colors instance for each test."""
    return Colors()


@pytest.fixture
def simulation_config() -> SimulationConfig:
    """Provide a fresh SimulationConfig instance for each test."""
    return SimulationConfig()


@pytest.fixture(autouse=True)
def cleanup_pygame() -> Generator[None, None, None]:
    """Ensure pygame is properly cleaned up after each test."""
    import pygame

    yield

    try:
        pygame.quit()
    except Exception:
        pass  # Ignore any pygame cleanup errors
