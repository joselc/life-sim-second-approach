"""Tests for the coordinate transformation utilities."""
import dataclasses
import math
import pytest

from src.domain.value_objects.grid_position import GridPosition
from src.interfaces.pygame_adapter.rendering.coordinate_transformer import (
    HexToPixelTransformer,
    PixelPosition,
)


def test_pixel_position_creation():
    """Test that pixel positions can be created."""
    pos = PixelPosition(x=100.0, y=200.0)
    assert pos.x == 100.0
    assert pos.y == 200.0


def test_pixel_position_immutability():
    """Test that pixel positions are immutable."""
    pos = PixelPosition(x=100.0, y=200.0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        pos.x = 300.0
    with pytest.raises(dataclasses.FrozenInstanceError):
        pos.y = 400.0


def test_hex_to_pixel_origin():
    """Test conversion of hex coordinates at origin."""
    transformer = HexToPixelTransformer(hex_size=50.0, origin_x=400.0, origin_y=300.0)
    pixel_pos = transformer.hex_to_pixel(GridPosition(q=0, r=0))
    assert pixel_pos.x == 400.0  # origin_x
    assert pixel_pos.y == 300.0  # origin_y


def test_hex_to_pixel_positive_coordinates():
    """Test conversion of positive hex coordinates."""
    transformer = HexToPixelTransformer(hex_size=50.0, origin_x=400.0, origin_y=300.0)
    
    # Test q-axis (horizontal movement)
    pixel_pos = transformer.hex_to_pixel(GridPosition(q=1, r=0))
    assert pixel_pos.x == (400.0 + (50.0 * 3)) # origin_x + h_spacing
    assert pixel_pos.y == 300.0 + (50.0 * (math.sqrt(3) / 2) * 0)  # origin_y + v_spacing/2
    
    # Test r-axis (vertical movement)
    pixel_pos = transformer.hex_to_pixel(GridPosition(q=0, r=1))
    assert pixel_pos.x == 400.0  + 50 * (3 * 0 + 1 * 1.5)# origin_x
    assert pixel_pos.y == 300.0 + (50.0 * (math.sqrt(3) / 2) * 1)  # origin_y + v_spacing


def test_hex_to_pixel_negative_coordinates():
    """Test conversion of negative hex coordinates."""
    transformer = HexToPixelTransformer(hex_size=50.0, origin_x=400.0, origin_y=300.0)
    
    # Test negative q-axis
    pixel_pos = transformer.hex_to_pixel(GridPosition(q=-1, r=0))
    assert pixel_pos.x == 400.0 + 50.0 * (3 * -1 + 0 * 1.5)   # origin_x - h_spacing
    assert pixel_pos.y == 300.0 + (50.0 * (math.sqrt(3) / 2) * 0)  # origin_y - v_spacing/2
    
    # Test negative r-axis
    pixel_pos = transformer.hex_to_pixel(GridPosition(q=0, r=-1))
    assert pixel_pos.x == 400.0 + 50.0 * (3 * 0 + 1 * 1.5)  # origin_x
    assert pixel_pos.y == 300.0 + (50.0 * (math.sqrt(3) / 2) * -1)  # origin_y - v_spacing


def test_get_hex_vertices():
    """Test calculation of hexagon vertices."""
    transformer = HexToPixelTransformer(hex_size=50.0, origin_x=0.0, origin_y=0.0)
    center = PixelPosition(x=100.0, y=100.0)
    vertices = transformer.get_hex_vertices(center)
    
    # Should return 6 vertices
    assert len(vertices) == 6
    
    # Verify each vertex is the correct distance from center
    for x, y in vertices:
        # Distance from center to any vertex should equal hex_size
        distance = math.sqrt((x - center.x)**2 + (y - center.y)**2)
        assert math.isclose(distance, 50.0, rel_tol=1e-9)
    
    # Verify vertices are in counter-clockwise order starting from rightmost point
    assert vertices[0][0] > vertices[2][0]  # Right x > Left x
    assert vertices[1][1] > vertices[4][1]  # Bottom y > Top y 