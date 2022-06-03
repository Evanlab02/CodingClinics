"""
This module is responsible for installing code_clinic
regardless of the install method, This redirect everything
or do everything related to install
"""

import os

from rich import print as rprint
from install_program.install_helper import determine_path, get_program_type, path_exists

def create_bin():
    """
    Create Bin

    Creates a binary using PyInstaller and Scripting and hides all
    output of this procedure.
    """
    os.system("python3 -m PyInstaller --onefile code_clinic.py >>/dev/null 2>&1")


def clean_bin():
    """
    Clean Bin

    Deletes all files that are created when bulding the binary using
    bash commands.
    """
    os.system("rm -r dist/")
    os.system("rm -r build/")
    os.system("rm code_clinic.spec")


def bin_install():
    """
    Bin Install

    Creates and Installs Binary into the selected path
    and also makes it executable for users to use instead
    of having to use the files.
    """
    path = determine_path()

    rprint("    [magenta]1: Creating Binary...[/magenta]")
    create_bin()
    rprint("    [green]2: Created Binary[/green]")
    if not path_exists("dist/code_clinic"):
        raise FileNotFoundError("Executable was lost")
    rprint("    [magenta]3: Making Binary Executable...")
    os.system("sudo chmod +X dist/code_clinic")

    rprint("    [magenta]4: Installing Binary...")
    os.system(f"sudo cp dist/code_clinic {path}")
    rprint("    [green]5: Installed Binary")
    clean_bin()
    rprint("    [magenta]6: Cleaning up...")


def install_codeclinics(program: str):
    """
    Install CodeClinics

    Installs everything related to code clinics for the
    client, from the files to the binaries

    param:
        program: str - The program we are using ex. code_clinic.py or code_clinic

    returns:
        str - The message indicating the result of the install
    """
    rprint("[magenta]Installing CodeClinics...[/magenta]")
    program_type = get_program_type(program)

    if program_type == "source":
        try:
            bin_install()
        except FileNotFoundError as file_error:
            return f"[red]Binary Installation Failed: {file_error}[/red]"

    return "[green]Installed CodeClinics[/green]"
