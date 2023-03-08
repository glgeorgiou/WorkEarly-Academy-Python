"""
Have the function ExOh(str) take the str parameter being passed and
return the string true if there is an equal number of x's and o's, otherwise return the string false.
Only these two letters will be entered in the string, no punctuation or numbers.

For example: if str is "xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.
"""


def ExOh(str):
    x_count = 0
    o_count = 0
    for char in str:
        if char == 'x':
            x_count += 1
        elif char == 'o':
            o_count += 1
    return True if x_count == o_count else False


print(ExOh(input()))

"""
The function ExOh takes in a string as input, and returns a string of either "true" or "false".
The algorithm checks if the number of 'x' characters in the string 
is equal to the number of 'o' characters in the string.
 
To do this, it first sets two variables x_count and o_count to zero. 
These variables will be used to keep track of the number of 'x' and 'o' characters in the input string.

Next, the function iterates through each character in the string. 
If the character is equal to 'x', the x_count variable is incremented. 
If the character is equal to 'o', the o_count variable is incremented.
"""