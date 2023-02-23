"""
Have the function EquivalentKeypresses(strArr)
read the array of strings stored in strArr which will contain 2 strings
representing two comma separated lists of keypresses.

Your goal is to return the string true if the keypresses produce the same printable string
and the string false if they do not.

A keypress can be either a printable character or a backspace represented by -B.
You can produce a printable string from such a string of keypresses
by having backspaces erase one preceding character.
"""


def EquivalentKeypresses(strArr):
    words = []
    for i in strArr:
        s = ""
        i = i.replace(",", "")
        i = i.replace("-B", "1")
        for n in i:
            if n == "1":
                s = s[:-1]
            else:
                s += n
        words.append(s)
    if words[0] == words[1]:
        return "true"
    else:
        return "false"


print(EquivalentKeypresses(input()))

""" EXPLANATION
The given function EquivalentKeypresses takes in an input list strArr that contains two strings 
that represent two comma separated lists of keypresses.
 
The goal of the function is to return the string "true" if the keypresses produce the same printable string 
and "false" if they don't.
In the function, the first step is to declare an empty list words. 
This list will store the final printable strings after processing the keypresses.
 
Then, we use a for loop to iterate through each string in strArr. 
The first step inside the loop is to initialize an empty string s
that will be used to store the final printable string for each iteration.

Next, we replace the commas in the input string with an empty string 
and replace all occurrences of -B with the character 1.
This is done so that the characters that represent backspaces are easy to identify later.
 
The next step is to loop through each character n in the input string. 
If the character is 1, it means it represents a backspace, 
so we remove the last character from the final printable string s using the string slicing technique s = s[:-1]. 
If the character is not 1,
we add it to the final printable string s using the string concatenation operator s += n.
 
After processing each input string, the final printable string is added to the words list.
Finally, after processing both strings, 
we compare the two final printable strings stored in the words list. 
If they are equal, we return "true". Otherwise, we return "false".
"""