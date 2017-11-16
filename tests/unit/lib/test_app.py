"""Unit tests for the ``lib.app`` module."""

from unittest import TestCase

from inc.lib import app


class TestApp(TestCase):
    """Test suite for the ``lib.app`` module."""

    def test_run(self):
        """A dummy test."""
        output = []
        app.run(output.append)
        self.assertEqual(output, ["Hello world."])
