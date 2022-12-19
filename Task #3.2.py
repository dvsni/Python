# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint as rnd
def randomize(input_list, qtys):
    i = 0
    qtys = int(qtys)
    input_list = []
    while i < qtys:
        input_list.append(rnd(0, 10))
        i += 1
    return input_list

def mult_elem (input_list):
    i=0
    multiplied_list = []
    while i<=len(input_list)%2+1:
        multiplied_list.append(input_list[i]*input_list[len(input_list)-i-1])
        i+=1
    return multiplied_list

qty = input('Введите количество элементов массива: ')
pure_list = []
pure_list = randomize(pure_list,qty)
print(pure_list)
print("Перемноженные элементы массива -> ",(mult_elem(pure_list)))


