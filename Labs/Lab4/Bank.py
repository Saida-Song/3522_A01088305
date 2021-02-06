class Bank:

	def __init__(self, name, balance):
		self._name = name
		self._balance = balance

	@property
	def name(self):
		return self._name

	@property
	def balance(self):
		return self._balance

	@balance.setter
	def balance(self, amount):
		self._balance -= amount

	def __repr__(self):
		return f"Bank: {self._name}, Balance: {self._balance}"

def main():
	bank = Bank("hello", 500)
	bank.balance = 20
	print(bank.balance)

if __name__ == '__main__':
    main()