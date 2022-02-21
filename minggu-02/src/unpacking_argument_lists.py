list(range(3, 6))            # normal call with separate arguments
# output
[3, 4, 5]

args = [3, 6]
list(range(*args))            # call with arguments unpacke
# output
[3, 4, 5]


# dictionaries can deliver keyword arguments with the **-operator
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
#output
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !