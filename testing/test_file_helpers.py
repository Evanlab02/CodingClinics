"""
Tests all file helper functions
"""

import unittest, json

from unittest.mock import patch
from io import StringIO
from file_helpers import json_helper

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_json_overwrite_file(self):
        """Testing function writes correctly to file"""
        expected = {
            "testing": "this function is testing my tests",
            "tests": "unittests"
        }

        json_helper.overwrite_json(expected, "testing/testing_files/testing.json")

        with open("testing/testing_files/testing.json", "r") as read_file:
            actual = json.load(read_file)

        self.assertEqual(expected, actual)

        expected = {}

        json_helper.overwrite_json(expected, "testing/testing_files/testing.json")

        with open("testing/testing_files/testing.json", "r") as read_file:
            actual = json.load(read_file)

        self.assertEqual(expected, actual)