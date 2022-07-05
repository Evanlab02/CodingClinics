"""Module containing all the functions related to logging a user into
code clinics"""
# Import Statements
import sys

# From Import Statements
from datetime import datetime
from rich import print as rprint
from first_time_setup.fts import get_storage_directory, get_home_directory
from authentication.token import create_token, load_token, check_token

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


def check_logged_in(storage_directory: str, permission):
    do_login = True
    creds = load_token(storage_directory, permission)

    if check_token(creds):
        do_login = input("You are already logged in, do you wish to log in again [y/n]: ")\
            .lower() != "n"

    if not do_login:
        sys.exit("Cancelled Login!")


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
    check_logged_in(storage_directory, api_details["permissions"])
    create_token(storage_directory, api_details["permissions"])
    end_login(api_details)
