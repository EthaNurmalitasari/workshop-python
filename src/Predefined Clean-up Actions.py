# Some objects define standard clean-up actions to be undertaken when the object is no longer needed
for line in open("myfile.txt"):
    print(line, end="")

# The with statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")