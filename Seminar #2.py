# 1. Напишите программу, которая принимает на вход число N
# и выдает последовательность из N членов.
# *Пример:*
# Для N = 5: 1,-3,9,-27,81

# import random
# n = int(input('Введите число N: '))
# for i in range(n):
#     print(random.randint(0,10), end=' ')

# 2. Для натурального числа n создать словарь индекс-значение,
# состоящий из элементов последовательности
# *Пример:*
# Для n = 6: {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

# n = int(input('Введите число N: '))
# my_dict = {}
# for i in range(1, n+1):
#     my_dict[i] = 3*i + 1
# print(my_dict)

# 3.Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# first_string = str(input('Введите строку, в которой будем искать: '))
# second_string = str(input('Введите строку, которую ищем: '))

# count = 0
# for i in range(len(first_string)- len(second_string)) :
#     if first_string[i] == second_string[0]:
#         flag = True
#         for j in range(1, len(second_string)):
#             if second_string[j] != first_string[i+j]:
#                 flag = False
#         if flag:
#             count += 1
# print(count)
