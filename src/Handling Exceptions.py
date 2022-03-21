while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# An except clause may name multiple exceptions as a parenthesized tuple
except (RuntimeError, TypeError, NameError):
pass

# A class in an except clause is compatible with an exception if it is the same class or a base class thereof
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# All exceptions inherit from BaseException, and so it can be used to serve as a wildcard
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# It is useful for code that must be executed if the try clause does not raise an exception
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#  One may also instantiate an exception first before raising it and add any attributes to it as desired
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
# output
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs

# Exception handlers don’t just handle exceptions if they occur immediately in the try clause
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
# output
Handling run-time error: division by zero