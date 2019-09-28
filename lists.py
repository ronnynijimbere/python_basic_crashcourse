# A List is a collection which is ordered and changeable. Allows duplicate members.

#create a list
numbers = [1,2,3,4,5,6,7]
fruits = ['banana','grapes','oranges','apples']

#use a constructor
#numbers2 = list((1,2,3,4,5,6,7))
#print(numbers, numbers2)

#Get a value
print(fruits[3])

#get lenth
print(len(fruits))

#append to list (allows you to add to your list)
fruits.append('mangos')
print(fruits)

#remove from list
fruits.remove('grapes')
print(fruits)

#insert into position
fruits.insert(2, 'peppers')
print(fruits)

#remove with pop method: default takes the last item in your list
fruits.pop(3)
print(fruits)

#change a value
fruits[0] = 'chicken'
print(fruits)

#reverse the list
fruits.reverse()
print(fruits)

#sort list: alphabetically
fruits.sort()
print(fruits)

#Reverse sort
fruits.sort(reverse=True)
print(fruits)


