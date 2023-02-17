"""
Have the function CountNumbers(str) take the str string parameter being passed
and return the the amount of numbers contained within the given string.
 If two or more numbers exist next to each other, their values need to be combined to a single number.
"""

import re


def CountNumbers(str):
    numbers = re.findall(r'\d+', str)
    return len(numbers)


result = CountNumbers("1a2b3c4d5e")
print(result)

# The result is one because number values are combined into one
result = CountNumbers("1234")
print(result)