import pytest

from src.domain.entities.grid import HexGrid, InvalidGridPosition
from src.domain.value_objects.grid_dimensions import GridDimensions
from src.domain.value_objects.grid_position import GridPosition


def test_grid_creation():
    """Test that a grid can be created with specified dimensions."""
    dimensions = GridDimensions(width=5, height=4)
    grid = HexGrid(dimensions=dimensions)
    assert grid.dimensions.width == 5
    assert grid.dimensions.height == 4


def test_grid_invalid_dimensions():
    """Test that grid creation fails with invalid dimensions."""
    with pytest.raises(ValueError):
        GridDimensions(width=0, height=5)
    with pytest.raises(ValueError):
        GridDimensions(width=5, height=0)
    with pytest.raises(ValueError):
        GridDimensions(width=-1, height=5)
    with pytest.raises(ValueError):
        GridDimensions(width=5, height=-1)


def test_position_validation():
    """Test that grid position validation works correctly."""
    grid = HexGrid(dimensions=GridDimensions(width=3, height=3))

    # Valid positions - all corners and center
    assert grid.is_valid_position(GridPosition(q=0, r=0)) is True  # Top-left corner
    assert grid.is_valid_position(GridPosition(q=2, r=0)) is True  # Top-right corner
    assert grid.is_valid_position(GridPosition(q=0, r=2)) is True  # Bottom-left corner
    assert grid.is_valid_position(GridPosition(q=2, r=2)) is True  # Bottom-right corner
    assert grid.is_valid_position(GridPosition(q=1, r=1)) is True  # Center


def test_position_validation_edge_cases():
    """Test grid position validation for edge cases and boundaries."""
    grid = HexGrid(dimensions=GridDimensions(width=3, height=3))

    # Test all invalid positions around the boundaries
    # Left edge
    assert grid.is_valid_position(GridPosition(q=-1, r=0)) is False
    assert grid.is_valid_position(GridPosition(q=-1, r=1)) is False
    assert grid.is_valid_position(GridPosition(q=-1, r=2)) is False

    # Right edge
    assert grid.is_valid_position(GridPosition(q=3, r=0)) is False
    assert grid.is_valid_position(GridPosition(q=3, r=1)) is False
    assert grid.is_valid_position(GridPosition(q=3, r=2)) is False

    # Top edge
    assert grid.is_valid_position(GridPosition(q=0, r=-1)) is False
    assert grid.is_valid_position(GridPosition(q=1, r=-1)) is False
    assert grid.is_valid_position(GridPosition(q=2, r=-1)) is False

    # Bottom edge
    assert grid.is_valid_position(GridPosition(q=0, r=3)) is False
    assert grid.is_valid_position(GridPosition(q=1, r=3)) is False
    assert grid.is_valid_position(GridPosition(q=2, r=3)) is False

    # Corners (diagonals)
    assert grid.is_valid_position(GridPosition(q=-1, r=-1)) is False
    assert grid.is_valid_position(GridPosition(q=3, r=-1)) is False
    assert grid.is_valid_position(GridPosition(q=-1, r=3)) is False
    assert grid.is_valid_position(GridPosition(q=3, r=3)) is False
