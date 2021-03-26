from store_item import StoreItem


class Toy(StoreItem):
    """
    Abstract class for Toys, inherit from the StoreItem class.
    """

    def __init__(self, name, description, product_id, has_battery, min_age):
        """
        Construct a new Toy.
        :param name: str
        :param description: str
        :param product_id: str
        :param has_battery: int
        :param min_age: int
        """
        super().__init__(name, description, product_id)
        self._is_battery_operated = has_battery
        self._min_age = min_age

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Has Batteries: {self._is_battery_operated}, " \
               f"Min recommended age: {self._min_age}"


class SantasWorkshop(Toy):
    """
    The premium Christmas present, this is not a battery operated toy.
    Inherits from the Toy class.
    """
    def __init__(self, name, product_id, **kwargs):
        """
        Initiate a new Santa's Workshop.
        :param width: int
        :param height: int
        :param num_rooms: int
        :param kwargs: other property attributes
        """
        super().__init__(name, kwargs["description"], product_id, has_battery=False, min_age=kwargs["min_age"])
        self._width = kwargs["width"]
        self._height = kwargs["height"]
        self._num_rooms = kwargs["num_rooms"]

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Width: {self._width}, " \
               f"Height: {self._height}, " \
               f"Num rooms: {self._num_rooms}"


class RCSpider(Toy):
    """
    The RC Spider is the toy to get during Halloween. This toy is battery operated.
    Inherits from the Toy class.
    """

    def __init__(self, name, product_id,  **kwargs):
        """
        Initiate a new RC Spider.
        :param speed: int
        :param jump_height: int
        :param has_glow: boolean
        :param spider_type: str
        :param kwargs: other property attributes
        """
        super().__init__(name, kwargs["description"], product_id, has_battery=True, min_age=kwargs["min_age"])
        self._speed = kwargs["speed"]
        self._jump_height = kwargs["jump_height"]
        self._glow_in_dark = kwargs["has_glow"]
        self._spider_type = kwargs["spider_type"]

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"Speed: {self._speed}, " \
               f"Jump_height: {self._jump_height}, " \
               f"glow_in_dark: {self._glow_in_dark}, " \
               f"spider_type: {self._spider_type}"


class RobotBunny(Toy):
    """
    The Robot Bunny is the toy for toddlers and infants out there. The toy is battery operated.
    Inherits from the Toy class.
    """

    def __init__(self, name, product_id,  **kwargs):
        """
        Initiate a new Robot Bunny.
        :param num_sound: int
        :param colour: str
        :param kwargs: other property attributes
        """
        super().__init__(name, kwargs["description"], product_id, has_battery=True, min_age=kwargs["min_age"])
        self._num_sound = kwargs["num_sound"]
        self._color = kwargs["colour"]

    def __str__(self):
        """
        String method of the class.
        """
        return f"{super().__str__()}, " \
               f"num_sound: {self._num_sound}, " \
               f"color: {self._color}"
