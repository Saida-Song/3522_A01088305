from store_item import StoreItem
from enums.stuffing import Stuffing
from enums.fabric import Fabric


class StuffedAnimal(StoreItem):
    """
    Abstract class for Stuffed Animals, inherit from the StoreItem class.
    """

    def __init__(self, name, description, product_id, stuffing, size, fabric):
        """
        Initiated a new Stuffed animal toy.
        """
        super().__init__(name, description, product_id)
        self._stuffing = stuffing
        self._size = size
        self._fabric = fabric

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Stuffing: {self._stuffing}, " \
               f"Size: {self._size}, " \
               f"Fabric: {self._fabric} "


class DancingSkeleton(StuffedAnimal):
    """
    The dancing skeleton is made out of Acrylic yarn and stuffed with Polyester Fiberfill.
    Inherits from the StuffedAnimal class.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(name, kwargs["description"], product_id,
                         stuffing=Stuffing.POLYESTER_FIBERFILL, fabric=Fabric.LINEN,
                         size=kwargs['size'])
        self._glow_in_dark = True

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Has glow: {self._glow_in_dark} "


class Reindeer(StuffedAnimal):
    """
    The reindeer comes with its very own personal mini sleigh and is the stuffed animal for Christmas.
    Inherits from the StuffedAnimal class.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(name, kwargs["description"], product_id,
                         stuffing=Stuffing.WOOL, fabric=Fabric.COTTON,
                         size=kwargs['size'])
        self._glow_in_dark = True

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Has glow: {self._glow_in_dark} "


class EasterBunny(StuffedAnimal):
    """
    The Easter Bunny is made out of Linen and stuffed with Polyester Fiberfill.
    Inherits from the StuffedAnimal class.
    """

    def __init__(self, name, product_id, **kwargs):
        super().__init__(name, kwargs["description"], product_id,
                         stuffing=Stuffing.POLYESTER_FIBERFILL, fabric=Fabric.LINEN,
                         size=kwargs['size'])
        self._color = kwargs['colour']

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Color: {self._color} "
