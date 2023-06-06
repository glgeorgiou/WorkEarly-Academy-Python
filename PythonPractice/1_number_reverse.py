"""
Have the function NumberReverse(str) take the str parameter being passed which will be a
string of numbers, and return a new string with the numbers in reverse order.
"""

def NumberReverse(strParam):
    return " ".join(reversed(strParam.split(" ")))


print(NumberReverse('23 5 14'))
