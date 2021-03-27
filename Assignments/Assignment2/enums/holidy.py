from enum import Enum


class Holiday(Enum):
    """
    Represents the holidays that item are made for.
    """
    CHRISTMAS = "Christmas"
    EASTER = "Easter"
    HALLOWEEN = "Halloween"

    def __str__(self):
        """
        String method of the class
        :return: str
        """
        return str(self.value)
