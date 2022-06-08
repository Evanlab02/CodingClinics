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
