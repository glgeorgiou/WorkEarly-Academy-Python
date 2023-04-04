# Experiment with files

from os import path

if path.exists('python_files_test.py'):
    src = path.realpath('python_files_test.py')
    head, tail = path.split(src)
    print('Head = ', head)
    print('Tail = ', tail)
else:
    print('Error')

