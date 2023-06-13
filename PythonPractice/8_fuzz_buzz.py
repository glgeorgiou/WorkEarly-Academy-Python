"""
Have the function FizzBuzz(num) take the num parameter being passed and return all the
numbers from 1 to num separated by spaces, but
replace every number that is divisible by 3 with the word "Fizz",
replace every number that is divisible by 5 with the word "Buzz", and
every number that is divisible by both 3 and 5 with the word "FizzBuzz".
For example: if num is 16, then your program should return the string
 "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16".
The input will be within the range 1 - 50.
"""

def FizzBuzz(num):
    # code goes here
    i = 1
    string = ''

    if (num < 1) or (num > 50):
        string = 'Num is out of range 1-50'
        return string

    while i <= num:
        if (i % 3 == 0) and (i % 5 == 0):
            string += ' ' + "FizzBuzz"
        elif i % 5 == 0:
            string += ' ' + 'Buzz'
        elif i % 3 == 0:
            string += ' ' + 'Fizz'
        else:
            string += ' ' + str(i)

        i += 1
    return string


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result = FizzBuzz(8)
print('Input : 8')
print("Expected result: 1 2 Fizz 4 Buzz Fizz 7 8")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 2-----------------------")
result = FizzBuzz(3)
print('Input : 3')
print("Expected result: 1 2 Fizz")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 3-----------------------")
result = FizzBuzz(53)
print('Input : 53')
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 4-----------------------")
result = FizzBuzz(-1)
print('Input : -1')
print("Actual result   {}".format((result)))