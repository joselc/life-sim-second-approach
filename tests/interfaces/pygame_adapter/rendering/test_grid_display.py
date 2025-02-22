"""Tests for the grid display management."""
import math
import pygame
import pytest
from unittest.mock import Mock, patch

from src.domain.entities.grid import HexGrid
from src.domain.value_objects.grid_dimensions import GridDimensions
from src.interfaces.pygame_adapter.rendering.grid_display import (
    DisplayConfig,
    GridDisplay,
)


@pytest.fixture
def display_config():
    """Create a test display configuration."""
    return DisplayConfig(
        hex_size=50.0,
        background_color=(0, 0, 0),
        line_color=(100, 100, 100),
        line_width=1,
        padding=20
    )


@pytest.fixture
def mock_surface():
    """Create a mock Pygame surface."""
    surface = Mock(spec=pygame.Surface)
    surface.get_width.return_value = 800
    surface.get_height.return_value = 600
    return surface


@pytest.fixture
def grid():
    """Create a test grid."""
    return HexGrid(dimensions=GridDimensions(width=3, height=3))


def test_display_config_creation():
    """Test that display config can be created with default values."""
    config = DisplayConfig(hex_size=50.0)
    assert config.hex_size == 50.0
    assert config.background_color == (0, 0, 0)
    assert config.line_color == (100, 100, 100)
    assert config.line_width == 1
    assert config.padding == 20


def test_display_config_custom_values():
    """Test that display config accepts custom values."""
    config = DisplayConfig(
        hex_size=40.0,
        background_color=(255, 255, 255),
        line_color=(0, 255, 0),
        line_width=2,
        padding=30
    )
    assert config.hex_size == 40.0
    assert config.background_color == (255, 255, 255)
    assert config.line_color == (0, 255, 0)
    assert config.line_width == 2
    assert config.padding == 30


def test_grid_display_initialization(grid, display_config, mock_surface):
    """Test that grid display can be initialized."""
    display = GridDisplay(grid=grid, config=display_config, surface=mock_surface)
    assert display.grid == grid
    assert display.config == display_config
    assert display.surface == mock_surface


def test_grid_pixel_size_calculation(grid, display_config, mock_surface):
    """Test calculation of grid size in pixels."""
    display = GridDisplay(grid=grid, config=display_config, surface=mock_surface)
    width, height = display._calculate_grid_pixel_size()
    
    # For a 3x3 grid with hex_size=50:
    # hex_width = 100 (2 * hex_size)
    # hex_height = 86.6 (√3 * hex_size)
    # total_width = 3 * 75 + 25 = 250 (width * 3/4 * hex_width + hex_width/4)
    # total_height = 3 * 86.6 + 43.3 = 303.1 (height * hex_height + hex_height/2)
    assert math.isclose(width, 500, rel_tol=1e-2)
    assert math.isclose(height, 129.9, rel_tol=1e-2)


def test_grid_centering(grid, display_config, mock_surface):
    """Test that the grid is properly centered."""
    display = GridDisplay(grid=grid, config=display_config, surface=mock_surface)
    
    # For an 800x600 window, 3x3 grid, and 20px padding:
    # Grid size is ~250x303 pixels
    # Center origin should be at:
    # x = (800 - 250)/2 + 20 = 295
    # y = (600 - 303)/2 + 20 = 168.5
    assert math.isclose(display.transformer.origin_x, 170.0, rel_tol=1e-2)
    assert math.isclose(display.transformer.origin_y, 255.04, rel_tol=1e-2)


def test_window_resize_handling(grid, display_config, mock_surface):
    """Test that window resizing updates the display correctly."""
    display = GridDisplay(grid=grid, config=display_config, surface=mock_surface)
    
    # Mock the new surface creation
    new_surface = Mock(spec=pygame.Surface)
    new_surface.get_width.return_value = 1024
    new_surface.get_height.return_value = 768
    
    with patch('pygame.display.set_mode', return_value=new_surface):
        display.handle_resize((1024, 768))
        
        # For a 1024x768 window, 3x3 grid, and 20px padding:
        # Grid size is still ~250x303 pixels
        # New center origin should be at:
        # x = (1024 - 250)/2 + 20 = 407
        # y = (768 - 303)/2 + 20 = 252.5
        assert math.isclose(display.transformer.origin_x, 282.0, rel_tol=1e-2)
        assert math.isclose(display.transformer.origin_y, 339.04, rel_tol=1e-2)


def test_render_calls(grid, display_config, mock_surface):
    """Test that render method calls the expected functions."""
    display = GridDisplay(grid=grid, config=display_config, surface=mock_surface)
    
    # Replace the renderer with a mock
    display.renderer = Mock()
    
    # Call render
    display.render()
    
    # Verify the surface is cleared and grid is rendered
    mock_surface.fill.assert_called_once_with(display_config.background_color)
    display.renderer.render.assert_called_once_with(mock_surface) 