"""
RegExpr Approach
Have the function CodelandUsernameValidation(str) take the str parameter being passed
and determine if the string is a valid username according to the following rules:

We are tasked to check if a usernames that has a data type of a string fullfills the following conditions.

1. The username is between 4 and 25 characters.

2. It must start with a letter.

3. It can only contain letters, numbers, and the underscore character.

4. It cannot end with an underscore character.

If the username is valid then your program should return the string true,
otherwise return the string false.

The regular expression pattern ^[a-zA-Z][a-zA-Z0-9_]{3,24}[a-zA-Z0-9]$ matches the following:
^: matches the start of the string
[a-zA-Z]: matches a letter (uppercase or lowercase) at the start of the string
[a-zA-Z0-9_]: matches a letter (uppercase or lowercase), a digit, or an underscore
{2,23}: the previous group is repeated between 2 and 23 times
[a-zA-Z0-9]: matches a letter (uppercase or lowercase) or a digit
$: matches the end of the string

"""

import  re


def CodelandUsernameValidation(p_str_un):
    pattern = "^[a-zA-Z][a-zA-Z0-9_]{2,23}[a-zA-Z0-9]$"
    match = re.match(pattern, p_str_un)
    # If the input string matches the pattern, return "true"
    if match:
        return "true"
    # If the input string doesn't match the pattern, return "false"
    else:
        return "false"


str_un = "John_1"
print(CodelandUsernameValidation(str_un))