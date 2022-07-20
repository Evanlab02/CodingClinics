"""
File responsible for creating and editing settings file based on preferences
"""

from file_helpers.json_helper import read_json

def check_settings(settings: dict):
    """Checks that the settings file is complete"""
    settings_keys = settings.keys()

    if not check_keys(settings_keys):
        return False
    
    all_checks = [
        check_data_format(settings)
        ]

    return not False in all_checks


def check_keys(key_values: set):
    """Checks that the required keys are in the settings file"""
    calendar_id_key = "calendarID" in key_values
    data_format_key = "DATA FORMAT" in key_values
    all_checks = [calendar_id_key, data_format_key]
    return not False in all_checks


def check_data_format(settings: dict):
    """Checks that the data format value is correct"""
    supported_formats = ["JSON"]
    data_format = settings["DATA FORMAT"]
    return data_format in supported_formats


def load_settings(storage_directory: str, file_name: str):
    """Loads specified file at specified directory"""
    file_path = storage_directory + file_name
    return read_json(file_path)
