#!/usr/bin/python3
"""Define class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Representation of class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing class Rectangle
    class Rectangle inherits the Base class"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets a new value for x"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the Rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets a new value for the height"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets a new value for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets a new value for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with the character #
        while taking care of x and y"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            print(" " * self.__x, end='')
            for w in range(self.__width):
                print("#", end='')
            print()


    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        elif kwargs ad len(kwargs) != 0:
            if 'id' in kwargs:
                if kwargs['id'] is not None:
                    self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """A method that returns a string representation of the class"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") "
        string += "{}/{}".format(str(self.__x), str(self.__y))
        string += " - " + "{}/{}".format(str(self.__width), str(self.__height))
        return string
