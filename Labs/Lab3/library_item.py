import abc


class LibraryItem(abc.ABC):

	def __init__(self, title, call_num, num_copies):
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
