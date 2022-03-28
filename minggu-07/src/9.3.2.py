# Class objects support two kinds of operations: attribute references and instantiation
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

# Just pretend that the class object is a parameterless function that returns a new instance of the class
x = MyClass()

# The instantiation operation (“calling” a class object) creates an empty object
def __init__(self):
    self.data = []

# When a class defines an __init__() method, class instantiation automatically invokes __init__() for the newly-created class instance
x = MyClass()

# the __init__() method may have arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__()
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
# output
(3.0, -4.5)