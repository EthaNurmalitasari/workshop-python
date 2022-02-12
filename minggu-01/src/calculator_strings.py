#  Python can also manipulate strings
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#  In the interactive interpreter, the output string is enclosed in quotes and special characters are escaped with backslashes.
'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)  # with print(), \n produces a new line

# You can use raw strings by adding an r before the first quote
print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#  String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''.
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#  3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

#  String literals
'Py' 'thon'

text = ('Put several strings within parentheses '
'to have them joined together.')
text

prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal

#  Invalid syntax
('un' * 3) 'ium'

#  Use +
prefix + 'thon'

# Strings can be indexed (subscripted)
word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

#  Indices may also be negative numbers
word[-1]  # last character
word[-2]  # second-last character
word[-6]

# In addition to indexing, slicing is also supported
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

#  Slice indices have useful defaults
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

#  s[:i] + s[i:] is always equal 
word[:2] + word[2:]
word[:4] + word[4:]

#  Attempting to use an index that is too large will result in an error
word[42]  # the word only has 6 characters

#  Out of range slice indexes are handled gracefully when used for slicing
word[4:42]
word[42:]

#  Python strings cannot be changed
word[0] = 'J'
word[2:] = 'py'

#  If you need a different string, you should create a new one
'J' + word[1:]
word[:2] + 'py'

#  len() returns the length of a string
s = 'supercalifragilisticexpialidocious'
len(s)