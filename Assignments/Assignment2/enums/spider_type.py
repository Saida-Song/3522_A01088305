from enum import Enum


class SpiderType(Enum):
    """
    The Spider type of the RC Spider, can either be Tarantula or a Wolf Spider.
    """
    TARANTULA = "Tarantula"
    WOLF_SPIDER = "Wolf Spider"

    def __str__(self):
        """
        String method of the class.
        """
        return str(self.value)
