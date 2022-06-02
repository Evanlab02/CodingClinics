"""
code_clinic.py

This module is the main entry module for the code_clinic program.
It will get the command and its arguments (that were passed) in using
sys.argv and then send it to be processed.
"""

# Import Statements
import sys

def main():
    """
    Will get the command and its arguments (that were passed) in using
    sys.argv and then pass it on to be processed
    """

    all_commands = ["install"]
    command = sys.argv[0]
    del sys.argv[0]
    argument = " ".join(sys.argv)

    print(all_commands) #Remove
    print(command) #Remove
    print(argument) #Remove


if __name__ == "__main__":
    main()
