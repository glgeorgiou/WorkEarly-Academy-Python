"""
Count the letters of a list
"""

# Import
from collections import Counter

# Produce list
lista = ['h', 'e', 'l', 'l', 'o']

print("The list is: ", lista)

# Count list items
count = Counter(lista)
print(count)

# Update the counter
count.update(['w', 'o', 'r', 'l', 'd'])
print('Added \'world\' into list: ', count)

# access the 'l' element
print('Count of \'l\' element: ', count['l'])

# counter values & keys are alphabetically ascending ordered
print('Counter values: ', count.values())
print('Counter keys: ', count.keys())