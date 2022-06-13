from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def create_token(storage_directory: str, permission):
    flow = InstalledAppFlow.from_client_secrets_file(
        f'{storage_directory}credentials.json', permission)

    creds = flow.run_local_server(port=0)

    with open(f'{storage_directory}token.json', 'w') as token:
        token.write(creds.to_json())

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Created new token\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")
