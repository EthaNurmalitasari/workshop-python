# lambda functions can reference variables from the containing scope
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
#output
42

f(1)
# output
43


# Another use is to pass a small function as an argument
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# output
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]