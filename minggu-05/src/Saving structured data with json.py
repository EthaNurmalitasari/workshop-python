# If you have an object x, you can view its JSON string representation with a simple line of code
import json
x = [1, 'simple', 'list']
json.dumps(x)
# output
'[1, "simple", "list"]'

# Another variant of the dumps() function, called dump()
json.dump(x, f)

# To decode the object again, if f is a text file object which has been opened for reading:
x = json.load(f)