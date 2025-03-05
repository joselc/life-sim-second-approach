"""Tests for the LayoutManager class."""
import unittest
from unittest.mock import MagicMock, patch

import pygame

from src.config import display
from src.interfaces.pygame_adapter.ui.layout_manager import LayoutManager


class TestLayoutManager(unittest.TestCase):
    """Test cases for the LayoutManager class."""

    def setUp(self) -> None:
        """Set up test case with a LayoutManager instance."""
        # Initialize pygame for testing
        pygame.init()
        self.test_size = (800, 600)
        self.layout_manager = LayoutManager(self.test_size)

    def tearDown(self) -> None:
        """Clean up after test case."""
        pygame.quit()

    def test_initial_calculation(self) -> None:
        """Test initial layout calculations."""
        # Column should be 1/5 of the window width
        expected_column_width = int(self.test_size[0] * display.COMMAND_COLUMN_RATIO)
        self.assertEqual(self.layout_manager.command_area.width, expected_column_width)
        self.assertEqual(self.layout_manager.command_area.height, self.test_size[1])

        # Separator should be positioned after the command column
        self.assertEqual(self.layout_manager.separator_rect.x, expected_column_width)
        self.assertEqual(
            self.layout_manager.separator_rect.width, display.AREA_SEPARATOR
        )

        # Simulation area should start after command column + separator
        expected_sim_x = expected_column_width + display.AREA_SEPARATOR
        expected_sim_width = self.test_size[0] - expected_sim_x

        self.assertEqual(self.layout_manager.simulation_area.x, expected_sim_x)
        self.assertEqual(self.layout_manager.simulation_area.width, expected_sim_width)
        self.assertEqual(self.layout_manager.simulation_area.height, self.test_size[1])

    def test_resize_handling(self) -> None:
        """Test layout recalculation after resize."""
        new_size = (1024, 768)
        self.layout_manager.handle_resize(new_size)

        # Check that new sizes are calculated correctly
        expected_new_column_width = int(new_size[0] * display.COMMAND_COLUMN_RATIO)
        self.assertEqual(
            self.layout_manager.command_area.width, expected_new_column_width
        )
        self.assertEqual(self.layout_manager.command_area.height, new_size[1])

        # Check separator position after resize
        self.assertEqual(
            self.layout_manager.separator_rect.x, expected_new_column_width
        )

        # Check simulation area after resize
        expected_new_sim_x = expected_new_column_width + display.AREA_SEPARATOR
        expected_new_sim_width = new_size[0] - expected_new_sim_x

        self.assertEqual(self.layout_manager.simulation_area.x, expected_new_sim_x)
        self.assertEqual(
            self.layout_manager.simulation_area.width, expected_new_sim_width
        )
        self.assertEqual(self.layout_manager.simulation_area.height, new_size[1])

    @patch("pygame.draw.rect")
    def test_render_separator(self, mock_draw_rect: MagicMock) -> None:
        """Test that separator is rendered correctly."""
        mock_surface = MagicMock()

        self.layout_manager.render_separator(mock_surface)

        mock_draw_rect.assert_called_once()
