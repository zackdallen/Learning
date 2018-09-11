# String functions

myStr = 'hello world'

# .capitalize() capitalizes the first letter in a string
print(myStr.capitalize())

# .swapcase changes the cases of all the letters in a string
print(myStr.swapcase())

# Get length
print(len(myStr))

# Replace
print(myStr.replace('world','everyone'))

# Count - counts number of occurrences of the item in question (capitalization does matter)
sub = 'l'
print(myStr.count(sub))
sub = "h"
print(myStr.count(sub))

# Starts with
print(myStr.startswith('hello'))

# Ends with
print(myStr.endswith('world'))

# Split to list
print(myStr.split())

# Find
print(myStr.find('world'))

# Index
print(myStr.index('l'))

# Is all alphanumeric? (numbers and letters, but no spaces or symbols)
print(myStr.isalnum())

# Is all alphabetic? (letters only)
print(myStr.isalpha())

# Is all numeric? (numbers only)
print(myStr.isnumeric())
