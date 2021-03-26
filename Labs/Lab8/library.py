""" This module houses the library"""
from catalogue import Catalogue
from library_item import Book, DVD, Journal
from libraryItemFactories import BookFactory, DVDFactory, JournalFactory


class Library:
    """
    The Library consists of a list of items and provides an
    interface for users to check out, return and find items.
    """
    def __init__(self, catalogue: Catalogue):
        """
        Intialize the library with a list of items.
        :param catalogue: a Catalogue.
        """
        self._catalogue = catalogue

    def add_item_to_catalogue(self):
        """
        Add a specified item to the library with a unique call number.
        :return: a Library item
        """
        print("\nWhat do you want to add?")
        print("-----------------------")
        print("1. Book")
        print("2. Journal")
        print("3. DVD")
        string_input = input("Please enter your choice (1-3)")

        user_input = int(string_input)

        if user_input < 1 or user_input > 3:
            print("Wrong input!!")
            return

        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies (positive number): "))

        if user_input == 1:
            author = input("Enter Author Name: ")
            return self._catalogue.add_item(BookFactory,
                                            title=title,
                                            call_num=call_number,
                                            num_copies=num_copies,
                                            author=author)
        if user_input == 2:
            issue_number = input("Enter Issue Number: ")
            publisher = input("Enter publisher")
            return self._catalogue.add_item(JournalFactory,
                                            title=title,
                                            call_num=call_number,
                                            num_copies=num_copies,
                                            issue_num=issue_number,
                                            publisher=publisher)
        release_date = input("Enter Release Date: ")
        region_code = input("Enter Region Code")
        return self._catalogue.add_item(DVDFactory,
                                        title=title,
                                        call_num=call_number,
                                        num_copies=num_copies,
                                        release_date=release_date,
                                        region_code=region_code)

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_item = self._catalogue.retrieve_item_by_call_number(call_number)
        if library_item.check_availability():
            status = self._catalogue.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self._catalogue.increment_item_count(call_number)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove a item.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out a item")
            print("3. Return a item")
            print("4. Find a item")
            print("5. Add a item")
            print("6. Remove a item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_items()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self._catalogue.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.add_item_to_catalogue()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("items List")
        print("--------------", end="\n\n")
        for library_item in self._catalogue.item_list:
            print(library_item)


def generate_test_items():
    """
    Return a list of items with dummy data.
    :return: a list
    """
    item_list = [
        Book("100.200.300", "Harry Potter 1", 2, author="J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, author="J K Rowling"),
        Journal("631.495.302", "Harry Potter 3", 4, issue_num="53434", publisher="Router"),
        DVD("123.02.204", "The Cat in the Hat", 1, release_date="2014-01-05", region_code="342DV")
    ]
    return item_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = generate_test_items()
    catalogue = Catalogue(item_list)
    my_epic_library = Library(catalogue)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
