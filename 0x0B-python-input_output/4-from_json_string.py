#!/usr/bin/python3
"""Function that returs object rep by JSON"""
import json
def from_json_string(my_str):
    """Returns obj from json string"""
    return json.loads(my_str)
