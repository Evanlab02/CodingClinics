"""Module containing all functions related to writing and reading
the token.json"""

from datetime import datetime
from rich import print as rprint
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from first_time_setup.fts import path_exists

def create_token(storage_directory: str, permission):
    """Creates a token (token.json) using oauth to login
    a user in with their gmail account, it will use the storage
    directory to find the client_secret(credentials.json) and the permission
    to determine what permissions the user should have, when the user
    goes through the oauth process, it will create a token.json
    meaning the user is signed in"""

    flow = InstalledAppFlow.from_client_secrets_file(
        f'{storage_directory}credentials.json', permission)

    creds = flow.run_local_server(port=0)
    rprint("[cyan]Writing Token[/cyan]")

    with open(f'{storage_directory}token.json', 'w', encoding="utf-8") as token:
        token.write(creds.to_json())

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Created new token\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")


def token_valid(creds):
    """
    Checks that the token exists and is valid
    """
    return creds and creds.valid


def token_expired(creds):
    """
    Checks that the token exists and is expired or needs to be refreshed
    """
    return creds and creds.expired and creds.refresh_token


def check_token(creds):
    """
    Checks that the token is valid and not expired, if it
    meets both these conditions will return True, otherwise False
    """
    return token_valid(creds) and not token_expired(creds)


def load_token(storage_directory: str, permission):
    """
    Will load the token off of the token.json file, if
    there is nothing to load, it will return None
    """
    creds = None
    if path_exists(f'{storage_directory}token.json'):
        creds = Credentials.from_authorized_user_file(f'{storage_directory}token.json', permission)
    return creds
