"""Main entry point for the HexLife simulation."""
import sys
import pygame

from src.config import display, colors
from src.domain.entities.grid import HexGrid
from src.domain.value_objects.grid_dimensions import GridDimensions
from src.interfaces.pygame_adapter.rendering.grid_display import GridDisplay, DisplayConfig


class GameLoop:
    """Main game loop class that handles the simulation lifecycle."""

    def __init__(self):
        """Initialize the game loop and Pygame."""
        pygame.init()
        self.screen = pygame.display.set_mode(display.WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption(display.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = False

        # Initialize grid and display components
        dimensions = GridDimensions(display.GRID_WIDTH, display.GRID_HEIGHT)
        self.grid = HexGrid(dimensions)
        
        # Create display configuration
        display_config = DisplayConfig(
            hex_size=display.HEX_SIZE,
            background_color=colors.BACKGROUND,
            line_color=colors.GRID_LINES,
            line_width=display.GRID_LINE_WIDTH,
            padding=display.GRID_PADDING
        )
        
        # Initialize grid display
        self.grid_display = GridDisplay(
            grid=self.grid,
            config=display_config,
            surface=self.screen
        )

    def handle_events(self):
        """Process all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.grid_display.handle_resize((event.w, event.h))

    def update(self):
        """Update game state."""
        pass  # Will be implemented in the next step

    def render(self):
        """Render the current game state."""
        self.grid_display.render()
        pygame.display.flip()

    def run(self):
        """Run the main game loop."""
        self.running = True
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(display.FPS)

    def cleanup(self):
        """Cleanup the game loop."""
        pygame.quit()

def main():
    """Entry point of the application."""
    game = GameLoop()
    try:    
        game.run()
    finally:
        game.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    main()
