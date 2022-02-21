# function definitions paying close attention to the markers / and *
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


# The first function definition
standard_arg(2)
#output
2

standard_arg(arg=2)
#output
2


# The second function pos_only_arg is restricted to only use positional parameters as there is a / in the function definition
pos_only_arg(1)
#output
1

pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'


# The third function kwd_only_args only allows keyword arguments as indicated by a *
kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

kwd_only_arg(arg=3)
#output
3


# uses all three calling conventions in the same function definition
combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given


combined_example(1, 2, kwd_only=3)
#output
1 2 3

combined_example(1, standard=2, kwd_only=3)
#output
1 2 3

combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'


# consider this function definition which has a potential collision between the positional argument name and **kwds
def foo(name, **kwds):
    return 'name' in kwds


# There is no possible call that will make it return True
foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'


# But using / (positional only arguments)
def foo(name, /, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})
True