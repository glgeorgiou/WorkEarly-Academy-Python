# import modules
from os import path
import shutil
import datetime
import time

###
# Checks files and directories existence
###
print('Checks existence by using \'exists\' keyword')
print('File exists:' + str(path.exists('python_files.txt')))
print('File exists:' + str(path.exists('nonexistedfiles.txt')))
print('Directory exists: ' + str(path.exists('nonexistedirectory')))

print('\n\nChecks existence by using \'isfile\' keyword')
print('Is it a file? ' + str(path.isfile('python_files.txt')))
print('Is is a directory? ' + str(path.isdir('WorkEarlyAcademyPython')))



#
# Copy files
#

# Does file exists?
if path.exists('python_files.py'):
    # Store file path
    src = path.realpath('python_files.txt')
else:
    print('File does not exists')

# separate path and file name and print them
head, tail = path.split(src)
print('head: ', head)
print('tail: ', tail)

# copy existed file and paste it by adding the '.bak' word.
dst = src + '.bak'
shutil.copy(src, dst)

# copy existed file by copying also the metadata date and time
shutil.copystat(src, dst)

# Print meta data from the .bak file
t = time.ctime(path.getmtime('python_files.txt.bak'))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime('python_files.txt.bak')))