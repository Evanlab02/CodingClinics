import unittest

from unittest.mock import patch
from io import StringIO
from install_codeclinic import install_codeclinic, install_helper

class MyTestCase(unittest.TestCase):

    @patch("sys.stdout", StringIO())
    def test_bin_gets_created(self):
        install_codeclinic.create_bin()
        self.assertTrue(install_helper.path_exists("dist/code_clinic"))
        install_codeclinic.clean_bin()