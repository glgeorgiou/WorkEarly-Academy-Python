"""
Have the function GroupTotals(strArr) read in the strArr parameter containing key:value
pairs where the key is a string and the value is an integer. Your program should return a string with
new key:value pairs separated by a comma such that each key appears only once with the total
values summed up.

For example: if strArr is ["B:-1", "A:1", "B:3", "A:5"] then your program should return the string
A:6,B:2.

Your final output string should return the keys in alphabetical order. Exclude keys that have a value
of 0 after being summed up.

BUG WITH FAILED TESTS
"""


def GroupTotals(strArr):
    # code goes here

    items_0 = [s.split(':') for s in strArr]

    # convert counts to integer
    items = [[item[0], int(item[1])] for item in items_0]


    # Create a dictionary groupded by Name
    d = {}

    for row in items:
        # Add name to dict if not exists
        if row[0] not in d:
            d[row[0]] = []
        # Add all non-Name attributes as an new list
        d[row[0]].append(row[1:])

    # Counds the values of the keys
    for key in d:
        d[key] = [sum(x) / len(x) for x in zip(*d[key])]

    # Removes the 0 values from the dictionary
    d = {k: v for k, v in d.items() if v != [0]}

    return d


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result = GroupTotals(["B:-1", "A:1", "B:3", "A:5"])
print('Input : ["B:-1", "A:1", "B:3", "A:5"]')
print("Expected result: A:6,B:2.")
print("Actual result   {}".format(result))