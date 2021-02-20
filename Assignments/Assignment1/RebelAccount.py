from Account import Account


class RebelAccount(Account):

	def __init__(self, bank, user):
		super().__init__(bank, user)
		self._user_type = "The Rebel"
		self._num_of_lock = 0

	def check_if_warn(self, budget):
		"""
		Warns the user if they exceed certain limit of the budget.
		:param budget: a Budget
		"""
		if budget.locked:
			print(f"-- Sorry, the category {budget.category} is locked.")
			return
		budget_status = budget.spent / budget.limit
		if budget_status > 1:
			self.lock_out(budget)
			self._num_of_lock += 1
			if self._num_of_lock >= 2:
				for budget in self._budgets:
					self.lock_out(budget)
				print(f"-- Sorry, exceeded 2 budget category. Your account is locked out")
				return
			print(f"-- Warning! Exceed the budget! the category {budget.category} is locked.")
			return
		if budget_status > 0.5:
			print(f"Warning: You have exceeded 50% of the budget {budget.category}")

	def lock_out(self, budget):
		budget.locked = True

	def __repr__(self):
		return f"Account Number: {self._account_num:05d}, Account Type: {self._user_type}, {self._bank}, {self._user}."
