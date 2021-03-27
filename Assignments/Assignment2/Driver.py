from CSTstore import Store

# please import the following packages
import pandas
import numpy
import openpyxl


class StoreMenu:
    def __init__(self):
        """
        Initiated a new Store menu.
        """
        self.store = Store()
        self.run = True

    def display_store_menu(self):
        """
        Display the menu of store operation.
        """
        print("-" * 10, "Welcome to CST store", "-" * 10)
        print(f"Please make sure you have imported the following python packages/library for program to function:\n"
              f"pandas, numpy, openpyxl.")

        while self.run:

            print(f"What Do You Want To Do Today?\n"
                  f"	1 - Process Web Orders\n"
                  f"	2 - Check Inventory\n"
                  f"	3 - Exit")
            user_input = input("Please enter your option: ")
            if user_input != "1" and user_input != "2" and user_input != "3":
                print("Invalid input. Please check!\n")
                continue
            if user_input == "1":
                file_path = input("Please enter your file name you want to proceed: ")
                self.store.receive_order(file_path)

            if user_input == "2":
                self.store.check_inventory()

            if user_input == "3":
                self.store.generate_daily_transaction_report()
                self.run = False

        print("Thank you for using the system. \n")


def main():
    """
    Drives the CST store program.
    """
    new_store = StoreMenu()
    new_store.display_store_menu()


if __name__ == '__main__':
    main()
