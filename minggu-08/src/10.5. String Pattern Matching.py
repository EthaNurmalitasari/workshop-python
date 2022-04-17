import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest'] #output
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat' #output

'tea for too'.replace('too', 'two')
'tea for two' #output