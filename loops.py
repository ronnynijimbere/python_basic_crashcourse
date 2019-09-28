# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['simon', 'thomas', 'mike', 'suzan']

#simple loop
#for person in people:
#	print(f'current person: {person}')

#break	
#for person in people:
#	if person == 'mike':
#		break
#	print(f'current person: {person}')

#continue
#for person in people:
#	if person == 'mike':
#		continue
#	print(f'current person: {person}')

#range
#for i in range(len(people)):
#	print(people[i])

#for i in range(0, 11):
#	print(f'Number: {i}')	

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 24:
	print(f'Count: {count}')
	count += 1