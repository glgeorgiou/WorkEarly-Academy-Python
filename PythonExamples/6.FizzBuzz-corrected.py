"""
Have the function FizzBuzz(num) take the num parameter being passed
and return all the numbers from 1 to num separated by spaces,
but replace every number that is divisible by 3 with the word "Fizz",
replace every number that is divisible by 5 with the word "Buzz",
and every number that is divisible by both 3 and 5 with the word "FizzBuzz".

For example: if num is 16, then your program should return
the string "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16".
The input will be within the range 1 - 50.

---- Comments on correction after manual testing
This file checks the last requirement 'The input will be within the range 1 - 50.' and
converts the input string to a number.
"""


def FizzBuzz(num):
    i = 1
    string = ''
    numn = int(num)
    if numn not in range(1, 51):
        return 0
    else:
        while (i <= numn):
            if (i % 3 == 0) and (i % 5 == 0):
                string += ' ' + "FizzBuzz"
            elif (i % 5 == 0):
                string += ' ' + "Buzz"
            elif (i % 3 == 0):
                string += ' ' + 'Fizz'
            else:
                string += ' ' + str(i)
            i += 1
        return string


print(FizzBuzz(input()))