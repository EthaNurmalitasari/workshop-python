x = int(input("Please enter an integer: "))x = int(input("Please enter an integer: "))
# An if … elif … elif … sequence is a substitute for the switch
if x < 0:
    x = 0
    print('Negative changed to zero')
# The keyword ‘elif’ is short for ‘else if’
# elif is useful to avoid excessive indentation
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')