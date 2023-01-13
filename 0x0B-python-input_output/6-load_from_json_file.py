#!/usr/bin/python3
"""Program to create an object from a JSON file"""


import json
 

def load_from_json_file(filename):
    """Function to create object from JSON file `filename`"""

    with open(filename, encoding="utf-8") as f:
        return json.load(f)
