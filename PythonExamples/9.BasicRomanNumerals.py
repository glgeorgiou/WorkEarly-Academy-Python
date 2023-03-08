"""
Have the function PowerSetCount(arr) take the array of integers stored in arr,
and return the length of the power set (the number of all possible sets) that can be generated.

For example: if arr is [1, 2, 3], then the following sets form the power set:
[]
[1]
[2]
[3]
[1, 2]
[1, 3]
[2, 3]
[1, 2, 3]
You can see above all possible sets, along with the empty set, are generated.
Therefore, for this input, your program should return 8.
"""


def BasicRomanNumerals(strParam):
    CharList = ["I", "V", "X", "L", "C", "D", "M"]
    ValueList = [1, 5, 10, 50, 100, 500, 1000]
    value = 0
    last_value = 0

    for ch in strParam[::-1]:
        x = CharList.index(ch)
        y = ValueList[x]
        if y >= last_value:
            value += y
            last_value = y
        else:
            value -= y

    # code goes here
    return value


# keep this function call here
print(BasicRomanNumerals(input()))

"""
The function BasicRomanNumerals takes a string strParam as input, which represents a Roman numeral. 
The function returns the equivalent decimal value of the Roman numeral.

The function first creates two lists, CharList and ValueList, where CharList contains the Roman numerals 
and ValueList contains their equivalent decimal values.
 
For example, CharList[0] = "I" and ValueList[0] = 1.
A variable value is initialized to 0, which will store the equivalent decimal value of the Roman numeral. 
Another variable last_value is also initialized to 0, 
which will store the value of the last processed Roman numeral.


"""