from enum import Enum


class Fabric(Enum):
    """
    The Fabric of the stuffed animal, can either be Linen, Cotton or Acrylic.
    """
    LINEN = "Linen"
    COTTON = "Cotton"
    ACRYLIC = "Acrylic"

    def __str__(self):
        """
        String method of the class.
        """
        return str(self.value)
