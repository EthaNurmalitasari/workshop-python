# The initial expression in a list comprehension can be any arbitrary expression
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# The following list comprehension will transpose rows and columns:
[[row[i] for row in matrix] for i in range(4)]

# the nested listcomp is evaluated in the context of the for that follows it
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

# which, in turn, is the same as:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed

# The zip() function would do a great job for this use case
list(zip(*matrix))