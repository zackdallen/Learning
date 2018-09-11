# Loops

# For loops
people = ['Jon', 'Sara', 'Tim', 'Chris']
for person in people:
    print('Current person: ', person)

# Iterate by sequence index
for i in range(len(people)):
    print('Current person: ', people[i])

for i in range(0, 10):
    print(i)

# While loops
count = 0
while count < 10:
    print('Count: ', count)
    if count == 5:
        break
    count += 1
