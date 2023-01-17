# ============================= Задача №1 =============================
# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# *Пример:* 
# 1+2*3 => 7; 
# (1+2)*3 => 9;

# def arythmetic(parse: list):
#     while '*' in parse or '/' in parse:
#         for i in range(1, len(parse) - 1, 2):
#             oper1 = int(parse.pop(i - 1))
#             oper2 = int(parse.pop(i))
#             if parse[i-1] == '*':
#                 parse[i-1] = oper1 * oper2
#                 break
#             elif parse[i] == '/':
#                 parse[i-1] = oper1 / oper2
#                 break

#     while '+' in parse or '-' in parse:
#         for i in range(1, len(parse) - 1, 2):
#             oper1 = int(parse.pop(i - 1))
#             oper2 = int(parse.pop(i))
#             if parse[i-1] == '+':
#                 parse[i-1] = oper1 + oper2
#                 break
#             elif parse[i] == '-':
#                 parse[i-1] = oper1 - oper2
#                 break
#     return parse

# user_input = input('Введите выражение: ')
# num_str = ''
# operands = user_input.replace('(', ' ( ').replace(')', ' ) ').replace('*', ' * ')\
#                    .replace('/', ' / ').replace('+', ' + ').replace('-', ' - ').split()
# if '(' in operands:
#     left = operands.index('(')
#     right = operands.index(')')
#     operands = operands[:left] + arythmetic(operands[left + 1:right]) + operands[right + 1:]
# print(arythmetic(operands))

# ============================= Задача №2 =============================
# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности.
# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 2, 3, 5, 1, 5, 3, 10]
# print(my_list)
# my_set = list(set(my_list))
# print(my_set)