"""Layout manager for the UI components."""
from typing import Tuple

import pygame

from src.config import colors, display


class LayoutManager:
    """Manages UI layout calculations and areas.

    This class handles calculating the dimensions and positions of different
    UI sections based on the window size. It manages the command column and
    simulation areas, ensuring they resize proportionally when the window size
    changes.

    Attributes:
        window_size (Tuple[int, int]): Current window width and height
        command_area (pygame.Rect): Rectangle defining the command column area
        simulation_area (pygame.Rect): Rectangle defining the simulation area
        separator_rect (pygame.Rect): Rectangle defining the area separator
    """

    def __init__(self, window_size: Tuple[int, int]) -> None:
        """Initialize the layout manager with the window size.

        Args:
            window_size (Tuple[int, int]): Initial window width and height
        """
        self.window_size = window_size
        self.command_area = self.calculate_command_area()
        self.simulation_area = self.calculate_simulation_area()
        self.separator_rect = self.calculate_separator_rect()

    def calculate_command_area(self) -> pygame.Rect:
        """Calculate the rectangle for the command column area.

        Returns:
            pygame.Rect: Rectangle defining the command column area
        """
        window_width, window_height = self.window_size
        column_width = int(window_width * display.COMMAND_COLUMN_RATIO)

        return pygame.Rect(0, 0, column_width, window_height)

    def calculate_simulation_area(self) -> pygame.Rect:
        """Calculate the rectangle for the simulation area.

        Returns:
            pygame.Rect: Rectangle defining the simulation area
        """
        window_width, window_height = self.window_size
        column_width = int(window_width * display.COMMAND_COLUMN_RATIO)
        separator_width = display.AREA_SEPARATOR

        # Start after command column + separator
        start_x = column_width + separator_width
        # Width is remaining space
        sim_width = window_width - start_x

        return pygame.Rect(start_x, 0, sim_width, window_height)

    def calculate_separator_rect(self) -> pygame.Rect:
        """Calculate the rectangle for the area separator.

        Returns:
            pygame.Rect: Rectangle defining the area separator
        """
        column_width = self.command_area.width
        window_height = self.window_size[1]

        # Separator sits between command area and simulation area
        return pygame.Rect(column_width, 0, display.AREA_SEPARATOR, window_height)

    def handle_resize(self, new_size: Tuple[int, int]) -> None:
        """Handle window resize event by recalculating all areas.

        Args:
            new_size (Tuple[int, int]): New window width and height
        """
        self.window_size = new_size
        self.command_area = self.calculate_command_area()
        self.simulation_area = self.calculate_simulation_area()
        self.separator_rect = self.calculate_separator_rect()

    def render_separator(self, surface: pygame.Surface) -> None:
        """Render the separator between command and simulation areas.

        Args:
            surface (pygame.Surface): Surface to render on
        """
        pygame.draw.rect(surface, colors.AREA_SEPARATOR_COLOR, self.separator_rect)
