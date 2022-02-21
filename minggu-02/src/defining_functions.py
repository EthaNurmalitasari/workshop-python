# create a function that writes the Fibonacci series to an arbitrary boundary
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)


fib
# output
<function fib at 10042ed0>

f = fib
f(100)
# output
0 1 1 2 3 5 8 13 21 34 55 89


# This value is called None (it’s a built-in name)
fib(0)
print(fib(0))
# output
None


# It is simple to write a function that returns a list of the numbers of the Fibonacci series
def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
f100                # write the result
# output
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]