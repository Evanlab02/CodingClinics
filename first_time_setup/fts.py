"""Keeps all the functions related to first time setup"""
import os

from rich import print as rprint
from file_helpers.json_helper import read_json, overwrite_json

def get_home_directory():
    """Returns the HOME directory for this system"""
    return os.getenv("HOME")


def get_storage_directory(home_dir: str):
    """Gets the storage directory for the storage files"""
    return f"{home_dir}/.codeclinic/"


def install_file(from_path: str, to_path: str):
    """Copies a file from one place to another"""
    os.system(f"cp {from_path} {to_path}")


def install_files(storage_directory: str):
    """Installs all program files into the specified storage directory"""
    if not path_exists(f"{storage_directory}log.txt"):
        install_file("files/text_files/log.txt", storage_directory)
        rprint("First Time Setup: Created Log File")

    if not path_exists(f"{storage_directory}settings.json"):
        install_file("files/json_files/settings.json", storage_directory)
        rprint("First Time Setup: Created Settings File")

    if not path_exists(f"{storage_directory}credentials.json"):
        install_file("files/json_files/credentials.json", storage_directory)
        rprint("First Time Setup: Created Credentials File")


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
