print("***inheritance using banking concept ***")
class Bank:
	def __init__(self,n,m,balance=0.0):
		self.acno=n
		self.name=m
		self.balance=balance
	def deposit(self,amt):
		self.balance+=amt
		return self.balance
	def withdraw(self,amt):
		if amt>self.balance:
			print('\n Balance amt is less,so cannot withdraw')
		else:
			self.balance-=amt
			return self.balance
accno=input('Enter Acct.no:')
name=input('Enter name:')
b=Bank(accno,name)
flag='yes'
while flag=='yes':
	print('d-deposit','w-withdrawal')
	ch=input('Enter choice:')
	if ch=='d':
		amt=float(input('Enter amount to be deposited:'))
		print('Balance amount:',b.deposit(amt))
	else:
		amt=float(input('Enter amount to be withdrawal:'))
		print('Balance amount:',b.withdraw(amt))
flag=input('\n Do you want to continue yes/no:')