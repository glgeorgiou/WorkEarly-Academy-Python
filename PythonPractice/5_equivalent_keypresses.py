"""
Have the function EquivalentKeypresses(strArr) read the array of strings stored in strArr
which will contain 2 strings representing two comma separated lists of keypresses. Your goal is to
return the string true if the keypresses produce the same printable string and the string false if they
do not. A keypress can be either a printable character or a backspace represented by -B. You can
produce a printable string
"""

def EquivalentKeypresses(strArr):

  # code goes here
  words=[]

  for i in strArr:
    s = ""
    i = i.replace(",","")
    i = i.replace("-B", "1")
    for n in i:
      if n == "1":
        s = s[:-1]
      else:
        s += n
    words.append(s)
  if words[0] == words[1]:
    return True
  else:
    return False



print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result1 = EquivalentKeypresses(["a,b,c,d", "a,b,c,d,-B,d"])
print("Expected result: True")
print("The actual result is {}".format((result1)))
assert result1 == True

print("\n--------------------Test case 2-----------------------")
result2 = EquivalentKeypresses(["c,a,r,d", "c,a,-B,r,d"])
print("Expected result: True")
print("The actual result is {}".format((result2)))
assert result2 == True