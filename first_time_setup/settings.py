"""
File responsible for creating and editing settings file based on preferences
"""

# pylint: disable=import-error

import inquirer

from file_helpers.json_helper import read_json, overwrite_json

def check_settings(settings: dict):
    """Checks that the settings file is complete"""
    settings_keys = settings.keys()

    if not check_keys(settings_keys):
        return False

    all_checks = [
        check_data_format(settings)
        ]

    return False not in all_checks


def check_keys(key_values: set):
    """Checks that the required keys are in the settings file"""
    calendar_id_key = "calendarID" in key_values
    data_format_key = "DATA FORMAT" in key_values
    all_checks = [calendar_id_key, data_format_key]
    return False not in all_checks


def check_data_format(settings: dict):
    """Checks that the data format value is correct"""
    supported_formats = ["JSON"]
    data_format = settings["DATA FORMAT"]
    return data_format in supported_formats


def load_settings(storage_directory: str, file_name: str):
    """Loads specified file at specified directory"""
    file_path = storage_directory + file_name
    return read_json(file_path)


def update_settings(settings: dict, data_format: str):
    """Updates settings dictionary if something is missing"""
    settings["DATA FORMAT"] = data_format
    return settings


def save_settings(storage_directory: str, file_name: str, new_settings: dict):
    """Saves data to specified file at specified directory"""
    file_path = storage_directory + file_name
    overwrite_json(new_settings, file_path)


def complete_settings(storage_directory: str, file_name: str):
    """Completes Settings Setup"""
    settings = load_settings(storage_directory, file_name)

    while not check_settings(settings):
        data_format = get_data_format()
        settings = update_settings(settings, data_format)
        save_settings(storage_directory, file_name, settings)

    return settings


def get_data_format():
    """Gets the data format the user would like to use"""
    data_formats = ["JSON - {'Example': 'Example'} (Default)"]

    data_formats_inquirer = [
        inquirer.List('Data Format',
                message="Which Data Format Should The Program Save In",
                choices=data_formats,
                default=["JSON"]
            ),
    ]
    selected = inquirer.prompt(data_formats_inquirer)
    return selected["Data Format"].split(" - ")[0]
