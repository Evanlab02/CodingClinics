"""
Tests check login
"""

import os
import unittest

from unittest.mock import patch
from io import StringIO
from authentication import check_login

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_get_permissions(self):
        """Tests the retrieval of permissions"""
        mock_details = {
        "permissions": ['https://www.googleapis.com/auth/calendar'],
        "credentials": None,
        "connection": None
        }

        actual = check_login.get_permissions(mock_details)
        expected = ['https://www.googleapis.com/auth/calendar']
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_get_creds_none(self):
        """Tests the retrieval of creds with no value"""
        mock_details = {
        "permissions": ['https://www.googleapis.com/auth/calendar'],
        "credentials": None,
        "connection": None
        }

        actual = check_login.get_creds(mock_details)
        expected = None
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_get_creds_value(self):
        """Tests the retrieval of creds"""
        mock_details = {
        "permissions": ['https://www.googleapis.com/auth/calendar'],
        "credentials": 12345,
        "connection": None
        }

        actual = check_login.get_creds(mock_details)
        expected = 12345
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_get_folder_path(self):
        """Tests the retrieval of the storage_directory"""
        home_dir = os.getenv("HOME")
        expected = home_dir+"/.codeclinic/"
        self.assertEqual(expected, check_login.get_folder_path())


    @patch("sys.stdout", StringIO())
    def test_check_login_permissions(self):
        """Tests check_login and its permissions key-value pair"""
        self.assertEqual(['https://www.googleapis.com/auth/calendar'],
        check_login.check_login()[1]["PERMISSIONS"])


    @patch("sys.stdout", StringIO())
    def test_check_login_connection(self):
        """Tests check_login and its connection key-value pair"""
        self.assertEqual(None,
        check_login.check_login()[1]["CONNECTION"])


    @patch("sys.stdout", StringIO())
    def test_check_login_folder_path(self):
        """Tests check_login and its folder path key-value pair"""
        expected = os.getenv("HOME")+"/.codeclinic/"
        self.assertEqual(expected,
        check_login.check_login()[1]["FOLDER PATH"])
