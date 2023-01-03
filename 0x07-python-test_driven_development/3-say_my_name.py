"""
    Insert here module comment
    Write a function that prints My name is <first name> <last name>
    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
    You are not allowed to import any module
"""

def say_my_name(first_name, last_name=""):
    """Print my first_name or last_name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
