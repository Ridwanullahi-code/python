class BankAccount:
	def __init__(self,AccName,AccNumber,AccType,Amount):
		self.AccName = AccName
		self.AccNumber = AccNumber
		self.AccType = AccType
		self.Amount = Amount

	def Withdraw(self):
		return f"{self.AccName} Withdraw {self.Amount} Today"

	def Deposite(self):
		return f"{self.AccName} Deposite {self.Amount} Yesterday"

	def CheckBalance(self):
		return f"{self.AccName} Account Balance remain {self.Amount}"

	def CreateAcct(self):
		return f'{self.AccName} Account was successfully created'

customer = BankAccount("AJAYI",3424792409,"Saving", 5000)
print(customer.AccName,customer.AccNumber,customer.AccType,customer.Amount)
print(customer.Withdraw())
print(customer.Deposite())
print(customer.CheckBalance())
print(customer.CreateAcct())

