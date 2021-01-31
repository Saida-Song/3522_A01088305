from library_item import LibraryItem


class Journal(LibraryItem):
	def __init__(self, call_num, title, num_copies, issue_num, publisher):
		super().__init__(title, call_num, num_copies)
		self._issue_num = issue_num
		self._publisher = publisher

	def get_issue_num(self):
		return self._issue_num

	def get_publisher(self):
		return self._publisher

	def __str__(self):
		return f"---- Name: {self.get_title()} ----\n" \
			f"Call Number: {self.call_number}\n" \
			f"Number of Copies: {self._num_copies}\n" \
			f"Issue Number: {self.get_issue_num()}\n" \
			f"Publisher: {self.get_publisher()}\n"
