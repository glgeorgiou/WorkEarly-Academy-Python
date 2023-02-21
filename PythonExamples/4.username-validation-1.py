"""
Have the function CodelandUsernameValidation(str) take the str parameter being passed
and determine if the string is a valid username according to the following rules:

We are tasked to check if a usernames that has a data type of a string fullfills the following conditions.

1. The username is between 4 and 25 characters.

2. It must start with a letter.

3. It can only contain letters, numbers, and the underscore character.

4. It cannot end with an underscore character.

If the username is valid then your program should return the string true,
otherwise return the string false.
"""


def CodelandUsernameValidation(str):
    if len(str) >= 4 and len(str) <= 25:
        if str[0].isalpha():
            if all(c.isalnum() or c == "_" for c in str[1:-1]):
                if str[-1] != "_":
                    return "true"
    return "false"


str = "John_1"
print(CodelandUsernameValidation(str))