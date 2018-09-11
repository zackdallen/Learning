# Variables and data types

greeting = 'Hello world'
greeting = 'Hello everyone'

print(greeting)

# Data type
myStr = 'Hello'
myInt = 25
myFloat = 1.3

myList = [1,2,3,'Hello']
myDict = {'a': 1, 'b': 2, 'c': 3}

print(type(myStr), myStr)
print(type(myInt), myInt)
print(type(myFloat), myFloat)
print(type(myList), myList)
print(type(myDict), myDict)

print(myList[3])
print(myDict['a'])

print(myStr, 'world')
greeting = myStr + ' world'
print(greeting)