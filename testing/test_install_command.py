"""
Primarily Tests The Install Functions
"""

import unittest

from unittest.mock import patch
from io import StringIO
from install_program import install_helper

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_source_program(self):
        """Tests if program does return source if it contains '.py'"""
        expected = "source"
        actual = install_helper.get_program_type("code_clinic.py")
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_bin_program(self):
        """Tests if program does return source if it does not contain '.py'"""
        expected = "bin"
        actual = install_helper.get_program_type("code_clinic")
        self.assertEqual(expected, actual)
