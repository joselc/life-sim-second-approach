"""Integration tests for UI components with the main game loop."""
import unittest
from unittest.mock import MagicMock, patch

import pygame

from src.config import display
from src.interfaces.pygame_adapter.ui.command_column import CommandColumn
from src.interfaces.pygame_adapter.ui.layout_manager import LayoutManager
from src.main import GameLoop


class TestUIIntegration(unittest.TestCase):
    """Integration tests for UI components in the game loop."""

    @patch("pygame.display.set_mode")
    def test_game_loop_initialization(self, mock_set_mode: MagicMock) -> None:
        """Test that game loop initializes UI components correctly."""
        # Mock the pygame surface
        mock_surface = MagicMock()
        mock_surface.subsurface.return_value = mock_surface
        mock_set_mode.return_value = mock_surface

        # Mock pygame initialization
        with patch("pygame.init"), patch("pygame.time.Clock"), patch(
            "src.interfaces.pygame_adapter.rendering.grid_display.GridDisplay"
        ):
            # Create the game loop
            game_loop = GameLoop()

            # Check that layout components are initialized
            self.assertIsInstance(game_loop.layout_manager, LayoutManager)
            self.assertIsInstance(game_loop.command_column, CommandColumn)

            # Check that simulation surface is created
            mock_surface.subsurface.assert_called_with(
                game_loop.layout_manager.simulation_area
            )

    @patch("pygame.display.set_mode")
    def test_resize_handling(self, mock_set_mode: MagicMock) -> None:
        """Test that resize is handled correctly by all components."""
        # Mock the pygame surface
        mock_surface = MagicMock()
        mock_surface.subsurface.return_value = mock_surface
        mock_set_mode.return_value = mock_surface

        # Mock pygame initialization
        with patch("pygame.init"), patch("pygame.time.Clock"):
            # Create the game loop with a mocked grid display
            game_loop = GameLoop()

            # Replace the grid display with a mock
            game_loop.grid_display = MagicMock()

            # Mock layout manager and command column
            game_loop.layout_manager = MagicMock()
            game_loop.layout_manager.simulation_area = pygame.Rect(200, 0, 800, 600)
            game_loop.layout_manager.command_area = pygame.Rect(0, 0, 200, 600)
            game_loop.command_column = MagicMock()

            # Create mock event
            mock_event = MagicMock()
            mock_event.type = pygame.VIDEORESIZE
            mock_event.w = 1024
            mock_event.h = 768

            # Mock pygame event queue
            with patch("pygame.event.get", return_value=[mock_event]):
                # Handle the resize event
                game_loop.handle_events()

                # Check that layout manager's handle_resize was called
                game_loop.layout_manager.handle_resize.assert_called_once_with(
                    (1024, 768)
                )

                # Check that command column's handle_resize was called
                game_loop.command_column.handle_resize.assert_called_once_with(
                    game_loop.layout_manager.command_area
                )

                # Check that grid display's handle_resize was called
                game_loop.grid_display.handle_resize.assert_called_once()

    @patch("pygame.display.set_mode")
    def test_render_sequence(self, mock_set_mode: MagicMock) -> None:
        """Test that rendering happens in the correct sequence."""
        # Mock the pygame surface
        mock_surface = MagicMock()
        mock_surface.subsurface.return_value = mock_surface
        mock_set_mode.return_value = mock_surface

        # Mock pygame initialization
        with patch("pygame.init"), patch("pygame.time.Clock"), patch(
            "src.interfaces.pygame_adapter.rendering.grid_display.GridDisplay"
        ) as mock_grid_display, patch("pygame.display.flip") as mock_flip:
            # Create a mock grid display instance
            mock_grid_display_instance = MagicMock()
            mock_grid_display.return_value = mock_grid_display_instance

            # Create the game loop
            game_loop = GameLoop()

            # Mock layout manager and command column
            game_loop.layout_manager = MagicMock()
            game_loop.command_column = MagicMock()
            game_loop.grid_display = MagicMock()

            # Call render
            game_loop.render()

            # Check the rendering sequence - command column should be rendered first
            self.assertEqual(
                game_loop.command_column.render.call_count,
                1,
                "Command column should be rendered once",
            )

            # Check that separator is rendered
            self.assertEqual(
                game_loop.layout_manager.render_separator.call_count,
                1,
                "Separator should be rendered once",
            )

            # Check that grid is rendered
            self.assertEqual(
                game_loop.grid_display.render.call_count,
                1,
                "Grid should be rendered once",
            )

            # Check that display.flip is called
            mock_flip.assert_called_once()
