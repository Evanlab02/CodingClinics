"""
Tests token.py
"""

import unittest

from unittest.mock import patch
from io import StringIO
from authentication import token
from google_api_helpers.api_helper import get_api_details

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_load_empty_token(self):
        """Testing function returns correct value"""
        expected = None
        actual = token.load_token("", get_api_details()["permissions"])
        self.assertEqual(expected, actual)
