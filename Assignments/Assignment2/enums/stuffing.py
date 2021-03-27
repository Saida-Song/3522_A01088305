from enum import Enum


class Stuffing(Enum):
    """
    The stuffing of the stuffed animal, can either be Polyester Fiberfill or Wool.
    """
    POLYESTER_FIBERFILL = "Polyester Fibrefill"
    WOOL = "Wool"

    def __str__(self):
        """
        String method of the class.
        :return: str
        """
        return str(self.value)
