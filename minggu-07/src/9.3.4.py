# Usually, a method is called right after it is bound
x.f()

# In the MyClass example, this will return the string 'hello world'
xf = x.f
while True:
    print(xf())