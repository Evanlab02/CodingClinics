"""
Tests api_helper
"""

import unittest

from unittest.mock import patch
from io import StringIO
from google_api_helpers import api_helper

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_get_api_detials(self):
        """Testing function returns correct value"""
        expected = {
        "permissions": ['https://www.googleapis.com/auth/calendar'],
        "credentials": None,
        "connection": None
        }
        actual = api_helper.get_api_details()
        self.assertEqual(expected, actual)
