"""
Given a string, return the first recurring character in it,
or None if there is no recurring character.

input = "workearly"
output = "r"

input = "work"
output = None

SOLUTION

We know we have to store a unique set of characters of the input string and loop through the string
to check which ones occur twice.
Given that we have to return the first index of the second repeating character,
we should be able to go through the string in one loop, save each unique character,and then
just check if the character exists in that saved set. If it does, return the character.
"""


def recurring(input):
    seen = set()

    for char in input:
        if char in seen:
            return char
        seen.add(char)

    return None



print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = recurring('workearly')
print('Input : "workearly"')
print("Expected result: r")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = recurring('work')
print('Input : "work"')
print("Expected result: None")
print("Actual result   {}".format(result))