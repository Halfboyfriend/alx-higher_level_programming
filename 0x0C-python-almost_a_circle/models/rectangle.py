#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__()
        self.width = width
        self.height = height
        self.x = x
        self.y = y


