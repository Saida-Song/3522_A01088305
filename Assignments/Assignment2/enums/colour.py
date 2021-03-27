from enum import Enum


class Colour(Enum):
    """
    All the available colors.
    """
    ORANGE = "Orange"
    BLUE = "Blue"
    PINK = "Pink"
    WHITE = "White"
    GREY = "Grey"
    RED = "Red"
    GREEN = "Green"

    def __str__(self):
        """
        String method of the class.
        :return: str
        """
        return str(self.value)
