# Source: Python course - Quiz 5 Functions

"""
# A custom test function
def myFunction(x, y):
    (a, b) = (x, y)
    return a, b

res = myFunction(1, 2)
fType = type(res)
print('The type of {} is {}'.format(res,fType))
"""

"""
# Quiz question 1
def f1(employee, age):
    print(employee, age)


# f1('John', 23)
name = 'John'
age = 23
f1(name, age)
"""


"""
# Quiz question 2
def add(a, b):
    return a + 5, b + 5

sum = add(3, 2)
print(sum)
"""



# Quiz questin 3
def minimum(a, b):
    if a < b:
        min = a
    else:
        min = b
    return min


x, y, z, w = 2, 5, 1, 0
m = minimum(x, minimum(y, minimum(z,w)))
print(m)