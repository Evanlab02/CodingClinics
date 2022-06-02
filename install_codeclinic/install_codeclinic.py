import os

from rich import print as rprint
from install_codeclinic.install_helper import determine_path, get_program_type, path_exists

def create_bin():
    os.system("python3 -m PyInstaller --onefile code_clinic.py >>/dev/null 2>&1")
    

def clean_bin():
    os.system(f"rm -r dist/")
    os.system(f"rm -r build/")
    os.system(f"rm code_clinic.spec")
    

def bin_install():
    path = determine_path()

    rprint("    [magenta]1: Creating Binary...[/magenta]")
    rprint("    [green]2: Created Binary[/green]")
    create_bin()
    if not path_exists("dist/code_clinic"):
        raise Exception("Executable was lost")
    rprint("    [magenta]3: Making Binary Executable...")
    os.system("sudo chmod +X dist/code_clinic")

    rprint("    [magenta]4: Installing Binary...")
    os.system(f"sudo cp dist/code_clinic {path}")
    rprint("    [green]5: Installed Binary")
    clean_bin()
    rprint("    [magenta]6: Cleaning up...")
    
    
def install_codeclinics(program: str):
    rprint("[magenta]Installing CodeClinics...[/magenta]")
    program_type = get_program_type(program)
    
    if program_type == "source":
        try:
            bin_install()
        except Exception as e:
            return f"[red]Binary Installation Failed: {e}[/red]"

    return "[green]Installed CodeClinics[/green]"