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

        # Ensure we have a positive window size
        window_width = max(1, window_width)
        window_height = max(1, window_height)

        # Calculate the column width as a proportion of the window width
        column_width = int(window_width * display.COMMAND_COLUMN_RATIO)

        # Ensure the column has at least 1 pixel width, but doesn't exceed window width
        column_width = max(1, min(column_width, window_width))

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

        # Ensure the simulation area has at least 1 pixel width
        # Width is remaining space (but at least 1 pixel to avoid errors)
        sim_width = max(1, window_width - start_x)

        # Make sure the simulation area doesn't extend beyond the window
        if start_x + sim_width > window_width:
            sim_width = window_width - start_x

        # As a final safety check, ensure all values are valid
        start_x = max(0, min(start_x, window_width - 1))
        sim_width = max(1, min(sim_width, window_width - start_x))
        window_height = max(1, window_height)

        return pygame.Rect(start_x, 0, sim_width, window_height)

    def calculate_separator_rect(self) -> pygame.Rect:
        """Calculate the rectangle for the area separator.

        Returns:
            pygame.Rect: Rectangle defining the area separator
        """
        window_width, window_height = self.window_size
        column_width = self.command_area.width

        # Ensure we have valid dimensions
        window_height = max(1, window_height)
        separator_width = min(display.AREA_SEPARATOR, window_width - column_width)

        # If there's no room for a separator, make it invisible
        if separator_width <= 0:
            separator_width = 0

        # Don't let the separator extend beyond the window
        x_pos = min(column_width, window_width - separator_width)

        # Separator sits between command area and simulation area
        return pygame.Rect(x_pos, 0, separator_width, window_height)

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
