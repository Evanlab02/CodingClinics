import unittest

from unittest.mock import patch
from io import StringIO
from commands import command_handler

class MyTestCase(unittest.TestCase):

    @patch("sys.stdout", StringIO())
    def test_not_existing_command_return(self):
        expected = f"[red]I did not understand 'unittests'.[/red]"
        actual = command_handler.not_existing_command("unittests")
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_invalid_command(self):
        expected = f"[red]I did not understand 'unittests'.[/red]"
        actual = command_handler.handle_command("code_clinic", "unittests")
        self.assertEqual(expected, actual)
        