#!/usr/bin/python3

"""models/Square.py"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square object.

        Args:
            size (int): The size of the square.
            x: The x-coordinate of the square's position. Defaults to 0.
            y: The y-coordinate of the square's position. Defaults to 0.
            id: The unique identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """int: The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            ValueError: If the value is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Examples:
            update(10) - Update size to 10.
            update(size=10) - Update size to 10.
        """
        if args:
            attribute_names = ['id', 'size', 'x', 'y']
            for attribute_name, value in zip(attribute_names, args):
                setattr(self, attribute_name, value)
        else:
            for key, value1 in kwargs.items():
                setattr(self, key, value1)

    def __str__(self) -> str:
        """Return a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def to_dictionary(self):
        """Convert the square object to a dictionary.

        Returns:
            dict: A dictionary representation of the square object.
        """
        dic = dict()
        dic['size'] = self.size
        dic['id'] = self.id
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
