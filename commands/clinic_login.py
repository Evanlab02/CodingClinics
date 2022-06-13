"""Module containing all the functions related to logging a user into
code clinics"""
# Import Statements
import sys

# From Import Statements
from datetime import datetime
from rich import print as rprint
from first_time_setup.fts import get_storage_directory, get_home_directory
from authentication.token import create_token

def start_login(api_details: dict):
    """Logs that the login process is starting"""
    storage_directory = get_storage_directory(get_home_directory())
    permission = api_details["permissions"]
    creds = api_details["credentials"]

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Started Login\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Credentials: {creds}\n")

    rprint("[cyan]Logging in...[/cyan]")


def end_login(api_details: dict):
    """Logs that that the user is logged in"""
    storage_directory = get_storage_directory(get_home_directory())
    permission = api_details["permissions"]

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Logged In\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")

    rprint("[green]Logged in[/green]")
    sys.exit()


def do_login(api_details: dict):
    """Does all Login related functions - main function for this module"""
    storage_directory = get_storage_directory(get_home_directory())
    start_login(api_details)
    create_token(storage_directory, api_details["permissions"])
    end_login(api_details)
