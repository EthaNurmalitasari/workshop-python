# if x is the instance of MyClass created above, the following piece of code will print the value 16, without leaving a trace
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter