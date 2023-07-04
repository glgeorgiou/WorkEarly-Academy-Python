"""
Have the function MissingDigit(str) take the str parameter, which will be a simple
mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and
return the digit that completes the equation. In one of the numbers in the equation, there will be an x
character, and your program should determine what digit is missing.
For example, if str is "3x + 12 = 46" then your program should output 4.
The x character can appear in any of the three numbers
and all three numbers will be greater than or equal to 0 and less than or equal to 1000000.
"""

def MissingDigit(exp):
    exp = list(exp.split())
    first_operand = exp[0]
    operator = exp[1]
    second_operand = exp[2]
    resultant = exp[-1]

    if 'x' in resultant:
        x = resultant
        first_operand = int(first_operand)
        second_operand = int(second_operand)

        if operator == '+':
            res = first_operand + second_operand
        elif operator == '-':
            res = first_operand - second_operand
        elif operator == '*':
            res = first_operand * second_operand
        else:
            res = first_operand // second_operand

    else:
        resultant = int(resultant)

        if 'x' in first_operand:
            x = first_operand
            second_operand = int(second_operand)
            if operator == '+':
                res = resultant - second_operand
            elif operator == '-':
                res = resultant + second_operand
            elif operator == '*':
                res = resultant // second_operand
            else:
                res = resultant * second_operand
        else:
            x = second_operand
            first_operand = int(first_operand)
            if operator == '+':
                res = resultant-first_operand
            elif operator == '-':
                res = first_operand - resultant
            elif operator == '*':
                res = resultant // first_operand
            else:
                res = first_operand // resultant
    res = str(res)
    k = 0
    for i in x:
        if i == 'x':
            result = res[k]
            break
        else:
            k = k + 1

    return result


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = MissingDigit("4 - 2 = x")
print('Input : "4 - 2 = x"')
print("Expected result: 2")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case A-----------------------")
result = MissingDigit("1x0 * 12 = 1200")
print('Input : "1x0 * 12 = 1200"')
print("Expected result: 0")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 1-----------------------")
result = MissingDigit("3x + 12 = 46")
print('Input : ""3x + 12 = 46"')
print("Expected result: 4")
print("Actual result   {}".format(result))
