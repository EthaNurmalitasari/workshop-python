# By now you have probably noticed that most container objects can be looped over using a for statement
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')

# You can call the __next__() method using the next() built-in function
s = 'abc'
it = iter(s)
it
# output
<str_iterator object at 0x10c90e650>

next(it)
# output
'a'

next(it)
# output
'b'

next(it)
# output
'c'

next(it)
# output
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration

# If the class defines __next__(), then __iter__() can just return self
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)
# output
<__main__.Reverse object at 0x00A1DB50>

for char in rev:
    print(char)
# output
m
a
p
s