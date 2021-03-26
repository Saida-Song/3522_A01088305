import abc

from library_item import Book, Journal, DVD
from abc import ABC


class LibraryItemFactory(ABC):
	"""
	Represents an item generator of the library items.
	"""
	@abc.abstractmethod
	def create_item(self):
		pass


class BookFactory(LibraryItemFactory):
	def create_item(self, **kwargs):
		return Book(**kwargs)


class DVDFactory(LibraryItemFactory):
	def create_item(self, **kwargs):
		return DVD(**kwargs)


class JournalFactory(LibraryItemFactory):
	def create_item(self, **kwargs):
		return Journal(**kwargs)