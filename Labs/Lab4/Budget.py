class Budget:
	"""
	A class that represents a Budget of a category.
	"""

	def __init__(self, category, limit, spent):
		self._category = category
		self._limit = limit
		self._spent = spent
		self._locked = False
		self._transaction = []

	def add_to_category(self, transaction):
		"""
		Add a Transaction to the category.
		:param transaction: a Transaction
		"""
		self._transaction.append(transaction)

	@property
	def category(self):
		"""
		Category getter.
		:return: a String
		"""
		return self._category

	@property
	def limit(self):
		"""
		Limit getter.
		:return: A float
		"""
		return self._limit

	@property
	def spent(self):
		"""
		Spent amount getter.
		:return: a float
		"""
		return self._spent

	@property
	def locked(self):
		"""
		Locked property getter.
		:return: a boolean
		"""
		return self._locked

	@property
	def transaction(self):
		"""
		transactions getter.
		:return: a list
		"""
		return self._transaction

	def __repr__(self):
		"""
		String method of the class.
		:return: a String
		"""
		return f"Category: {self._category}, locked: {self._locked}, Limit: {self._limit}" \
			   f", Spent: {self._spent}, Amount Left: {self._limit - self._spent}"
