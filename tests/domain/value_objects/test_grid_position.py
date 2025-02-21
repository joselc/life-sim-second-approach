import dataclasses
import pytest
from src.domain.value_objects.grid_position import GridPosition

def test_grid_position_creation():
    """Test that a grid position can be created with coordinates."""
    pos = GridPosition(q=1, r=2)
    assert pos.q == 1
    assert pos.r == 2

def test_grid_position_immutability():
    """Test that grid positions are immutable."""
    pos = GridPosition(q=1, r=2)
    with pytest.raises(dataclasses.FrozenInstanceError):
        pos.q = 3
    with pytest.raises(dataclasses.FrozenInstanceError):
        pos.r = 4

def test_grid_position_equality():
    """Test that grid positions with same coordinates are equal."""
    pos1 = GridPosition(q=1, r=2)
    pos2 = GridPosition(q=1, r=2)
    pos3 = GridPosition(q=2, r=1)
    
    assert pos1 == pos2
    assert pos1 != pos3
    assert hash(pos1) == hash(pos2)

def test_grid_position_as_tuple():
    """Test conversion to tuple representation."""
    pos = GridPosition(q=1, r=2)
    assert pos.as_tuple() == (1, 2)

def test_grid_position_string_representation():
    """Test string representation of grid position."""
    pos = GridPosition(q=1, r=2)
    assert str(pos) == "GridPosition(q=1, r=2)" 