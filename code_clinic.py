"""
code_clinic.py

This module is the main entry module for the code_clinic program.
It will get the command and its arguments (that were passed) in using
sys.argv and then send it to be processed.
"""

# Import Statements
import sys

# From Import Statements
from commands.command_handler import handle_command
from first_time_setup.fts import do_fts

def main():
    """
    Will get the command and its arguments (that were passed) in using
    sys.argv and then pass it on to be processed
    """
    del sys.argv[0]
    command = " ".join(sys.argv)
    do_fts()
    handle_command(command)


if __name__ == "__main__":
    main()
