"""
Have the function KUniqueCharacters(str) take the str parameter being passed and find the
longest substring that contains k unique characters, where k will be the first character from the
string. The substring will start from the second position in the string because the first character will
be the integer k.
For example: if str is "2aabbacbaa" there are several substrings that all contain 2
unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba"
because it is the longest substring. If there are multiple longest substrings, then return the first
substring encountered with the longest length. k will range from 1 to 6.
"""


def KUniqueCharacters(strParam):
    kunique = int(strParam[0])
    strParam = strParam[1:]
    max_array = ''
    for i in range(len(strParam)):
        for j in range(len(strParam)):
            sarr = strParam[i:j+1]
            if len(set(sarr)) == kunique and len(sarr) > len(max_array):
                max_array = sarr
    return max_array


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = KUniqueCharacters("3aabacbebebe")
print('Input : "3aabacbebebe"')
print("Expected result: cbebebe")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case b-----------------------")
result = KUniqueCharacters("2aabbcbbbadef")
print('Input : "2aabbcbbbadef"')
print("Expected result: bbcbbb")
print("Actual result   {}".format(result))
