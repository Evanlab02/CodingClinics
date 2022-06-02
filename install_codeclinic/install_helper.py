import os

from rich import print as rprint

def get_program_type(program: str):
    if ".py" in program:
        return "source"
    else:
        return "bin"


def path_exists(file_path: str):
    return os.path.exists(file_path)


def get_custom_path():
    custom_path = input("Enter the directory you would like to use: ")

    while not path_exists(custom_path):
        rprint("[yellow]This directory does not exist[/yellow]")
        custom_path = input("Enter the directory you would like to use: ")

    return custom_path


def determine_path():
    default_bin_path = "/usr/local/bin/"
    use_custom_path = False
    
    if path_exists(default_bin_path):
        use_custom_path = input("Do you want to use the default directory(/usr/local/bin/) [Y/n]: ").lower() == "n"

    if use_custom_path or not path_exists(default_bin_path):
        custom_path = get_custom_path()
        return custom_path
    else:
        return default_bin_path
