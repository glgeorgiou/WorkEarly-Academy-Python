"""
Have the function StringChanges(str) take the str parameter being passed, which will be a
string containing letters from the alphabet, and return a new string based on the following rules.

- Whenever a capital M is encountered, duplicate the previous character (then remove the M), and
- whenever a capital N is encountered remove the next character from the string (then remove the N).
- All other characters in the string will be lowercase letters.
For example: "abcNdgM" should return "abcgg". The final string will never be empty.
"""

def StringChanges(strParam):
    # code goes here
    res = ''

    for co in (strParam):
        if res and res[-1] == 'N':
            res = res[:-1]
            continue
        if co == 'M':
            if res:
                res += res[-1]
            continue
        res += co

    res = res.strip('N')
    return res


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result = StringChanges('MrtyNNgMM')
print('Input : MrtyNNgMM')
print("Expected result: rtyggg")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 2-----------------------")
result = StringChanges('oMoMkkNrrN')
print('Input : oMoMkkNrrN')
print("Expected result: ooookkr")
print("Actual result   {}".format((result)))

result = 0

print("\n--------------------Test case 3-----------------------")
result = StringChanges('abcNdgM')
print('Input : abcNdgM')
print("Expected result: abcgg")
print("Actual result   {}".format((result)))