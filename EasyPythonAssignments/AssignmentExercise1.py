"""
Print the sum of the first and last elements in the given list.
The list's length may vary throughout the different test cases.
"""


def BasicAssignmentExercise1(arr):

  # code goes here
  return arr[0]+arr[-1]


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = BasicAssignmentExercise1([1, 2, 3, 4, 5])
print('Input : [1,2,3,4,5]')
print("Expected result: 6")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = BasicAssignmentExercise1([56, 43, 87, 34, 675, 2])
print('Input : [56,43,87,34,675,2]')
print("Expected result: 58")
print("Actual result   {}".format(result))