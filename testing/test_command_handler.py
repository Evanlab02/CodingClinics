"""
Tests command handler
"""

import unittest

from unittest.mock import patch
from io import StringIO
from commands import command_handler

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_not_existing_command_return(self):
        """Testing function returns correct value"""
        expected = "[red]I did not understand 'unittests'.[/red]"
        actual = command_handler.not_existing_command("unittests")
        self.assertEqual(expected, actual)
        