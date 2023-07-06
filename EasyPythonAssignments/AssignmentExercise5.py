"""
Print the amount of numbers contained within the given string.
If two or more numbers exist next to each other, their values need to be combined to a single number.
"""


def BasicAssignmentExercise5(strParam):
    # code goes here
    nCounter = 0

    for char in strParam:
        if char.isnumeric():
            nCounter += 1

    return nCounter


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = BasicAssignmentExercise5("This string has 1 number!")
print('Input : "This string has 1 number!"')
print("Expected result: 1")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = BasicAssignmentExercise5("2 + 13 = 15")
print('Input : "2 + 13 = 15"')
print("Expected result: 3")
print("Actual result   {}".format(result))