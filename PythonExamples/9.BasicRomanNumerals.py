"""
Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals.
The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and M for 1000.
In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so you get XI.
But to create a number like 19,
you use the subtraction notation, https://en.wikipedia.org/wiki/Roman_numerals#Roman_numeric_system,
which is to add an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX.

The goal of your program is to return the decimal equivalent of the Roman numeral given.
For example: if str is "XXIV" your program should return 24

Examples
Input: IV
Output: 4
Input: XLVI
Output: 46
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

The function first creates two lists, CharList and ValueList,
 where CharList contains the Roman numerals and ValueList contains their equivalent decimal values.
 
For example, CharList[0] = "I" and ValueList[0] = 1.
A variable value is initialized to 0, which will store the equivalent decimal value of the Roman numeral.
Another variable last_value is also initialized to 0,
which will store the value of the last processed Roman numeral.

The Roman numeral string is processed in reverse order using a for loop. 
The loop iterates over the characters in strParam in reverse order using strParam[::-1].
 
For each character, the index x of the character in CharList is found using CharList.index(ch), 
where ch is the current character in the loop. 
The equivalent decimal value of the Roman numeral is obtained from ValueList using y = ValueList[x].

If the value of y is greater than or equal to last_value, 
it means that the current Roman numeral is not being subtracted from the previous numeral. 
In this case, the value of y is added to value.

If the value of y is less than last_value, 
it means that the current Roman numeral is being subtracted from the previous numeral. 
In this case, the value of y is subtracted from value.
After the loop has processed all the characters in strParam, 
the final value of value is returned, which is the equivalent decimal value of the Roman numeral.
"""