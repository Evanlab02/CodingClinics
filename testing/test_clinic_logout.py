"""
Tests clinic logout
"""

import unittest
import os

from unittest.mock import patch
from io import StringIO
from google_api_helpers.api_helper import get_api_details
from commands import clinic_logout

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_start_log_logout(self):
        """Testing start log, logs correctly"""
        os.system("touch log.txt")
        api_details = get_api_details()

        clinic_logout.start_logout(api_details, "")

        with open("log.txt", "r", encoding="utf-8") as test_file:
            actual_lines = test_file.readlines()

        expected_lines = [
            ": Started Logout\n",
            ": Permissions: ['https://www.googleapis.com/auth/calendar']\n",
            ": Credentials: None\n"
        ]

        for index, value in enumerate(expected_lines):
            actual_line = actual_lines[index]
            expected_line = value
            self.assertTrue(expected_line, actual_line)

        os.system("rm log.txt")
