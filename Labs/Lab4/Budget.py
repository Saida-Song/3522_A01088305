class Budget:

	def __init__(self, category, limit, spent):
		self._category = category
		self._limit = limit
		self._spent = spent
		self._locked = False
		self._transaction = []

	def add_to_category(self, transaction):
		self._transaction.append(transaction)

	@property
	def category(self):
		return self._category

	@property
	def limit(self):
		return self._limit

	@property
	def spent(self):
		return self._spent

	@property
	def locked(self):
		return self._locked

	@property
	def transaction(self):
		return self._transaction

	def __repr__(self):
		return f"Category: {self._category}, locked: {self._locked}, Limit: {self._limit}" \
			   f", Spent: {self._spent}, Amount Left: {self._limit - self._spent}"
