"""
Have the function CountLetter(strArr) take the strArr string array parameter being passed and
return the number of times that the character 'a' is included within the string array.
"""


def countLetter(strArr):
    countA = 0;

    for strEl in strArr:
        countA += strEl.count('a')
    return countA


result = countLetter(["This is", "an array", "of strings!"])
print(result)