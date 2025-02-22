"""Coordinate transformation utilities for rendering hexagonal grids."""
from dataclasses import dataclass
from math import sqrt
from typing import Tuple

from src.domain.value_objects.grid_position import GridPosition


@dataclass(frozen=True)
class PixelPosition:
    """Screen coordinates for rendering.

    This class represents a position in pixel coordinates on the screen.
    It is specific to the rendering layer and should not be used in domain logic.

    Attributes:
        x (float): The x-coordinate in pixels
        y (float): The y-coordinate in pixels
    """

    x: float
    y: float


class HexToPixelTransformer:
    """Transforms hex grid coordinates to pixel coordinates for rendering.

    This class handles the conversion between hex grid coordinates (q,r)
    and screen pixel coordinates (x,y) for flat-topped hexagons.

    The conversion uses the following constants for flat-topped hexagons:
    - Width = size * 2
    - Height = size * sqrt(3)
    - Horizontal spacing = width * 3/4
    - Vertical spacing = height

    Attributes:
        hex_size (float): The size (radius) of a hexagon in pixels
        origin_x (float): The x-coordinate of the grid's origin in pixels
        origin_y (float): The y-coordinate of the grid's origin in pixels
    """

    def __init__(self, hex_size: float, origin_x: float, origin_y: float):
        """Initialize the transformer with hexagon size and origin position.

        Args:
            hex_size (float): The size (radius) of a hexagon in pixels
            origin_x (float): The x-coordinate of the grid's origin in pixels
            origin_y (float): The y-coordinate of the grid's origin in pixels
        """
        self.hex_size = hex_size
        self.origin_x = origin_x
        self.origin_y = origin_y

        # Precalculate constants for flat-topped hexagons
        self.width = hex_size * 2  # Distance between parallel sides
        self.height = hex_size * sqrt(3)  # Distance between vertices

    def hex_to_pixel(self, hex_pos: GridPosition) -> PixelPosition:
        """Convert hex coordinates to pixel coordinates.

        Args:
            hex_pos (GridPosition): The hex grid position to convert

        Returns:
            PixelPosition: The corresponding pixel coordinates
        """
        # For flat-topped hexagons in rectangular layout:
        # x = origin_x + size * (3/2 * q + (r % 2))  # Use 3/2 for proper horizontal spacing
        # y = origin_y + size * sqrt(3)/2 * r        # Keep current vertical spacing
        x = self.origin_x + self.hex_size * (3 * hex_pos.q + (hex_pos.r % 2) * 1.5)
        y = self.origin_y + self.hex_size * (sqrt(3) / 2) * hex_pos.r
        return PixelPosition(x=x, y=y)

    def get_hex_vertices(self, center: PixelPosition) -> list[Tuple[float, float]]:
        """Get the vertex coordinates for a hexagon at the given center position.

        Args:
            center (PixelPosition): The center position of the hexagon

        Returns:
            list[Tuple[float, float]]: List of (x,y) coordinates for the vertices
        """
        # Flat-topped hexagon vertices, starting at the rightmost point
        # and going counter-clockwise
        vertices = [
            (center.x + self.hex_size, center.y),  # Right
            (center.x + self.hex_size / 2, center.y + self.height / 2),  # Bottom-right
            (center.x - self.hex_size / 2, center.y + self.height / 2),  # Bottom-left
            (center.x - self.hex_size, center.y),  # Left
            (center.x - self.hex_size / 2, center.y - self.height / 2),  # Top-left
            (center.x + self.hex_size / 2, center.y - self.height / 2),  # Top-right
        ]
        return vertices
