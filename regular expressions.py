# Examples of regular expressions.
# Source: Python course quiz 4 - reqular expressions
import re


"""# Example 1 -
# Here the expression "w+" and "\W" will match the words starting with letter ‘p’
# and thereafter, anything which is not started with 'p' will not be identified.

L = ["python practice", "wo1rkearly training"]
for element in L:
      z = re.match("(p\w+)\W(p\w+)", element)
      if z:
          print((z.groups()))
"""



"""
# Example 2 - It will take the "pattern" and "text" to scan from the main string
# and return a match object when the pattern is found
# (or no match if the pattern is not found).
# In this example we took two literal strings "Learning Python" and "workearly",
# in a text string "Learning Python now".
# For "learning python now" we found the match giving as the result of "found a match".
# For the word “workearly" we didn’t find it so we go the “no match found” message.

patterns = ['Learning Python', 'workearly']
text = 'Learning Python now'
for pattern in patterns:
     print('Looking for "%s" in "%s" --> ' %(pattern, text), end = '')
     if re.search(pattern, text):
          print('Found a match')
     else:
          print('No match found!')
"""



"""# Example 3
# We  create a list of e-mail addresses.
# We will use the re.findall  method to get all the emails from the list.
em = 'john@gmail.com, angie123@outlook.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', em)
for email in emails:
     print(email)
"""




"""# Example 4
# Sub() function turns the phone number (210)-345-0987 into 2103450987
# using the pattern \D, which matches any single character which is not digit. The syntax of the sub() function is:
# re.sub(pattern, repl, string, count=0, flags=0)
phone_number = '(210)-345-0987'
pattern = '\D'
outcome = re.sub(pattern, '', phone_number)
print(outcome)"""




"""# Example 5
# The string_pattern finds two consecutive digits in the string birthdate.
# It is compiled to re.Pattern object,
# find all the matches in birthdate and print the numbers.
birthdate = "John's birthday is on 18/12/94"
string_pattern = r"\d{2}"
regex_pattern = re.compile(string_pattern)
outcome = regex_pattern.findall(birthdate)
print(outcome)"""




"""# Example 6 - 7
# We split each word by using the re.split() function
# the expression \s, that allows to parse each word in the string separately.
print(re.split(r'\s', 'the process of splitting'))
# print(re.split(r's', 'the process of splitting')
"""




