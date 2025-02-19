"""Main entry point for the HexLife simulation."""
import sys
from typing import NoReturn

import pygame

from src.config import colors, display

class GameLoop:
    """Main game loop handler following clean architecture principles."""
    
    def __init__(self) -> None:
        """Initialize pygame and create the main window."""
        pygame.init()
        self.screen = pygame.display.set_mode(display.WINDOW_SIZE)
        pygame.display.set_caption(display.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = False
        
    def handle_events(self) -> None:
        """Process all pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
    def update(self) -> None:
        """Update game state."""
        pass  # Will be implemented as we add simulation features
        
    def render(self) -> None:
        """Render the current game state."""
        self.screen.fill(colors.BACKGROUND)
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
        """Clean up pygame resources."""
        pygame.quit()

def main() -> NoReturn:
    """Main entry point of the application."""
    game = GameLoop()
    try:
        game.run()
    finally:
        game.cleanup()
    sys.exit(0)

if __name__ == "__main__":
    main() 