from dataclasses import dataclass
from typing import List, Tuple


@dataclass(frozen=True)
class GridPosition:
    """A value object representing a position in the hexagonal grid.

    This is an immutable value object that represents a position in the grid
    using axial coordinates (q, r) system for hexagonal grids.

    The axial coordinate system for hexagons uses two axes:
    - q: The column axis (pointing from left to right)
    - r: The row axis (pointing diagonally down-right)

    Attributes:
        q (int): The q-coordinate in the axial coordinate system (column)
        r (int): The r-coordinate in the axial coordinate system (row)
    """

    q: int
    r: int

    # Relative coordinates for neighbors in a flat-topped hexagonal grid
    # Starting from east and going counter-clockwise
    _NEIGHBOR_VECTORS = [
        (1, 0),  # E
        (0, 1),  # SE
        (-1, 1),  # SW
        (-1, 0),  # W
        (0, -1),  # NW
        (1, -1),  # NE
    ]

    def get_neighbors(self) -> List["GridPosition"]:
        """Get all neighboring positions in the grid.

        Returns a list of all six adjacent positions in the hexagonal grid,
        starting from the east position and going counter-clockwise.

        Returns:
            List[GridPosition]: List of neighboring positions
        """
        return [
            GridPosition(q=self.q + dq, r=self.r + dr)
            for dq, dr in self._NEIGHBOR_VECTORS
        ]

    def get_neighbor(self, direction: int) -> "GridPosition":
        """Get a specific neighboring position.

        Args:
            direction (int): Direction index (0=E, 1=SE, 2=SW, 3=W, 4=NW, 5=NE)

        Returns:
            GridPosition: The neighboring position in the specified direction

        Raises:
            ValueError: If direction is not in range [0,5]
        """
        if not 0 <= direction < 6:
            raise ValueError("Direction must be in range [0,5]")
        dq, dr = self._NEIGHBOR_VECTORS[direction]
        return GridPosition(q=self.q + dq, r=self.r + dr)

    def as_tuple(self) -> Tuple[int, int]:
        """Convert the position to a tuple representation.

        Returns:
            Tuple[int, int]: A tuple of (q, r) coordinates
        """
        return (self.q, self.r)

    def __str__(self) -> str:
        return f"GridPosition(q={self.q}, r={self.r})"
