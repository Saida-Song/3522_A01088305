class StoreItem:
    """
    Base class for a store item.
    """

    def __init__(self, name, description, product_id, **kwargs):
        """
        Initiate a new item in the store.
        :param name: str
        :param description: str
        :param product_id: str
        """
        self._name = name
        self._description = description
        self.product_id = product_id

    def get_name(self):
        """
        Return the name of the item.
        :return: str
        """
        return self._name

    def get_id(self):
        """
        Return the id of the item.
        :return: str
        """
        return self.product_id

    def __str__(self):
        """
        String method of the class.
        :return: str
        """
        return f"Mame:{self._name}, Product Id: {self.product_id}, Description:{self._description} "

    def __eq__(self, other):
        """
        Equals method of the class.
        :return: bool
        """
        return True if self.product_id == other.product_id else False

    def __hash__(self):
        """
        Hash function of the class.
        :return: str
        """
        return hash(self.product_id)
