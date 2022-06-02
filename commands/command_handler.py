# From Import Statements
from install_codeclinic.install_codeclinic import install_codeclinics
from rich import print as rprint

def not_existing_command(command: str):
    return f"[red]I did not understand '{command}'.[/red]"


def handle_command(program:str, command:str):
    all_commands = ["install"]

    if not command in all_commands:
        output = not_existing_command(command)
        rprint(output)
    elif command == "install":
        output = install_codeclinics(program)
        rprint(output)

    return output