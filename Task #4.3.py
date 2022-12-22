# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint as rnd
def randomize(input_list, qtys):
    i = 0
    qtys = int(qtys)
    input_list = []
    while i < qtys:
        input_list.append(rnd(0, 10))
        i += 1
    return input_list

def remove_dubs(input_list):
    cleared_list = []
    for i in input_list:
        if i not in cleared_list:
            cleared_list.append(i)
    return cleared_list
qty = input('Введите количество элементов массива: ')
pure_list = []
pure_list = randomize(pure_list, qty)
print(pure_list)
print(remove_dubs(pure_list))