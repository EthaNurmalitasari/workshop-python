# To read a file’s contents, call f.read(size)
f.read()
# output
'This is the entire file.\n'
f.read()
# output
''

# f.readline() reads a single line from the file
f.readline()
# output
'This is the first line of the file.\n'

f.readline()
# output
'Second line of the file\n'

f.readline()
# output
''

# For reading lines from a file, you can loop over the file object
for line in f:
    print(line, end='')
# output
This is the first line of the file.
Second line of the file

# f.write(string) writes the contents of string to the file
f.write('This is a test\n')
# output
15

# Other types of objects need to be converted either to a string or a bytes object before writing them:
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
# output
18

# To change the file object’s position, use f.seek(offset, whence)
f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
# output
16

f.seek(5)      # Go to the 6th byte in the file
# output
5

f.read(1)
# output
b'5'

f.seek(-3, 2)  # Go to the 3rd byte before the end
# output
13

f.read(1)
# output
b'd'