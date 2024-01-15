#!/usr/bin/python3
"""Define a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of class Square
    inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing class Square

        Args:
           size(int): the size of the square
           x(int): the x coordinate of the square
           y(int): the y coordinate of the square
           id(int): the identity of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets a new value for the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the values of the attributes
        Args:
          *args: new vlues for attributes:
            - 1st argument represents id attribute
            - 2nd argument represents size attribute
            - 3rd argument represents x attribute
            - 4th argument represents y attribute
          **kwargs (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            if 'id' in kwargs:
                if kwargs['id'] is not None:
                    self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """A method that returns the dictionary representation of a class"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
