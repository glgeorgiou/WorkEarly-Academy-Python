"""
Have the function DistinctList(arr) take the array of numbers stored in arr and determine the
total number of duplicate entries.
For example if the input is [1, 2, 2, 2, 3]
then your program should output 2 because there are two duplicates of one of the elements.
"""


def DistinctList(arr):
  arsret = set(arr)
  duplicates = len(arr)-len(arsret)

  return duplicates



print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = DistinctList([0,-2,-2,5,5,5])
print('Input : [0,-2,-2,5,5,5]')
print("Expected result: 3")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = DistinctList([100,2,101,4])
print('Input : [100,2,101,4]')
print("Expected result: 0")
print("Actual result   {}".format(result))

