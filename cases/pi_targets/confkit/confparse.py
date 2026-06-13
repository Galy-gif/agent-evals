import json


def load_config(text):
    """Parse a JSON config string into a dict, rejecting non-object roots."""
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("config root must be a JSON object")
    return data
