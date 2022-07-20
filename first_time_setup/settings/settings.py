"""
File responsible for creating and editing settings file based on preferences
"""

from file_helpers.json_helper import read_json

def load_settings(storage_directory: str, file_name: str):
    """Loads specified file at specified directory"""
    file_path = storage_directory + file_name
    return read_json(file_path)
