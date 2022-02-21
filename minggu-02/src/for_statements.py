# Measure some strings:
words = ['cat', 'window', 'defenestrate']
# Python’s for statement iterates over the items of any sequence (a list or a string)
for w in words:
    print(w, len(w))
# Output
cat 3
window 6
defenestrate 12


# Code that modifies a collection while iterating over that same collection can be tricky to get right
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status