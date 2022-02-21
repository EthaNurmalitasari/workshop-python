# The pass statement does nothing
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# used for creating minimal classes
class MyEmptyClass:
    pass


#The pass is silently ignored
def initlog(*args):
    pass   # Remember to implement this!