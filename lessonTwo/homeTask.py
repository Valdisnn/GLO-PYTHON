"""
                        СПРАВКА :
1) Типы данных: https://pythonworld.ru/tipy-dannyx-v-python
2) Арифметические операции : http://pythonicway.com/python-operators
3) Переменные: http://pythonicway.com/python-data-types
4) Комментарии: https://pythonru.com/uroki/28-kak-pisat-kommentarii-dlja-nachinajushhih

                        ЗАДАНИЕ :
1) Создайте по 3 переменные с каждым типом данных, которые были рассмотрены в уроке
2) Выведите созданные переменные в консоль и рядом их тип данных
3) С каждым арифметическим оператором сделайте по 2 действия, используя переменные
4) Написать правильные комментарии, там, где на ваш взгляд необходимо
"""

# int
intOne = 100
intTwo = 500
intThree = intOne + intTwo
print('int :', intOne, intTwo, intThree, type(intOne))  # output

# float
floatOne = 19.45
floatTwo = 20.65
floatThree = floatOne - floatTwo
print('float :', floatOne, floatTwo, floatThree, type(floatOne))  # output

# str
strOne = '- Say my name'
strTwo = '- Heisenberg'
strThree = "- You're god damn right"
print('str :', strOne, strTwo, strThree, type(strOne))  # output

# list
listOne = [1, 2, 3, 4]
listTwo = ['one', 'two', 'three', 'four']
listThree = [1, 'two', 3, False]
print('list :', listOne, listTwo, listThree, type(listOne))  # output

# dict
dictOne = {'name': 'Heisenberg', 'age': 52, 'alive?': False}
dictTwo = {
    'User': {
        'id': 123456789,
        'email': 'test@mail.ru',
        'password': '****'
    }
}
dictThree = {
    'newArr': [
        'name',
        'age',
        'isMale?'
    ]
}
print('dict :', dictOne, '\n', dictTwo, '\n', dictThree, type(dictOne))  # output

# tuple
tupleOne = (1, 2, 3, 4, 5)
tupleTwo = ('one', 'two', 'three')
tupleThree = (True, False, False, True)
print('tuple :', tupleOne, tupleTwo, tupleThree, type(tupleOne))  # output

# set
setOne = {'Alpha', 'Beta', 'Gamma'}
setTwo = {20, 10, 30, 45}
setThree = {100, '200', True, 100 + 200}
print('set :', setOne, setTwo, setThree, type(setOne))  # output

# boolean
boolOne = True
boolTwo = False
boolThree = True
print('boolean :', boolOne, boolTwo, boolThree, type(boolOne))  # output


#
# actions
#


def action_one(x=0.0, y=0):  # func
    """return x * y #(intTwo,floatTwo)"""  # result = 401.6425
    """return x + y #(boolOne,boolTwo)"""  # result = 1
    """return x - y #(floatThree,intThree)"""  # result = -601.2
    """return x / y #(floatThree,floatThree)"""  # result = 1.0
    """return x // y #(intTwo,intOne)"""  # result = 5
    """return x % y #(intOne,floatTwo)"""  # result = 17.400000000000006
    """return x ** y #(floatTwo, 2)"""  # result = 426.42249999999996
    return x ** y


# var
print(action_one(floatTwo, 2))  # output


def action_two(x=0, y=0):  # func
    """return x * y #(intOne,intTwo)"""  # result = 50000
    """return x + y #(strOne,strTwo)"""  # result = - Say my name- Heisenberg
    """return x - y #(floatTwo,floatOne)"""  # result = 1.1999999999999993
    """return x / y #(intThree,intOne)"""  # result = 6.0
    """return x // y #(intThree,intOne)"""  # result = 6
    """return x % y #(floatThree,intThree)"""  # result = 598.8
    """return x ** y #(intThree, 3)"""  # result = 216000000
    return x ** y


# var
print(action_two(intThree, 3))  # output
