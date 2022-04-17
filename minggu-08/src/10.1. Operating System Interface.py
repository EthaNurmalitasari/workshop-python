import os
os.getcwd()      # Return the current working directory
'C:\\Python310' #output
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
0 #output

import os
dir(os)
<returns a list of all module functions> #output
help(os)
<returns an extensive manual page created from the module's docstrings> #output

import shutil
shutil.copyfile('data.db', 'archive.db')
'archive.db' #output
shutil.move('/build/executables', 'installdir')
'installdir' #output