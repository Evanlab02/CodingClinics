from datetime import datetime
from rich import print as rprint
from first_time_setup.fts import get_home_directory, get_storage_directory

def start_logout(api_details: dict):
    """Logs that the login process is starting"""
    storage_directory = get_storage_directory(get_home_directory())
    permission = api_details["permissions"]
    creds = api_details["credentials"]

    with open(f"{storage_directory}log.txt", "a", encoding="utf-8") as log_file:
        log_file.writelines(f"[{datetime.now()}]: Started Logout\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Permissions: {permission}\n")
        log_file.writelines(f"-->    [{datetime.now()}]: Credentials: {creds}\n")

    rprint("[magenta]Logging out...[/magenta]")


def do_logout(api_details: dict):
    storage_directory = get_storage_directory(get_home_directory())
    start_logout()
