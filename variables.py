# A variable is a container for a value, which can be of various types

"""
Variable rules
-Variable names are case sensitive (name and NAME are different variables)
-Must start with a letter or an underscore
-Can have numbers but cannot start with one
"""

# In python there are no semicolon (;)

#x = 1		 #int
#y = 2.5 		# float
#name = 'Ronny' # str
#is_cool = True #bool

#Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Ronny',True)

#basic math
a = x + y

#print(x, y, name, is_cool, a)

#Casting
x = str(x)
y = int(y)
z = float(y)

#types
#print(type(x))
#print(type(y), y)
print(type(z), z)