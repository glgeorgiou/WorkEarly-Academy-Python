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
    parts = strParam.split(' ')
    result = []
    cur_param = None
    cur_val = None

    for part in parts:
        if '=' in part:
            # append the previous parameter-value pair to the result
            if cur_param is not None and cur_val is not None:
                result.append(f"{len(cur_param)}={len(cur_val)}")

            # start a new parameter-value pair
            if part.endswith('='):
                cur_param = part[:-1]
                cur_val = ''
            else:
                cur_param, cur_val = part.split('=')
        else:
            # continuation of the current value
            cur_val += ' ' + part

    # append the last parameter-value pair to the result
    if cur_param is not None and cur_val is not None:
        result.append(f"{len(cur_param)}={len(cur_val)}")

    return ' '.join(result)



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
print("Expected result: 1=1 1=1 1=2 1=6 1=0 ")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 1-----------------------")
result = CommandLine("origin=2;3 destination=7;9 stops= 3;6 8;9 12;17")
print('Input : "origin=2;3 destination=7;9 stops= 3;6 8;9 12;17" ')
print("Expected result: 6=3 11=3 5=14 ")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 2-----------------------")
result = CommandLine("BNF=number :: (0..9){0..9}; variable :: {A..Z}")
print('Input : "BNF=number :: (0..9){0..9}; variable :: {A..Z}" ')
print("Expected result: 3=42 ")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 3-----------------------")
result = CommandLine("name=A value= 3 name=B value=8")
print('Input : "name=A value= 3 name=B value=8" ')
print("Expected result: 4=1 5=2 4=1 5=1  ")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 4-----------------------")
result = CommandLine("code=3320 date=2017/09/19 value=42 name=H G T T G")
print('Input : "code=3320 date=2017/09/19 value=42 name=H G T T G" ')
print("Expected result: 4=4 4=10 5=2 4=9 ")
print("Actual result   {}".format(result))