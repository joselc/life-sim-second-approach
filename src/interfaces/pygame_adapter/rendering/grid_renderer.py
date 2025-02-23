"""Grid rendering implementation using Pygame."""
from typing import Tuple

import pygame

from src.domain.entities.grid import HexGrid
from src.domain.value_objects.grid_position import GridPosition

from .coordinate_transformer import HexToPixelTransformer


class GridRenderer:
    """Renders a hexagonal grid using Pygame.

    This class is responsible for drawing the hexagonal grid on the screen.
    It uses the coordinate transformer to convert grid positions to screen
    coordinates and handles the actual Pygame drawing operations.

    Attributes:
        grid (HexGrid): The grid to render
        transformer (HexToPixelTransformer): Coordinate transformer
            for pixel conversion
        line_color (Tuple[int, int, int]): RGB color for grid lines
        line_width (int): Width of grid lines in pixels
    """

    def __init__(
        self,
        grid: HexGrid,
        transformer: HexToPixelTransformer,
        line_color: Tuple[int, int, int] = (100, 100, 100),
        line_width: int = 1,
    ) -> None:
        """Initialize the grid renderer.

        Args:
            grid (HexGrid): The grid to render
            transformer (HexToPixelTransformer): Coordinate transformer
                for pixel conversion
            line_color (Tuple[int, int, int], optional): RGB color for
                grid lines. Defaults to gray (100, 100, 100).
            line_width (int, optional): Width of grid lines in pixels.
                Defaults to 1.
        """
        self.grid = grid
        self.transformer = transformer
        self.line_color = line_color
        self.line_width = line_width

    def render(self, surface: pygame.Surface) -> None:
        """Render the grid on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw on
        """
        # Iterate through all possible grid positions
        for q in range(self.grid.dimensions.width):
            for r in range(self.grid.dimensions.height):
                pos = GridPosition(q=q, r=r)
                if self.grid.is_valid_position(pos):
                    self._draw_hex(surface, pos)

    def _draw_hex(self, surface: pygame.Surface, pos: GridPosition) -> None:
        """Draw a single hexagon at the given grid position.

        Args:
            surface (pygame.Surface): The surface to draw on
            pos (GridPosition): The grid position to draw at
        """
        # Convert grid position to pixel coordinates
        pixel_pos = self.transformer.hex_to_pixel(pos)
        # Get vertex coordinates for the hexagon
        vertices = self.transformer.get_hex_vertices(pixel_pos)
        # Draw the hexagon outline
        pygame.draw.polygon(
            surface,
            self.line_color,
            vertices,
            self.line_width,
        )
