import json

def overwrite_json(new_value, file_path: str):
    with open(f"{file_path}", "w") as write_file:
        json.dump(new_value, write_file)