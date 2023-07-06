"""
Use the input as x and the function shown below in order to produce the needed integer results.
f(x) = (x+2) * X/5
"""


def BasicAssignmentExercise2(num):

  # code goes here
  res = ((num + 2) * num) / 5
  return int(res)


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = BasicAssignmentExercise2(5)
print('Input : 5')
print("Expected result: 7")
print("Actual result   {}".format(result))
result = 0

print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case B-----------------------")
result = BasicAssignmentExercise2(10)
print('Input : 10')
print("Expected result: 24")
print("Actual result   {}".format(result))