from functools import reduce

age = 18
name = 'Godlike'

print(f'My name is {name}, my age is {age}, my gender is {"male"}')

var1 = 30
var2 = 250
result = var1 - var2 if var1 > var2 else var2 - var1
print(result)

i = 0
while i < 5:
    i += 1
    if i == 4:
        continue
    print(f'{i}')
else:
    print('Finished!')

for i in range(5):
    print(i)
    if i == 4:
        continue
else:
    print('Finished!')

str1 = 'Hello hello'
print(str1.find('el', 6, 9))

list1 = [1, 2, 3, 4, 5]


def func(x):
    return x ** 2


map_obj = map(func, list1)
print(map_obj)
print(list(map_obj))


def func2(a, b):
    return a + b


result = reduce(func2, list1)

print(result)
