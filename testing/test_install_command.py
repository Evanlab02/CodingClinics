"""
Primarily Tests The Install Functions
"""

import unittest
import os

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


    @patch("sys.stdout", StringIO())
    def test_valid_path_exists(self):
        """Tests if path exists returns true on a valid directory"""
        actual = install_helper.path_exists("testing/")
        self.assertTrue(actual)


    @patch("sys.stdout", StringIO())
    def test_invalid_path_exists(self):
        """Tests if path exists returns false on a invalid directory"""
        actual = install_helper.path_exists("fishering/")
        self.assertFalse(actual)


    @patch("sys.stdin", StringIO("testing/"))
    @patch("sys.stdout", StringIO())
    def test_first_time_valid_custom_path(self):
        """Tests custom path returns value entered using mock input"""
        expected = "testing/"
        actual = install_helper.get_custom_path()
        self.assertEqual(expected, actual)


    @patch("sys.stdin", StringIO("fishering/\ntesting/"))
    @patch("sys.stdout", StringIO())
    def test_second_time_valid_custom_path(self):
        """Tests custom path returns value entered using mock input"""
        expected = "testing/"
        actual = install_helper.get_custom_path()
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_get_home_dir(self):
        """Tests that get home directory is the same as that of OS"""
        expected = os.getenv("HOME")
        actual = install_helper.get_home_directory()
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_install_file(self):
        """Tests that install file works correctly"""

        install_helper.install_file("testing/testing_files/testing.txt", "testing/")
        actual = install_helper.path_exists("testing/testing.txt")
        self.assertTrue(actual)
        os.system("rm testing/testing.txt")
