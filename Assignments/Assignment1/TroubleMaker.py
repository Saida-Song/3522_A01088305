from Account import Account


class TroubleMaker(Account):

	def __init__(self, bank, user):
		super().__init__(bank, user)
		self._user_type = "The TroubleMaker"

	def check_if_warn(self, budget):
		"""
		Warns the user if they exceed certain limit of the budget.
		:param budget: a Budget
		"""
		if budget.locked:
			print(f"-- Sorry, the category {budget.category} is locked.")
			return
		budget_status = budget.spent / budget.limit
		if budget_status > 1.2:
			self.lock_out(budget)
			print(f"-- Sorry, the category {budget.category} is locked.")
			return
		if budget_status > 1:
			print(f"-- Dear customer, you have exceeded the budget category: {budget.category}")
			return
		if budget_status > 0.75:
			print(f"-- Caution! You have exceed 75% of the budget: {budget.category}")
			return

	def lock_out(self, budget):
		budget.locked = True

	def __repr__(self):
		return f"Account Number: {self._account_num:05d}, Account Type: {self._user_type}, {self._bank}, {self._user}."
