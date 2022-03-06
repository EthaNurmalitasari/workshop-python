# The variables sys.ps1 and sys.ps2 define the strings used as primary and secondary prompts:
import sys
sys.ps1
# output
'>>> '

sys.ps2
# output
'... '

sys.ps1 = 'C> '
# output
C> print('Yuck!')
Yuck!
C>

# The variable sys.path is a list of strings that determines the interpreter’s search path for modules
import sys
sys.path.append('/ufs/guido/lib/python')