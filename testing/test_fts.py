"""
Tests fts
"""

import unittest
import os

from unittest.mock import patch
from io import StringIO
from first_time_setup import fts
from file_helpers.json_helper import read_json, overwrite_json

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_get_home_directory(self):
        """Testing function returns correct value"""
        expected = os.getenv("HOME")
        actual = fts.get_home_directory()
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_get_storage_directory(self):
        """Testing function returns correct value"""
        home_dir = os.getenv("HOME")
        expected = f"{home_dir}/.codeclinic/"
        actual = fts.get_storage_directory(home_dir)
        self.assertEqual(expected, actual)

    
    @patch("sys.stdout", StringIO())
    def test_install_file(self):
        """Testing that files are getting copied over correctly"""
        fts.install_file("testing/testing_files/testing.txt", "testing/")
        self.assertTrue(os.path.exists("testing/testing.txt"))
        os.system("rm testing/testing.txt")

    
    @patch("sys.stdout", StringIO())
    def test_install_files(self):
        """Testing that storage files are installed correctly"""
        fts.install_files("testing/")
        self.assertTrue(os.path.exists("testing/log.txt"))
        self.assertTrue(os.path.exists("testing/settings.json"))
        os.system("rm testing/log.txt")
        os.system("rm testing/settings.json")


    @patch("sys.stdout", StringIO())
    def test_make_directory(self):
        """Testing that the storage directory is created correctly"""
        fts.make_directory("testing/testing_directory/")
        self.assertTrue(os.path.exists("testing/testing_directory/"))
        os.system("rm -r testing/testing_directory/")


    @patch("sys.stdout", StringIO())
    def test_valid_path_exists(self):
        """Testing that a valid path returns true"""
        actual = fts.path_exists("testing/")
        self.assertTrue(actual)
    

    @patch("sys.stdout", StringIO())
    def test_invalid_path_exists(self):
        """Testing that a invalid path returns false"""
        actual = fts.path_exists("fishing/")
        self.assertFalse(actual)


    @patch("sys.stdout", StringIO())
    def test_invalid_settings_list_file(self):
        """Testing that invalid settings file will return true"""
        actual = fts.invalid_settings("testing/testing_files/list.json")
        self.assertTrue(actual)


    @patch("sys.stdout", StringIO())
    def test_invalid_settings_key_file(self):
        """Testing that invalid settings file will return true"""
        actual = fts.invalid_settings("testing/testing_files/invalid_key.json")
        self.assertTrue(actual)


    @patch("sys.stdout", StringIO())
    def test_valid_settings_file(self):
        """Testing that valid settings file will return false"""
        actual = fts.invalid_settings("testing/testing_files/valid.json")
        self.assertFalse(actual)

    
    @patch("sys.stdin", StringIO("1234\n"))
    @patch("sys.stdout", StringIO())
    def test_setup_settings(self):
        """Testing that settings get set up correctly"""
        fts.setup_settings("testing/testing_files/mock_settings.json")
        actual = read_json("testing/testing_files/mock_settings.json")["calendarID"]
        self.assertEqual("1234", actual)
        overwrite_json({}, "testing/testing_files/mock_settings.json")
        
