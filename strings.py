# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


name = 'ronny'
age = 33

#concatenate (can only concatenate a string and not an interger)
print('Word up, my name is ' + name + 'and Im ' + str(age))

# String Formatting

# Arguments by position
print('my name is {name} and i am {age}'.format(name=name, age=age))

#F-strings (3.6+)
print(f'Hello, my name is {name} and i am {age}')

# String Methods
s = 'hello world'

#capitalize string
print(s.upper()) # Returns HELLO WORLD
print(s.capitalize()) #Returns Hello world
print(s.lower()) # Returns hello world
print(s.swapcase()) #Returns HELLO WORLD
print(len(s))

#replace
#print(s.replace('world', 'everyone'))

#Count
#sub = 'h'
print(s.count(sub))

#Starts with: this is a boolean
print(s.startswith('hello'))

#Ends with: this is a boolean
print(s.endswith('d'))

#split into a list
print(s.split()) #Returns ['hello', 'world']

#find position
print(s.find('r'))

# Is all alphanumeric: this is a boolean
print(s.isalnum())

# Is all alphabetic: this is a boolean
print(s.isalpha())

# Is all numeric: this is a boolean
print(s.isnumeric())