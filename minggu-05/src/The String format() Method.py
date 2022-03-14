# Basic usage of the str.format() method looks like this:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# output
We are the knights who say "Ni!"

#The brackets and characters within them (called format fields)
print('{0} and {1}'.format('spam', 'eggs'))
# output
spam and eggs

print('{1} and {0}'.format('spam', 'eggs'))
# output
eggs and spam

# their values are referred to by using the name of the argument
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
# output
This spam is absolutely horrible.

# Positional and keyword arguments can be arbitrarily combined:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
other='Georg'))
# output
The story of Bill, Manfred, and Georg.

# This can be done by simply passing the dict and using square brackets '[]' to access the keys
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# output
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# This could also be done by passing the table as keyword arguments with the ‘**’ notation.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# output
Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# the following lines produce a tidily-aligned set of columns giving integers and their squares and cubes:
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# output
1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000