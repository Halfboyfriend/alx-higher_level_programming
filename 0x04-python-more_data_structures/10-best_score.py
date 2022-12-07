#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    b = 0
    for key, value in a_dictionary.items():
        if value > b:
            b = value
    for key, value in a_dictionary.itesm():
        if value == b:
            return key
