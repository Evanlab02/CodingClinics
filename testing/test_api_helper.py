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


    @patch("sys.stdout", StringIO())
    def test_add_to_dict_none(self):
        """Testing add to dictionary with no new values"""
        mock_dict = {"Author": "Evan Labuschagne"}
        actual = api_helper.add_to_dict(mock_dict, [], [])
        self.assertEqual(mock_dict, actual)


    @patch("sys.stdout", StringIO())
    def test_add_to_dict(self):
        """Testing add to dictionary with no new values"""
        mock_dict = {"Author": "Evan Labuschagne"}
        actual = api_helper.add_to_dict(mock_dict, ["Age"], [20])
        self.assertEqual({"Author": "Evan Labuschagne", "Age": 20}, actual)
