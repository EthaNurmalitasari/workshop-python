# Range() generates arithmetic progressions
for i in range(5):
    print(i)
#output
0
1
2
3
4


# The given end point is never part of the generated sequence
list(range(5, 10))
#output
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
#output
[0, 3, 6, 9]

list(range(-10, -100, -30))
#output
[-10, -40, -70]


# To iterate over the indices of a sequence, you can combine range() and len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
#output
0 Mary
1 had
2 a
3 little
4 lamb


# A strange thing happens if you just print a range
range(10)
#output
range(0, 10)


# example of a function that takes an iterable is sum()
sum(range(4))  # 0 + 1 + 2 + 3
#output
6