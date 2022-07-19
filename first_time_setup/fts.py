"""Keeps all the functions related to first time setup"""
import os
import sys

from rich import print as rprint
from file_helpers.json_helper import read_json, overwrite_json

def get_home_directory():
    """Returns the HOME directory for this system"""
    return os.getenv("HOME")


def get_storage_directory(home_dir: str):
    """Gets the storage directory for the storage files"""
    return f"{home_dir}/.codeclinic/"


def install_files(storage_directory: str):
    """Installs all program files into the specified storage directory"""
    if not path_exists(f"{storage_directory}credentials.json"):
        rprint("[red]Please Install Credentials File[/red]")
        sys.exit(1)

    if not path_exists(f"{storage_directory}settings.json"):
        os.system(f"touch {storage_directory}settings.json")
        overwrite_json({}, f"{storage_directory}settings.json")

    if not path_exists(f"{storage_directory}log.txt"):
        os.system(f"touch {storage_directory}log.txt")


def make_directory(storage_directory: str):
    """Makes a directory if it does not already exist"""
    if not path_exists(storage_directory):
        os.system(f"mkdir {storage_directory}")
        rprint(f"First Time Setup: Created Storage Directory({storage_directory})")


def path_exists(directory: str):
    """Returns true or false based on if a path exists"""
    return os.path.exists(directory)


def invalid_settings(settings_directory: str):
    """Checks if a settings file is in the correct format"""
    json_data = read_json(settings_directory)

    if not isinstance(json_data, dict):
        return True


    if not "calendarID" in json_data.keys():
        return True

    return False


def setup_settings(settings_directory: str):
    """Sets up the settings file based on user input"""
    rprint("Setting up...")
    settings_json = {"calendarID": input("Enter The Central Calendar ID: ")}
    overwrite_json(settings_json, settings_directory)
    rprint("Thank you for using CodeClinics")


def do_fts():
    """Does the first time setup of the program"""
    home_dir = get_home_directory()
    storage_dir = get_storage_directory(home_dir)
    make_directory(storage_dir)
    install_files(storage_dir)

    settings_directory = f"{storage_dir}settings.json"
    if invalid_settings(settings_directory):
        setup_settings(settings_directory)
