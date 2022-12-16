# Реализуйте алгоритм перемешивания списка.

import random
def mix_list(list_mix):
     list = list_mix[:]
     list_length = len(list)
     for i in range(list_length):
         index_unknow = random.randint(0, list_length-1)
         temp = list[i]
         list[i] = list[index_unknow]
         list[index_unknow] = temp
     return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Список в случайном порядке: ")
print(mixed_list)