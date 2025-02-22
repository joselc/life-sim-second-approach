from dataclasses import dataclass


@dataclass(frozen=True)
class GridDimensions:
    """A value object representing the dimensions of a hexagonal grid.

    This is an immutable value object that represents the size of the grid
    in terms of columns and rows.

    Attributes:
        width (int): The number of columns in the grid
        height (int): The number of rows in the grid
    """

    width: int
    height: int

    def __post_init__(self) -> None:
        """Validate the dimensions after initialization."""
        if self.width <= 0:
            raise ValueError("Grid width must be a positive integer")
        if self.height <= 0:
            raise ValueError("Grid height must be a positive integer")

    def __str__(self) -> str:
        return f"GridDimensions(width={self.width}, height={self.height})"
