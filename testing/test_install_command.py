import unittest

from unittest.mock import patch
from io import StringIO
from install_codeclinic import install_helper

class MyTestCase(unittest.TestCase):

    @patch("sys.stdout", StringIO())
    def test_source_program(self):
        expected = "source"
        actual = install_helper.get_program_type("code_clinic.py")
        self.assertEqual(expected, actual)


    @patch("sys.stdout", StringIO())
    def test_bin_program(self):
        expected = "bin"
        actual = install_helper.get_program_type("code_clinic")
        self.assertEqual(expected, actual)
