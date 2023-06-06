"""
Have the function HappyNumbers(num) determine if a number is Happy, which is a number whose
sum of the square of the digits eventually converges to 1. Return true if it's a Happy number,
otherwise return false.
For example: the number 10 is Happy because 1^2 + 0^2 converges to 1.
"""


def HappyNumbers(num):
    # code goes here
    if num == 1:
        return True;

    sum = 0

    while num > 0:
        rem = num % 10
        sum = sum + (rem * rem)
        num //= 10
    return num


print(HappyNumbers(101)) # Expected result = False
print(HappyNumbers(1)) # Expected result = True