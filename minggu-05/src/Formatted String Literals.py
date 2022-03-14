# The following example rounds pi to three places after the decimal
import math
print(f'The value of pi is approximately {math.pi:.3f}.')
# output
The value of pi is approximately 3.142.

# This is useful for making columns line up
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
#output
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678

# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
# output
My hovercraft is full of eels.

print(f'My hovercraft is full of {animals!r}.')
# output
My hovercraft is full of 'eels'.