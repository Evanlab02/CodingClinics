"""
This module is responsible for supplying
install helper files that make the installation
of code_clinics easier and can be used in
mutiple different scenarios
"""

import os

from rich import print as rprint

def get_program_type(program: str):
    """
    Get Program Type

    Gets the program type based on the program we are running
    that is passed in

    param:
        program: str - the program we are running ex. code_clinic.py or code_clinic

    returns:
        str - source if we are running program using python files, or
        bin if we are using binary/executable
    """
    if ".py" in program:
        return "source"
    return "bin"


def path_exists(file_path: str):
    """
    Path Exists

    Checks if the path that is passed in as a string exists.

    param:
        file_path: str - The path we want to check in string format

    returns:
        True/False: boolean - True if the path exists otherwise False
    """
    return os.path.exists(file_path)


def get_custom_path():
    """
    Get Custom Path

    Asks the user to enter a file path as a string, it also
    checks if this path exists and if not, reasks the user to
    enter the path

    returns:
        custom_path: str - The path the user entered as a string
    """
    custom_path = input("Enter the directory you would like to use: ")

    while not path_exists(custom_path):
        rprint("[yellow]This directory does not exist[/yellow]")
        custom_path = input("Enter the directory you would like to use: ")

    return custom_path


def determine_path():
    """
    Determine Path

    Determines if the user wants to store
    the binary in the default location or
    in a custom path and returns the path selected

    returns:
        path: str - The path the binary was installed in
    """

    default_bin_path = "/usr/local/bin/"
    use_custom_path = False

    if path_exists(default_bin_path):
        use_custom_path = input("Do you want to use the default directory\
(/usr/local/bin/) [Y/n]: ").lower() == "n"

    if use_custom_path or not path_exists(default_bin_path):
        custom_path = get_custom_path()
        return custom_path

    return default_bin_path


def get_home_directory():
    """Returns the HOME directory for this system"""
    return os.getenv("HOME")


def install_file(from_path: str, to_path: str):
    """Copies a file from one place to another"""
    os.system(f"cp {from_path} {to_path}")
