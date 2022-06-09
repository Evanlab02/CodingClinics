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

def main():
    """
    Will get the command and its arguments (that were passed) in using
    sys.argv and then pass it on to be processed
    """
    del sys.argv[0]
    command = " ".join(sys.argv)
    handle_command(command)


if __name__ == "__main__":
    main()
