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


def test_get_neighbors():
    """Test getting all neighbors of a position."""
    pos = GridPosition(q=2, r=2)
    neighbors = pos.get_neighbors()

    # Should return exactly 6 neighbors
    assert len(neighbors) == 6

    # Verify each neighbor position
    expected_neighbors = [
        GridPosition(q=3, r=2),  # E
        GridPosition(q=2, r=3),  # SE
        GridPosition(q=1, r=3),  # SW
        GridPosition(q=1, r=2),  # W
        GridPosition(q=2, r=1),  # NW
        GridPosition(q=3, r=1),  # NE
    ]

    assert set(neighbors) == set(expected_neighbors)


def test_get_neighbor():
    """Test getting specific neighbors by direction."""
    pos = GridPosition(q=2, r=2)

    # Test each direction
    assert pos.get_neighbor(0) == GridPosition(q=3, r=2)  # E
    assert pos.get_neighbor(1) == GridPosition(q=2, r=3)  # SE
    assert pos.get_neighbor(2) == GridPosition(q=1, r=3)  # SW
    assert pos.get_neighbor(3) == GridPosition(q=1, r=2)  # W
    assert pos.get_neighbor(4) == GridPosition(q=2, r=1)  # NW
    assert pos.get_neighbor(5) == GridPosition(q=3, r=1)  # NE

    # Test invalid direction
    with pytest.raises(ValueError, match="Direction must be in range"):
        pos.get_neighbor(-1)
    with pytest.raises(ValueError, match="Direction must be in range"):
        pos.get_neighbor(6)
