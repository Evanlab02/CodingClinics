"""Tests Settings.py file"""

import unittest

from unittest.mock import patch
from io import StringIO
from first_time_setup.settings import settings


class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """
    STORAGE_DIRECTORY: str = "testing/resources/"

    @patch("sys.stdout", StringIO())
    def test_load_settings(self):
        """Tests load_settings function"""
        file_name = "mock_load_settings.json"
        expected = {"TEST LOAD": "LOAD TEST"}
        actual = settings.load_settings(self.STORAGE_DIRECTORY, file_name)
        self.assertEqual(expected, actual)
