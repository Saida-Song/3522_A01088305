import pandas as pd
import numpy as np
# import openpyxl

from ItemFactory import ChristmasItemFactory, HalloweenItemFactory, EasterItemFactory
from Order import Order
from enums.stuffing import Stuffing
from enums.fabric import Fabric
from enums.holidy import Holiday
from enums.colour import Colour


class OrderProcessor:
    """
    Processes the order.
    It is responsible for reading each row of these files
    and creating and yielding an Order object.
    """

    @staticmethod
    def read_file(filename):
        """
        Read orders from an excel file.
        :param filename: str
        :return: list of Orders
        """
        orders_list = []
        factory_map = FactoryMapping()
        try:
            orders = pd.read_excel(filename)
            orders.replace({np.nan: None})

            for i in range(0, len(orders)):
                order = orders.iloc[i]

                order_number = order["order_number"]
                product_id = order["product_id"]
                item = order["item"]
                name = order["name"]
                quantity = order["quantity"]
                details = order[6:].replace({np.nan: None}).to_dict()

                if details["dimensions"]:
                    width, height = details["dimensions"].split(",", 1)
                    details["width"] = width
                    details['height'] = height

                factory = factory_map.get_factory(holiday=order["holiday"])
                holiday = order["holiday"]

                temp_order = Order(order_number=order_number,
                                   product_id=product_id,
                                   item_type=item,
                                   name=name,
                                   product_details=details,
                                   factory=factory,
                                   quantity=quantity,
                                   holiday=holiday)
                orders_list.append(temp_order)

        except FileNotFoundError as e:
            print(e)
        except ImportError as e:
            print(e)
            print(f"Please make sure you have imported openpyxl, "
                  f"by typing \'pip install openpyxl\' in terminal")
        finally:
            return orders_list

    @staticmethod
    def validate_order(order):
        """
        Validate a single order.
        :param order: Order
        """
        error = "Could not process order data was corrupted, InvalidDataError -"
        details = order.product_details

        # check if its a valid Toy
        if order.item_type == "Toy":
            if details['has_batteries'] is None or details['min_age'] is None:
                order.is_invalid()
                error += "\n This toy is missing info about: Whether the toy is battery operated or not " \
                         "and The minimum recommended age of the child that the toy is safe for."

            if order.holiday == Holiday.HALLOWEEN.value:
                if not (details['spider_type'] == "Tarantula" or details['spider_type'] == 'Wolf Spider'):
                    order.is_invalid()
                    error += "\n The type of spider can either be a Tarantula or a Wolf Spider."

            elif order.holiday == Holiday.EASTER.value:
                if not (details['colour'] == Colour.ORANGE.value
                        or details['colour'] == Colour.BLUE.value
                        or details['colour'] == Colour.PINK.value):
                    order.is_invalid()
                    error += "\n The colour can be either Orange, Blue, or Pink."

        # check if its a valid StuffedAnimal
        elif order.item_type == "StuffedAnimal":
            # check size
            if not (details['size'] == 'S' or details['size'] != 'M' or details['size'] != 'L'):
                order.is_invalid()
                error += "\nSize - This can either be Small, Medium or Large for Stuffed Animal."

            if order.holiday == Holiday.HALLOWEEN.value:
                if details['stuffing'] != Stuffing.POLYESTER_FIBERFILL.value \
                        or details['fabric'] != Fabric.ACRYLIC.value:
                    order.is_invalid()
                    error += "\nIt should only made out of Acrylic yarn " \
                             "and stuffed with Polyester Fiberfill."

            elif order.holiday == Holiday.CHRISTMAS.value:
                if details['stuffing'] != Stuffing.WOOL.value or details['fabric'] != Fabric.COTTON.value:
                    order.is_invalid()
                    error += "\nIt should only made out of Cotton and and stuffed with Wool."

            elif order.holiday == Holiday.EASTER.value:
                if details['stuffing'] != Stuffing.POLYESTER_FIBERFILL.value or details['fabric'] != Fabric.LINEN.value:
                    order.is_invalid()
                    error += "\nIt should only made out of Linen and " \
                             "and stuffed with Polyester Fibrefill."
                if not (details['colour'] == Colour.WHITE.value
                        or details['colour'] == Colour.GREY.value
                        or details['colour'] == Colour.PINK.value
                        or details['colour'] == Colour.BLUE.value):
                    order.is_invalid()
                    error += "\n The colour can only be White, Grey, Pink or Blue."

        # check if its a valid Candy
        elif order.item_type == "Candy":
            # check size
            if details['has_nuts'] is None or details['has_lactose'] is None:
                order.is_invalid()
                error += "\nCandy should contain info about if it contains any nuts or " \
                         "if it is lactose free."

            if order.holiday == Holiday.HALLOWEEN.value:
                if not (details['variety'] == "Sea Salt" or details['variety'] == "Regular"):
                    order.is_invalid()
                    error += "\nPumpkin Caramel Toffee should only comes in two varieties " \
                             "— Sea Salt and Regular."
                if details['has_lactose'] == "N":
                    order.is_invalid()
                    error += "\nThe Pumpkin Caramel Toffee should not be lactose free."

            elif order.holiday == Holiday.CHRISTMAS.value:
                if details['has_lactose'] == "Y" or details['has_nuts'] == "Y":
                    order.is_invalid()
                    error += "\nThe Candy Canes should be lactose free and should not contain nuts."
                if not (details['colour'] == "Red" or details['colour'] == "Green"):
                    order.is_invalid()
                    error += "\nThe stripes on the candy cane can only be Red or Green."

            elif order.holiday == Holiday.EASTER.value:
                if details['has_lactose'] == "N":
                    order.is_invalid()
                    error += "\nThe Creme Eggs should not be lactose free."
                if details['pack_size'] is None:
                    order.is_invalid()
                    error += "\nThe Creme Eggs should come in different packets."

        order.set_invalid_notes(error)


class FactoryMapping:
    def __init__(self):
        self.factory_map = {
            "Christmas": ChristmasItemFactory,
            "Halloween": HalloweenItemFactory,
            "Easter": EasterItemFactory
        }

    def get_factory(self, holiday):
        """
        Return the factory based on the holiday.
        """
        return self.factory_map[holiday]
