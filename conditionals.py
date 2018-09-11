# Conditionals

x = 4

# Basic if
if x < 6:
    print('This is true')

# If Else
if x < 6:
    print('This is true')
else:
    print('This is false')

# Elif
color = 'red'
if color == 'red':
    print('The color is red')
elif color == 'blue':
    print('The color is blue')
else:
    print('The color is not red or blue')

# Nested if
if color == 'red':
    if x < 10:
        print('Color red and x < 10')

# Logical operators (and or)
if color == 'red' and x < 10:
    print('Color red and x < 10')