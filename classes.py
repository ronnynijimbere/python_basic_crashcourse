# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create class
class User:
	#constructor
	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age

	#method
	def greeting(self):
		return f'My is {self.name}, my email is {self.email} and i am {self.age}'	

	def has_birthday(self):
		self.age += 1	

# Extend class
class Customer(User):
	#constructor
	def __init__(self, name, email, age):
		self.name = name
		self.email = email
		self.age = age
		self.balance = 0

	def set_balance(self, balance):
		self.balance = balance

	def greeting(self):
		return f'My is {self.name}, my email is {self.email} and i am {self.age} and my balance is {self.balance}'	
	
				

#init user object
ronny = User('Ronny Nijimbere', 'ron@gmail.com', 33)
#init customer object
ronnelly = Customer('Ronnelly Nijimbere', 'ronnelly@gmail.com', 27)

ronnelly.set_balance(500)
print(ronnelly.greeting())

#print(ronny.name)
ronny.has_birthday()
print(ronny.greeting())
