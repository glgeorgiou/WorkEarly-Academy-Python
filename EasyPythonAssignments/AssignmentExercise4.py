"""
Find the sum of all the list's elements, excluding the last one.
Afterwards, multiply the sum you found with the last element in the list.
Finally, convert the output to an integer.
"""


def BasicAssignmentExercise4(arr):
    # code goes here
    lastLe = arr.pop()
    lCounter = 0

    for el in arr:
        lCounter += el

    return int(lCounter * lastLe)


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = BasicAssignmentExercise4([1, 2, 3, 4, 5])
print('Input : [1, 2, 3, 4, 5]')
print("Expected result: 50")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = BasicAssignmentExercise4([12, 12, 43, 54, 0])
print('Input : [12, 12, 43, 54, 0]')
print("Expected result: 0")
print("Actual result   {}".format(result))
