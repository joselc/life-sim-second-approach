import dataclasses
import pytest
from src.domain.value_objects.grid_dimensions import GridDimensions


def test_grid_dimensions_creation():
    """Test that grid dimensions can be created with valid values."""
    dims = GridDimensions(width=5, height=4)
    assert dims.width == 5
    assert dims.height == 4


def test_grid_dimensions_immutability():
    """Test that grid dimensions are immutable."""
    dims = GridDimensions(width=5, height=4)
    with pytest.raises(dataclasses.FrozenInstanceError):
        dims.width = 3
    with pytest.raises(dataclasses.FrozenInstanceError):
        dims.height = 2


def test_grid_dimensions_validation():
    """Test that grid dimensions validation works correctly."""
    with pytest.raises(ValueError, match="Grid width must be a positive integer"):
        GridDimensions(width=0, height=5)
    with pytest.raises(ValueError, match="Grid height must be a positive integer"):
        GridDimensions(width=5, height=0)
    with pytest.raises(ValueError, match="Grid width must be a positive integer"):
        GridDimensions(width=-1, height=5)
    with pytest.raises(ValueError, match="Grid height must be a positive integer"):
        GridDimensions(width=5, height=-1)


def test_grid_dimensions_equality():
    """Test that grid dimensions with same values are equal."""
    dims1 = GridDimensions(width=5, height=4)
    dims2 = GridDimensions(width=5, height=4)
    dims3 = GridDimensions(width=4, height=5)

    assert dims1 == dims2
    assert dims1 != dims3
    assert hash(dims1) == hash(dims2)


def test_grid_dimensions_string_representation():
    """Test string representation of grid dimensions."""
    dims = GridDimensions(width=5, height=4)
    assert str(dims) == "GridDimensions(width=5, height=4)"
