"""
Have the function DifferentCases(str) take the str parameter being passed and
return it in upper camel case format where the first letter of each word is capitalized.
The string will only contain letters and some combination of delimiter punctuation characters separating each word.
"""
import re

def DifferentCases(strParam):

  # code goes here

  temp_list = []
  temp_list = re.split(r'[\s`~!@#$%^&*()_+\':;\"\\|-]',strParam)
  my_str = ''

  for word in temp_list:
    word = word.capitalize()
    my_str += '' + word
  return my_str



print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result = DifferentCases('cats AND*Dogs-are Awesome')
print("Expected result: CatsAndDogsAreAwesome")
print("The actual result is {}".format((result)))
result=0

print("\n--------------------Test case 2-----------------------")
result = DifferentCases('a b   c d-e-f%g')
print("Expected result: ABCDEFG")
print("The actual result is {}".format((result)))


