"""
Houses all the logic for the logout command
"""
import sys

from datetime import datetime
from rich import print as rprint
from authentication.token import remove_token
from first_time_setup.fts import get_home_directory, get_storage_directory

def start_logout(api_details: dict, storage_directory: str):
    """Logs that the logout process is starting"""
    permission = api_details["permissions"]
    creds = api_details["credentials"]

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Started Logout\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Credentials: {creds}\n")

    rprint("[magenta]Logging out...[/magenta]")


def end_logout(api_details: dict, storage_directory: str):
    """Logs that that the user is logged out"""
    permission = api_details["permissions"]

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Logged Out\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")

    rprint("[green]Logged Out[/green]")


def do_logout(api_details: dict):
    """Does all Logout related functions - main function for this module"""
    storage_directory = get_storage_directory(get_home_directory())
    start_logout(api_details, storage_directory)
    remove_token(storage_directory)
    end_logout(api_details, storage_directory)
    sys.exit()
