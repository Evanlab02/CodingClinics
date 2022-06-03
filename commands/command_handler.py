"""
Command Handler.py

Will process commands that are passed into
its main function and redirect it to the correct modules
or functions to start producing the output and/or process
the input
"""

# From Import Statements
from rich import print as rprint
from install_program.install_codeclinic import install_codeclinics

def not_existing_command(command: str):
    """
    not_existing_command

    This will return the message for when a command
    was not a existing or valid one, error message to
    indicate it is invalid or non existing

    returns:
        str - Error message to indicate invalid command
    """
    return f"[red]I did not understand '{command}'.[/red]"


def handle_command(program:str, command:str):
    """
    handle_command

    This will process the command that was passed in
    and redirect to the correct module or function for
    the command. It will also use the program param to
    determine how it must run some commands.

    param:
        program: str - The programs name ex. code_clinic.py or code_clinic
        command: str - The command that the user wants to use, made with
        the sys.argv

    returns:
        output: str - The last output the command must print
    """
    all_commands = ["install"]

    if not command in all_commands:
        output = not_existing_command(command)
        rprint(output)
    elif command == "install":
        output = install_codeclinics(program)
        rprint(output)

    return output
