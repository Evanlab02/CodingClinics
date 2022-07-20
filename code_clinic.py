"""
code_clinic.py

This module is the main entry module for the code_clinic program.
It will get the command and its arguments (that were passed) in using
sys.argv and then send it to be processed.
"""
# pylint: disable=import-error

# Import Statements
import sys

# From Import Statements
from commands.command_handler import handle_command
from first_time_setup.fts import do_fts, get_home_directory, get_storage_directory
from first_time_setup.settings import complete_settings

def main():
    """
    Will get the command and its arguments (that were passed) in using
    sys.argv and then pass it on to be processed
    """
    del sys.argv[0]
    command = " ".join(sys.argv)

    home_dir = get_home_directory()
    storage_directory = get_storage_directory(home_dir)
    file_name = "settings.json"

    do_fts()
    complete_settings(storage_directory, file_name)
    handle_command(command)


if __name__ == "__main__":
    main()
