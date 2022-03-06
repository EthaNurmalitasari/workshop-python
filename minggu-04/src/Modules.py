# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Now enter the Python interpreter and import this module with the following command:
import fibo

# Using the module name you can access the functions
fibo.fib(1000)
# output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

fibo.fib2(100)
# output
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

fibo.__name__
# output
'fibo'

# If you intend to use a function often you can assign it to a local name:
fib = fibo.fib
fib(500)
# output
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377