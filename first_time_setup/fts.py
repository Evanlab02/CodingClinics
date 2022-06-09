import os

from rich import print as rprint
from file_helpers.json_helper import read_json, overwrite_json

def get_home_directory():
    """Returns the HOME directory for this system"""
    return os.getenv("HOME")


def get_storage_directory(home_dir: str):
    return f"{home_dir}/.codeclinic/"


def install_file(from_path: str, to_path: str):
    """Copies a file from one place to another"""
    os.system(f"cp {from_path} {to_path}")


def install_files(storage_directory: str):
    if not path_exists(f"{storage_directory}log.txt"):
        install_file("files/text_files/log.txt", storage_directory)
        rprint("First Time Setup: Created Log File")
    
    if not path_exists(f"{storage_directory}settings.json"):
        install_file("files/json_files/settings.json", storage_directory)
        rprint("First Time Setup: Created Settings File")


def make_directory(storage_directory: str):
    if not path_exists(storage_directory):
        os.system(f"mkdir {storage_directory}")
        rprint(f"First Time Setup: Created Storage Directory({storage_directory})")


def path_exists(directory: str):
    return os.path.exists(directory)


def invalid_settings(settings_directory: str):
    json_data = read_json(settings_directory)

    if not type(json_data)==dict:
        return True


    if not "calendarID" in json_data.keys():
        return True

    return False


def setup_settings(settings_directory: str):
    rprint("Setting up...")
    settings_json = {"calendarID": input("Enter The Central Calendar ID: ")}
    overwrite_json(settings_json, settings_directory)
    rprint("Thank you for using CodeClinics")


def do_fts():
    home_dir = get_home_directory()
    storage_dir = get_storage_directory(home_dir)
    make_directory(storage_dir)
    install_files(storage_dir)

    settings_directory = f"{storage_dir}settings.json"
    if invalid_settings(settings_directory):
        setup_settings(settings_directory)
