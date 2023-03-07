"""
Have the function DistinctList(arr) take the array of numbers stored in arr
and determine the total number of duplicate entries.

For example if the input is [1, 2, 2, 2, 3] then your program should output 2
because there are two duplicates of one of the elements.
"""


def DistinctList(arr):
    arrset = set(arr)
    duplicates = len(arr) - len(arrset)

    return duplicates


# print(DistinctList(input()))

# My function call solution
pinax = [1, 2, 2, 2, 3]
print((DistinctList(pinax)))

"""
The function DistinctList(arr) takes a list arr as input and returns the number of duplicates in the list. 
It does so by first converting the list into a set. Since sets only contain unique elements, 
the length of the set will be less than or equal to the length of the original list
if the original list contains duplicates.
 
The number of duplicates can be found 
by subtracting the length of the set from the length of the original list: 
duplicates = len(arr) - len(arrset). This is the value that the function returns.
"""