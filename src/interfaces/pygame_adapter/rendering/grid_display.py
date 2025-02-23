"""Grid display management for the hexagonal grid."""
from dataclasses import dataclass
from typing import Tuple

import pygame

from src.domain.entities.grid import HexGrid

from .coordinate_transformer import HexToPixelTransformer
from .grid_renderer import GridRenderer


@dataclass
class DisplayConfig:
    """Configuration for grid display.

    Attributes:
        hex_size (float): Size (radius) of hexagons in pixels
        background_color (Tuple[int, int, int]): RGB color for background
        line_color (Tuple[int, int, int]): RGB color for grid lines
        line_width (int): Width of grid lines in pixels
        padding (int): Minimum padding around the grid in pixels
    """

    hex_size: float
    background_color: Tuple[int, int, int] = (0, 0, 0)
    line_color: Tuple[int, int, int] = (100, 100, 100)
    line_width: int = 1
    padding: int = 20


class GridDisplay:
    """Manages the display of the hexagonal grid.

    This class handles:
    - Grid positioning and centering
    - Window resize handling
    - Grid rendering with proper configuration

    Attributes:
        grid (HexGrid): The grid to display
        config (DisplayConfig): Display configuration
        surface (pygame.Surface): The surface to render on
        transformer (HexToPixelTransformer): Coordinate transformer
        renderer (GridRenderer): Grid renderer
    """

    def __init__(
        self,
        grid: HexGrid,
        config: DisplayConfig,
        surface: pygame.Surface
    ) -> None:
        """Initialize the grid display.

        Args:
            grid (HexGrid): The grid to display
            config (DisplayConfig): Display configuration parameters
            surface (pygame.Surface): The surface to render on
        """
        self.grid = grid
        self.config = config
        self.surface = surface

        # Initialize with centered grid
        self.transformer = self._create_centered_transformer()
        self.renderer = GridRenderer(
            grid=grid,
            transformer=self.transformer,
            line_color=config.line_color,
            line_width=config.line_width,
        )

    def _calculate_grid_pixel_size(self) -> Tuple[float, float]:
        """Calculate the total size of the grid in pixels.

        Returns:
            Tuple[float, float]: The (width, height) of the grid in pixels
        """
        # For flat-topped hexagons:
        # Total width = columns * (3 * size) + size
        # Total height = rows * (sqrt(3)/2 * size)
        total_width = (
            self.grid.dimensions.width * 3 * self.config.hex_size
        ) + self.config.hex_size
        total_height = self.grid.dimensions.height * (
            self.config.hex_size * (3**0.5) / 2
        )

        return total_width, total_height

    def _create_centered_transformer(self) -> HexToPixelTransformer:
        """Create a transformer with the grid centered in the window.

        Returns:
            HexToPixelTransformer: A new transformer with centered origin
        """
        # Get surface and grid dimensions
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()
        grid_width, grid_height = self._calculate_grid_pixel_size()

        # Calculate origin position to center the grid
        origin_x = (surface_width - grid_width) / 2
        origin_y = (surface_height - grid_height) / 2

        # Add padding
        origin_x += self.config.padding
        origin_y += self.config.padding

        return HexToPixelTransformer(
            hex_size=self.config.hex_size,
            origin_x=origin_x,
            origin_y=origin_y
        )

    def handle_resize(self, new_size: Tuple[int, int]) -> None:
        """Handle window resize event.

        Args:
            new_size (Tuple[int, int]): New window size (width, height)
        """
        # Update surface reference
        self.surface = pygame.display.set_mode(new_size, pygame.RESIZABLE)
        # Recalculate transformer for new window size
        self.transformer = self._create_centered_transformer()
        # Update renderer with new transformer
        self.renderer = GridRenderer(
            grid=self.grid,
            transformer=self.transformer,
            line_color=self.config.line_color,
            line_width=self.config.line_width,
        )

    def render(self) -> None:
        """Render the grid centered in the window."""
        # Clear background
        self.surface.fill(self.config.background_color)
        # Render grid
        self.renderer.render(self.surface)
