"""
Tests token.py
"""

import unittest
import os

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


    @patch("sys.stdout", StringIO())
    def test_delete_non_existing_token(self):
        """Testing function returns correct value"""
        expected = False
        actual = token.remove_token("token.json")
        self.assertEqual(expected, actual)

    @patch("sys.stdout", StringIO())
    def test_delete_existing_token(self):
        """Testing function returns correct value"""
        os.system("touch token.json")

        expected = True
        actual = token.remove_token("")
        self.assertEqual(expected, actual)
