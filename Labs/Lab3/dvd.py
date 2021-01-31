from library_item import LibraryItem


class DVD(LibraryItem):
	"""
	Represents a DVD in a library that is identified through a call number.
	"""
	def __init__(self, call_num, title, num_copies, release_date, region_code):
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
		self._release_date = release_date
		self._region_code = region_code

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
