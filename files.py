# Python has functions for creating, reading, updating, and deleting files.

#open a file
myFile = open('myfile.txt', 'w')

#get some info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

#write to file
myFile.write('Python is awesome')
myFile.write(' and javascript, and mongoDB')
myFile.close()

#append to file
myFile = open('myfile.txt', 'a')
myFile.write(' I also love redux')
myFile.close()

#read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)