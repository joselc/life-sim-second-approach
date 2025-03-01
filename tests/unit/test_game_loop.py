"""Unit tests for the game loop implementation."""
from unittest.mock import MagicMock, create_autospec, patch

import pygame
import pytest

from src.main import GameLoop


@pytest.fixture
def mock_pygame() -> MagicMock:
    """Set up mock for pygame module."""
    with patch("src.main.pygame") as mock:
        # Create a proper surface mock
        surface_mock = create_autospec(pygame.Surface)
        surface_mock.fill = MagicMock()

        # Mock display module
        mock.display.set_mode.return_value = surface_mock
        mock.display.set_caption = MagicMock()
        mock.display.flip = MagicMock()

        # Mock drawing functions
        mock.draw = MagicMock()
        mock.draw.polygon = MagicMock()  # This is the key addition

        # Mock time module
        clock_mock = MagicMock()
        clock_mock.tick = MagicMock()
        mock.time.Clock.return_value = clock_mock

        # Mock event module
        mock.event.get.return_value = []

        # Mock QUIT and VIDEORESIZE constants
        mock.QUIT = pygame.QUIT
        mock.VIDEORESIZE = pygame.VIDEORESIZE
        mock.RESIZABLE = pygame.RESIZABLE

        yield mock


def test_game_loop_initialization(mock_pygame: MagicMock) -> None:
    """Test that GameLoop initializes pygame and creates window correctly."""
    game = GameLoop()

    # Check pygame initialization
    mock_pygame.init.assert_called_once()

    # Check window creation
    mock_pygame.display.set_mode.assert_called_once()
    mock_pygame.display.set_caption.assert_called_once()

    # Check clock creation
    mock_pygame.time.Clock.assert_called_once()

    # Check initial state
    assert not game.running


def test_game_loop_cleanup(mock_pygame: MagicMock) -> None:
    """Test that cleanup properly calls pygame.quit()."""
    game = GameLoop()
    game.cleanup()
    mock_pygame.quit.assert_called_once()


def test_game_loop_handle_quit_event(mock_pygame: MagicMock) -> None:
    """Test that quit event stops the game loop."""
    game = GameLoop()
    game.running = True

    # Create a mock event with the QUIT type
    quit_event = MagicMock()
    quit_event.type = pygame.QUIT
    mock_pygame.event.get.return_value = [quit_event]

    game.handle_events()
    assert not game.running


def test_game_loop_render(mock_pygame: MagicMock) -> None:
    """Test that render method updates the display."""
    with patch("src.main.GridDisplay") as mock_grid_display, \
         patch("src.main.LayoutManager") as mock_layout_manager, \
         patch("src.main.CommandColumn") as mock_command_column:
        
        # Create instances of the mocks
        mock_grid_display_instance = MagicMock()
        mock_grid_display.return_value = mock_grid_display_instance
        
        mock_layout_manager_instance = MagicMock()
        mock_layout_manager.return_value = mock_layout_manager_instance
        
        mock_command_column_instance = MagicMock()
        mock_command_column.return_value = mock_command_column_instance

        game = GameLoop()
        
        # Replace the real objects with mocks to avoid pygame
        game.layout_manager = mock_layout_manager_instance
        game.command_column = mock_command_column_instance
        game.grid_display = mock_grid_display_instance
        
        game.render()

        # Check that all rendering components are called
        mock_command_column_instance.render.assert_called_once()
        mock_layout_manager_instance.render_separator.assert_called_once()
        mock_grid_display_instance.render.assert_called_once()
        
        # Check that display was flipped
        mock_pygame.display.flip.assert_called_once()


def test_game_loop_run_sequence(mock_pygame: MagicMock) -> None:
    """Test that run method executes the game loop in correct sequence."""
    with patch("src.main.GridDisplay") as mock_grid_display, \
         patch("src.main.LayoutManager") as mock_layout_manager, \
         patch("src.main.CommandColumn") as mock_command_column:
        
        # Create instances of the mocks
        mock_grid_display_instance = MagicMock()
        mock_grid_display.return_value = mock_grid_display_instance
        
        mock_layout_manager_instance = MagicMock()
        mock_layout_manager.return_value = mock_layout_manager_instance
        
        mock_command_column_instance = MagicMock()
        mock_command_column.return_value = mock_command_column_instance

        game = GameLoop()
        
        # Replace the real objects with mocks to avoid pygame
        game.layout_manager = mock_layout_manager_instance
        game.command_column = mock_command_column_instance
        game.grid_display = mock_grid_display_instance

        # Make the game loop run only once
        def stop_after_one_iteration(*args: tuple, **kwargs: dict) -> None:
            game.running = False

        mock_pygame.time.Clock().tick.side_effect = stop_after_one_iteration

        game.run()

        # Check that the game loop executed all steps
        assert mock_pygame.event.get.called
        assert mock_command_column_instance.render.called
        assert mock_layout_manager_instance.render_separator.called
        assert mock_grid_display_instance.render.called
        assert mock_pygame.display.flip.called
        assert mock_pygame.time.Clock().tick.called
