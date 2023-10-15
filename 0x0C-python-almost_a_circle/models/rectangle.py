#!/usr/bin/python3
"""models/rectangle.py"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x: The x-coordinate of the rectangle's position. Defaults to 0.
            y: The y-coordinate of the rectangle's position. Defaults to 0.
            id: The unique identifier of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: The x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle's position.

        Args:
            value (int): The x-coordinate value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: The y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle's position.

        Args:
            value (int): The y-coordinate value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Display the rectangle as a series of '#' characters."""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """Return a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Examples:
            update(10, 20) - Update width to 10 and height to 20.
            update(width=10, height=20) - Update width to 10 and height to 20.
        """
        if args:
            attribute_names = ['id', 'width', 'height', 'x', 'y']
            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)
        else:
            for key, value1 in kwargs.items():
                setattr(self, key, value1)

    def to_dictionary(self):
        """Convert the rectangle object to a dictionary.

        Returns:
            dict: A dictionary representation of the rectangle object.
        """
        dic = dict()
        dic['width'] = self.width
        dic['height'] = self.height
        dic['id'] = self.id
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
