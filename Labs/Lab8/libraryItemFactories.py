import abc
from library_item import Book, Journal, DVD


class LibraryItemFactory(abc.ABC):
	"""
	Represents an item factory of the library items.
	"""
	@abc.abstractmethod
	def create_item(self):
		pass


class BookFactory(LibraryItemFactory):
	"""
	Represents a book factory.
	"""
	def create_item(self, **kwargs):
		"""
		Return a Book.
		:param kwargs: variable keyword arguments
		:return: a Book
		"""
		return Book(**kwargs)


class DVDFactory(LibraryItemFactory):
	"""
	Represents a DVD factory.
	"""
	def create_item(self, **kwargs):
		"""
		Return a DVD.
		:param kwargs: variable keyword arguments
		:return: a DVD
		"""
		return DVD(**kwargs)


class JournalFactory(LibraryItemFactory):
	"""
	Represents a Journal factory.
	"""
	def create_item(self, **kwargs):
		"""
		Return a Journal.
		:param kwargs: variable keyword arguments
		:return: a Journal
		"""
		return Journal(**kwargs)
