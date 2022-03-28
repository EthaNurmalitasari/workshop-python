# Generators are a simple and powerful tool for creating iterators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)
# output
f
l
o
g