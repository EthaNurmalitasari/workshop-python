# The raise statement allows the programmer to force a specified exception to occur
raise NameError('HiThere')
# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere

# The sole argument to raise indicates the exception to be raised
raise ValueError  # shorthand for 'raise ValueError()'

# a simpler form of the raise statement allows you to re-raise the exception
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
# output
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere