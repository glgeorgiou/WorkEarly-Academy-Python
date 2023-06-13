"""
Have the function ConsonantCount(str) take the str string parameter being passed and
return the number of consonants the string contains.
"""

def ConsonantCount(strParam):
  # code goes here
  number = 0

  consonant = 'qwrtypsdfghjklzxcvbnm'
  for i in strParam.lower():
    if i in consonant:
      number += 1

  return number


print(ConsonantCount('hello world'))
print(ConsonantCount('Alphabets'))