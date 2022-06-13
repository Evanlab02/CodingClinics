"""Module containing all functions related to writing and reading
the token.json"""

from datetime import datetime
from rich import print as rprint
from google_auth_oauthlib.flow import InstalledAppFlow

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
