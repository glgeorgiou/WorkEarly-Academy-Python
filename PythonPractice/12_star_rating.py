"""
Have the function StarRating(str) take the str parameter being passed which will be an
average rating between 0.00 and 5.00, and convert this rating into a list of 5 image names to be
displayed in a user interface to represent the rating as a list of stars and half stars. Ratings should
be rounded to the nearest half. There are 3 image file names available: "full.jpg", "half.jpg",
"empty.jpg".
The output will be the name of the 5 images (without the extension), from left to right,
separated by spaces.
For example: if str is "2.36" then this should  return the string "full full half empty empty".
"""

def StarRating(strParam):
    # code goes here
    num = float(strParam)
    strParam = ""
    list = []
    diff = 5 - num

    if num < 1:
        if num > 0.25:
            list.append("half")
        else:
            list.append("empty")
        for i in range(4):
            list.append("empty")
    else:
        while num >= 1:
            list.append("full")
            num = num - 1
        if num > 0.25 and num < 0.75:
            list.append("half")
        elif num < 0.25 and num > 0:
            list.append("empty")
        elif num >= 0.75 and num < 1:
            list.append("full")
        while diff >= 1:
            list.append("empty")
            diff -= 1

    for el in list:
        strParam = strParam + " " + el

    return strParam


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = StarRating("0.38")
print('Input : "0.38"')
print("Expected result: half empty empty empty empty")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = StarRating("1.38")
print('Input :1.38')
print("Expected result: full half empty empty empty")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 1-----------------------")
result = StarRating("2.36")
print('Input :2.36')
print("Expected result: full full half empty empty")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 2-----------------------")
result = StarRating("4.5")
print('Input :4.5')
print("Expected result: full full full full half")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 3-----------------------")
result = StarRating("5.0")
print('Input :5.0')
print("Expected result: full full full full full")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 4-----------------------")
result = StarRating("3.02")
print('Input :3.02')
print("Expected result: full full full empty empty")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 5-----------------------")
result = StarRating("2.75")
print('Input :2.75')
print("Expected result: full full full empty empty")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 6-----------------------")
result = StarRating("1.37")
print('Input :1.37')
print("Expected result: full half empty empty empty")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 7-----------------------")
result = StarRating("4.63")
print('Input :4.63')
print("Expected result: full full full full half")
print("Actual result   {}".format((result)))
result = 0

print("\n--------------------Test case 8-----------------------")
result = StarRating("2.5")
print('Input :2.5')
print("Expected result: full full half empty empty")
print("Actual result   {}".format((result)))