import difflib
from libraryItemFactories import LibraryItemFactory


class Catalogue:

	def __init__(self, item_list):
		"""
		Intialize the library with a list of books.
		:param item_list: a sequence of library item objects.
		"""
		self._item_list = item_list

	def retrieve_item_by_call_number(self, call_number):
		"""
		A private method that encapsulates the retrieval of an book with
		the given call number from the library.
		:param call_number: a string
		:return: book object if found, None otherwise
		"""
		found_book = None
		for library_book in self._item_list:
			if library_book.call_number == call_number:
				found_book = library_book
				break
		return found_book

	def find_items(self, title):
		"""
		Find items with the same and similar title.
		:param title: a string
		:return: a list of titles.
		"""
		title_list = []
		for library_item in self._item_list:
			title_list.append(library_item.get_title())
		results = difflib.get_close_matches(title, title_list, cutoff=0.5)
		return results

	def add_item(self, factory, **kwargs):
		"""
		Add an item to the item list.

		:return: an item added to the list
		"""
		new_item = factory().create_item(**kwargs)
		if new_item is None:
			print("Wrong input!!")
			return
		found_item = self.retrieve_item_by_call_number(new_item.call_number)
		if found_item:
			print(f"Could not add book with call number {new_item.call_number}. It already exists. ")
		else:
			self._item_list.append(new_item)
			print("item added successfully! book details:")
			print(new_item)

	def remove_item(self, call_number):
		"""
		Remove an existing book from the library
		:param call_number: a string
		:precondition call_number: a unique identifier
		"""
		found_book = self.retrieve_item_by_call_number(call_number)
		if found_book:
			self._item_list.remove(found_book)
			print(f"Successfully removed {found_book.get_title()} with call number: {call_number}")
		else:
			print(f"book with call number: {call_number} not found.")

	def reduce_item_count(self, call_number):
		"""
		Decrement the book count for an book with the given call number
		in the library.
		:param call_number: a string
		:precondition call_number: a unique identifier
		:return: True if the book was found and count decremented, false
		otherwise.
		"""
		library_book = self.retrieve_item_by_call_number(call_number)
		if library_book:
			library_book.decrement_number_of_copies()
			return True
		else:
			return False

	def increment_item_count(self, call_number):
		"""
		Increment the book count for an book with the given call number
		in the library.
		:param call_number: a string
		:precondition call_number: a unique identifier
		:return: True if the book was found and count incremented, false
		otherwise.
		"""
		library_book = self.retrieve_item_by_call_number(call_number)
		if library_book:
			library_book.increment_number_of_copies()
			return True
		else:
			return False

	@property
	def item_list(self):
		"""
		Return the item list
		:return: a list of item
		"""
		return self._item_list
