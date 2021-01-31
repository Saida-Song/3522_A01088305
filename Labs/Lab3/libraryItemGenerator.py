from book import Book
from dvd import DVD
from journal import Journal


class LibraryItemGenerator:

	def __init__(self):
		self._item = self.item_generator()

	@staticmethod
	def add_basic_info():
		call_number = input("Enter Call Number: ")
		title = input("Enter title: ")
		num_copies = int(input("Enter number of copies (positive number): "))
		data = (call_number, title, num_copies)
		return data

	def add_book(self):
		"""
		Add a brand new book to the library with a unique call number.
		"""
		book_data = self.add_basic_info()
		author = input("Enter Author Name: ")
		new_book = Book(book_data[0], book_data[1], book_data[2], author)
		return new_book

		# found_book = self.retrieve_item_by_call_number(
		# 	new_book.call_number)
		# if found_book:
		# 	print(f"Could not add book with call number {new_book.call_number}. It already exists. ")
		# else:
		# 	self._item_list.append(new_book)
		# 	print("book added successfully! book details:")
		# 	print(new_book)

	def add_journal(self):
		journal_data = self.add_basic_info()
		issue_number = input("Enter Issue Number: ")
		publisher = input("Enter publisher")
		new_journal = Journal(journal_data[0], journal_data[1], journal_data[2], issue_number, publisher)
		return new_journal

	def add_dvd(self):
		dvd_data = self.add_basic_info()
		release_date = input("Enter Release Date: ")
		region_code = input("Enter Region Code")
		new_dvd = DVD(dvd_data[0], dvd_data[1], dvd_data[2], release_date, region_code)
		return new_dvd

	def item_generator(self):
		print("\nWhat do you want to add?")
		print("-----------------------")
		print("1. Book")
		print("2. Journal")
		print("3. DVD")
		string_input = input("Please enter your choice (1-3)")

		user_input = int(string_input)

		if user_input == 1:
			return self.add_book()
		if user_input == 2:
			return self.add_journal()
		if user_input == 3:
			return self.add_dvd()
		print("Wrong input!!")
		return

	@property
	def item(self):
		return self._item