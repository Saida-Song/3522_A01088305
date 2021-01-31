from library_item import LibraryItem


class Journal(LibraryItem):
	"""
	Represents a single Journal in a library which is identified through it's call number.
	"""
	def __init__(self, call_num, title, num_copies, issue_num, publisher):
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
		self._issue_num = issue_num
		self._publisher = publisher

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
