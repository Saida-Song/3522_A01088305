from enum import Enum, auto


class Variety(Enum):
    """
    The Variety of the Pumpkin Caramel Toffee candy, can either be Sea Salt and Regular.
    """
    SEA_SALT = auto()
    REGULAR = auto()

    def __str__(self):
        """
        String method of the class.
        :return: str
        """
        return str(self.value)

