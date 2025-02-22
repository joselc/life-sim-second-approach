"""Tests for the grid renderer."""
from unittest.mock import Mock, patch

import pygame
import pytest

from src.domain.entities.grid import HexGrid
from src.domain.value_objects.grid_dimensions import GridDimensions
from src.domain.value_objects.grid_position import GridPosition
from src.interfaces.pygame_adapter.rendering.coordinate_transformer import (
    HexToPixelTransformer,
    PixelPosition,
)
from src.interfaces.pygame_adapter.rendering.grid_renderer import GridRenderer


@pytest.fixture
def mock_surface():
    """Create a mock Pygame surface."""
    return Mock(spec=pygame.Surface)


@pytest.fixture
def grid():
    """Create a test grid."""
    return HexGrid(dimensions=GridDimensions(width=2, height=2))


@pytest.fixture
def transformer():
    """Create a coordinate transformer for testing."""
    return HexToPixelTransformer(hex_size=50.0, origin_x=100.0, origin_y=100.0)


def test_grid_renderer_initialization(grid, transformer):
    """Test that the grid renderer can be initialized with default values."""
    renderer = GridRenderer(grid=grid, transformer=transformer)
    assert renderer.grid == grid
    assert renderer.transformer == transformer
    assert renderer.line_color == (100, 100, 100)
    assert renderer.line_width == 1


def test_grid_renderer_custom_style(grid, transformer):
    """Test that the grid renderer accepts custom style parameters."""
    renderer = GridRenderer(
        grid=grid, transformer=transformer, line_color=(255, 0, 0), line_width=2
    )
    assert renderer.line_color == (255, 0, 0)
    assert renderer.line_width == 2


def test_grid_renderer_draws_all_valid_positions(grid, transformer, mock_surface):
    """Test that the renderer draws all valid positions in the grid."""
    renderer = GridRenderer(grid=grid, transformer=transformer)

    # Mock the draw_polygon function
    with patch("pygame.draw.polygon") as mock_draw:
        renderer.render(mock_surface)

        # For a 2x2 grid, should call draw_polygon 4 times (once per cell)
        assert mock_draw.call_count == 4

        # Verify each call used the correct color and line width
        for call in mock_draw.call_args_list:
            args, kwargs = call
            assert args[1] == (100, 100, 100)  # line_color
            assert args[3] == 1  # line_width


def test_grid_renderer_correct_vertex_calculation(grid, transformer, mock_surface):
    """Test that the renderer calculates correct vertices for hexagons."""
    renderer = GridRenderer(grid=grid, transformer=transformer)

    # Mock the transformer's methods
    expected_pixel_pos = PixelPosition(x=150.0, y=150.0)
    expected_vertices = [
        (x, y)
        for x, y in [
            (200, 150),
            (175, 193.3),
            (125, 193.3),
            (100, 150),
            (125, 106.7),
            (175, 106.7),
        ]
    ]

    with patch.object(
        transformer, "hex_to_pixel", return_value=expected_pixel_pos
    ) as mock_hex_to_pixel:
        with patch.object(
            transformer, "get_hex_vertices", return_value=expected_vertices
        ) as mock_get_vertices:
            with patch("pygame.draw.polygon") as mock_draw:
                renderer.render(mock_surface)

                # Verify transformer methods were called for each grid position
                assert mock_hex_to_pixel.call_count == 4
                assert mock_get_vertices.call_count == 4

                # Verify the vertices were used in drawing
                for call in mock_draw.call_args_list:
                    args, kwargs = call
                    assert args[2] == expected_vertices
