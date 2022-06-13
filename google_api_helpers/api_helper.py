"""Module containing helper functions for all api stuff"""

def get_api_details():
    """Returns empty api_details to be populated with values"""
    return {
        "permissions": ['https://www.googleapis.com/auth/calendar'],
        "credentials": None,
        "connection": None
    }
