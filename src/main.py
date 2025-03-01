"""Main entry point for the HexLife simulation."""
import sys

import pygame

from src.config import colors, display
from src.domain.entities.grid import HexGrid
from src.domain.value_objects.grid_dimensions import GridDimensions
from src.interfaces.pygame_adapter.rendering.grid_display import (
    DisplayConfig,
    GridDisplay,
)
from src.interfaces.pygame_adapter.ui.command_column import CommandColumn
from src.interfaces.pygame_adapter.ui.layout_manager import LayoutManager


class GameLoop:
    """Main game loop class that handles the simulation lifecycle."""

    def __init__(self) -> None:
        """Initialize the game loop and Pygame."""
        pygame.init()
        self.screen = pygame.display.set_mode(display.WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption(display.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = False

        # Initialize grid and display components
        dimensions = GridDimensions(display.GRID_WIDTH, display.GRID_HEIGHT)
        self.grid = HexGrid(dimensions)

        # Initialize UI layout components
        self.layout_manager = LayoutManager(display.WINDOW_SIZE)
        self.command_column = CommandColumn(self.layout_manager.command_area)

        # Create display configuration for the grid
        display_config = DisplayConfig(
            hex_size=display.HEX_SIZE,
            background_color=colors.BACKGROUND,
            line_color=colors.GRID_LINES,
            line_width=display.GRID_LINE_WIDTH,
            padding=display.GRID_PADDING,
        )

        # Create a subsurface for the simulation area
        self.simulation_surface = self.screen.subsurface(
            self.layout_manager.simulation_area
        )

        # Initialize grid display within the simulation area
        self.grid_display = GridDisplay(
            grid=self.grid, config=display_config, surface=self.simulation_surface
        )

    def handle_events(self) -> None:
        """Process all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                # Ensure minimum window size to avoid layout problems
                width = max(100, event.w)  # Minimum width of 100 pixels
                height = max(100, event.h)  # Minimum height of 100 pixels

                # Create the new window
                self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

                # Update layout components with new size
                self.layout_manager.handle_resize((width, height))
                self.command_column.handle_resize(self.layout_manager.command_area)

                try:
                    # Update simulation surface
                    self.simulation_surface = self.screen.subsurface(
                        self.layout_manager.simulation_area
                    )

                    # Update grid display with new simulation surface
                    self.grid_display.surface = self.simulation_surface
                    self.grid_display.handle_resize(self.simulation_surface.get_size())
                except ValueError as e:
                    # If we get an error creating the subsurface,
                    # use the full screen as a fallback
                    print(f"Warning: Error in resize handling: {e}")
                    self.simulation_surface = self.screen
                    self.grid_display.surface = self.screen
                    self.grid_display.handle_resize(self.screen.get_size())

    def update(self) -> None:
        """Update game state."""
        pass  # Will be implemented in the next step

    def render(self) -> None:
        """Render the current game state."""
        # Clear the whole screen first
        self.screen.fill(colors.BACKGROUND)

        # Render command column
        self.command_column.render(self.screen)

        # Render area separator
        self.layout_manager.render_separator(self.screen)

        # Render grid in simulation area
        self.grid_display.render()

        # Flip the display
        pygame.display.flip()

    def run(self) -> None:
        """Run the main game loop."""
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(display.FPS)

    def cleanup(self) -> None:
        """Clean up resources before exiting."""
        pygame.quit()


def main() -> None:
    """Entry point of the application."""
    game = GameLoop()
    try:
        game.run()
    finally:
        game.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    main()
