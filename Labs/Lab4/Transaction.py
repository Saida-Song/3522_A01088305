from datetime import datetime


class Transaction:
	"""
	A class that represent a transaction.
	"""

	def __init__(self, amount, category, place):
		self._time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self._amount = amount
		self._category = category
		self._place = place

	@property
	def amount(self):
		"""
		Amount getter.
		:return: a float
		"""
		return self._amount

	@property
	def category(self):
		"""
		Category getter.
		:return: a String
		"""
		return self._category

	@property
	def place(self):
		"""
		Position getter.
		:return: a String
		"""
		return self._place

	def __repr__(self):
		"""
		String method of the class.
		:return: a string
		"""
		return f"Time: {self._time}, Amount: ${self._amount}, Category: {self._category}, Place: {self._place}\n"
