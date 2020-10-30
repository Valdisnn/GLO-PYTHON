# ---------------------------------
print('variables :')
# ---------------------------------

# types
age = 19
print(age, type(age))  # int

# myName = 'Vladislav'
# my_profession = 'programmer'

age = '19'
print(age, type(age))  # str

# comments

# 1) default

"""
2) 
big
comment 
first
"""

'''
3)
bit 
comment
second
'''

#
# multiline comment
#

# ---------------------------------
print('operators :')


# ---------------------------------

# arithmetic operators

def do_some(a=0, b=0):
    # return a * b
    # return a + b
    # return a - b
    # return a / b  # деление с остатком ( 1.0 )
    # return a // b  # деление без остатка  ( 1 )
    # return a % b  # деление по модулю ( 0 )
    return a ** b  # возведение в степень


print(do_some(5, 5))

# ---------------------------------
print('data types :')
# ---------------------------------

# data types

myInt = 19
print(myInt, type(myInt))

myFloat = 100.500
print(myFloat, type(myFloat))

myStr = 'this is string !'
print(myStr, type(myStr))

# sequence of obj
myList = [1, 2.5, 'str', [5, 6]]
print(myList, type(myList))

# dictionaries (obj in JS)
myDict = {
    'name': 'Vladislav',
    'age': 19
}
print(myDict, type(myDict))

# tuple ( corteges )tuple
myCort = (1, 2, 3, 4)
print(myCort, type(myCort))

# set ( collections )
mySet = {10, 'Alpha', 10, 'Beta'}
print(mySet, type(mySet))

# boolean ( logic )
myBool = True
print(myBool, type(myBool))
