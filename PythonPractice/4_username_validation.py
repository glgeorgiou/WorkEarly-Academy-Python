"""
Have the function CodelandUsernameValidation(str) take the str parameter being passed
and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string
false.
"""

import re


def CodelandUsernameValidation(strParam):
    number_of_letters = 0

    for i in strParam:
        number_of_letters += 1

    if (number_of_letters in range(4, 26)) and (strParam[0].isalpha()) and (re.match("^[A-Za-z0-9_]*$", strParam)) and (
            strParam[-1] != "_"):
        return True
    else:
        return False


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = CodelandUsernameValidation('u__hello_world123')
print("Expected result: True")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = CodelandUsernameValidation('aa_')
print("Expected result: False")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case 1-----------------------")
result = CodelandUsernameValidation('aaaaaaaaaa')
print("Expected result: True")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case 2 -----------------------")
result = CodelandUsernameValidation('u__hello_world123')
print("Expected result: True")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case 3 -----------------------")
result = CodelandUsernameValidation('__bbbbbbb')
print("Expected result: False")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case 4 -----------------------")
result = CodelandUsernameValidation('b3333434_')
print("Expected result: False")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case 5 -----------------------")
result = CodelandUsernameValidation('usernamehello123')
print("Expected result: True")
print("Actual result is {}".format(result))
result = 0

print("\n--------------------Test case 6 -----------------------")
result = CodelandUsernameValidation('123abc444')
print("Expected result: False")
print("Actual result is {}".format(result))
