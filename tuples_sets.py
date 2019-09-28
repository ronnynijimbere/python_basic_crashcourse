# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#create tuple: uses () instead of []
fruits = ('apples', 'bananas', 'oranges', 'grapes')

#use a constructor
fruits1 = tuple(('apples', 'bananas', 'oranges', 'grapes'))
print(fruits, fruits1)

#single value needs a trailing comma
fruits1 = ('apples',)
print(fruits1)

#get value
print(fruits[1])

#cant change value
#fruits[0] = 'straberries'
#print(fruits[0])

#delete tuple
#del fruits1
#print(fruits1)

#get lenth
#print(len(fruits))



# A Set is a collection which is unordered and unindexed. 
#No duplicate members and is create with {}.

#create a set
fruit_set = {'apples', 'bananas', 'oranges', 'grapes'}
print(fruit_set)

#check if something is in a set: returns Boolean
print('bananas' in fruit_set)

#add to set
fruit_set.add('lobsters')
print(fruit_set)

#remove
fruit_set.remove('lobsters')

#add duplicate
fruit_set.add('bananas')


#clear set
#fruit_set.clear()

#delete set
#del fruit_set
print(fruit_set)