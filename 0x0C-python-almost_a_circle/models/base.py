#!/usr/bin/python3
"""Defines the base model class."""
import csv
import turtle
import json


class Base:

    """Represents the model base.
    Attributes:
            __nb_objects (int): The number of instantiated Bases
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects



