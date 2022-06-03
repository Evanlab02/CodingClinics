"""
Tests if binary executable
is created correctly in right directory
"""

import unittest

from unittest.mock import patch
from io import StringIO
from install_program import install_codeclinic, install_helper

class MyTestCase(unittest.TestCase):
    """
    Just a class to contain tests
    """

    @patch("sys.stdout", StringIO())
    def test_bin_gets_created(self):
        """
        Tests if binary executable
        is created correctly in right directory
        """
        install_codeclinic.create_bin()
        self.assertTrue(install_helper.path_exists("dist/code_clinic"))
        install_codeclinic.clean_bin()
