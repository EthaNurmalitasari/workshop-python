# open() returns a file object, and is most commonly used with two arguments: open(filename, mode)
f = open('workfile', 'w')

# either by a with statement or by calling f.close(), attempts to use the file object will automatically fail
f.close()
f.read()
# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.