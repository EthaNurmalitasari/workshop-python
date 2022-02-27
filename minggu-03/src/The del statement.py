# The del statement can also be used to remove slices from a list or clear the entire list
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
a

del a[2:4]
a

del a[:]
a

# del can also be used to delete entire variables:
del a