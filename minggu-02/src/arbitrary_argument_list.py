# the least frequently used option is to specify that a function can be called with an arbitrary number of arguments
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
# output
'earth/mars/venus'

concat("earth", "mars", "venus", sep=".")
# output
'earth.mars.venus'