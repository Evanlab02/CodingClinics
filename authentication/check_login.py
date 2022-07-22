"""This file contains all the logic for checking that
the user is logged in."""

from first_time_setup.fts import get_home_directory, get_storage_directory
from authentication.token import load_token, check_token

def check_login():
    """Checks that the user is logged in with valid credentials"""
    program_details = {
        "PERMISSIONS": ['https://www.googleapis.com/auth/calendar'],
        "CREDENTIALS": None,
        "CONNECTION": None
    }

    permissions = program_details["PERMISSIONS"]

    folder_path = get_folder_path()
    creds = load_token(folder_path, permissions)
    logged_in = check_token(creds)

    program_details["FOLDER PATH"] = folder_path
    program_details["CREDENTIALS"] = creds

    return logged_in, program_details


def get_permissions(api_details: dict):
    """Gets permissions for the API"""
    permissions = api_details["permissions"]
    return permissions


def get_creds(api_details: dict):
    """Gets credentials for the API"""
    creds = api_details["credentials"]
    return creds


def get_folder_path():
    """Gets the path of the storage directory"""
    home_directory = get_home_directory()
    storage_directory = get_storage_directory(home_directory)
    return storage_directory
