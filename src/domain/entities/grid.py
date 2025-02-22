from dataclasses import dataclass
from typing import Optional

from ..value_objects.grid_dimensions import GridDimensions
from ..value_objects.grid_position import GridPosition


class InvalidGridPosition(Exception):
    """Exception raised when an invalid grid position is accessed."""

    pass


@dataclass
class HexGrid:
    """A hexagonal grid entity.

    This class represents the core domain entity for our hexagonal grid system.
    It is framework-independent and handles the basic grid structure and validation.

    Attributes:
        dimensions (GridDimensions): The dimensions of the grid
    """

    dimensions: GridDimensions

    def is_valid_position(self, position: GridPosition) -> bool:
        """Check if the given position is within the grid boundaries.

        Args:
            position (GridPosition): The position to validate

        Returns:
            bool: True if the position is valid, False otherwise
        """
        return (
            0 <= position.q < self.dimensions.width
            and 0 <= position.r < self.dimensions.height
        )
