"""
How many times can the letter e be found in the given string arrays?
"""


def BasicAssignmentExercise3(strArr):
    # code goes here
    countEs = 0

    for el in strArr:
        for e in el:
            if e == 'e':
                countEs += 1

    return countEs


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = BasicAssignmentExercise3(["This is", "an array", "of strings!"])
print('Input : ["This is", "an array", "of strings!"]')
print("Expected result: 0")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = BasicAssignmentExercise3(["Python exercises", "are", "so much", "fun!"])
print('Input : ["Python exercises", "are", "so much", "fun!"]')
print("Expected result: 4")
print("Actual result   {}".format(result))
