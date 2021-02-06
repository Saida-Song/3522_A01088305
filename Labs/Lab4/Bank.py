class Bank:
	"""
	A class that represents a Bank.
	"""
	def __init__(self, name, balance):
		self._name = name
		self._balance = balance

	@property
	def name(self):
		"""
		Name getter.
		:return: a String
		"""
		return self._name

	@property
	def balance(self):
		"""
		Balace getter.
		:return: a float
		"""
		return self._balance

	@balance.setter
	def balance(self, amount):
		"""
		Balance setter.
		:param amount: a float
		"""
		self._balance -= amount

	def __repr__(self):
		"""
		String method of the class.
		:return: a String
		"""
		return f"Bank: {self._name}, Balance: {self._balance}"
