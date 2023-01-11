from collections import Counter

lista = ['a', 'b', 'r', 'a', 'c', 'a', 't', 'a', 'm', 'b', 'r', 'a']
count = Counter(lista)
print(count)

# Add symbols
count.update(['a', 'b', 'b', 'c'])
print('Updated: ', count)

# How many 'b' characters
print('Count of \'b\':', count['b'])

# Print values and keys
print('Counter values: ', count.values())
print('Counter keys: ', count.keys())