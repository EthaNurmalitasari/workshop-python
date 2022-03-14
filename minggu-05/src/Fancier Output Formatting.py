# you can write a Python expression between { and } characters that can refer to variables or literal values
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'
# output
'Results of the 2016 Referendum'

# need to provide the information to be formatted.
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
# output
' 42572654 YES votes  49.67%'

# str() will return the same value as repr()
s = 'Hello, world.'
str(s)
# output
'Hello, world.'

repr(s)
# output
"'Hello, world.'"

str(1/7)
# output
'0.14285714285714285'

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# output
The value of x is 32.5, and y is 40000...

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# output
'hello, world\n'

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
# output
"(32.5, 40000, ('spam', 'eggs'))"