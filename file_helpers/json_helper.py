"""
json_helper.py

Will help with any JSON file processing
"""

# Import Statements
import json

def overwrite_json(new_value, file_path: str):
    """
    This will overwrite a json file with a new JSON object
    at the file path

    params:
        new_value - new JSON Object
        file_path: str - The path where the file is located
    """
    with open(f"{file_path}", "w", encoding="utf-8") as write_file:
        json.dump(new_value, write_file)


def read_json(file_path: str):
    """
    This will read and return the value of the json file at file path

    param:
        file_path: str - The path where the file is located

    returns:
        the json file contents
    """
    with open(f"{file_path}", "r", encoding="utf-8") as read_file:
        return json.load(read_file)
