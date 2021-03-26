import abc


class LibraryItem(abc.ABC):
	"""
	A class that represents the library item.
	"""

	def __init__(self, title, call_num, num_copies, **kwargs):
		"""
		:param title: a string
		:param call_num: a string
		:param num_copies: an int
		:precondition call_num: a unique identifier
		:precondition num_copies: a positive integer
		"""
		self._call_num = call_num
		self._num_copies = num_copies
		self._title = title

	def get_title(self):
		"""
		Returns the title of the book
		:return: a string
		"""
		return self._title.title()

	def increment_number_of_copies(self):
		"""
		Set's the number of copies of an book
		"""
		self._num_copies += 1

	def decrement_number_of_copies(self):
		"""
		Set's the number of copies of an book
		"""
		self._num_copies -= 1

	def get_num_copies(self):
		"""
		Returns the number of copies that are available for this
		specific book.
		:return: an int
		"""
		return self._num_copies

	@property
	def call_number(self):
		"""
		Right, this here is another way of using properties.
		We use decorators. The @property decorator defines a property
		that only allows us to GET a value and not set one.

		I want to point out that I have not expected you to do this in
		your labs. I'm using this as an opportunity to introduce you to
		a new way of avoiding mechanical getters and setters.
		:return:
		"""
		return self._call_num

	def check_availability(self):
		"""
		Returns True if the book is available and False otherwise
		:return: A Boolean
		"""
		if self._num_copies > 0:
			return True
		else:
			return False

	@abc.abstractmethod
	def __str__(self):
		pass


class Book(LibraryItem):
	"""
	A class that represents a Book.
	"""

	def __init__(self, title, call_num, num_copies, **kwargs):
		"""
        :param title: a string
        :param call_num: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
		super().__init__(title, call_num, num_copies)
		self._author = kwargs["author"]

	def get_author(self):
		"""
        Returns the author of the book.
        :return: a string
        """
		return self._author

	def __str__(self):
		return f"---- Book: {self.get_title()} ----\n" \
			   f"Call Number: {self.call_number}\n" \
			   f"Number of Copies: {self._num_copies}\n" \
			   f"Author: {self._author}\n"


class DVD(LibraryItem):
	"""
	Represents a DVD in a library that is identified through a call number.
	"""

	def __init__(self, title,  call_num, num_copies, **kwargs):
		"""
		:param call_num: a string
		:param title: a string
		:param num_copies: an int
		:param release_date: a string
		:param region_code: a string
		:precondition call_num: a unique identifier
		:precondition num_copies: a positive integer
		"""
		super().__init__(title, call_num, num_copies)
		self._release_date = kwargs["release_date"]
		self._region_code = kwargs["region_code"]

	def get_release_date(self):
		"""
		Return the release date of the DVD.
		:return: a string
		"""
		return self._release_date

	def get_region_code(self):
		"""
		Return the region code of the DVD
		:return: a string
		"""
		return self._region_code

	def __str__(self):
		return f"---- Title: {self.get_title()} ----\n" \
			   f"Call Number: {self.call_number}\n" \
			   f"Number of Copies: {self._num_copies}\n" \
			   f"Release date: {self.get_release_date()}\n" \
			   f"Region code: {self.get_region_code()}\n"


class Journal(LibraryItem):
	"""
	Represents a single Journal in a library which is identified through it's call number.
	"""

	def __init__(self, title, call_num, num_copies, **kwargs):
		"""
		:param call_num: a string
		:param title: a string
		:param num_copies: an int
		:param issue_num: a string
		:param publisher: a string
		:precondition call_num: a unique identifier
		:precondition num_copies: a positive integer
		"""
		super().__init__(title, call_num, num_copies)
		self._issue_num = kwargs["issue_num"]
		self._publisher = kwargs["publisher"]

	def get_issue_num(self):
		"""
		Return the issue number of the journal
		:return: a string
		"""
		return self._issue_num

	def get_publisher(self):
		"""
		Return the publisher of the journal
		:return: a string
		"""
		return self._publisher

	def __str__(self):
		return f"---- Name: {self.get_title()} ----\n" \
			   f"Call Number: {self.call_number}\n" \
			   f"Number of Copies: {self._num_copies}\n" \
			   f"Issue Number: {self.get_issue_num()}\n" \
			   f"Publisher: {self.get_publisher()}\n"
