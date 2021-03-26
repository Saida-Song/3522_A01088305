from OrderProcessor import OrderProcessor
from datetime import datetime


class Store:
    """
    The Store Class.
    """

    def __init__(self):
        self.inventory = {}
        self.order_list = []
        self.valid_orders = []

    def receive_order(self, filename):
        """
        Receive order. Validate order, if order invalid, print error msg. If order valid, print order msg.

        :param filename: str
        """
        temp_orders = OrderProcessor.read_file(filename)
        self.order_list = temp_orders
        self.valid_orders.clear()

        for order in temp_orders:
            # validate order
            OrderProcessor.validate_order(order)

            # if order is in valid:
            if order.is_valid:
                self.valid_orders.append(order)

        for i in self.valid_orders:
            factory = i.factory
            name = i.name
            product_id = i.product_id
            details = i.product_details

            functions = {"Toy": factory().create_toy,
                         "StuffedAnimal": factory().create_stuffed_animal,
                         "Candy": factory().create_candy}

            item = functions[i.item_type](name=name, product_id=product_id, **details)
            if self.inventory.get(item) is None:
                self.inventory[item] = 100
            if self.inventory[item] - i.quantity < 0:
                self.inventory[item] += 100 - i.quantity
            else:
                self.inventory[item] -= i.quantity

    def check_inventory(self):
        """
        Print item in the inventory with their quantity.
        """
        for key, value in self.inventory.items():
            print(f"Name: {key.get_name()}, PRODUCT_ID: {key.get_id()}, STATUS: {Store.return_stock_status(value)}")

    def generate_daily_transaction_report(self):
        """
        Write all orders into a new file with it's time stamp.
        """
        current_time = datetime.now()
        file_time_stamp = current_time.strftime("%d%m%Y_%H%M")
        output_file_name = f"DTR_{file_time_stamp}.txt"
        with open(output_file_name, mode='w', encoding='utf-8') as output_file:
            header = (f"CST STORE - DAILY TRANSACTION REPORT (DTR)\n"
                      f"{current_time.strftime('%d-%m-%Y %H:%M')}")
            output_file.write(header + "\n")
            print(header)

            for order in self.order_list:
                # validate order
                OrderProcessor.validate_order(order)

                # if order is in valid:
                if not order.is_valid:
                    output_file.write(f"Order {order.order_num}, {order.invalid_notes}\n")
                    print(f"Order {order.order_num}, {order.invalid_notes}")
                else:
                    output_file.write(f"Order {order.order_num}, Item {order.item_type}, Product ID {order.product_id},"
                                      f" Name \"{order.name}\", Quantity {order.quantity}\n")
                    print(f"Order {order.order_num}, Item {order.item_type}, Product ID {order.product_id},"
                          f" Name \"{order.name}\", Quantity {order.quantity}")

    @staticmethod
    def return_stock_status(num_of_item):
        """
        Return the status of the item in the inventory.
        """
        if num_of_item == 0:
            return "Out of Stock"
        if num_of_item < 3:
            return "Very Low"
        if num_of_item < 10:
            return "Low"
        return "In Stock"
