"""
Have the function HDistance(strArr) take the array of strings stored in strArr, which will only
contain two strings of equal length and return the number of characters at each position that are
different between them. For example: if strArr is ["house", "hours"] then your program should
return 2.
The string will always be of equal length and will only contain lowercase characters from
the alphabet and numbers.
"""


def HDistance(strArr):
    # code goes here
    dif_char = 0
    i = 0

    while i < len(strArr[0]):
        if strArr[0][i] != strArr[1][i]:
            dif_char += 1
        i += 1
    return dif_char


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result = HDistance(["10011", "10100"])
print('Input : ["10011", "10100"]')
print("Expected result: 3")
print("The actual result is {}".format((result)))
result = 0

print("\n--------------------Test case 2 -----------------------")
result = HDistance(["abcdef", "defabc"])
print('Input : abcdef", "defabc"]')
print("Expected result: 6")
print("The actual result is {}".format((result)))
