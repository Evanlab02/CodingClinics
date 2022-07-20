"""Tests Settings.py file"""

# pylint: disable=import-error

import unittest

from unittest.mock import patch
from io import StringIO
from first_time_setup import settings

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


    @patch("sys.stdout", StringIO())
    def test_update_settings(self):
        """Tests update_settings function"""
        mock_settings = {"CalendarID": "XML"}
        actual = settings.update_settings(mock_settings, "XML")
        self.assertEqual({"CalendarID": "XML", "DATA FORMAT": "XML"}, actual)


    @patch("sys.stdout", StringIO())
    def test_complete_settings_valid_setings(self):
        """Tests check_data_format function on a invalid data format - xml"""
        mock_file = "mock_valid_settings.json"
        actual = settings.complete_settings(self.STORAGE_DIRECTORY, mock_file)
        self.assertEqual({"CalendarID": "XML", "DATA FORMAT": "JSON"}, actual)


    @patch("sys.stdout", StringIO())
    def test_save_settings(self):
        """Tests check_data_format function on a invalid data format - xml"""
        mock_file = "mock_save_settings.json"
        settings.save_settings(self.STORAGE_DIRECTORY, mock_file, {"SETTINGS": "SETTINGS"})
        actual = settings.load_settings(self.STORAGE_DIRECTORY, mock_file)
        self.assertEqual({"SETTINGS": "SETTINGS"}, actual)
        settings.save_settings(self.STORAGE_DIRECTORY, mock_file, {})
