from Account import Account


class AngelAccount(Account):

	def __init__(self, bank, user):
		super().__init__(bank, user)
		self._user_type = "The Angel"

	def check_if_warn(self, budget):
		"""
		Warns the user if they exceed certain limit of the budget.
		:param budget: a Budget
		"""
		budget_status = budget.spent / budget.limit
		if budget_status > 1:
			print(f"-- Dear customer, you have exceeded the budget category: {budget.category}")
			return
		if budget_status > 0.9:
			print(f"-- Caution! You have exceed 90% of the budget: {budget.category}")
			return

	def lock_out(self, budget):
		pass

	def __repr__(self):
		return f"Account Number: {self._account_num:05d}, Account Type: {self._user_type}, {self._bank}, {self._user}."
