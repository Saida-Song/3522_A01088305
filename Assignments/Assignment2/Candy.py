from store_item import StoreItem


class Candy(StoreItem):
    """
    Abstract class for Candies, inherit from the StoreItem class.
    """

    def __init__(self, name, description, product_id, has_nuts, has_lactose):
        """
        Construct a new Candy.
        :param name: str
        :param description: str
        :param product_id: str
        :param has_nuts: str
        :param has_lactose: str
        """
        super().__init__(name, description, product_id)
        self._contain_nut = has_nuts
        self._has_lactose = has_lactose

    def __str__(self):
        """
        String method of the class
        """
        return f"{super().__str__()}, " \
               f"Contain nut: {self._contain_nut}, " \
               f"Has lactose: {self._has_lactose}, "


class PumpkinCaramelToffee(Candy):
    """
    The Pumpkin Caramel Toffee is Halloween themed and is not lactose free and may contain traces of nuts.
    Inherits from the Candy class.
    """

    def __init__(self, name, product_id, **kwargs):
        """
        Initiated a new Pumpkin Caramel Toffee.
        :param name: str
        :param product_id: str
        :param kwargs: dict
        """
        super().__init__(name, kwargs["description"], product_id,
                         has_nuts=kwargs['has_nuts'], has_lactose=True)
        self._variety = kwargs['variety']

    def __str__(self):
        """
        String method of the class
        """
        return f"{super().__str__()} " \
               f"Variety: { self._variety}. "


class CandyCanes(Candy):
    """
    Candy Canes are Christmas themed. It is lactose free and does not contain nuts.
    Inherits from the Candy class.
    """

    def __init__(self, name, product_id, **kwargs):
        """
        Initiated a new Candy Cane.
        :param name: str
        :param product_id: str
        :param kwargs: dict
        """
        super().__init__(name, kwargs["description"], product_id,
                         has_nuts=False, has_lactose=False)
        self._stripes = kwargs['colour']

    def __str__(self):
        """
        String method of the class
        """
        return f"{super().__str__()} " \
                f"Stripes: {self._stripes}. "


class CremeEggs(Candy):
    """
    Creme Eggs are Easter themed and are not lactose free and may contain traces of nuts.
    Inherits from the Candy class.
    """

    def __init__(self, name, product_id, **kwargs):
        """
        Initiated a new Creme Eggs.
        :param name: str
        :param product_id: str
        :param kwargs: dict
        """
        super().__init__(name, kwargs["description"], product_id,
                         has_nuts=kwargs['has_nuts'], has_lactose=True)
        self._pack_size = kwargs['pack_size']

    def __str__(self):
        """
        String method of the class
        """
        return f"{super().__str__()} " \
                f"Pack size: {self._pack_size}. "
