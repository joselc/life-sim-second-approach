"""Command column UI component."""
from typing import Optional

import pygame

from src.config import colors, display


class CommandColumn:
    """Renders the command column and its contents.

    This class is responsible for drawing the command column UI element
    and all of its contents, including the title and (in the future)
    command buttons or other interactive elements.

    Attributes:
        rect (pygame.Rect): Rectangle defining the command column area
        title_font (pygame.font.Font): Font used for the title text
    """

    def __init__(self, rect: pygame.Rect) -> None:
        """Initialize the command column.

        Args:
            rect (pygame.Rect): Rectangle defining the command column area
        """
        self.rect = rect
        self.title_font: Optional[pygame.font.Font] = None
        self._initialize_fonts()

    def _initialize_fonts(self) -> None:
        """Initialize fonts used by the command column."""
        pygame.font.init()
        self.title_font = pygame.font.SysFont(
            "arial", display.TITLE_FONT_SIZE, bold=True
        )

    def render(self, surface: pygame.Surface) -> None:
        """Render the command column and its contents.

        Args:
            surface (pygame.Surface): Surface to render on
        """
        # Draw the command column background
        pygame.draw.rect(surface, colors.COMMAND_COLUMN_BACKGROUND, self.rect)

        # Render the title
        self._render_title(surface)

    def _render_title(self, surface: pygame.Surface) -> None:
        """Render the title text at the top of the command column.

        Args:
            surface (pygame.Surface): Surface to render on
        """
        if self.title_font is None:
            return

        title_surface = self.title_font.render(
            display.TITLE_TEXT, True, colors.COMMAND_COLUMN_TEXT
        )

        # Center the title in the command column
        title_x = self.rect.x + (self.rect.width - title_surface.get_width()) // 2
        title_y = self.rect.y + display.TITLE_PADDING

        surface.blit(title_surface, (title_x, title_y))

    def handle_resize(self, new_rect: pygame.Rect) -> None:
        """Handle resizing of the command column.

        Args:
            new_rect (pygame.Rect): New rectangle for the command column
        """
        self.rect = new_rect
