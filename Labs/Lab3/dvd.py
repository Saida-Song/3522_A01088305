from library_item import LibraryItem


class DVD(LibraryItem):
	def __init__(self, call_num, title, num_copies, release_date, region_code):
		super().__init__(title, call_num, num_copies)
		self._release_date = release_date
		self._region_code = region_code

	def get_release_date(self):
		return self._release_date

	def get_region_code(self):
		return self._region_code

	def __str__(self):
		return f"---- Title: {self.get_title()} ----\n" \
			f"Call Number: {self.call_number}\n" \
			f"Number of Copies: {self._num_copies}\n" \
			f"Release date: {self.get_release_date()}\n" \
			f"Region code: {self.get_region_code()}\n"
