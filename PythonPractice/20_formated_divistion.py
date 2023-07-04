"""
Have the function FormattedDivision(num1,num2) take both parameters being passed, divide
num1 by num2, and return the result as a string with properly formatted commas and 4 significant
digits after the decimal place.
 For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789".
 The output must contain a number in the one's place even if it is a zero.
"""


def FormattedDivision(num1,num2):
    division = "%.4f" %(float(num1)/num2)
    return "{:,}".format(float(division))


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = FormattedDivision(123456789, 10000)
print('Input : 123456789, 10000')
print("Expected result: 12,345.6789")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = FormattedDivision(2,3)
print('Input : 2,3')
print("Expected result: 0.6667")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case C-----------------------")
result = FormattedDivision(10,10)
print('Input : 10, 10')
print("Expected result: 1.0000")
print("Actual result   {}".format(result))

result = 0

print("\n--------------------Test case 1-----------------------")
result = FormattedDivision(912, 2)
print('Input : 912, 2')
print("Expected result: 4,556.0000")
print("Actual result   {}".format(result))