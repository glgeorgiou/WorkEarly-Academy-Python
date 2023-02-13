"""
Have the function ConsonantCount (str) take the str string parameter being passed
 and return the number of consonants the string contains
"""

def ConsonantCount(strParam):
    counter = 0
    consonants = 'qwrtypsdfghjklzxcvbnm'

    for char in strParam.lower():
        if char in consonants:
            counter += 1
    return counter


# White box testing
print('WHITE BOX TESTING')
print('The number of consonants in English alphabet should be 21')
print('The actual result is: ', len('qwrtypsdfghjklzxcvbnm'), '\n\n')

print('The number of consonants in the string \'Hello world \' should be', 7)
print('The number of the consonants in the string \'Hello world\' is', ConsonantCount('Hello world'), '\n\n')

print('The number of consonants in the string \'ea \' should be', 0)
print('The number of the consonants in the string \'ea\' is', ConsonantCount('ea'), '\n\n')

print('The number of consonants in the string \'#$@ \' should be', 0)
print('The number of the consonants in the string \'#$@\' is', ConsonantCount(''))