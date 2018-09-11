# Open a file
# 'w' is to write to the file. This will delete anything previously stored and will write something new
fo = open('txt.txt', 'w')
# Get some info
print('Name:', fo.name)
print('Is closed:', fo.closed)
print('Opening mode:', fo.mode)
# Writes to file
fo.write('I love python')
fo.write(' and JavaScript')
# Closes the txt.txt file
fo.close()

# 'a' opens to append mode to add onto previous edits
fo = open('txt.txt', 'a')
fo.write('. I also like PHP.')
fo.close()

# Read from file
fo = open('txt.txt', 'r+')
# Reads full text
text = fo.read()
print(text)
fo.close()

fo = open('txt.txt', 'r+')
# Reads first 10 characters
text2 = fo.read(10)
print(text2)
fo.close()

# Create a file (the 'w+' creates then writes to the document if it isn't already created)
fo = open('txt2.txt', 'w+')
fo.write('This is my new file')
fo.close()