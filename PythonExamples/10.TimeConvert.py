"""
Have the function TimeConvert(num) take the num parameter being passed
and return the number of hours and minutes the parameter converts to
(ie. if num = 63 then the output should be 1:3).
Separate the number of hours and minutes with a colon.
"""


def TimeConvert(num):
    hours = int(num) // 60
    minutes = int(num) % 60
    # code goes here
    return f"{hours}:{minutes}"


# keep this function call here
print(TimeConvert(input()))


"""
The function TimeConvert takes an integer num as an input and returns a string in the format of hours:minutes.
First, it calculates the number of hours by dividing the input number num by 60 using integer division (// operator) which discards any fractional part and returns the result as an integer.
 
Next, it calculates the number of minutes by taking the modulo of the input number num and 60 using the modulo operator (%). The result gives the remainder when the input number num is divided by 60, which represents the minutes.
 
Finally, it returns the result in the format of hours:minutes by using a formatted string literal (f-string) and returning the values of hours and minutes separated by a colon.
Note that the input value num represents minutes and the output will be the equivalent hours and minutes in the format of hours:minutes.
"""