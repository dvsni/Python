# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rnd
def randomize(input_list, qtys):
    i = 0
    qtys = int(qtys)
    input_list = []
    while i < qtys:
        input_list.append(rnd(0, 10))
        i += 1
        return input_list

def sum_elem(input_list):
    i = 1
    sum = 0
    while i < len(input_list):
        sum += input_list[i]
        i += 2
    return sum

qty = input('Введите количество элементов массива: ')
pure_list = []
pure_list = randomize(pure_list,qty)
print(pure_list)
print("Сума элементов массива под нечетными индексами: ", int(sum_elem(pure_list)))

# Улучшение кода:

from typing import List
def count_sum(num_list: List[int]):
    return sum([num for i, num in enumerate(num_list) if i % 2])
