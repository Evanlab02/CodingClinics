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


    @patch("sys.stdout", StringIO())
    def test_check_valid_settings_combination_1(self):
        """Tests check_settings function on a valid settings file"""
        mock_settings = {"calendarID": "ABCD", "DATA FORMAT": "JSON"}
        actual = settings.check_settings(mock_settings)
        self.assertEqual(True, actual)


    @patch("sys.stdout", StringIO())
    def test_check_invalid_settings_no_data_formatting(self):
        """Tests check_settings function on a invalid settings file with no 
        data formatting key-value pair"""
        mock_settings = {"calendarID": "ABCD"}
        actual = settings.check_settings(mock_settings)
        self.assertEqual(False, actual)


    @patch("sys.stdout", StringIO())
    def test_check_valid_settings_keys(self):
        """Tests check_keys function on a valid settings file"""
        mock_settings = {"calendarID": "", "DATA FORMAT": ""}
        actual = settings.check_keys(mock_settings.keys())
        self.assertEqual(True, actual)


    @patch("sys.stdout", StringIO())
    def test_check_invalid_settings_keys(self):
        """Tests check_keys function on a invalid settings file with no 
        data format key-value pair"""
        mock_settings = {"calendarID": ""}
        actual = settings.check_keys(mock_settings.keys())
        self.assertEqual(False, actual)


    @patch("sys.stdout", StringIO())
    def test_check_json_data_format(self):
        """Tests check_data_format function on a valid data format - JSON"""
        mock_settings = {"DATA FORMAT": "JSON"}
        actual = settings.check_data_format(mock_settings)
        self.assertEqual(True, actual)


    @patch("sys.stdout", StringIO())
    def test_check_invalid_data_format(self):
        """Tests check_data_format function on a invalid data format - xml"""
        mock_settings = {"DATA FORMAT": "XML"}
        actual = settings.check_data_format(mock_settings)
        self.assertEqual(False, actual)