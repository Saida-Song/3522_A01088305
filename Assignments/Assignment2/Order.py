class Order:
    """
    Initiated a new order for the store
    """

    def __init__(self, order_number, product_id, item_type, name, product_details, factory, quantity, holiday):
        self._order_number = order_number
        self._product_id = product_id
        self._item_type = item_type
        self._name = name
        self._product_details = product_details
        self._factory = factory
        self._quantity = quantity
        self._holiday = holiday
        self._is_valid = True
        self._invalid_notes = ""

    @property
    def quantity(self):
        """
        Return quantity of the order.
        """
        return self._quantity

    @property
    def order_num(self):
        """
        Return order num of the order.
        """
        return self._order_number

    @property
    def product_id(self):
        """
        Return product id of the order.
        """
        return self._product_id

    @property
    def item_type(self):
        """
        Return item type of the order.
        """
        return self._item_type

    @property
    def name(self):
        """
        Return item name of the order.
        """
        return self._name

    @property
    def product_details(self):
        """
        Return other details of the item of the order.
        """
        return self._product_details

    @property
    def factory(self):
        """
        Return the factory that can generate the item.
        """
        return self._factory

    @property
    def holiday(self):
        """
        Return the holiday that the item for.
        """
        return self._holiday

    @property
    def invalid_notes(self):
        """
        Return the invalid notes if the item is invalid.
        """
        return self._invalid_notes

    @property
    def is_valid(self):
        """
        Return the valid status.
        """
        return self._is_valid

    def is_invalid(self):
        """
        Set the status to invalid.
        """
        self._is_valid = False

    def set_invalid_notes(self, error):
        """
        Set the invalid notes.
        """
        self._invalid_notes = error

    def __str__(self):
        """
        String method of the class.
        """
        return f"Order Number: {self._order_number} " \
               f"Product ID: {self._product_id} " \
               f"Item: {self._item_type} " \
               f"Name: {self._name} " \
               f"Quantity: {self._quantity} " \
               f"Product details: {self._product_details} "
