"""
Have the function CommandLine(str) take the str parameter being passed which represents the
parameters given to a command in an old PDP system. The parameters are alphanumeric tokens
(without spaces) followed by an equal sign and by their corresponding value. Multiple
parameters/value pairs can be placed on the command line with a single space between each pair.
Parameter tokens and values cannot contain equal signs but values can contain spaces. The
purpose of the function is to isolate the parameters and values to return a list of parameter and value
lengths. It must provide its result in the same format and in the same order by replacing each entry
(tokens and values) by its corresponding length.

For example, if str is: "SampleNumber=3234 provider=Dr. M. Welby patient=John Smith
priority=High" then your function should return the string "12=4 8=12 7=10 8=4"
because "SampleNumber" is a 12 character token with a 4 character value ("3234")
followed by "provider" which is an 8 character token
followed by a 12 character value ("Dr. M. Welby"), etc.
"""


def CommandLine(strParam):
    str_arr = strParam.split("=")
    right_side = []
    solutions = []
    count = 1
    for i in range(len(str_arr)):
        if str_arr[i].count(" ") > 1:
            right_side.append((str_arr[i])[:str_arr[i].rfind(' ')].strip())
            right_side.append((str_arr[i])[str_arr[i].rfind(' '):].strip())
        else:
            right_side.append(str_arr[i])
    for i in range(0, len(right_side), 2):
        sol = str(len(right_side[i])) + "=" + str(len(right_side[count]))
        solutions.append(sol)
        count = count + 2
    return " ".join(solutions)


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = CommandLine("letters=A B Z T numbers=1 2 26 20 combine=true")
print('Input : "letters=A B Z T numbers=1 2 26 20 combine=true" ')
print("Expected result: 7=7 7=9 7=4 ")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = CommandLine("a=3 b=4 a=23 b=a 4 23 c=")
print('Input : "a=3 b=4 a=23 b=a 4 23 c=" ')
print("Expected result: ")
print("Actual result   {}".format(result))
result = 0

result = 0

print("\n--------------------Test case 1-----------------------")
result = CommandLine("SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High")
print('Input : "SampleNumber=3234 provider=Dr. M. Welby patient=John Smith priority=High" ')
print("Expected result: 12=4 8=12 7=10 8=4")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 2-----------------------")
result = CommandLine("a=3 b=4 a=23 b=a 4 23 c=")
print('Input : "a=3 b=4 a=23 b=a 4 23 c=" ')
print("Expected result: 1=1 1=1 1=2 1=6 1=0")
print("Actual result   {}".format(result))
result = 0