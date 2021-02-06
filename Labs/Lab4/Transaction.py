from datetime import datetime


class Transaction:

	def __init__(self, amount, category, place):
		self._time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		self._amount = amount
		self._category = category
		self._place = place

	@property
	def amount(self):
		return self._amount

	@property
	def category(self):
		return self._category

	@property
	def place(self):
		return self._place

	def __repr__(self):
		return f"Time: {self._time}, Amount: ${self._amount}, Category: {self._category}, Place: {self._place}\n"
