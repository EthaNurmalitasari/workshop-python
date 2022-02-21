# This creates a function that can be called with fewer arguments
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# The default values are evaluated at the point of function definition in the defining scope
i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# The default value is evaluated only once
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))
# output
[1]
[1, 2]
[1, 2, 3]


# this is another option If you don’t want the default to be shared between subsequent calls
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L