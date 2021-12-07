# single line comment
# another line
# print('hello world!')
"""
Multiline comment
Great
"""
# print(type(3.15))
# b = 'sdfdsf'
# print(type(b))
# print(9 // 2)
# print(9 % 2)
# print(2 ** 3)

# print('aaa')
import random

print('aaa', end='')
print('bbb')

# name = 'Jarry'
# age = 18
# salary = 100.98
# my_format = 'His name is %s, his age is %d, his salary is %.3f.' % (name, age, salary)
# print(my_format)
# print('Winrate: %.2f%%' % 57.53)
#
# input_content = input('Please input your name:')
# print('Your name is: %s, welcome aboard, %s' % (input_content, input_content))
# a = 20
# b = 20
# if a > b:
#     print('a')
# elif b > a:
#     print('b')
# else:
#     print('c')
# res = 1 and 0
# print(res)

# a = 10
# b = 20
# res = a < b and a or b
# print(res)
# a = 10
# b = 20
# if a > b:
#     pass
# elif a < b:
#     pass

# user_quan = int(input('0.shitou. 1.jiandao 2.bu'))
# computer_quan = random.randint(0, 2)
# if (user_quan == 0 and computer_quan == 1) or \
#         (user_quan == 1 and computer_quan == 2) or \
#         (user_quan == 2 and computer_quan == 0):
#     print('Computer chooses: %d. You win!' % computer_quan)
# elif (user_quan == 0 and computer_quan == 0) or \
#         (user_quan == 1 and computer_quan == 1) or \
#         (user_quan == 2 and computer_quan == 2):
#     print('Computer chooses: %d. It\'s a draw!' % computer_quan)
# else:
#     print('Computer chooses: %d. You lose!' % computer_quan)

# i = 1
# while i <= 100:
#     total_sum = 0
#     total_sum += i
#     i += 1
# print(total_sum)

# def print_numbers(k, m):
#     i = 0
#     while i <= k:
#         j = 0
#         print(i)
#         i += 1
#         while j <= m:
#             if j == 1:
#                 j += 1
#                 continue
#             print(j, end=' ')
#             j += 1
#     if k >= 10:
#         return False
#     return True
#
#
# print_numbers(m=10, k=2)
# # print(print_numbers(k=20, m=4))
#
# print(isinstance('s', str))

# test_number = 20
#
#
# def test_function(m1, m2):
#     """This is a test function.
#
#     :param int m1: The first param.
#     :param str m2: The first param, a string.
#     :return: The return value.
#     """
#     test_number = 100
#     print(test_number)
#
#
# test_function()
# print(test_number)

# str1 = """
# I tell you, I tell you,
# The dragonborn comes.
# """
# print(str1[-2])
# for v in str1:
#     print(v, end=' ')
# str2 = str1.replace('tell', 'tale', 1)
# print(str2)
# print(str1[0: 20: 1])
# str3 = 'IamASuperGod'
# print(str3[0: 20: 3])
# print(str3[20:0:-1])
# str4 = 'tosskfksk123fskfksf'
# print(str4.split('k')[0])
# print(str4.strip())
# print(str4.isalpha())
# print(str4.isalnum())

# help(print)

# my_list = [[10, 10], [20], [10, 20], [30], [40]]
# print(type(my_list[1]))
# for i in my_list:
#     for o in i:
#         print(o)
# my_list.append([20, 30])
# my_list.insert(1, [12, 13])
# my_list.pop(4)
# my_list.pop()
# my_list.remove([10, 10])
# my_list.sort(reverse=True)
# my_list.reverse()
# print(my_list)
# print(my_list.index([12, 13]))
# my_list2 = [[12, 24], [124, 125]]
# my_list.extend(my_list2)
# print(my_list)

# my_tuple = (10,)
# my_tuple = (1, 20)
# print(my_tuple.count(2))
# my_tuple = my_tuple[1:]
# print(my_tuple)

# my_dict = {'name': 'Obama', 'age': 20}
# print(my_dict.get('name2', 'Default Value'))
# print(list(my_dict.keys()))
# for key in my_dict:
#     print(key)
# print(list(my_dict.values()))
# print(list(my_dict.items()))
# key_value_list = list(my_dict.items())
# for key_value in key_value_list:
#     print('Key:', key_value[0], 'Value:', key_value[1])
# print(my_dict.items())

# fa = open('a.txt', 'r')
# my_content = fa.readlines()
# print(my_content)
# fa.close()
