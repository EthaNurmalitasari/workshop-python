squares = [1, 4, 9, 16, 25]
squares

#  All other built-in sequence types lists can be indexed and sliced
squares[0]  # indexing returns the item
squares[-1]
squares[-3:]  # slicing returns a new list

#  All slice operations return a new list containing the requested elements
squares[:]

# Lists also support operations like concatenation
squares + [36, 49, 64, 81, 100]

# Lists are a mutable type
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
cubes

#  You can also add new items at the end of the list, by using the append()
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes

#  Assignment to slices is also possible, and this can even change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
# now remove them
letters[2:5] = []
letters
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters

#  The built-in function len() also applies to lists
letters = ['a', 'b', 'c', 'd']
len(letters)

#  It is possible to nest lists (create lists containing other lists)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
x[0]
x[0][1]