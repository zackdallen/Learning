# Functions

# Create a function
def sayHello(name = 'Jack'):
    'This is a comment in a function'
    print('Hello', name)

sayHello('Jon')

# Return value
def getSum(num1, num2):
    total = num1 + num2
    return total

numSum = getSum(1,2)
print(numSum)

# Ints are mutable as shown below
def addOneToNum(num):
    num = num + 1
    print('Value inside function:', num)
    return

# Int num doesn't change in value outside of the function when its value inside the function is changed
num = 5
addOneToNum(num)
print('Value outside of function:', num)


# Lists are immutable
def addOneToList(myList):
    myList.append(4)
    print('Value inside function:', myList)
    return

# Lists do change in value outside of the function when its value inside the function is changed
myList = [1,2,3]
addOneToList(myList)
print('Value outside of function:', myList)