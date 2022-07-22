"""Module containing helper functions for all api stuff"""

def get_api_details():
    """Returns empty api_details to be populated with values"""
    return {
        "permissions": ['https://www.googleapis.com/auth/calendar'],
        "credentials": None,
        "connection": None
    }


def add_to_dict(change_dict: dict, new_keys: list[str], new_values: list):
    """Returns an edited dictionary - Using the following format

    {
        "new_keys[0]":new_values[0],
        "new_keys[1]":new_values[1]
    }
    """
    for value_index, key in enumerate(new_keys):
        change_dict[key] = new_values[value_index]
    return change_dict
