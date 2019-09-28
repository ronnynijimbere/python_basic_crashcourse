# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#create dictionary
person = {
	'first_name' : 'ronny',
	'last_name' : 'nijimbere',
	'age' : 33
}

print(person, type(person))

#use constructor
#person2 = dict(first_name= 'makelele', last_name='fatty')
#print(person2, type(person2))

#get value
print(person['first_name'])
print(person.get('last_name'))

#add key/value
person['phone'] = '+27-968-6553'

#get dict keys 
print(person.keys())

#get dict items
print(person.items())
#print(person)

#copy a dictionary
person2 = person.copy()
person2['city'] = 'Cape Town'
print(person2)

#remove item
del(person['age'])
person.pop('phone')
print(person)

#clear
person.clear()

#get lengh
print(len(person2))

#list of dict
people = [
	{
	'name': 'roxanne',
	'age': 25
	},
	{
	'name': 'thomas',
	'age': 28
	}
]

print(people[0]['name'])